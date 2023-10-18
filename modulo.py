import json
import os

"""
pessoas = [
    {
        "name": "joao",
        "lastname": "miranda",
        "age": 23,
        "childs": 2,
        "Telephone": {
            "residencial": '0000.8888',
            "celular":' 555.555.9595',
        },
    },
    {
        "name": "joao",
        "lastname": "miguel miranda",
        "age": 15,
        "childs": "No",
        "pattern": {
            "monther": "Damylle da silva miranda",
            "father": "João victor de sousa miranda",
        },
        "Telephone": {
            "residencial": '0000.8888',
            "celular":' 555.555.9595',
        },
    },
    {
        "name": "Alice",
        "lastname": "miranda",
        "age": 10,
        "childs": "No",
        "pattern": {
            "monther": "Damylle da silva miranda",
            "father": "João victor de sousa miranda",
        },
        "Telephone": {
            "residencial": '0000.8888',
            "celular":' 555.555.9595',
        },
    },
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(SAVE_TO, 'w') as file:
    json.dump(pessoas, file, indent=2)

print(json.dumps(pessoas, indent=2))
"""
"""BASE_DIR = os.path.dirname(__file__)
JSON_FILE= os.path.join(BASE_DIR, 'arquivo-python.json')

with open(JSON_FILE, 'r') as file:
    pessoas = json.load(file)
    print(json.dumps(pessoas))
    
"""
    #for pessoa in pessoas:
    #    print(pessoa['name'], pessoa['age'])

json_string = """
[
{
"name": "joao", "lastname": "miranda", "age": 23, "childs": 2, "Telephone": {"residencial": "0000.8888", "celular": " 555.555.9595"}
},
{
"name": "Alice",
"lastname": "miranda",
"age": 10,
"childs": "No",
"pattern": {
    "monther": "Damylle da silva miranda",
    "father": "Jo\u00e3o victor de sousa miranda"
},
"Telephone": {
    "residencial": "0000.8888",
    "celular": " 555.555.9595"
}
}
] 
"""
pessoas = json.loads(json_string)
for pessoa in pessoas:
    print(pessoa['name'])