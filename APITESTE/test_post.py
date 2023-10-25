import requests

def test_iserindo_funcionario():
    # criar cabeçalho
    headers = {
        'Accept': '*/*',
        'User-Agent': 'requets',
    }

    url = "https://dummy.restapiexample.com/api/v1/create"
    NovoFuncionario =  {
    "name": "clarisse",
    "lastname": "miranda",
    "age": 37,
    "childs": "No",
    "pattern": {
      "monther": "Damylle da silva miranda",
      "father": "João victor de sousa miranda"
    },
    "Telephone": {
      "residencial": "0000.8888.9999",
      "celular": "9090-9595"
    }
  }
    #Realize o request informando ao método get o novo employee (data=new_employee, esse request deverá ser salvo em uma variável para análise futura) e converta a informação para um dicionário.
    resposta = requests.post(url, headers=headers, data=NovoFuncionario)
    resposta_dict = resposta.json()

    if resposta.status_code == 201:
        status = resposta_dict['status']
        funcionario_employeed = resposta_dict['data']

        assert status == 'success' and funcionario_employeed is not None
    else:
        False