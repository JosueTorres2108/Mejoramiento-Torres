def EncontrarNatural(num):
    sum = 0
    contador = 0
    for i in range(1,num+1):
        sum = sum +i
        print("suma= ",sum)
        if num >= sum:   
            contador += 1

    return contador
         
n = int(input("Ingresa el número: "))
cont = EncontrarNatural(n)
print("se debe sumar ",cont, " numeros de la serie para superar el maximo ", n)