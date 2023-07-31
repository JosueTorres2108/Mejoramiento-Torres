def CalcularPrimo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        print("entra")
        return True
    elif numero == 3:
         print("entra1")
         return True
    elif numero > 3 & numero % 2 == 0:
        print("entra2")
        return False
    else:
        for i in range(3,numero):
            if numero % i == 0:
                print("entra3")
                return False   
        return True

numero = int(input("Ingresa el número: "))
resultado = CalcularPrimo(numero)
if resultado == True:
    print("el numero ", numero, "es primo ")
else:
    print("el numero ", numero, "NO es primo ")





