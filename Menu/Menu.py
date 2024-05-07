import os

os.system("cls")

from subalgoritmos import *

v = [45, -89, 32, -12, 33]
v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]
while True:
    print(""" 
    0. S A I R
    1. Primeiro elemento do vetor. 
    2. Exiba somente os números negativos contidos no vetor.
    3. Soma dos elementos do vetor
    4. Média dos elementos do vetos
    5. Numeros ímpares contidos no vetor
    6. Exibe na tela o primeiro e o ultimo elemento do vetor.
    7. Exibe os elementos cujos índices sejam pares.
    8. Exibe no vetor, senão False.
    9. Ordene os elementos do vetor.
    10.Copia vetor de v1 em v2.
    11. inverte vetor que copie os elementos invertidos do vetor v1 em v2
    12. Ordena vetor em crescente 
    13. Ordena vetor em decrescente 
    14. Ordena vetor que baseando-se em 'c' para crescente ou 'd' para decrescente
    15.Separa pares impares que coloque nas posições mais a esquerda os valores pares e mais a diretia os impares.
    16. Conta acima media que retorne quantos elementos do vetor estão acima da média.
    17.Maior elemento que retorne o elemento de maior valor do vetor.

    """)

    opcao = input("Escolha: ")
    if not opcao.isnumeric():
        input("Opção inválida!\nPressione alguma tecla para continuar . . .")
        continue
    opcao = int(opcao)
    match opcao:
        case 0:
            break
        case 1:
            print(primeiroElemento(v))

        case 2:
            print(numerosNegativos(v))

        case 3:
            print(soma_elementos(v))

        case 4:
            print(mediav(v))

        case 5:
            print(numerosImpares(v))

        case 6:
            print(exibeExtremos(v))

        case 7:
            print(IndiceImpar(v))

        case 8:
            print(busca(v))

        case 9:
            print(ordenav(v))

        case 10:
            print(copiavetor(v1, v2))

        case 11:
            print(invertevetor(v1, v2))

        case 12:
            print(ordenavetorCrescente(v1))

        case 13:
            print(ordenavDecrescente(v1))

        case 14:
            print(ordena_vetor(v1, 'C'))

        case 15:
            print(separaParesImpares(v1))

        case 16:
            print(contaAcimaMedia(v1))

        case 17:
            print(maior_elemento(v1))
        case _:
            print("\n-----Insira uma opção válida!-----") 