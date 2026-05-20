def maior():
    mnumero = int (input('Digite um número: '))

    while True:
        resp = input('Você deseja adicionar mais valores? (S/N): ')

        if (resp == 'S'):
            numero = int (input('Digite outro número: '))
            
            if numero > mnumero:
                mnumero = numero 

        elif (resp == 'N'):
            break
    
        else:
            print ('Resposta invalida')

    return mnumero

n_maior = maior()

print (f'O maior número digitado foi {n_maior}')