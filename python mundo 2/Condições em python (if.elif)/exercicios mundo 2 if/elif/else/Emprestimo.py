casa = float(input('Qual o valor da casa que deseja comprar: R$ '))
salario = float(input('Qual seu salario atual: R$ '))
tempo = int(input('Em quanto tempo pretende pagar a casa ? '))
mensalidade = casa / (tempo * 12)
minimo = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, tempo), end='')
print(' a prestação será de R${:.2f}'.format(mensalidade))
if mensalidade <= minimo:
    print('Você conseguiu um emprestimo! ')
    print('PARABÉNS')
else:
    print('Seu emprestimo não foi aprovado!')
