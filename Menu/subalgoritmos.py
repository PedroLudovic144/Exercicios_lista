v = [45, -89, 32, -12, 33]
v1 = [41, 72, 39, 4, 35]
v2= [0, 0, 0, 0, 0]
#1
def primeiroElemento(v: list) -> int:
    print(f"O primeiro elemento do vetor {v[0]}")

#2
def numerosNegativos(v: list) -> int:
    for i in range(0, 5):
        if v[i] < 0:
            print(f'{v[i]}')
#3
def soma_elementos(v):
    soma = 0
    for elemento in v:
        soma += elemento
    return soma
    x = soma_elementos(v)
    print(x)
#4
def mediav(v: list) -> float:
    soma = v[0]
    x = 0
    for i in range(0, 5, 1):
        x = v[i] + x
    x = x / 5
    print(f"A média é: {x}")
#5
def numerosImpares(v: list) -> int:
    for i in range(0, 5, 1):
        if v[i] % 2 == 1:
            print(v[i])
#6
def exibeExtremos(v: list) -> int:
    primeiro, *_, ultimo = v
    print(primeiro, ultimo)
#'*_' = é usado para ignorar os elementos entre o primeiro e o ultimo numero do vetor

#7
def IndiceImpar(v: list):
    for i in range(0, 5, 1):
        if i % 2 != 0:
            print(v[i])
#8
def busca(v: list,) -> bool:
    valor = 32
    if valor in v:
        return True
    else:
        return False
#9
def ordenav(v: list):
    v.sort()
    print(*v)
# para ordenar uma lista em ordem crescente
# '*' separa por espaços os elementos do vetor
#10
def copiavetor(v1: list, v2: list):
    for i in range(0, 5, 1):
        v2[i] = v1[i]
    print(v2)
#11
def invertevetor(v1: list, v2: list):
    v2[:] = v1[::-1]
    print(v2)
#v1[::-1] = cria uma copia invertida de v1
#v2[:] = v1[::-1] = atribui v1 em v2

#12
def ordenavetorCrescente(v1: list):
    v1.sort()
    print(v1)
#sort = Ordena o vetor em ordem crecente

#13
def ordenavDecrescente(v1: list):
    v.sort(reverse=True)
    print(v1)
#14
def ordena_vetor(v1: list, forma: str):
    if forma.lower() == 'c':
        v1.sort()
        print(v1)
    elif forma.lower() == 'd':
        v1.sort(reverse=True)
        print(v1)
    else:
        print("Digite ou C (crecente) ou D (decrecente)")

#15
def separaParesImpares(v1: list):
    pares = []
    impares = []
    lista = []
    for num in v1:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    lista = pares + impares
    print(lista)
#v1.sort(key=lambda x: x % 2)
#print(v1)

#16
def contaAcimaMedia(v1: list):
    media = sum(v1) / len(v1)
    cont = 0
    for num in v1:
        if num > media:
            cont += 1
    print(cont)
#sum = soma os elementos do vetor

#17
def maior_elemento(v1: list):
    return max(v)
x = maior_elemento(v1)
print(x)