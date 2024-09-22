#jogo com utilizador a adivinhar
from random import randint
num1=int(randint(0,100))
num=int(input("escolha um número de 0 a 100"))
tentativas=1
while num!=num1:
    if num<num1:
        print ("o número que pensei é maior")
    else:
        print ("o número que pensei é menor")
    tentativas=tentativas+1
    num=int(input("escolha outro número de 0 a 100"))
resultado="Acertou com "+ str(tentativas) + " tentativas"
print(resultado)