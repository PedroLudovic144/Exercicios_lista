def exibicao_manual(d: dict) -> None:
    print(f"Nome.....: {d['nome']}")
    print(f"idade....: {d['idade']}")
    print(f"Casado...: {d['casado']}")
    print(f"Peso.....: {d['peso']}")

def exibicao_metodos(d: dict) -> None:
    for k, v in d.items():
        print(f"{k} -> {v}")



import os
os.system("cls")
dicionario = {} # ou dict()
print(dicionario)
contato = {
    # 'key' : value,
    'nome' : 'Edson',
    'idade': 50,
    'casado': True,
    'peso': 80.9,
}
# Exibição bruta
print(contato)

# Exibição manual
print(f"Nome.....: {contato['nome']}")
print(f"idade....: {contato['idade']}")
print(f"Casado...: {contato['casado']}")
print(f"Peso.....: {contato['peso']}")

# Adicionar uma nova key
print(contato)
contato['altura'] = 1.70
print(contato)

# Remover uma key
# print(contato)
# del contato['altura']
# contato.pop('nome')
# print(contato)

# manipulando as keys
os.system("cls")
# bruto
print(contato.keys())
# colocandoemuma lista
print(list(contato.keys()))
# individualmente
for chave in contato.keys():
    print(chave)

# values
os.system("cls")
print(contato.values())
print(list(contato.values()))
for chave in contato.values():
    print(chave)

# manipulando os items
os.system("cls")
print(contato.items())
print(list(contato.items()))
for k, v in contato.items():
    print(f"{k} -> {v}")


os.system("cls")

exibicao_manual(contato)
del contato['nome']
exibicao_metodos(contato)