primeiro = int(input("Digite o primeiro número: "))
razao = int(input("Digite a razão da PA: "))

termo = primeiro - razao

for i in range (0, 10):
    termo = termo + razao
    print(termo)

    
resp = input("Deseja mostrar mais 5 termos? (SIM ou NAO) ")


while resp != 'NAO':

    if resp == 'SIM':
        for i in range (0, 5):
            termo = termo + razao
            print(termo)
    
    elif resp == 'NAO':
        break

    resp = input("Deseja mostrar mais 5 termos? (SIM ou NAO) ")

print('Fim da PA')