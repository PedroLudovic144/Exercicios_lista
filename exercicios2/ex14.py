v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]
def ordena_vetor(v, forma):
    if forma == 'c':
        v.sort() 
    elif forma == 'd':
        v.sort(reverse=True)
ordena_vetor(v1, 'c')
print(v1) 