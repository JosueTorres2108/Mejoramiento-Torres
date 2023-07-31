def CalcularPrimo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    elif numero == 3:
         return True
    elif numero > 3 & numero % 2 == 0:
        return False
    else:
        for i in range(3,numero):
            if numero % i == 0:
                return False   
        return True

def NumerosPrimos(numero):
    cont = 0
    for i in range(1, numero+1):
        resultado = CalcularPrimo(i)
        if resultado == True:
            cont += 1
            print(i, 'es un número primo')
    print("del 1 al 1000 hay ", cont, " numeros primos")

numero = 1000
NumerosPrimos(numero)
