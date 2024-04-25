import math
an = float(input('digite o angulo que voce deseja : '))
seno = math.sin(math.radians(an))
cons = math.cos(math.radians(an))
tang = math.tan(math.radians(an))
print(f'O angulo de {an} tem o SENO de {seno:.2f}')
print(f'O angulo de {an} tem o COSSENO de {cons:.2f}')
print(f'O angulo de {an} tem a TANGENTE de {tang:.2f}')