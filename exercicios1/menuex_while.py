while True:
    opc = int(input("Digite seu exercicio 1 a 11: "))
    match opc:
        case 1:
            n = int(input("1 Numero: "))
            n2 = int(input("2 Numero: "))
            if n == n2:
                print("Digite Novamente!")
            elif n < n2:
                print(n2)
            else:
                print(n)
            continue
        case 2:
            data_de_nascimento = int(input("Digite sua ano de nascimento:"))
            if data_de_nascimento <= 2008 : 
                print("Pode votar")
            else:
                print("Nao pode votar") 
            continue
        case 3:
            passwordus = int(input("Digite a Senha: ")) 
            password = 1234
            if passwordus == password:
                print("Acesso Permitido!")
            else:
                print("Acesso Negado!")
            continue
        case 4:
            macas = int(input("Quantas maças vc comprou ?"))
            preco = float
            if macas >= 12:
                preco = macas*0.25
                print("Preco é {}".format(preco))
            elif macas < 12:
                preco = macas * 0.30
                print("Preco é {}".format(preco))
            continue
        case 5:
            val1 = int(input("Digite o valor 1: "))
            val2 = int(input("Digite o valor 2: "))
            val3 = int(input("Digite o valor 3: "))
            if val1 < val2 < val3:
                print(val1, val2, val3)
            if val1 < val3 < val2:
                print(val1, val3, val2)
            if val2 < val1 < val3:
                print(val2, val1, val3)
            if val2 < val3 < val1:
                print(val2, val3, val1)
            if val3 < val2 < val1:
                print(val3, val2, val1)
            if val3 < val1 < val2:
                print(val3, val1, val2)
            continue
        case 6:
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
            continue
        case 7:
            n1 = float(input("Digite o primeiro lado:"))
            n2 = float(input("Digite o segundo lado:"))
            n3 = float(input("Digite o terceiro lado:"))
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
            continue
        case 8:
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
            continue
        case 9:
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
            continue
        case 10:
            n1 = (float(input("Digite o primeiro lado:")))
            n2 = (float(input("Digite o segundo lado:")))
            n3 = (float(input("Digite o terceiro lado:")))
            if n1 == n2 ==n3:
                print("É um triangulo equilatero")
            elif n1 == n2 or n1 == n3 or n2 == n3:
                print("É um triangulo isóceles")
            else:
                print("É um triangulo escaleno")
            continue
        case 11:
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
            continue
        case _:
            print("Digite uma opcão Válida!")
            continue



        




