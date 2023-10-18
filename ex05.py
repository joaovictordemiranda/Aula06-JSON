"""
list Comprehension - estudos - dia:15
"""

l1 = [1,2,3,4,5,6,7]
l1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['miguel', 'alice', 'Damylle']
ex4 = [v.replace('a', '@') for v in l2]

tuple = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
ex5 = [(x, y) for x, y in tuple]
ex5 = dict(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0]

ex7 = [v if v % 2 == 0 else 'Não é' for v in l3]
print(ex7)