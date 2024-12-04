def suma ():
    num1 = int(input("numero 1: "))
    num2= int(input("numero 2: "))
    resultado = num1 + num2
    return resultado

def resta ():
    num1 = int(input("numero 1: "))
    num2= int(input("numero 2: "))
    resultado = num1 - num2
    return resultado

def multiplicar ():
    num1 = int(input("numero 1: "))
    num2= int(input("numero 2: "))
    resultado = num1 * num2
    return resultado

def dividir ():
    num1 = int(input("numero 1: "))
    num2= int(input("numero 2: "))
    if num1 != 0 and num2 == 0:
        print ('La division no se puede hacer')
    else:
        resultado = num1 * num2
        return resultado

print(f"el resultado de la suma es {suma()}")
print(f"el resultado de la resta es {resta()}")
print(f"el resultado de la multiplicacion es {multiplicar()}")
print(f"el resultado de la division es {multiplicar()}")