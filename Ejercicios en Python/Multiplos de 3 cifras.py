def primer_multiplo (n) :
    con=0
    for i in range (100, 1000):
        if i % n == 0:
            con+=1
        if con==3:
            return i
n=int(input("Ingrese un numero menor a 3 cifras:"))
print(primer_multiplo(n))
