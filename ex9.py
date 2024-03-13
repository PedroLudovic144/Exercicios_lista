n1 = int(input("digite o primeiro numero:"))
n2 = int(input("digite o segundo numero:"))
n3 = int(input("digite o terceiro numero:"))
if n1 == n2 or n2 == n3 or n1 == n3:
    print("numeros repetidos digite outros numeros")
    exit()
    
if n1 > n2:
    print(n1)

elif n2 > n3:
    print(n2)

else:
    print(n3)