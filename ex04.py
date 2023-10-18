print()
print('TEXTO EXPLICATIVO')

perguntas = {
    'pergunta1': {
        'pergunta': 'quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '3',},
        'resposta_certa': 'b',
    },
    'pergunta2': {
        'pergunta': 'quanto é 2*5? ',
        'respostas': {'a': '10', 'b': '12', 'c': '33',},
        'resposta_certa': 'a',
    },
}

print()

respostas_certas  = 0
for pk, pv in perguntas.items():
    print(f'{pk}.{pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
        
    respostas_usuario = input('sua resposta: ')

    if respostas_usuario == pv['resposta_certa']:
        print('eeeeeeeeh parabéns !')
        respostas_certas += 1
    else:
        print('IXIIIIIII ERROU TENTE DE NOVO !')
        
    print()

qtd_perguntas = len(perguntas)
porcetagem_acertos = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} respostas.')
print(f'Sua Porcetagem de acerto foi de {porcetagem_acertos}%.')