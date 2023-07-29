def mcd(num1,num2,repeticiones=1):
    if num1<num2:
        num1,num2=num2,num1
    
    residuo = num1%num2

    if residuo ==0:
        return (num2,repeticiones)
    
    return mcd(num2,residuo,repeticiones+1)

n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

comunDivisor,repeticiones=mcd(n1,n2)
print("El mcd es ",comunDivisor)
