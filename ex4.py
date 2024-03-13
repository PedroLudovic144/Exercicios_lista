macas = int(input("Quantas maças vc comprou ?"))
preco = float
if macas >= 12:
    preco = macas*0.25
    print("Preco é {}".format(preco))
elif macas < 12:
    preco = macas * 0.30
    print("Preco é {}".format(preco))
   