ver = True
while(ver):
    pasos = 0
    c0 = int(input("Ingrese un número: "))
    if(c0 <= 0):
        print("¡Solo se admiten números positivos!")
        ver = False
    else:
        while(c0 > 1):
            if(not(c0%2)):
                c0 /= 2
                pasos += 1
            else:
                c0 = (3 * c0) + 1
                pasos += 1
            print(c0)
        print("pasos = ", pasos)