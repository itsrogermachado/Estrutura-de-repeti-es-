viagem = float(input('Qual a distancia da sua viagem ? '))
print(F'Vocês está preste a começar uma viagem de {viagem}km. ')
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print(F'O preço da sua viagem vai custar R${preço}')