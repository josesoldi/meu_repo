soma_id = 0
mulher20 = 0
idhv = 0
nome_hv = ''

for i in range(1, 5):
    nome = input(f'Digite o nome da pessoa {i}: ')
    idade = int(input(f'Digite a idade da pessoa {i}: '))
    sexo = input(f'Digite o sexo da pessoa {i} (M/F): ')
    
    soma_id += idade

    if sexo == 'F' and idade < 20:
        mulher20 += 1

    if sexo == 'M' and idade > idhv:
        idhv = idade
        nome_hv = nome

media_id = soma_id / 4

print(f'A média de idade do grupo é: {media_id:.1f} anos')
print(f'O nome do homem mais velho é: {nome_hv}')       
print(f'O número de mulheres com menos de 20 anos é: {mulher20}')

