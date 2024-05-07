def retorna_indice(elemento):
    n = int(input("Digite o índice do valor a ser procurado: "))  # Convertendo para inteiro
    for i in range(len(elemento)):
        if i == n:
            return elemento[i]
    return -1

lista1 = [5, 7, 8, 9, 7]
resultado = retorna_indice(lista1)
print(resultado)
