num=0
op=0
num=float(input("Digite un numero entero: "))
if num > 0 :
  while num >= 0 :
    op=pow(num, 1/2)
    print(op)
else:
  print("no se admiten numeros negativos")