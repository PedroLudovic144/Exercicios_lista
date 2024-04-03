def exibe_indice_impar(vetor):
    elementos_indice_impar = [vetor[i] for i in range(len(vetor)) if i % 2 != 0]
    print(*elementos_indice_impar)


v = [45, -89, 32, -12, 33]
exibe_indice_impar(v)  
