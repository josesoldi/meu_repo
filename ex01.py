dias = int(input('quantos dias? '))
km = float(input('quantos km rodados? '))

total = dias * 60 + km * 0.15

print(f'O total gasto foi {total:.2f} reais')