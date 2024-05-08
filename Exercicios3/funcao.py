def preenche_lista(i):
    while True:
        n = input("Digite um elemento para adicionar à lista (ou 'sair' para terminar): ")
        if n == 'sair':
            break
        i.append(n)
def exibe_lista(l):
    for i in l:
        print(i)
def conta_elementos(l):
    c = 0
    for i in l:
        if i is not None:
            c += 1
    return c
def retorna_indice(elemento):
    n = int(input("Digite o índice do valor a ser procurado: "))  # Convertendo para inteiro
    for i in range(len(elemento)):
        if i == n:
            return elemento[i]
    return -1
def busca(l, elemento):
    c = 0

    for i in l:
        if i == elemento:
            c += 1
    return c
def conta_inteiro(l):
    contador = 0
    for elemento in l:
        if isinstance(elemento, int): 
            contador += 1
    return contador