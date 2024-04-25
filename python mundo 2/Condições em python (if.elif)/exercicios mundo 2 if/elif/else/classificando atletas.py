from datetime import date # biblioteca do ano atual e etc
atual = date.today().year # Ano atual
nasc = int(input('Ano de nascimento: ')) # comando para o usuario digitar seu ano de nascimento
idade = atual - nasc # DESCOBRIR A IDADE PELO ANO ATULA - O NASCIMENTO
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')