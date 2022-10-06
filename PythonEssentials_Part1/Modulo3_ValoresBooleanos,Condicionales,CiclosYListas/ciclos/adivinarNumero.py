from tokenize import Number


numeroSecreto = 777
ver = True

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
while(ver):
    num = int(input("Ingresa un número"))
    if(num == numeroSecreto):
        ver = False
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")

print("¡Bien hecho, muggle! Eres libre ahora")