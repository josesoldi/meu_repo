valor = float(input('Qual o valor da casa?'))
salario = float(input('Qual o salario do comprador?'))
anos = float(input('Em quantos anos gostaria de pagar?'))

prest = valor / (anos * 12)

if prest > salario * 0.3:
    print('Emprestimo negado')
else:
    print('Emprestimo aprovado')