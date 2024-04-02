contador_acima_nove = 0
soma_notas = 0

for aluno in range(1, 11):
    print("\n")
    menor_nota = 11
    for nota in range(1, 4):
        nota_input = input("Digite a nota {0} do aluno {1} (ou pressione Enter para pular): ".format(nota, aluno))

        while not nota_input.strip():  # Loop enquanto a entrada estiver vazia
            print("Nota não digitada. Por favor, digite a nota.")
            nota_input = input("Digite a nota {0} do aluno {1} (ou pressione Enter para pular): ".format(nota, aluno))

        nota_aluno = float(nota_input)
        if nota_aluno < 0 or nota_aluno > 10:
            print("\nNota inválida, a nota deve estar entre 0 e 10.")
            while nota_aluno < 0 or nota_aluno > 10:
                nota_input = input("Digite novamente a nota {0} do aluno {1}: ".format(nota, aluno))
                if nota_input.strip():
                    nota_aluno = float(nota_input)

        if nota_aluno < menor_nota:
            menor_nota = nota_aluno

        soma_notas += nota_aluno

    media_aluno = (soma_notas - menor_nota) / 2
    if media_aluno >= 9:
        contador_acima_nove += 1

media_turma = soma_notas / 20
print("\n")
print(f"Média da sala: {media_turma:.2f}")
print(f"Número de alunos com nota 9 ou acima: {contador_acima_nove}")
