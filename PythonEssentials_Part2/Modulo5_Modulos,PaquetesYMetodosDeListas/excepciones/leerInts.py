def readint(prompt, min, max):
    ver = True
    while ver:
        try:
            num = int(input(prompt))
            assert num >= min and num <= max
            ver = False
            return num
        except AssertionError:
            print("Error: el valor no está dentro del rango permitido (", min, "..", max,")")
        except ValueError:
            print("Error: entrada incorrecta")

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)