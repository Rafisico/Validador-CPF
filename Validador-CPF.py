import string

while True:
    CPF=input('Dgite seu CPF: ')
    ponto=string.punctuation
    lista_cpf=[]
    lista_n=[]

    for c in ponto:                             #Para tirar os pontos e traço do CPF.
        CPF = CPF.replace(c, '')

    for c in CPF:                               #Para adicionar cada item do cpf em uma lista.
        lista_cpf.append(c)

    lista_cpf=list(map(int,lista_cpf))        #Para transformar todos os itens da lista em um nº inteiro.

    del(lista_cpf[9:11])

    for r in range(10, 1, -1):                  #Para adicionar de 10 a 2 em uma lista.
        lista_n.append(r)

    produto = [x*y for x, y in zip(lista_cpf, lista_n)]  #Multiplicação entre as listas, criando uma nova lista 'produto'.

    soma_produto = 0

    for n in produto:                 #Interar a lista produto e criar a soma.
        soma_produto += n

    conta= 11-(soma_produto%11)
    digito_1=0

    if conta>9:
        digito_1=0
        lista_cpf.append(digito_1)
    else:
        digito_1=conta
        lista_cpf.append(digito_1)

    lista_n2=[]

    for r in range(11, 1, -1):                  #Para adicionar de 11 a 2 em uma lista.
        lista_n2.append(r)

    produto2 = [a*b for a, b in zip(lista_cpf, lista_n2)]  #Multiplicação entre as listas, criando uma nova lista 'produto'.

    soma_produto2 = 0

    for m in produto2:                 #Interar a lista produto e criar a soma.
        soma_produto2 += m

    conta2= 11-(soma_produto2%11)
    digito_2=0

    if conta2>9:
        digito_2=0
        lista_cpf.append(digito_2)
    else:
        digito_2=conta2
        lista_cpf.append(digito_2)

    novo_cpf = ''.join(map(str,lista_cpf))
    novo_cpf=int(novo_cpf)

    CPF=int(CPF)

    sequencia = novo_cpf == lista_cpf[0]*11111111111

    if novo_cpf == CPF and not sequencia:
        print('CPF Válido')
    else:
        print('CPF Inválido')

