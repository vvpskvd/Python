def primer_multiplo (n) :
    con=0
    for i in range (1, n):
        if i % n == 0:
            con+=1
        if con == n:
            return(con)
n=int(input("Ingrese un numero menor a 3 cifras:"))
print(primer_multiplo(n))