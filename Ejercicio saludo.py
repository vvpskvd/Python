def n (saludo):
    if saludo>=5 and saludo<=12:
        print("Buenos dias!")
    elif saludo>12 and saludo<=22:
        print("Buenas tardes!")
    elif saludo>=0 and saludo<5:
            print("Buenas noches!")
    elif saludo>22 and saludo<=24:
        print("Buenas noches!")
    else:
        print("Hora fuera de rango")
saludo=int(input("Ingrese la hora actual:"))
n(saludo)