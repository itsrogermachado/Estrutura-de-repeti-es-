from datetime import date
atual = date.today().year
totmaior = 0 # variavel do total 
totmenor = 0 # variavel do total
for pess in range(1,8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu: '.format(pess)))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1 # total MAIS UM 
    else:
        totmenor += 1 # total MAIS UM 
print('Ao todo tivemos {} pessoas maiores de idade '.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))