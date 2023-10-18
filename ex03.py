import copy

"""d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['joao', 'alice']}

# v= copy.deepcopy(d1)
v = d1.copy()
v[0] = 'Miguel'
v[1] = 'Damylle'

print(d1)
print(v)"""

# transformando lista em dicionarios

"""lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)

print(d1)
"""

# concatenando os dicionario

d1 = {    
    'c1', 1,
    'c2', 2,
    'c3', 3,
    }



d2 = {
    'a' : 'b',
    'c' : 'd',
}

d1.update(d2)
print(d1)