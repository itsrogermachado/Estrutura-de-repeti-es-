dias = int(input('O carro foi alugado por quantos dias ? '))
kmp = float(input('Quantos Kilometros foram rodados ? '))
pd = dias * 60
pk = kmp * 0.15
pago = pd + pk
print(f'O total a pagar é R${pago:.2f}') 