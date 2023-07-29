def NumeroPerfecto(numero):
    contador = 0
    for divisor in range(1,numero):
        if (numero % divisor) == 0 :
            contador += divisor
    if numero == contador:
         return True
    else:
        return False

numero = int(input("Ingresa el número: "))
if NumeroPerfecto(numero):
    print("el numero ",numero," es perfecto")
else:
     print("el numero ",numero," No es perfecto")   
