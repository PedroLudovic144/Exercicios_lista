"""
l = ["Edson", 12, 1.67, True, 34]
print(f"Exibe a posição 1 da lista: L[1] = {l[1]}")
print(f"Exibe a Lista Inteira: L = {l}")
l[4] = "Edson"
print(f"L = {l}")
"""
lista = list()
#Adiciona um elemento na lista
lista.append(22)
lista.append("Lógica")
print(lista)
#insert add um conteúdo a partir do índice
lista.insert(1, 57.7)
print(lista)
#Pop Excloe em delimitadas posições ou sem () Excloe o ultimo
lista.pop(0)
print(lista)
lista.pop()
print(lista)
#Remove o elemento Pelo Conteúdo da posição
lista = [22, 57.7, "Lógica"]
lista.remove(57.7)
print(lista)
#index mostra o indice a partir do valor
lista = [22, 57.7, "Lógica"]
indice=lista.index("Lógica")
print(f"índice = {indice}")
#Conta Quantas vezes tem um elemento dentro da lista
lista = [22, 22, 57.7, "Lógica"]
qtd = lista.count(22)
print(f"Quantidade = {qtd}")
#len conta quantos elementos tem no vetor
lista = [22, 22, 57.7, "Lógica"]
qtd_elementos = len(lista)
print(f"Quantidade = {qtd_elementos}")
#soma os itens da lista
lista = [19, 4, 25, 33, -5]
print(sum(lista))
# + Concatena
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(f"Lista 1 = {lista1}")
print(f"Lista 2 = {lista2}")
print(f"Lista 3 = {lista3}")
lista2 = lista1 + lista2
lista3= lista2+ lista1
print(f"Lista 3 = {lista3}")
#extend extende uma lista com a a outra
lista1 = [1, 2, 3]
print(f"Lista 1 = {lista1}")
lista2 = [4, 5, 6]
print(f"Lista 2 = {lista2}")
lista2.extend(lista1)
print(f"Lista 2 = {lista2}")
#Copy Copia
lista1 = [1,2,3]
lista2 = lista1.copy()
print(f"Lista 1 = {lista1}")
print(f"Lista 2 = {lista2}")
#Por isso existe o copy para diferenciar as listas criadas
lista1= [1, 2, 3]
lista2= lista1
lista1.append(4)
print(lista1, lista2)
#sort organiza a lista em ordem crescente
lista = [19, 4, 25, 33, -5]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
#inverte o vetor
lista = [19, 4, 25, 33, -5]
lista.reverse()
print(lista)
#clear limpa a lista
lista = [19, 4, 25, 33, -5]
lista.clear()
print(lista)
#del deleta a lista
lista = [19, 4, 25, 33, -5]
del(lista)
