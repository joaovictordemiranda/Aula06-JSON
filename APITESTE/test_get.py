import requests

def test_status_and_data():
    url ="https://dummy.restapiexample.com/api/v1/employees"

    header = {
        'Accept': '*/*',
        'User-Agent': 'requests',
    }

    resposta = requests.get(url, headers=header)

    print('---------------------------------\n')
    print(resposta.text)