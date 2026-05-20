frs = input('Digite a sua frase: ')

def minusculo_espaco(frs):
    fmi = frs.lower()
    
    i = 0
    nfrs = ''
    while i < len(fmi):
        if fmi[i] != ' ':
            nfrs += fmi[i]
        i += 1
    
    return nfrs

def palindromo(nfrs):
    tst = 0
    i = 0

    while i < len(nfrs):
        if nfrs[i] != nfrs[len(nfrs) - 1 - i]:
            tst += 1
            break
        i += 1

    return tst

frs_limpa = minusculo_espaco(frs)
conf = palindromo(frs_limpa)

if conf == 0:
    print('Sim, é um palindromo')

else:
    print('Não, não é um palindromo')



