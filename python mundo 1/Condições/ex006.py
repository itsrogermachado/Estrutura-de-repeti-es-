from time import sleep
num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo Valor: '))
num3 = int(input('Tercerio Valor: '))
#verificando quem é menor
if num1<num2 and num1<num3:
    menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
#verificando quem é maior
if num1>num2 and num1>num3:
    maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print('---------------------')
sleep(3)
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))