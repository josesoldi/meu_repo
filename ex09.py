soma = 0
for i in range(1, 6):
    numero = int(input(f'Digite o numero {i}: '))
                 
    if numero % 2 == 0:
        soma += numero

print(f'A soma dos pares é {soma}')

