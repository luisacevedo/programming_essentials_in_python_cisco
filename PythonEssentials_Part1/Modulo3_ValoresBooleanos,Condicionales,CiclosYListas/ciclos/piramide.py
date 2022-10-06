bloques = int(input("Ingrese el número de bloques:"))
altura = 0
while(bloques):
    altura += 1
    bloques -= altura
    if(bloques < altura + 1):
        break;
print("La altura de la pirámide:", altura)