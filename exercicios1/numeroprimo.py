c= 1
i= 0
n = int(input("Digite seu valor: "))
while n>c:
    if n % c == 0:
        i= i + 1
    c=c+1
if i==1:
    print("Numero é Primo")
else:
    print(" Numero não é primo")