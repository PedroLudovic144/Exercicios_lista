# Inicializando o dicionário com 3 chaves e valores iniciais
meu_dict = {'nome': '', 'idade': '', 'cidade': ''}

# Função para exibir o menu
def exibir_menu():
    print("\nMenu de opções:")
    print("0 - Sair")
    print("1 - Preencher dicionário")
    print("2 - Exibir dicionário (dado a dado)")
    print("3 - Editar dicionário")
    print("4 - Criar nova Key")
    print("5 - Excluir Key")
    print("6 - Excluir todas as Keys")

# Função para preencher o dicionário
def preencher_dicionario():
    for chave in meu_dict:
        try:
            valor = input(f"Digite o valor para '{chave}': ")
            meu_dict[chave] = valor
        except Exception as e:
            print(f"Erro ao preencher o dicionário: {e}")

# Função para exibir o dicionário
def exibir_dicionario():
    if meu_dict:
        for chave, valor in meu_dict.items():
            print(f"{chave}: {valor}")
    else:
        print("O dicionário está vazio.")

# Função para editar uma chave existente no dicionário
def editar_dicionario():
    chave = input("Digite a chave que deseja editar: ")
    if chave in meu_dict:
        try:
            novo_valor = input(f"Digite o novo valor para '{chave}': ")
            meu_dict[chave] = novo_valor
        except Exception as e:
            print(f"Erro ao editar o dicionário: {e}")
    else:
        print("Chave não encontrada.")

# Função para criar uma nova chave
def criar_nova_key():
    nova_chave = input("Digite o nome da nova chave: ")
    if nova_chave not in meu_dict:
        try:
            valor = input(f"Digite o valor para '{nova_chave}': ")
            meu_dict[nova_chave] = valor
        except Exception as e:
            print(f"Erro ao adicionar nova chave: {e}")
    else:
        print("Chave já existe.")

# Função para excluir uma chave
def excluir_key():
    chave = input("Digite a chave que deseja excluir: ")
    if chave in meu_dict:
        try:
            del meu_dict[chave]
            print(f"Chave '{chave}' excluída.")
        except Exception as e:
            print(f"Erro ao excluir a chave: {e}")
    else:
        print("Chave não encontrada.")

# Função para excluir todas as chaves
def excluir_todas_as_keys():
    confirmar = input("Tem certeza que deseja excluir todas as chaves? (s/n): ")
    if confirmar.lower() == 's':
        meu_dict.clear()
        print("Todas as chaves foram excluídas.")
    else:
        print("Operação cancelada.")

# Função principal que exibe o menu e gerencia as opções
def main():
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        
        if opcao == 0:
            print("Saindo do programa...")
            break
        elif opcao == 1:
            preencher_dicionario()
        elif opcao == 2:
            exibir_dicionario()
        elif opcao == 3:
            editar_dicionario()
        elif opcao == 4:
            criar_nova_key()
        elif opcao == 5:
            excluir_key()
        elif opcao == 6:
            excluir_todas_as_keys()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executando a função principal
if __name__ == "__main__":
    main()
