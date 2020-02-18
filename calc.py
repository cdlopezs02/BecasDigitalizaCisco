# Tarea Calculadora
# Author: Carlos David Lopez Sanchez
import math as m
resultados = []

def Suma(a, b):
    result = a+b
    resultados.append((str(a)+'+'+str(b)+'= ', result))
    print(result)


def Resta(a, b):
    result = a-b
    resultados.append((str(a)+'-'+str(b)+'= ', result))
    print(result)


def Multiplicacion(a, b):
    result= a*b
    resultados.append((str(a)+'*'+str(b)+'= ', result))
    print(result)

def Division(a, b):
    result= a/b
    resultados.append((str(a)+'/'+str(b)+'= ', result))
    print(result)


def Exponencial(a, b):
    result= a**b
    resultados.append((str(a)+'^'+str(b)+'= ', result))
    print(result) 


def RaizCuadrada(a):
    result= m.sqrt(a)
    resultados.append(('Raiz Cuadrada de '+str(a)+'= ', result))
    print(result)


def Resultados():
    print()
    for texto,res in resultados:
        print(texto+str(res))


def calc():
    print('Elige una opcion:')
    print('''        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Exponencial
        6. Raiz Cuadrada
        7. Resultados Anteriores
        '''
        )

    print('Escriba el numero de la opcion elegida o escriba \"exit\" para salir:', end='\n')
    o = input()

    while o != 'exit':
        if o == '1':
            print('Suma')
            a = int(input('Operando 1:   '))
            b = int(input('Operando 2:   '))
            Suma(a, b)
        elif o == '2':
            print('Resta:')
            a = int(input('Operando 1:   '))
            b = int(input('Operando 2:   '))
            Resta(a, b)
        elif o == '3':
            print('Multiplicacion:')
            a = int(input('Operando 1:   '))
            b = int(input('Operando 2:   '))
            Multiplicacion(a, b)
        elif o == '4':
            print('Division:')
            a = int(input('Operando 1:   '))
            b = int(input('Operando 2:   '))
            Division(a, b)
        elif o == '5':
            print('Exponencial:')
            a = int(input('Operando 1:   '))
            b = int(input('Operando 2:   '))
            Exponencial(a, b)
        elif o == '6':
            print('RaizCuadrada:')
            a = int(input('Operando 1:   '))
            RaizCuadrada(a)
        elif o == '7':
            print('Resultados:')
            Resultados()

        print()
        print('Elige una opcion:')
        print('''        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Exponencial
        6. Raiz Cuadrada
        7. Resultados Anteriores
        '''
        )
        print('Escriba el numero de la opcion elegida o escriba \"exit\" para salir:', end='\n')
        o = input()



try:
    calc()
except ZeroDivisionError as id:   
    #No se cual es el fallo pero solo arregla la primera excepcion y las demas salta un error.
    #Supongo que es porque el segundo calc se ejecuta dentro de la excepcion y fuera de un try.
    print()
    print(id.args[0])
    print('Introduzca valores validos. \n')
    calc()

except Exception as id:
    print()
    print(id.args[0])
    print('Introduzca valores validos. \n')
    calc()
