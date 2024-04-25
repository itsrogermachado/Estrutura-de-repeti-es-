n1 = float(input('Primeira nota do aluno: ')) #aqui o aluno colocará a primeira nota   
n2 = float(input('Segunda nota do aluno: ')) #aqui o aluno colocará a segunda nota
media = (n1+n2) / 2 #calculo para saber uma média
print(f'Tirando {n1} e {n2}, a média do aluno é {media}')#f no começo das aspas é o mesmo que .format no final delas!
if media < 5.0:# SE FOR MENOR QUE 5 ELE ESTARÁ REPROVADO
    print("O aluno está REPROVADO")
elif 7 > media >=5: # se for entre 7 e 5 o aluno está de recuperação
    print('O aluno está de recuperação!')
elif media >=7: # se a media for maior que 7 ou 7 ele está aprovado
    print('O aluno está APROVADO')