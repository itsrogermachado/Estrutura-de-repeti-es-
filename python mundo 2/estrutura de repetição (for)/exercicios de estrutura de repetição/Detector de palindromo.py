frase = str(input('Digite uma frase: ')).strip().upper() #.strip tira os espaços e upper deixa tudo em maiusculo
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # maneira mais facil de se fazer em vez de usar o for é simplesmente ir por fatiamento que é esse [::-1]
'''for letra in range (len(junto) - 1, -1, -1):  # len = ler toda a frase 
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um PALINDROMO!')
else:
    print('Não é um PALINDROMO!')

