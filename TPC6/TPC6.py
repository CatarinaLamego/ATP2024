turma = []

def criarTurma(turma):
    elems = int(input("Quantos elementos tem a turma"))
    while elems > 0 and len(turma) < elems:
        nome = input("Qual o nome do aluno")
        id = int(input("Qual a id do aluno?"))
        notaTPC = float(input("Qual a nota TPC?"))
        notaProj = float(input("Qual a nota do projeto?"))
        notaTeste = float(input("Qual a nota do teste?"))
        aluno = (nome, id, [notaTPC, notaProj, notaTeste])
        if aluno[0] and aluno[1] not in turma:
            turma.append(aluno)
            print("Aluno adicionado com sucesso.")
        else:
            print("Esse aluno já foi adicionado.")

def inserirAluno(turma, aluno):
    if aluno in turma:
        print("Esse aluno já existe.")
    else:   
        turma.append(aluno)      
        
def listarTurma(turma):
    print("Nome do aluno      iD               Notas"            )
    for aluno in turma:
        print(f"         {aluno[0]}     {aluno[1]}       {aluno[2]}")

        
def consultarId(turma):
    id = int(input("Qual a id do aluno que queres consultar?"))
    i = 0
    while i < len(turma):
        if turma[i][1] == id:
            print(turma[i])
        i = i + 1

def guardarturma(turma):
    f = open ("turmabiomficheiro.txt", "w")
    for aluno in turma:
        linha = f"{aluno[0]}::{aluno[1]}::{aluno[2][0]}::{aluno[2][1]}::{aluno[2][2]}\n"
        f.write(linha)
    f.close()
    print("Ficheiro guardado em turmabiomficheiro.txt")

def carregarturma(fnome):
    res = []
    ficheiro = open(fnome)
    for linha in ficheiro:
        if linha != "":
            campos = linha.split("::")
            notas = (float(campos[2]), float(campos[3]), float(campos[4]))
            res.append((campos[0], campos[1], notas))
    ficheiro.close()
    return print(res)

def menu():
    print("""Menu:
    1) Criar turma
    2) Inserir aluno na turma
    3) Listar turma
    4) Consultar aluno por id
    5) Guardar a turma em ficheiro
    6) Carregar uma turma dum ficheiro
    0) Sair""")


menu()
op =int( input("Escolhe uma opção"))
while op != 0:
    if op == 1:
        criarTurma(turma)
    elif op == 2:
        nome = input("Qual é o nome do aluno")
        id = int(input("Qual a id do aluno?"))
        notaTPC = float(input("Qual a nota TPC?"))
        notaProj = float(input("Qual a nota do projeto?"))
        notaTeste = float(input("Qual a nota do teste?"))
        aluno = (nome, id, [notaTPC, notaProj, notaTeste])
        inserirAluno(turma, aluno)
    elif op == 3:
        if turma == []:
            print("Esta turma não tem elementos, adiciona primeiro alunos à turma.")
        else:
            listarTurma(turma)
    elif op == 4:
        if turma == []:
            print("A turma não existe")
        else:
            consultarId(turma)
    elif op == 5:
        if turma == []:
            print("A turma não existe")
        else:
            guardarturma(turma)
    elif op == 6:
        carregarturma("turmabiom.txt")
    else:
        print("Essa opção é inválida, escolhe outra opção.")
    menu()
    op = int(input("introduz a opção que pretendes realizar"))

print("Obrigada, volte sempre!")