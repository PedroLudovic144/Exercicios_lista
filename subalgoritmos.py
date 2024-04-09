v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]
def mostra_elemento(v):
    v = [45, 34, 23, 12, 67]
    print(f"O primeiro elemento do vetor {v[0]}")
def mostra_negativo(v):
    for i in range(0, 5):
        if v[i] < 0:
            print(f'{v[i]}')
def soma_vetor(x):
    for i in range(0,5,1):
        y = v[i] + x
    print(f"A soma é: {y}")
def media_vetor(x):
    for i in range(0,5,1):
        x = v[i] + x
    x= x/5
    print(f"A média é: {x}")
v = [45, -89, 32, -12, 33]
def impares_vetor(v):
    for i in range(0, 5, 1):
        if v[i]%2==1:
            print(v[i])
def exibe_extremos(vetor):
    primeiro_elemento = vetor[0]
    ultimo_elemento = vetor[-1]
    print(primeiro_elemento, ultimo_elemento)

v = [45, -89, 32, -12, 33]
exibe_extremos(v)
def exibe_indice_impar(vetor):
    elementos_indice_impar = [vetor[i] for i in range(len(vetor)) if i % 2 != 0]
    print(*elementos_indice_impar)


v = [45, -89, 32, -12, 33]
exibe_indice_impar(v)
def busca(v, valor):
    if valor in v:
        return True
    else:
        return False


v = [45, -89, 32, -12, 33]
x = busca(v,valor=32)
print(x)

def ordena(vetor):
    vetor.sort()
    print(*vetor)


v = [45, -89, 32, -12, 33]
ordena(v)
# outros vetores
def copia_vetor(v1, v2):
    for i in range(len(v1)):
        v2[i] = v1[i]
copia_vetor(v1, v2)
print(v2)
def inverte_vetor(v1, v2):
    for i in range(len(v1)):
        v2[i] = v1[len(v1) - 1 - i]
inverte_vetor(v1, v2)
print(v2)
def ordena_vetor_crescente(v):
    v.sort()
ordena_vetor_crescente(v1)
print(v1)
def ordena_vetor_crescente(v):
    v.sort()
ordena_vetor_crescente(v1)
print(v1)
def ordena_vetor_decrescente(v):
    v.sort(reverse=True)
ordena_vetor_decrescente(v1)
print(v1)
def ordena_vetor(v, forma):
    if forma == 'c':
        v.sort()
    elif forma == 'd':
        v.sort(reverse=True)
ordena_vetor(v1, 'c')
print(v1)
def separa_pares_impares(v):
    v.sort(key=lambda x: x % 2)
separa_pares_impares(v1)
print(v1)
def conta_acima_media(v):
    media = sum(v) / len(v)
    return sum(1 for num in v if num > media)
x = conta_acima_media(v1)
print(x)
def maior_elemento(v):
    return max(v)
x = maior_elemento(v1)
print(x)