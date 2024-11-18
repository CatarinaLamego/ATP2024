#TabMeteo = [(Data,TempMin,TempMax,Precipitacao)]
tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

def medias(tabMeteo):
    media = []
    for valor in tabMeteo:
        data = valor[0]
        média = (valor[2] + valor[1])/2
        media.append((média, data))
    return media


def guardar(tabMeteo, fnome ):
    f= open(fnome, "w")
    for data, tmin, tmax, precip in tabMeteo:
        linha = f"{data[0]} -- {data[1]} -- {data[2]} -- {tmin} -- {tmax} -- {precip}\n"
        f.write(linha)
    f.close()
    return f

def carregar(fnome):
    res = []
    ficheiro = open(fnome)
    for linha in ficheiro:
        if linha != "":
            campos = linha.split(" -- ")
            data = (int(campos[0]), int(campos[1]), int(campos[2])) 
            res.append((data, float(campos[3]),  float(campos[4]) ) )  
    ficheiro.close()
    return res  
    
    
#guardar(tabMeteo1, "tabelameteorologica.txt")
#tabMeteo2 = carregar("tabelameteorologica.txt")
#print(tabMeteo2)

def minMin(tabMeteo):
    tmin = tabMeteo[0][1]
    for valor in tabMeteo:
        if valor[1] < tmin :
            tmin = valor[1]
    return tmin

#print(minMin(tabMeteo1))

def amplTerm(tabMeteo):
    res = []
    for valor in tabMeteo:
        data = valor[0]
        amp = valor[2] - valor[1]
        res.append((data,amp))
    return res

def maxChuva(tabMeteo):
    chuvamax = tabMeteo[0][3]
    for valor in tabMeteo:
        data = valor[0]
        if valor[3] > chuvamax :
            chuvamax = valor[3]
    return chuvamax, data

def diasChuvosos(tabMeteo, p):  
    res = []
    for valor in tabMeteo:
        data = valor[0]
        if valor[3] > p:
            precip = valor[3]
            res.append((data, precip))
    return res


def maxPeriodoChuva(tabMeteo, p):
    consecutivos = 0
    contador = 0
    for *_, precip in tabMeteo:
        if precip < p:
            contador = contador + 1
        else:
            if consecutivos < contador:
                consecutivos = contador
            contador = 0
    if consecutivos < contador:
            consecutivos = contador
    return consecutivos


import matplotlib.pyplot as plt
def grafTabMeteo(t):
    x1 = []
    y1 = []
    y2 = []
    y3 = []
    for data, tmin, tmax, precipit in t:
        data1 = f"{data[0]}/{data[1]}/{data[2]}"
        x1.append(data1)
        y1.append(tmin)
        y2.append(tmax)
        y3.append(precipit)


    plt.plot(x1, y1, label = "Temp. mínima", marker='o', markerfacecolor='blue', markersize=6)
    plt.plot(x1, y2, label = "Temp. máxima", marker='o', markerfacecolor='orange', markersize=6)
    plt.xlabel('Data')
    plt.ylabel('Temperatura ºC')
    plt.title('Temperatura mínima e máxima')
    plt.legend()
    plt.show()
    

    plt.bar(x1,y3, color = 'skyblue')
    plt.xlabel('Data')
    plt.ylabel('Pluviosidade')
    plt.title('Pluviosidade')
    plt.show()


def menu():
    print(""")
    1- média das temperaturas;
    2- guardar tabela meteorológica em ficheiro;
    3- carregar tabela meteorológica;
    4- averiguar a temperatura mais baixa;
    5- amplitude térmica;
    6- valor máximo de precipitação;
    7- averiguar dias em que a precipitação é maior que p;
    8- maior número de dias consecutivos de chuva dentro de p;
    9- gráficos de máxima e mínima plusividade   
    0- Sair 
         """)

menu()
op = int(input("Introduza uma opção: "))
while op != 0:
    if op == 1:
        print("Média das temperaturas:", medias(tabMeteo1))
    elif op == 2:
        fnome = input("Escolhe o nome do ficheiro com que queres guardar (acabar com .txt): ")
        guardar(tabMeteo1, fnome)
        print(f"Tabela meteorológica guardada no ficheiro {fnome}.")
    elif op == 3:
        fnome = input("Qual o nome do ficheiro que pretendes carregar? ")
        tabela = carregar(fnome)
        print("Tabela carregada:", tabela)
    elif op == 4:
        print("Temperatura mais baixa:", minMin(tabMeteo1))
    elif op == 5:
        print("Amplitude térmica:", amplTerm(tabMeteo1))
    elif op == 6:
        print("Valor máximo de precipitação:", maxChuva(tabMeteo1))
    elif op == 7:
        p = float(input("Qual o limite p? "))
        print("Dias com precipitação maior que p:", diasChuvosos(tabMeteo1, p))
    elif op == 8:
        p = float(input("Qual o valor de p? "))
        print("Maior número de dias consecutivos de chuva dentro de p:", maxPeriodoChuva(tabMeteo1, p))
    elif op == 9:
        grafTabMeteo(tabMeteo1)
    else:
        print("Essa opção é inválida, escolhe outra opção.")
    menu()
    op = int(input("Introduz a opção que pretendes realizar: "))
print("Obrigada!")