somaidade = 0
mediaidade = 0
maioridadedade = 0
nomevelho = ''
totmulher = 0

for p in range (1,5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Seco [M/F]: ')).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadedade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedade:
        maioridadedade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher += 1
        
mediaidade = somaidade / 4

print('A media de idade do grupo é {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadedade, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))