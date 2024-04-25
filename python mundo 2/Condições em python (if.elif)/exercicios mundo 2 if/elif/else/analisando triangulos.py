print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro seguinto de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Tercerio segmento de reta: '))
if r1 == r2 == r3:
    print('Você tem um triangulo equilatero! ')
elif r1 != r2 != r3 != r1:
    print('Voceê tem um triangulo Escaleno')
else:
    print('Você tem um triangulo Isosceles!')