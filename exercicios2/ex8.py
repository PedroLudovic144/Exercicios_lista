def busca(v, valor):
    if valor in v:
        return True
    else:
        return False


v = [45, -89, 32, -12, 33]
x = busca(v, 32)
print(x)  
