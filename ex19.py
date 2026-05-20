lista = []
lista_par = []
lista_impar = []


valor = int (input ('Insira um valor: '))
lista.append(valor)

if valor % 2 == 0:
     lista_par.append(valor)
else:
    lista_impar.append(valor)

while True: 
    resp = input ('Você deseja adicionar mais valores? (s/n): ')

    if resp == 's':
        valor = int (input ('Insira um valor: '))
        lista.append(valor)

        if valor % 2 == 0:
            lista_par.append(valor)
        else:
            lista_impar.append(valor)

    elif resp == 'n':
        break

    else:
        print ('Insira uma resposta válida')

print (f'Lista final: {lista}')
print (f'Lista dos números pares: {lista_par}')
print (f'Lista dos números impares: {lista_impar}')