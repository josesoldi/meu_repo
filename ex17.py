import random

numeros_lista = []

for i in range(0, 5):
    numeros_lista.append(random.randint(1, 100))

numeros_tupla = tuple(numeros_lista)

print(f'Os números sorteados foram: {numeros_tupla}')

print(f'O maior valor é {max(numeros_lista)}')
print(f'O menor valor é {min(numeros_lista)}')
