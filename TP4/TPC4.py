def menu ():
    print ("""
    (1) Criar Lista 
    (2) Ler lista
    (3) Soma de todos os valores da lista
    (4) Média dos valores da lista
    (5) Maior da lista
    (6) Menor da lista
    (7) A lista ordenada por ordem crescente
    (8) A lista ordenada por ordem decrescente
    (9) Procurar por um elemento
    (0) Sair 
    """ )
    
    return int(input("O que pretende fazer com os dados? Escolha uma opção"))


import random

def crialista():
    listainteiro = []
    N = int(input("Quantos valores pretendes ter na lista"))
    listainteiro = [random.randint(1,100) for x in range(N)]
    print(listainteiro)
    return listainteiro
def crialista2():
    listainteiro = []
    N = int(input("escolhe o número de valores da lista"))
    listainteiro = []
    i = 1
    while i <= N:
        num = int(input(f" Escolhe um número {i} da sua lista"))
        listainteiro.append(num)
        i = i + 1
    print(listainteiro)
    return listainteiro
    

def soma(listainteiro):
    print(listainteiro)
    soma = 0
    i = 0
    while i < len(listainteiro):
        soma = soma + listainteiro[i]
        i = i + 1
    print(f"a soma é {soma}")
    return soma

def medialista(listainteiro):
    soma(listainteiro)
    media = soma(listainteiro) / len(listainteiro)
    print(f" a média é {media} ")
    return media

def menor(listainteiro):
    print (listainteiro)
    res = listainteiro[0]
    for valor in listainteiro[1:]:
        while valor < res:
            res = valor
    print(f"O menor número é {res}")
    return res

def maior(listainteiro):
    print(listainteiro)
    res = listainteiro[0]
    for valor in listainteiro[1:]:
        while valor > res:
            res = valor
    print(f"O maior número é {res}")
    return res

def crescente(listainteiro):
    print (listainteiro)
    i = 0
    while i < len(listainteiro) - 1:
        if listainteiro[i] > listainteiro [i+1]:
           print("A lista não está ordenada de forma crescente")
           return
        i = i + 1
    print("SIM, a lista está ordenada de forma crescente")
    
    

def decrescente(listainteiro):
    print(listainteiro)
    i = 0
    while i < len(listainteiro) - 1:
        if listainteiro[i] < listainteiro [i+1]:
            print("A lista não está ordenada de forma decrescente")
            return
        i = i + 1
    print("SIM, a lista está ordenada de forma decrescente")
    

def procurar(listainteiro):
    print(listainteiro)
    pos = -1
    procurado = int(input("Que elemento pretendes encontrar?"))
    #while i <= len(listainteiro):
    for valor in range(len (listainteiro)):
        if listainteiro[valor] == procurado:
            pos = valor + 1
    if pos == -1:
        print("-1")
        print("esse valor não existe")
    else:
        print(f"O elemento {procurado} está na posição {pos}")
    
### OPÇÕES
listainteiro = []
escolha = -1
while escolha != 0:
    escolha = menu()
    if escolha not in {1,2,3,4,5,6,7,8,9}:
        print("impossível, escolha uma opção possível")
    else:
        if escolha == 1:
            listainteiro = crialista()
        if escolha == 2:
            listainteiro= crialista2()
        if escolha == 3:
            print (listainteiro)
            if listainteiro != [] :
                soma(listainteiro)
            else:
                print("precisa de gerar uma lista")
        if escolha == 4:
            if listainteiro != [] :
                medialista(listainteiro)
            else:
                print("precisa de gerar uma lista")
        if escolha == 5:
            if listainteiro != [] :
                maior(listainteiro)
            else:
                print("precisa de gerar uma lista") 
        if escolha == 6:
            if listainteiro != [] :
                menor(listainteiro)
            else:
                print("precisa de gerar uma lista") 
        if escolha == 7:
            if listainteiro != [] :
                crescente(listainteiro)
            else:
                print("precisa de gerar uma lista") 
        if escolha == 8:
            if listainteiro != [] :
                decrescente(listainteiro)
            else:
                print("precisa de gerar uma lista") 
        if escolha == 9:
            if listainteiro != [] :
                procurar(listainteiro)
            else:
                print("precisa de gerar uma lista") 
        if escolha == 0:
            print (f"Obrigada!A lista guardada neste momento é {listainteiro}   ")
