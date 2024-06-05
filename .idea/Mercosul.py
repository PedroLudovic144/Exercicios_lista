#--------------------- Função
def PlacaMercosul(s: str) -> bool:
    digito = "0123456789"
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Especial = "@#!$%¨&*()+_§\|,°ºª[]}{."
    valido = True
    if len(s) != 7:
        valido = False
    else:
            if s[0] not in alfabeto and s[1] not in alfabeto and s[2] not in alfabeto and s[4] not in alfabeto:
                valido = False
            if s[3] not in digito and s[5] not in digito and s[6] in digito:
                valido = False
            for i in range(0, 6):
                if s[i] in Especial:
                    valido = False
    return valido


        
    
    #if s[3] in digito and s[5] in digito and s[6] in digito:
        #if s[0 and 1 and 2 and 4] in alfabeto:


    
#--------------------- Principal
import os
os.system("cls")    #0123456
print(PlacaMercosul("ABC5D67")) # True
print(PlacaMercosul("ABC5D6")) # False 
print(PlacaMercosul("1234567")) # False
print(PlacaMercosul("ABC5D678")) # False
print(PlacaMercosul("AB@5D67")) # False
print(PlacaMercosul("ABC@D67")) # False
print(PlacaMercosul("aBC5d71"))