clientes = {
    'cliente1': {
        'nome' : 'João',
        'sobrenome' : 'victor',
    },
    'cliente2' : {
        'nome' : 'damylle',
        'sobrenome' : 'silva'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} : {dados_v}')