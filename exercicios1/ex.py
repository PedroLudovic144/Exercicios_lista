"""
import os
os.system("cls")

x = 7
y = 5
res = x + y
print('o resultado da soma entre {} e {} é {}'.format(x,y,res))

idade = int(input("idade:"))
if idade >= 18:
    print("Maior de idade")
else:
    print("menor de idade")

numero = int(input("Numero: "))
if numero < 0:
    print("Negativo!")
elif numero > 0:
    print("Positivo!")
else:
    print("Nulo!") 

Numero = int(input("Numero: 5"))
print(""
1 - Exercico 1
2 - Exercico 2
3 - Exercico 3
4 - Exercico 4      
"")
opcao = int(input("Escolha: "))
match opcao:
    case 1:
        print("Executando ex 1!")
    case 2:
        print("Executando ex 2!")
    case 3:
        print("Executando ex 3!")
    case 4:
        print("Executando ex 4!")
    case _:
        print("Erro!")
"""
x = 1
while x <= 10:
    print(x)
    x = x + 1
    print("EDShow")
    if x == 5:
        break
else:
    print("será executado se houver interrupção")