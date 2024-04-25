print('-='*20)
print('Calculadora de IMC')
print('-='*20)
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso!')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
