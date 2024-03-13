altura = float(input("Digite sua altura:"))
sexo = int(input("Digite o seu sexo(Digite 1 para homem ou 2 para mulher):"))
if sexo == 1:
    peso_ideal = altura * 72.7
    print("Seu peso ideal é {}".format(peso_ideal))
elif  sexo == 2:
    peso_ideal = altura* 62.1
    print("Seu peso ideal é {}".format(peso_ideal))
else:
    print("Digite um numero valido")
