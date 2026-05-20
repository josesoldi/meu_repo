reta1 = float(input('Qual a medida 1? '))
reta2 = float(input('Qual a medida 2? '))
reta3 = float(input('Qual a medida 3? '))

if reta1 + reta2 > reta3 and reta3 + reta1 > reta2 and reta2 + reta3 > reta1:

    if reta1 == reta2 or reta2 == reta3 or reta1 == reta3:

        if reta3 == reta2 == reta1:
            print('Forma uma triângulo Equilátero')
            
        elif reta1 != reta2 or reta1 != reta3 or reta2 != reta3:
            print('Forma um triângulo Isóceles')

    else:
        print('Forma um triângulo Escaleno')

else:
    print('Não forma triângulo')