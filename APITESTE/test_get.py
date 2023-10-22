import requests

def test_status_and_data():
    url ="https://dummy.restapiexample.com/api/v1/employees"

    header = {
        'Accept': '*/*',
        'User-Agent': 'requests',
    }

    resposta = requests.get(url, headers=header)
    resposta_dict = resposta.json()

    status = resposta_dict['status']
    tamanho_da_lista = len(resposta_dict['data'])

    assert status == 'success' and tamanho_da_lista > 0