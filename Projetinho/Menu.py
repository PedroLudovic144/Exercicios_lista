import os

os.system("cls")

from Escola import *
alunos = {}
while True:
    print("""
            0 - SAIR
            1 - Adicionar novo Aluno | Nota (limite 10 alunos)
            2 - Editar Aluno | Nota
            3 - Listar os Alunos
            4 - Excluir um Aluno
            5 - Calcular a média da turma
            6 - Consultar um aluno
            7 - Apagar todos os alunos da sala
        Escolha: 

         """)
    
    opcao = input("Escolha: ")
    if not opcao.isnumeric():
        input("Opção inválida!\nPressione alguma tecla para continuar . . .")
        continue
    opcao = int(opcao)
    match opcao:
        case 0:
            break
        case 1:
            print(adicionar_aluno(alunos))

        case 2:
            print(editar_aluno(alunos))

        case 3:
            print(listar_alunos(alunos))

        case 4:
            print(deleta_aluno(alunos))

        case 5:
            print(calcula_media(alunos))

        case 6:
            print(consulta_aluno(alunos))
        case 7:
            print(apaga_geral(alunos))
        case _:
            print("\n-----Insira uma opção válida!-----") 