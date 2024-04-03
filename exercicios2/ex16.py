v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]
def conta_acima_media(v):
    media = sum(v) / len(v)
    return sum(1 for num in v if num > media)
x = conta_acima_media(v1)
print(x) 