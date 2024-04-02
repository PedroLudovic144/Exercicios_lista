import os
os.system("cls")
while True:
    opc = int(input("0 - Sair\n1 - Ex 1\n2 - Ex 2\n3 - Ex 3\n4 - Ex 4\n5 - Ex 5\n"))
    match opc:
        case 0:
            break
        case 1:
            import exercicios2.ex1v as ex1v
            ex1v
            os.system("pause")
        case 2:
            import ex2v
            ex2v
            os.system("pause")
        case 3:
            import ex3v
            ex3v
            os.system("pause")
        case 4:
            import exv4
            exv4
            os.system("pause")
        case 5:
            import ex5v
            ex5v
            os.system("pause")
        case _:
            print("Digite uma opção Válida!")

