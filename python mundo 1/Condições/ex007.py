salário = float(input('Qual seu salário ? '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganha R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))