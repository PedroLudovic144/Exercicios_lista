alunos = {}

def adicionar_aluno(d: dict) -> None:
    while len(d) < 10:
        nome = input("Coloque o nome do aluno: ").strip()
        if not nome:
            print("Nome não pode ser vazio.")
            continue
        
        while True:
            nota_str = input("Coloque a nota do aluno (0 a 10): ").strip()

            if nota_str.replace('.', '', 1).isdigit() and nota_str.count('.') <= 1:
                nota = float(nota_str)

                if 0 <= nota <= 10:
                    d[nome] = nota
                    break
                else:
                    print("Nota inválida. A nota deve estar entre 0 e 10.")
            else:
                print("Entrada inválida. Por favor, insira um número válido.")
        
        if len(d) < 10:
            continuar = input("Deseja adicionar outro aluno? (s/n): ").strip().lower()
            if continuar != 's':
                break
        else:
            print("Limite de 10 alunos atingido.")
            break

    
def editar_aluno(d: dict) -> None:
    escolha = input("O que você quer mudar (nome ou nota): ").strip()
    
    if escolha == 'nome':
        novo_nome = input("Escreva o novo nome do aluno: ").strip()
        d['nome'] = novo_nome
    elif escolha == 'nota':
        nova_nota_str = input("Escreva a nova nota do aluno: ").strip()
        
        # Validação da nota para garantir que seja um número válido
        if nova_nota_str.replace('.', '', 1).isdigit() and nova_nota_str.count('.') <= 1:
            nova_nota = float(nova_nota_str)
            d['nota'] = nova_nota
        else:
            print("Nota inválida. Por favor, insira um número válido entre 0 e 10.")
    else:
        print("Escolha inválida. Por favor, escolha 'nome' ou 'nota'.")

def listar_alunos(d: dict) -> dict:
    for k,v in d.items():
        print(f"{k} -> {v}")

def deleta_aluno(d: dict) -> None:
    selc_aluno = input("Qual aluno você quer deletar ?")
    del d[selc_aluno]

def calcula_media(d: dict) -> float:
    s = 0
    c = 0  
    for k, v in d.items():
        s += v  
        c += 1  
    media = s / c  
    print(f"A média dos alunos é: {media:.2f}")  
    return media  

def consulta_aluno(d: dict) -> dict:
    while True:
        aluno_cons = input("Digite o nome do aluno a ser consultado: ")
        if aluno_cons in d:
            resultado = {aluno_cons: d[aluno_cons]}  # Retorna o nome e a nota do aluno como um dicionário
            print(resultado)
            return resultado
        else:
            print("Esse aluno não existe, digite novamente.")

def apaga_geral(d: dict) -> None:
    d.clear()  # Apaga todos os itens do dicionário


