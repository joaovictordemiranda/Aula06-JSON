from http import HTTPStatus
import requests

url =" https://dummy.restapiexample.com/api/v1/employees"

# Precisamos criar um cabeçalho (header) informando que vamos realizar um request e que aceitamos diversos tipos de resposta do endpoint:

header = {
    'Accept': '*/*',
    'User-Agent': 'requests',
}

# Agora, precisamos realizar essa busca por todos os empregados utilizando a biblioteca requests e sua respectiva rota com a linha de código requests.get(url, headers=headers).

resposta = requests.get(url, headers=header)

# Finalmente imprimimos nossa variável de resposta e analisamos seu conteúdo:

print(resposta.text)