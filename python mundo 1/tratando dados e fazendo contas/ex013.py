salario = float(input('Qual o salario do funcionario ? R$'))
novo = salario + (salario * 15 / 100)
print(f'Um funcionario que ganhava R${salario:.2f}, com 15% de aumento passou a ganhar R${novo:.2f}.')