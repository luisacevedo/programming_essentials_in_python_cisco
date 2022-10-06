ingreso=float(input("Ingrese el ingreso anual:"))
ipi = 0
base = 85528

if(ingreso <= base):
    ipi = 0.18
    impuesto = (ingreso*ipi)-556.2
else:
    ipi = 0.32
    impuesto = 14839.2 + ((ingreso-base)*ipi)

if(impuesto < 0):
    impuesto = 0

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")