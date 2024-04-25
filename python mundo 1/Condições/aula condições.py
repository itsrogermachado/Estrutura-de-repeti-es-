n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2 )/2
print('A sua média foi {:.1f}'.format(m))
if m >= 5.0:
    print('Voce passou de ano parabens!')
else:
    print('Voce esta reprovado!')