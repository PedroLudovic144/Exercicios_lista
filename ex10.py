n1 = (float(input("Digite o primeiro lado:")))
n2 = (float(input("Digite o segundo lado:")))
n3 = (float(input("Digite o terceiro lado:")))
if n1 == n2 ==n3:
    print("É um triangulo equilatero")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("É um triangulo isóceles")
else:
    print("É um triangulo escaleno")