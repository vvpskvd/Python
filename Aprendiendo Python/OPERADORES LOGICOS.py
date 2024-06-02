a = 30
b = 40
c = 50
z = ((a < b) or (b > c))
print (z)
z = not((a < b) or (b > c)) #El not simplemente niega todo el resultado, si daba True pues lo convierte en False
print (z)