print("TENEMOS UNA ECUACION:")
print("(c + 5) * (b^2 - 3*a*c) * a^2 \n" + "----------------------------- \n" + "           4*a")

a = float(input("Ingrese valor de \"a\" = "))
b = float(input("Ingrese valor de \"b\" = "))
c = float(input("Ingrese valor de \"c\" = "))
final = ( (c + 5) * ((b**2) - (3*a*c)) * (a**2) ) / (4*a)

print(f"El resultado final es = {final}")