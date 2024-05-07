def busca(l, elemento):
    c = 0

    for i in l:
        if i == elemento:
            c += 1
    return c
lista1 = [1, 2, 2, 3, 4, 2, 5, 2]
n = int(input("Digite o numero a ser procurado:"))
resultado = busca(lista1,n)
print("Ele se repete {} vezes".format(resultado))
