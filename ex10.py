numero = int(input('Digite um número: '))

while True:

    if numero < 0:
        print('Número negativo.')
        break

    for i in range(10):
        print(f'{numero} x {i+1} = {numero * (i+1)}')
    
    numero = int(input('Digite um número: '))



