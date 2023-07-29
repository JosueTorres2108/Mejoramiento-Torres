def SumaCubos(num):
    contador = 0
    while num > 0:
        num1 = num % 10
        contador += num1 ** 3
        num //= 10
    return contador

lista = []

for numero in range(100, 1000):
    if SumaCubos(numero) == numero:
        lista.append(numero)


resultado = (lista)
print("los numeros son: ",resultado)