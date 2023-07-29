def NumeroPerfecto(numero):
    contador = 0
    for divisor in range(1,numero):
        if (numero % divisor) == 0 :
            contador += divisor
    if numero == contador:
         return True
    else:
        return False 

def NumerosPerfectos(numero):
    cont = 0
    for i in range(1, numero+1):
        if NumeroPerfecto(i):
            cont += 1
            print(i, 'es un número perfecto')
    print("del 1 al 1000 hay ", cont, " numeros perfectos")

 
numero = 1000
NumerosPerfectos(numero)