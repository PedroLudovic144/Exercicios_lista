v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]
def copia_vetor(v1, v2):
    for i in range(len(v1)):
        v2[i] = v1[i]
copia_vetor(v1, v2)
print(v2)