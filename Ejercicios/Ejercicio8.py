def Multiplo(num):
    contador = 0
    for i in range (1,num+1):
        if i % 5 ==0:
            contador +=1
            print("el numero ",i," es multiplo de 5")

    return contador

n = int(input("Ingresa el número: "))
print("el total de multiplos es ",Multiplo(n))
