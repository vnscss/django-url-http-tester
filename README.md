Esse script tem como objetivo mapear as urls de um projeto django e realizar testes de requisição `HTTP`, informando o status code, facilitando assim o debug e mapeamento de urls sem proteção.

Como usar:

 1. Ative o ambiente virtual antes de executar o script.
 2. Especifique o host em `mainUrl`. Ex: `mainUrl` = 'localhost:9000'
 3. Vá para a pasta Mãe do projeto. Ex: `cd /projeto-django/`.
 4.  Execute o script:  `python3 ./urltester.py`.

OBS: Caso queria rodar os testes usando `HTTPS` altere o código da função `http.client.HTTPConnection` para `http.client.HTTPSConnection` que é chamada 2 vezes no código.

Como funciona:
OBS: Nenhuma lib externa é necessária, script feito apenas com libs built in do python. 

 1. Com o `subprocess.run` recebo todas as url do projeto.
 2. Depois faço um  for loop para percorrer as urls, e executo um wget simples com a  função `http.client.HTTPConnection`.
 3. Caso o status da requisição seja `503` realizo novamente o wget, especificando para qual url o user foi redirecionado.
 4. Print do resultado.
 5. Close na requisição `conn.close`

