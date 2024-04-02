
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


    
