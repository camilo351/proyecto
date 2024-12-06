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

def calculadora ():
    while True:
        opcion = int(input("que operación deseas hacer: "))
        if opcion == 1:
            print(f"El resultado de la suma es: {suma()}")
        elif opcion ==2:
            print(f"El resultado de la resta es: {resta()}")
        elif opcion ==3:
            print(f"El resultado de la multiplicacion es: {multiplicar()}")
        elif opcion ==4:
            print(f"el resultado de la division es {dividir()}")
        else:
            print("la opción que cogistes no esta disponible")
            break

calculadora()