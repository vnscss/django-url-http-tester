import subprocess , http.client , json

mainUrl = '0.0.0.0:9000'
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    AMARELO = '\033[0;33m'  
    PADRAO = '\033[0m'      
    VERMELHO = '\033[0;31m'  


output = subprocess.run("bash -c 'python manage.py show_urls --format=pretty-json'", shell=True , check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
output = output.stdout.decode('utf-8')
data = json.loads(output)

for item in data:
    conn = http.client.HTTPConnection(mainUrl)
    conn.request("GET", item['url'])
    response = conn.getresponse()
    
    if response.status in [301, 302]:
        location = response.getheader('Location')
        conn = http.client.HTTPConnection(mainUrl)
        conn.request("GET", location)
        response = conn.getresponse()
        
        print('\n' , bcolors.VERMELHO ,'REDIRECTD TO' , bcolors.ENDC , '\n' ,  "url: ", location, '\n',  "Status:", bcolors.OKCYAN , response.status, bcolors.ENDC)
    
    if response.status == 200:
        print('\n', "url: ", item['url'], '\n',  "Status:", bcolors.OKGREEN , response.status, bcolors.ENDC)
    elif response.status == 404:
        print( "url: ", item['url'], '\n',  "Status:", bcolors.VERMELHO , response.status, bcolors.ENDC)      
    elif response.status == 403:
        print( "url: ", item['url'], '\n',  "Status:", bcolors.AMARELO , response.status, bcolors.ENDC)  
    elif response.status == 401:
        print("url: ", item['url'], '\n',  "Status:", bcolors.AMARELO , response.status, bcolors.ENDC)
    elif response.status == 503:
        print( "url: ", item['url'], '\n',  "Status:", bcolors.AMARELO , response.status, bcolors.ENDC)
    else:
        print( "url: ", item['url'], '\n',  "Status:", bcolors.PADRAO , response.status, bcolors.ENDC)
    conn.close()