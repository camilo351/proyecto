def menu ():
    print ("LAS OPERACIONES QUE PUEDES HACER SON ESTAS: \n ")
    print ("1.Suma")
    print ("2.Resta")
    print ("3.Multiplicacion")
    print ("4.Dividir")

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
        print ("La division no se puede hacer")
    else:
        resultado = num1 / num2
        return resultado

def calculadora():
    menu()
    opción = int(input("escribe la opcion que deseas: "))
    if opción == 1:
        print (f"el resultado de la suma es: {suma()}")
    elif opción == 2:
        print (f"el resultado de la resta es: {resta()}")
    elif opción == 3:
        print (f"el resultado de la multiplicar es: {multiplicar()}")
    elif opción == 4:
        print (f"el resultado de la division es: {dividir()}")
    else:
        print("la opción no esta disponible")

calculadora()