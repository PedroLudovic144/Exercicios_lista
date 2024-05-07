def conta_inteiro(l):
    contador = 0
    for elemento in l:
        if isinstance(elemento, int): 
            contador += 1
    return contador

lista_exemplo = [1, 2, 'a', 3.5, 4, 'b', 5]
resultado = conta_inteiro(lista_exemplo)
print('A lista possui {} elementos inteiros.'.format(resultado))
