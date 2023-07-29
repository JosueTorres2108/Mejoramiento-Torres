def cocienteyresiduo(num1,num2):
    if num1<num2:
        num1,num2=num2,num1

    cociente = num1 / num2
    residuo = num1 % num2

    return cociente,residuo

n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))    

resultado=(cocienteyresiduo(n1,n2))
print("El cociente y el residuo son: ",resultado)

