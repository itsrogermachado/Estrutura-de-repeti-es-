import random
from time import sleep
num1 = random.randint(0, 5)
print('-=-' * 20)
print('Estou pensando em um numero entre 0 e 5 tente adivinhar...')
print('-=-' * 20)
num = int(input('Eae pensei em qual ? '))
print('Processando...')
sleep(2)
if num == num1:
    print('Parabens voce acertou!')
else:
    print('Oh não voce errou feio!')
    print('Eu estava pensando no {}'.format(num1))

print('Obrigado por tentar, volte sempre!')
