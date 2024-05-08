def retorna_indice(elemento,n):
    for i in range(len(elemento)):
        if elemento == n:
            return elemento[i]
        else:
            return -1
        
import os
os.system("cls")

n = int(input("Digite o índice do valor a ser procurado: "))
lista1 = [5, 7, 8, 9, 7]
resultado = retorna_indice(lista1,5)
print(resultado)
#Pegue uma lista e retorne todos os indeces de uma lista
#Retornar true se uma LISTA SÓ CONTEM DADOS INTEIROS
#29/05/