from datetime import date

Cinema = []



def inserirsala(cinema):
    nomesala = input("Qual o número da sala")
    nomefilme = input("Qual o nome do filme em exibição?")
    lugares = int(input("Quantos lugares tem a sala?"))
    lugaresvendidos = []
    existe = False
    sala = (nomesala, nomefilme, lugares, lugaresvendidos)
    for i in cinema:
        if i[0] == nomesala or i[1] == nomefilme:
            print("já existe")
            existe = True
    if not existe:    
            cinema.append(sala)

    print("As salas:", cinema)
    
def listar(cinema):
    print('Sala          Filme')
    print('                    ')
    for sala in cinema:
        print(f' {sala[0]}          {sala[1]}')
    today = date.today()
    print('                        ')
    print(today)
    
def listardisponibilidades( cinema ):
    print('Sala          Filme          Nº lugares disponíveis')
    for sala in cinema:
        print(f"{sala[0]}             {sala[1]}           {sala[2]- len(sala[3])}")
        today = date.today()
    print("                            ")
    print(today)
    
def disponivel( cinema, filme, lugar ):
    filme_existe = False
    for sala in cinema:
        if filme == sala[1]:
            if lugar in sala[3]:
                print('False')
            else:
                print('True')
            filme_existe = True
    if not filme_existe:
        for sala in cinema:
            print("Filme não se encontra em exposição.")
        
def vendebilhete( cinema, filme, lugar ):
    lugar_vendido = False
    for sala in cinema:
        if filme == sala[1] :
            if lugar not in sala[3]:
                sala[3].append(lugar)
                print(f'Bilhete vendido para o lugar {lugar}')
                lugar_vendido = True
            else:
                print('Lugar já vendido')
    if not lugar_vendido:
            print('Operação não é possível')
    print('Sala          Filme          Lugares Ocupados')
    print('                                             ')
    for sala in cinema:
        print(f'{sala[0]}         {sala[1]}              {sala[3]}')
    today = date.today()
    print('                                            ')
    print(today)


def menu():
    print('''
1) Criar Sala
2) Listar Cinema
3) Listar Disponibilidade
4) Confirmar Disponibilidade
5) Vender Bilhete
0) Sair''')

op = -1
while op!= 0:
    menu()
    op= int(input("Escolhe uma opção"))
    if op == 1:
        inserirsala(Cinema)
    elif op == 2:
          listar(Cinema)
    elif op == 3:
        if Cinema == []:
            print('Cinema sem filmes em exposição')
        else:
            listardisponibilidades(Cinema)
    elif op == 4:
        if Cinema == []:
            print('Cinema sem filmes em exposição')
        else:
            filme = input('Qual o filme que deseja ver? ')
            lugar = int(input('Qual o lugar que deseja? '))
            disponivel(Cinema, filme, lugar)
    elif op == 5:
        if Cinema == []:
            print('Cinema sem filmes em exposição')
        else:
            filme = input('Qual o filme que deseja ver? ')
            lugar = int(input('Qual o lugar que deseja? '))
            vendebilhete(Cinema, filme, lugar)
    elif op not in [0, 1, 2, 3, 4, 5]:
        print('Opção inválida')
print('Programa Encerrado.')