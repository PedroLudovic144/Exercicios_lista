from subalgoritmos import *

import os
while True:
    os.system("cls")
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
            print(mostra_elemento(v))
        case 2:
            print(mostra_negativo(v))
        case 3:
            print(soma_vetor(x))
        case 4:
            print(media_vetor(x))
        case 5:
            print(impares_vetor(v))
        case 6:
             print(exibe_extremos(v))
        case 7:
            print(exibe_indice_impar(v))
        case 8:
            print(busca(v,valor=32))
        case 9:
            print(ordena(v))
        case 10:
            print(copia_vetor(v1, v2))
        case 11:
            print(inverte_vetor(v1, v2))
        case 12:
            print(ordena_vetor_crescente(v))
        case 13:
            print(ordena_vetor_decrescente(v))
        case 14:
            print(ordena_vetor(v1, v2))
        case 15:
            print(separa_pares_impares(v))
        case 16:
            print(conta_acima_media(v))
        case 17:
            print(maior_elemento(v))

    input("Digite algo para continuar . . .")