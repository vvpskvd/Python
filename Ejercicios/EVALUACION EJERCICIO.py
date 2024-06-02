def RiesgoCardio(p, h, LDL, fuma):
    if p/(h*h) > 35 and (LDL < 71 or LDL > 300) and fuma=="F" or fuma=="f":
        return True
    else:
        return False

p=int(input("Digita un determinado peso en kg:"))
h=float(input("Digita una altura en metros:"))
LDL=int(input("Digita la cantidad de colesterol en mg:"))
fuma=input("¿Usted fuma? T para verdadero o F para falso:")
resultado=RiesgoCardio(p, h, LDL, fuma)
print(resultado)
