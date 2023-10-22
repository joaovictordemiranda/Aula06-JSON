import requests

def test_put_new_data():
    headers = {
        'Accept': '*/*',
        'User-Agent': 'requets',
    }

    new_data =  {
        "id": 1,
        "title": "A some test tiltle",
        "body": "some test description",
        "userId": '1'
    }
    
    post_id = 1
   
    url = 'https://jsonplaceholder.typicode.com/posts/'    #Realize o request informando ao método get o novo employee (data=new_employee, esse request deverá ser salvo em uma variável para análise futura) e converta a informação para um dicionário.
    resposta = requests.put(url + str(post_id), data=new_data, headers=headers)
    resposta_dict = resposta.json()

    if resposta.status_code == 200:
        assert resposta_dict == new_data
    else:
        assert False