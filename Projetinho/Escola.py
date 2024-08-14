dados =
def adc_aluno()  :
    nome = input("Coloque o nome do aluno:")
    nota = input("Coloque a nota do aluno:")
    condicao = True
    while condicao == True:
        if nome in dados:
            print("Aluno já colocado")
            exit()
        else:
            dados = {'nome': nome, 'nota': nota}
            v = input(print("Quer inderir mais um ?(sim ou não)"))
            if v == 'sim' or 'Sim':
                condicao == True
            else:
                condicao == False

        print(dados)
print(adc_aluno())height