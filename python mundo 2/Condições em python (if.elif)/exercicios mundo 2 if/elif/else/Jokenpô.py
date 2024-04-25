from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA 
''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print(f'Jogador jogou {itens[jogador]}...')
sleep(1)
print(f'Computador jogou {itens[computador]}')
print('-=' * 11)
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('Vocês empataram!')
    elif jogador == 1:
        print('Parabens, Você ganhou!')
    elif jogador == 2:
        print('Infelizmente você perdeu...')
    else:
        print('Opção invalida!')
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('Infelizmente você perdeu...')
    elif jogador == 1:
        print('Vocês empataram!')
    elif jogador == 2:
        print('Parabens, Você ganhou!')
    else:
        print('Opção invalida!')
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('Parabens, Você ganhou!')
    elif jogador == 1:
        print('Infelizmente você perdeu...!')
    elif jogador == 2:
        print('Vocês empataram!')
    else:
        print('Opção invalida!')
