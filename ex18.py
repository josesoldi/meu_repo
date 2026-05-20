numeros_list = []

for i in range(5):
    valor = int(input(f'Qual o valor {i + 1}: '))
    numeros_list.append(valor)

print (f'O maior valor digitado foi {max(numeros_list)} e está na posição {numeros_list.index(max(numeros_list)) + 1}')
print (f'O menor valor digitado foi {min(numeros_list)} e está na posição {numeros_list.index(min(numeros_list)) + 1}')