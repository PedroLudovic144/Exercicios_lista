a1 = float(input("Digite o valor do primeiro ângulo: "))
a2 = float(input("Digite o valor do segundo ângulo: "))
a3 = float(input("Digite o valor do terceiro ângulo: "))

if a1 + a2 + a3 == 180 and a1 == 90:
    print("O triângulo é retângulo")
elif a1 + a2 + a3 == 180 and a1 > 90:
    print("O triângulo é obtusângulo")
elif a1 + a2 + a3 == 180 and a1 < 90:
    print("O triângulo é acutângulo")
else:
    print("Os ângulos não formam um triângulo")