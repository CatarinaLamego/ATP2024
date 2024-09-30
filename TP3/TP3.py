def menu():
    print("Bem-vindo ao jogo dos fósforos")
    print("Menu:")
    print("1) Opção1- O computador joga primeiro")
    print("2) Opção2- O utilizador joga primeiro")
def opcao_1():
    i = 21
    from random import randint
    escolha = randint(1,4)
    while i > 1 and i -escolha !=1:
            if i > 5:
                escolha = randint(1,4)
            elif i == 4:
                escolha = 3
            elif i == 3:
                escolha = 2
            elif  i == 2:
                escolha = 1
            print (f"o compputador tirou {escolha} fósforos")
            escolhautilizador= int(input("escolhe um número de fósforos a tirar"))
            i= i- escolha - escolhautilizador
            print (f"sobram {i} fósforos")
            if i < 1:
                print("perdeste o jogo")
            if i== 1:
                print("ganhaste o jogo")
 
    if i-escolha == 1:
                print("perdeste o jogo")

def opcao_2():
    i = 21
    f = int(input("introduz numero de fosforos que queres retirar (1/2/3/4)"))
    diferença = 21 - f
    while diferença > 1 :
        computador = 5 - f
        diferença = diferença - computador
        if diferença == 1:
                print ("perdeste")
        else:
            print(f"eu retiro {computador} fósforos, restando {diferença} fósforos. Quantos pretendes retirar?")
            f = int(input("introduz numero de fosforos que queres retirar (1/2/3/4)"))
            diferença = diferença - f


#Jogo
menu()
opção=int(input(print("Qual o modo que queres jogar? ")))
if opção == 1:
    print("Escolheste a opção 1, és o segundo a jogar")
    opcao_1()
if opção == 2:
    print("Escolheste a segunda opção, és o primeiro a jogar")
    opcao_2()
while opção != 1 and opção != 2:
    print("essa opção não existe, escolha a opção 1 ou 2")
    opção=int(input(print("Qual o modo que queres jogar? ")))