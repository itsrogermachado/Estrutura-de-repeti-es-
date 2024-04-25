produto = float((input('Digite o valor de suas compras: R$')))
print('''Métodos de pagamento:
      [1] A vista: 10% de desconto
      [2] A vista no cartão: 5% de desconto
      [3] Em até 2x no cartão: preço normal
      [4] 3x ou mais no cartão: 20% de juros
 ''')
opção = int(input('Escolha seu método de pagamento: '))
if opção == 1:
    op1 = produto - (produto * 10/100)
    print(f'Suas compras sairão no valor de R${op1}!')
elif opção == 2:
    op2 = produto - (produto * 5/100)
    print(f'Suas compras sairão no valor de R${op2}')
elif opção == 3:
    total = produto 
    parcela = produto / 2
    print(f'Sua será parcelada em 2x sem juros de R${parcela}')
elif opção == 4:
    total = produto + (produto * 20 / 100)
    totalparcelas = int(input('Em quantas parcelas será ? '))
    parcela = total / totalparcelas
    print(f'Sua compra será parcelada em {totalparcelas}x de R${parcela:.2f} com juros')
    print(f'Sua compra de R${produto} vai custar R${total} no final.')