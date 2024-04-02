v = [45, -89, 32, -12, 33]
def mostra_negativo(v):
    for i in range(0, 5):
        if v[i] < 0:
            print(f'{v[i]}')
print(mostra_negativo(v))