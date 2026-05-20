frs = input('Digite uma frase: ')

print(f'O caractere "A" aparece {frs.count('A', 0, len(frs))} vezes')

if frs.find('A') != -1:
    print(f'O primeiro caractere "A" aparece na posição {frs.find('A') + 1}')

else: 
    print('A frase não tem o caractere "A"')

i = 0
utermo = 0

while i < len(frs):
    if frs[i] == 'A':
        utermo = i
    i += 1
    
if utermo != 0:
    print(f'O ultimo caractere "A" aparece na posição {utermo + 1}')