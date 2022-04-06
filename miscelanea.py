# menu
opcion = '0'
while not (opcion == '4'):
    print(' 1. Operadores')
    print(' 2. Condicionales')
    print(' 3. Ciclos')
    print(' 4. Salir')

    opcion = input('  --- ¿Cuál opcion?: ')

    if (opcion == '1'):
        print(' **** menu opcion 01 ****')
        print("OPERADORES")

        print('Ejercicio 1')
        print("Calcular el área de un triángulo")
        base = input("Cual es la base: ")
        altura = input("Cual es la altura: ")
        area = int(base) * int(altura) / 2.0
        print("el resultado es: " + str(area))

        print('Ejercicios 2')
        print("suma de dos numeros enteros")
        n1 = float(input("Intro número uno: "))
        n2 = float(input("Intro numero dos: "))
        suma = n1 + n2
        print("La suma es: ", suma)

        print('Ejercicio 3')
        print("visualizar el número elevado al cuadrado.")
        numero=int(input('introducir un numero: '))
        print('el cuadrado de', numero, 'es', numero**2)

        print('Ejercicio 4')
        print('conviertir de euros a dólares')
        dolar = 0.91
        euro = float(input('¿cuantos euros desea convertir?'))
        dolares = euro / dolar
        print('{} euros equivale a {} dolares'.format(euro, dolares))

        print('Ejercicio 5')
        print('valor del área y del perímetro')
        lado = int(input('ingrese medida del lado del cuadrado'))
        perimetro = lado * 4
        area = lado * lado
        print('El perimetro de cuadrado es: ')
        print(perimetro)
        print('El area del cuadrado es: ')
        print(area)

        print('Ejercicio 6')
        print('Determinar el área y el volúmen de un cilindro')
        radio = float(input('ingresar el rario del cilindro'))
        altura = float(input('ingresar la altura del cilindro'))
        pi = 3.14
        volumen = pi*(radio**2)
        area = 2 * pi * (radio) * radio + altura
        print('el volumen del cilindro es :', volumen, 'cm3')
        print('el area del cilindro es :', area, 'cm2')

        print('Ejercicio 7')
        print('algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área')
        import math
        radio = float(input('Ingrese el radio'))
        area = math.pi * radio**2
        longitud = 2 * math.pi * radio
        print('el area es :', area,)
        print('La longitud de la circulo es:', longitud,)

        print('Ejercicio 8')
        print('Calcular el promedio de tres (3) números ingresados')
        numero1 = float(input('Ingrese numero'))
        numero2 = float(input('Ingrese numero'))
        numero3 = float(input('Ingrese numero'))
        promedio = ( numero1 + numero2 + numero3)/3
        print('El promedio de los tres numeros es:', promedio,)

    elif (opcion == '2'):
        print(' **** menu opcion 02 ****')
        print("CONDICIONALES")

        print('Ejercicio 1')
        print('Determinar si un numero es positivo o negativo')
        n = int(input('Ingrese un numero: '))
        if n == 0:
            print('El numero ',n,'es neutro')
        else:
            if n < 0:
                print('El numero ',n,' es negativo')
            else:
                print('El numero ',n,' es positivo')

        print('Ejercicio 2')
        print('Cuál es el mayor y cuál el menor')
        print('Ingresa dos numeros')
        numero1 = int(input('Numero 1: '))
        numero2 = int(input('Numero 2: '))
        if numero1 == numero2:
            print('Los numeros son iguales')
        elif numero1 > numero2:
            print('El numero', numero1, 'es mayor que', numero2, )
        else:
            print('El numero', numero2, 'es mayor que', numero1, )

        print('Ejercicio 3')
        print('tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos.')
        numero1 =float(input('ingrese el primer numero'))
        numero2 = float(input('ingrese el segundo numero'))
        numero3 = float(input('ingrese el tercero numero'))
        #NUMERO MAYOR
        if numero2 < numero1 > numero3:
            print('El numero mayor es el primer numero',numero1,)
        elif numero1 < numero2 > numero3:
            print('El numero mayor es el segundo nummero',numero2,)
        elif numero1 < numero3 > numero2:
            print('El numero mayor es el tercer numoro',numero3,)
        #NUMERO MENOR
        if numero2 > numero1 < numero3:
            print('El numero menor es el primer numero',numero1,)
        elif numero1 > numero2 < numero3:
            print('El numero menor es el segundo nummero',numero2,)
        elif numero1 > numero3 < numero2:
            print('El numero menor es el tercer numoro',numero3,)

        print('Ejercicio 4')
        print('Dados dos números A y B, sumarlos si A es menor que B o sino restarlos')
        numero1 = float(input('ingrese el primer numero'))
        numero2 = float(input('ingrese el segundo numero'))
        if numero1 < numero2:
            suma= numero1 + numero2
            print('Las suma es:',format(suma))
        elif numero1 > numero2:
            resta= numero1 - numero2
            print('La resta es:',format(resta))

        print('Ejercicio 5')
        print('Dados dos números A y B encontrar el cociente entre A y B')
        numero1 = float(input('ingrese el primer numero'))
        numero2 = float(input('ingrese el segundo numero'))
        if numero2 == 0:
            print('¡NO se puede dividir entre 0!')
        elif numero2 > 0:
            cociente= numero1/numero2
            print('El cociente es:',format(cociente))

        print('Ejercicio 6')
        print('Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos')
        numero1 = float(input('ingrese el primer numero'))
        numero2 = float(input('ingrese el segundo numero'))
        if numero1 < 0 or numero2 < 0:
            suma = numero1 + numero2
            print('La suma es:', format(suma))
        elif numero1 > 0 and numero2 > 0:
            multiplicar = numero1 * numero2
            print('La multiplicacion es:',format(multiplicar))

        print('Ejercicio 7')
        print('Determine si un año es bisiesto o no')
        año = int(input('Introduce un año: '))
        if año % 4 == 0:
            if año % 100 == 0:
                if año % 400 == 0:
                    print('El año es bisiesto')
                else:
                    print('El año no es bisiesto')
            else:
                print('El año es bisiesto.')
        else:
            print('El año no es bisiesto.')
    elif (opcion == '3'):
        print(' **** menu opcion 03 ****')
    print('CICLOS')
    print('Ejercicio 1')
    print('Imprimir todos los múltiplos de 3 que hay entre 1 y 100')
    for x in range(100):
        x += 1
        if (x % 3 == 0):
            print(str(x))
    print('Ejercicio 2')
    print('Imprimir los números impares entre 0 y 100')
    x = 1
    while x <= 100:
        if x % 2 == 1:
            print('El numero',x,'es impar')
        x += 1
    print('Ejercicio 3')
    print('Imprimir los números pares del 1 al 100')
    x = 1
    while x <= 100:
        if x % 2 == 0:
            print('El numero',x,'es par' )
        x = x + 1
    print('Ejericicio 4')
    print('cuadrados de los números del 1 al 30')
    lista = []
    def cuadrados():
        for i in range(1, 31):
            lista_elevada = i ** 2
            lista.append(lista_elevada)
    cuadrados()
    print(lista)
    print('Ejercicio 5')
    print('sume los cuadrados de los cien primeros números naturales')
    suma = 0
    for i in range(1, 100 + 1):
        suma += i
        print('La suma es',suma,)
        print()




