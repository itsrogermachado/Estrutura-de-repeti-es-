num1 = int(input('Digite um número: '))
tot = 0
for c in range (1,num1+1):
    if num1 % c ==0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num1,tot))
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')