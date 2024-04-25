num = int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases numericas: 

[1] Converter para binario: 

[2] Converter para octal: 

[3] Converter para hexadecimal ''')

opção = int(input('Sua opção: '))

if opção == 1:
   
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))

elif opção == 2:
    
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))

elif opção == 3:

    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

else:
    print('Sua opção é invalida!')
