import math as m

radio = float(input("Ingrese valor para el radio = "))

area = m.pi * (radio ** 2)
longitud = 2 * m.pi * radio

#Para que solamente de las decimales que queramos se puede usar {variable:.Xf} siendo X la cantidad de decimales
print(f"El valor del area es {area:.2f} \n El valor de longitud es {longitud:.2f}")