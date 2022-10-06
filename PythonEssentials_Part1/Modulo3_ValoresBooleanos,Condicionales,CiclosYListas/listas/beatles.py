beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)
for i in range(2):
    integrantes = input("Por favor ingrese a Stu Sutcliffe y a Pete Best: ")
    beatles.append(integrantes)
print(beatles)
del beatles[-2]
del beatles[-1]
print(beatles)
beatles.insert(0,"Ringo Starr")
print(beatles)