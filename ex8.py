n1 = float(input("Digite o primeiro lado:"))
n2 = float(input("Digite o segundo lado:"))
n3 = float(input("Digite o terceiro lado:"))
if n3 == 0:
    print("Numero de lados invalidos")
else:
    p1 = "c"
    p1 = input("Digite q para sair ou c para continuar:")
if p1 == "q":
    print("É um triangulo!!!!")
elif p1 == "c":
    n4 = float(input("Digite o quarto lado:"))
    p1 = input("Digite q para sair ou c para continuar:")
elif p1 == "q":
    print("É um quadrado!!!!")
else:
    n5 = float(input("Digite o quinto lado:"))
    print("É um pentagono!!!!")