import math
co = float(input('Qual o valor do cateto oposto ? '))
ca = float(input('Qual o valor do cateto adsjacente ? '))
hip = math.hypot(co, ca)
print(f'A Hipotenusa vai medir {hip:.2f}')