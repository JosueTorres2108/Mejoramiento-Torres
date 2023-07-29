def calculodivisores(numero):
    contador = 0
    for divisor in range(1,numero+1):
        if (numero % divisor) == 0 :
            print(divisor,"es divisor")
            contador += 1
    return contador

numero = int(input("Ingresa el número: "))
print("los divisores de ",numero)
contador1 = calculodivisores(numero)
print("el numero ",numero," tiene ",contador1," divisores")
