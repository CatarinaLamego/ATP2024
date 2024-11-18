
#Tpc1

#a)
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8] 
ncomuns = [x for x in lista1 + lista2 if (x in lista1)!= (x in lista2)]
 
#b)
texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
lista = [x for x in texto.split(" ") if len(x)>= 3]

#c)
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [x for x in enumerate(lista)]

#TPc2
#a)
def strCount(s, subs):
    contador = 0
    i = 0
    while i <= len (s) - len(subs):
        if s[i:i+len(subs)] == subs:
            contador += 1
            i += len(subs)
        else: 
            i += 1
    return contador

#b)
def produtoM3(lista):
    baixo1 = lista[0]
    baixo2 = lista[1]
    baixo3 = lista[2]
    for valor in lista:
        if valor < baixo1:
            baixo3 = baixo2
            baixo2 = baixo1
            baixo1 = valor
        elif valor < baixo2:
            baixo3 = baixo2
            baixo2 = valor
        elif valor < baixo3:
            baixo3 = valor
    res = baixo1*baixo2*baixo3
    return res  

#c)
def reduxInt(n):
    while n >= 10:
        soma = 0
        for digito in str(n):
            soma += int(digito)
        n = soma

    return n

#d)
def myIndexOf(s1, s2):
    i = 0
    res = -1
    while i <= len(s1) - len(s2):
        if s1[i:i+len(s2)] == s2:
            res = i
            i += 1
        else:
            i += 1
    return res

#TPC3

#a)
def quantosPost(redeSocial):
    contador = 0
    for dicionario in redeSocial:
        contador += 1
    return contador

#b)
def postsAutor(redeSocial, autor):
    lista = []
    for posts in redeSocial:
        if autor in posts["autor"]:
            lista.append(posts)
   
    return lista 
post1 = {"autor": "josé", "conteudo": "biologia"}
post2 = {"autor": "josé", "conteudo": "educação"}
redesocial1 = [post1, post2]
#print(postsAutor(redesocial1, "josé"))

#c)
def autores(redeSocial):
    lista=[]
    for posts in redeSocial:
        if "autor" in posts:
            lista.append(posts["autor"])
    return  lista

#d)
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    n = len(redeSocial) + 1
    id = f"p{n}"
    post = {"id" : id, "conteudo" : conteudo, "autor" : autor, 'dataCriacao': dataCriacao, 'comentarios': comentarios}
    redeSocial.append(post)
    return redeSocial
p1 = {"id":"p1","autor": "josé", "conteudo": "biologia"}
p2 = {"id":"p2", "autor": "josé", "conteudo": "educação"}
redesocial1 = [p1, p2]
#print(insPost(redesocial1, "jejum", "tomé", "3/11/2024", "mucho bom"))


#e)
def remPost(redeSocial, id):
    Redesocialatualizada = []
    for posts in redeSocial:
        if posts[0] != id:
            Redesocialatualizada.append(posts)
    return Redesocialatualizada


#f)
def postsPorAutor(redeSocial):
    dicposts = {}
    for post in redeSocial:
        autor = post.get("autor")
        if autor in dicposts:
            dicposts[autor] += 1
        else:
            dicposts[autor] = 1
    return dicposts
p1 = {"id":"p1","autor": "josé", "conteudo": "biologia"}
p2 = {"id":"p2", "autor": "tomé", "conteudo": "educação"}
redesocial1 = [p1, p2]
#print(postsPorAutor(redesocial1))

#g)
def comentadoPor(redeSocial, autor):
    lista = []
    for post in redeSocial:
        if "comentarios" in post:
            for comentario in post["comentarios"]:
                if comentario.get("autor") == autor:
                    lista.append(post)
    return lista
p1 = {"id":"p1","autor": "josé", "conteudo": "biologia", "comentarios":[{"autor": "josé", "texto": "muito bom"}]}
p2 = {"id":"p2", "autor": "tomé", "conteudo": "educação"}
redesocial1 = [p1, p2]
#print(comentadoPor(redesocial1, "josé"))




