def preenche_lista(i):
    while True:
        n = input("Digite um elemento para adicionar à lista (ou 'sair' para terminar): ")
        if n == 'sair':
            break
        i.append(n)

lista = []
preenche_lista(lista)
print("Lista preenchida: {}".format(lista))

