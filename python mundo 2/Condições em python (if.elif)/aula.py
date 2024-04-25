nome = str(input('Qual é o seu nome ? '))
if nome == 'Roger':
    print('Que nome bonito!')
elif nome == 'Rayssa' or nome == 'Ana Paula' or nome == 'Farias':
    print('Seu nome é maravilhoso')
elif nome == 'Ana' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é muito Popular no brasil! Sabia disso ?')
elif nome in 'Rogerio Carlos Joao Roberto':
    print('Que nome masculo!')
else:
    print('Seu nome é bem normal.') 
print(f'Tenha um bom dia, {nome}! ')