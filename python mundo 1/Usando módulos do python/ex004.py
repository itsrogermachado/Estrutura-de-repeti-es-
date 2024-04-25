import random
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro Aluno: '))
aluno4 = str(input('Quarto Alunoo: '))
lista = [aluno1, aluno2, aluno3, aluno4]
'''Uma lista para o python fica entre []'''
print(f'O aluno escolhido foi {random.choice(lista)}')
