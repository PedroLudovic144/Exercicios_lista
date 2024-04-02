def caso_1():
    n = int(input("1 Numero: "))
    n2 = int(input("2 Numero: "))
    if n == n2:
        print("Digite Novamente!")
    elif n < n2:
        print(n2)
    else:
        print(n)

def caso_2():
    data_de_nascimento = int(input("Digite seu ano de nascimento: "))
    if data_de_nascimento <= 2008:
        print("Pode votar")
    else:
        print("Não pode votar")

def caso_3():
    passwordus = int(input("Digite a Senha: "))
    password = 1234
    if passwordus == password:
        print("Acesso Permitido!")
    else:
        print("Acesso Negado!")

def caso_4():
    macas = int(input("Quantas maçãs você comprou? "))
    if macas >= 12:
        preco = macas * 0.25
    else:
        preco = macas * 0.30
    print("O preço é {}".format(preco))

def caso_5():
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

def caso_6():
    altura = float(input("Digite sua altura: "))
    sexo = int(input("Digite o seu sexo (Digite 1 para homem ou 2 para mulher): "))
    if sexo == 1:
        peso_ideal = altura * 72.7
        print("Seu peso ideal é {}".format(peso_ideal))
    elif sexo == 2:
        peso_ideal = altura * 62.1
        print("Seu peso ideal é {}".format(peso_ideal))
    else:
        print("Digite um número válido.")

def caso_7():
    n1 = float(input("Digite o primeiro lado: "))
    n2 = float(input("Digite o segundo lado: "))
    n3 = float(input("Digite o terceiro lado: "))
    
    if n3 == 0:
        print("Número de lados inválidos")
    else:
        p1 = input("Digite q para sair ou c para continuar: ")

        if p1 == "q":
            print("É um triângulo!!!!")
        elif p1 == "c":
            n4 = float(input("Digite o quarto lado: "))
            p1 = input("Digite q para sair ou c para continuar: ")

            if p1 == "q":
                print("É um quadrado!!!!")
            else:
                n5 = float(input("Digite o quinto lado: "))
                print("É um pentágono!!!!")
        else:
            print("Escolha inválida.")

def caso_8():
    n1 = float(input("Digite o primeiro lado: "))
    n2 = float(input("Digite o segundo lado: "))
    n3 = float(input("Digite o terceiro lado: "))
    
    if n3 == 0:
        print("Número de lados inválidos")
    else:
        p1 = input("Digite q para sair ou c para continuar: ")

        if p1 == "q":
            print("É um triângulo!!!!")
        elif p1 == "c":
            n4 = float(input("Digite o quarto lado: "))
            p1 = input("Digite q para sair ou c para continuar: ")

            if p1 == "q":
                print("É um quadrado!!!!")
            else:
                n5 = float(input("Digite o quinto lado: "))
                print("É um pentágono!!!!")
        else:
            print("Escolha inválida.")

def caso_9():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))
    
    if n1 == n2 or n2 == n3 or n1 == n3:
        print("Números repetidos. Digite outros números.")
        exit()
    
    if n1 > n2:
        print(n1)
    elif n2 > n3:
        print(n2)
    else:
        print(n3)

def caso_10():
    n1 = float(input("Digite o primeiro lado: "))
    n2 = float(input("Digite o segundo lado: "))
    n3 = float(input("Digite o terceiro lado: "))
    
    if n1 == n2 == n3:
        print("É um triângulo equilátero.")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")

def caso_11():
    a1 = float(input("Digite o valor do primeiro ângulo: "))
    a2 = float(input("Digite o valor do segundo ângulo: "))
    a3 = float(input("Digite o valor do terceiro ângulo: "))

    if a1 + a2 + a3 == 180 and a1 == 90:
        print("O triângulo é retângulo.")
    elif a1 + a2 + a3 == 180 and a1 > 90:
        print("O triângulo é obtusângulo.")
    elif a1 + a2 + a3 == 180 and a1 < 90:
        print("O triângulo é acutângulo.")
    else:
        print("Os ângulos não formam um triângulo.")


casos = {
    1: caso_1,
    2: caso_2,
    3: caso_3,
    4: caso_4,
    5: caso_5,
    6: caso_6,
    7: caso_7,
    8: caso_8,
    9: caso_9,
    10: caso_10,
    11: caso_11,
}


def switch(opcao):
    if opcao in casos:
        casos[opcao]()
    else:
        print("Opção inválida.")


opcao_escolhida = int(input("Escolha a opção (1 a 11): "))
switch(opcao_escolhida)
