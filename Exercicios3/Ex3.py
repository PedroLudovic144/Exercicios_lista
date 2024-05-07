def conta_elementos(l):
    c = 0
    for i in l:
        if i is not None:
            c += 1
    return c
lista1 = [5, 7, 8, 9, None]
resultado = conta_elementos(lista1)
print(resultado)
