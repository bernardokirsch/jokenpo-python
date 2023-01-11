import random

choices = ['Pedra', 'Papel', 'Tesoura']

player = 'start'

while player != 'Sair':
    
    choice = random.choice(choices)
    
    print('')
    print('----- Jokenpô -----')
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')
    print('4 - Sair')
    
    op = int(input('Informe sua escolha: '))
    while op < 1 or op > 4:
        op = int(input('Opção inválida. Informe sua escolha novamente: '))

    if op == 1:
        player = 'Pedra'
    elif op == 2:
        player = 'Papel'
    elif op == 3:
        player = 'Tesoura'
    elif op == 4:
        player = 'Sair'
        print('\nSaindo...')
        break

    print(f'\n{player} x {choice}')

    if player == 'Pedra':
        if choice == player:
            print('Você empatou!')
        if choice == 'Papel':
            print('Você perdeu!')
        if choice == 'Tesoura':
            print('Você ganhou!')
    elif player == 'Papel':
        if choice == player:
            print('Você empatou!')
        if choice == 'Tesoura':
            print('Você perdeu!')
        if choice == 'Pedra':
            print('Você ganhou!')
    elif player == 'Tesoura':
        if choice == player:
            print('Você empatou!')
        if choice == 'Pedra':
            print('Você perdeu!')
        if choice == 'Papel':
            print('Você ganhou!')

print('Jogo encerrado')