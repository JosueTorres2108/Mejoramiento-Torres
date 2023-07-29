def Figura(numl):
    for i in range(numl):
        for j in range(i+1):
            print("*",end=" ")
        print()
    return    

n1 = int(input("Ingrese el numero que desee para armar la figura: "))
resultado = Figura(n1)
