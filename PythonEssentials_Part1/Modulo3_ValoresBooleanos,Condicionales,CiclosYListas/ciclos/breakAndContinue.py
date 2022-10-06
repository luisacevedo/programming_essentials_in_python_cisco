while(True):
    palabra = input("Ingrese una palabra: ")
    if(palabra == "chupacabra"):
        break;
print("¡Has dejado el ciclo con exito!")

userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()
for word in userWord:
    if((word == "A") or (word == "E") or (word == "I") or (word == "O") or (word == "U")):
        continue
    else:
        print(word)