v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]
def separa_pares_impares(v):
    v.sort(key=lambda x: x % 2)
separa_pares_impares(v1)
print(v1)