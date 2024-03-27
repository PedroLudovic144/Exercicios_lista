x = 0
v = [45, -89, 32, -12, 33]
def media_vetor(x):
    for i in range(0,5,1):
        x = v[i] + x
    x= x/5
    print(f"A média é: {x}")
print(media_vetor(x))
