velocidade = float(input('Qual velocidade atual do veiculo ? '))
if velocidade > 80:
    print('Multado! Voce excedeu o limite que é 80KM/H!')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança! ')