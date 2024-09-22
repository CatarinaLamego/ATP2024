#jogo com computador a adivinhar
from random import randint
num=int(input("escolha um número de 0 a 100"))
min=0
max=100
num1=int(randint(min,max))
tentativas=1
while num!=num1:
    if num1<num:
        print ("o número que pensei é maior")
        min=min+1
    else:
        print ("o número que pensei é menor")
        max=max-1
    num1=int(randint(min,max))
    tentativas=tentativas+1
resultado="Acertou com "+ str(tentativas) + "tentativas"
print(resultado)