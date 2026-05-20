time = []
goltime = 0

while True:
    
    i = 0
    jogador = {}

    jogador['nome'] = input ('Digite o nome do jogador: ')
    jogador['npart'] = int (input (f'Digite o número de partidas que o jogador {jogador['nome']} jogou: '))
    jogador['jgdgol'] = 0
    
    while i < jogador['npart']:
        jogador[f'gpart{i + 1}'] = int (input (f'Digite o numero de gols que o jogador fez na partida {i + 1}: '))
        jogador['jgdgol'] += jogador[f'gpart{i + 1}']
        i += 1

    goltime += jogador['jgdgol']

    time.append (jogador)

    resp = input('Você quer adicinar um novo jogador? (s/n): ').lower()

    while resp != 's' and resp != 'n':

        print('Insira uma resposta válida')
        resp = input('Você quer adicinar um novo jogador? (s/n): ').lower()


    if resp == 'n':
        break
    else:
        continue


i = 0
j = 0
while i < len(time):
    print(f'Nome: {time[i]['nome']}; Número de Partidas: {time[i]['npart']}; Total de gols: {time[i]['jgdgol']}')
    
    
    while j < time[i]['npart']:
        print(f'{time[i]['nome']} fez {time[i][f'gpart{j + 1}']} gol(s) na partida {j + 1}')
        j += 1

    j = 0
    i += 1

print (f'O time realizou ao todo {goltime} gol(s)!')

