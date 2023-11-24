def es_triangulo(a, b ,c):
    if a>=a+b or b>=a+c or c>=b+a:
        return False
    else:
        return True
num1=int(input("Ingrese dato numero 1:"))
num2=int(input("Ingrese dato numero 2:"))
num3=int(input("Ingrese dato numero 3:"))
print(es_triangulo(num1, num2, num3))