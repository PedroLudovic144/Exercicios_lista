v = [45, -89, 32, -12, 33]
def impares_vetor(v):
    for i in range(0, 5, 1):
        if v[i]%2==1:
            print(v[i])
print(impares_vetor(v))