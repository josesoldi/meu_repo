import numpy as np

def matriz(nome):
    print (f'Digite os valores para a matriz {nome} (3x3):')
    valores = []

    for i in range (3):
        linha = []

        for j in range (3):

            valor = int(input(f'Digite o valor do termo [{i + 1}][{j + 1}]: '))
            linha.append(valor)
        
        valores.append(linha)
    
    return np.array(valores)

A = matriz('A')
B = matriz('B')

print (f'Matriz A:')
print (f'{A}')

print (f'Matriz B:')
print (f'{B}')

C = A + B

print (f'Matriz C:')
print (f'{C}')

D = A * B

print (f'Matriz D:')
print (f'{D}')

E = A @ B

print (f'Matriz E:')
print (f'{E}')
