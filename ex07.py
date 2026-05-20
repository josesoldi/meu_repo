maior = 0
homem = 0
mulher_menor20 = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M ou F): ")

    if sexo == 'M':
        homem += 1
    elif idade > 18:
        maior += 1
    elif sexo == 'F' and idade < 20:
        mulher_menor20 += 1

    resp = input('Deseja continuar? S/N: ')

    if resp == 'N':
        break

print(f'Total de pessoas maiores de 18 anos: {maior}')
print(f'Total de homens cadastrados: {homem}') 
print(f'Total de mulheres menores de 20 anos: {mulher_menor20}')

