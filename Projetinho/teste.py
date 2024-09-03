import sys
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade_natal": "São Paulo",
    "profissao": "Engenheira"
}
print(pessoa)
nome_pessoa = pessoa["nome"]
print(nome_pessoa)



pessoa["idade"] = 31
pessoa["cidade_natal"] = "Xique-Xique, Bahia"

print(pessoa["idade"],pessoa["cidade_natal"])




pessoa["Estado-civil"] = "Casado"
pessoa["telefone"] = "123-456-7890"
print("Dicionário atualizado:", pessoa)


if "telefone" in pessoa:
    del pessoa["telefone"]
print(pessoa)
"""
del pessoa["telefone"]
"""

amigos = {
    "João": 25,
    "Ana": 30,
    "Carlos": 28
}

for nome, idade in amigos.items():
    print(f"{nome} tem {idade} anos.")

nome_amigo = input("Digite o nome do amigo:").title().strip()
if nome_amigo in amigos:
    print(f"O seu nome é {nome_amigo} e sua idade é {amigos[nome_amigo]}")
else:
    print("Não existe")


quantidade_amigos = len(amigos)
print (f"Existem {quantidade_amigos} amigos na lista")