nm = input('Digite um nome: ')

print(nm.upper())
print(nm.lower())

i = 0
lts = 0

while i < len(nm):
    if nm[i] != ' ':
        lts += 1
    i += 1

print (f'Tem {lts} letras ao todo')

pn = ''
i = 0

while i < len(nm) and nm[i] != ' ':
    pn += nm[i]
    i += 1

print (f'O primeiro nome tem {len(pn)} letras')