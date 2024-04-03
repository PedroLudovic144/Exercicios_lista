def busca(vetor, valor):
    if valor in vetor:
        return True
    else:
        return False


v = [45, -89, 32, -12, 33]
x = busca(v, 32)
print(x)  
