valor = int(input('Digite um valor: '))
ced = 0

ced += valor // 50 
resto = valor % 50

ced += resto // 20
resto = resto % 20

ced += resto // 10
resto = resto % 10

ced += resto // 1

print(f'Total de Cédulas: {ced}')

