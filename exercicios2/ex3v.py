
x = 0
v = [45, -89, 32, -12, 33]
def soma_vetor(x):
    for i in range(0,5,1):
        x = v[i] + x
    print(f"A soma é: {x}")
print(soma_vetor(x))
