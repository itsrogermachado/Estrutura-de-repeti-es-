preço = float(input('Qual é o preço do produto ? R$'))
novo = preço - (preço * 5 / 100)
print(f'O produto que custava R${preço}, na promoção com desconto de 5% vai para R${novo}')