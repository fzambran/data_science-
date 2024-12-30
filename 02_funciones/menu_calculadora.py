import calculadora

print('Calculadora')
print('===========')

while True:
    print('1.- Suma')
    print('2.- Resta')
    print('3.- Multiplicacion')
    print('4.- Division real')
    print('5.- Salir')
    print(' ')

    opcion = input('Ingresa una opción: ')

    if opcion == '1':
        print(' ')
        a = int(input('Ingresa el primer número: '))
        b = int(input('Ingresa el segundo número: '))
        print('Suma = ', calculadora.suma(a, b))
        print(' ')
    elif opcion == '2':
        print(' ')
        a = int(input('Ingresa el primer número: '))
        b = int(input('Ingresa el segundo número: '))
        print('Resta = ', calculadora.resta(a, b))
        print(' ')
    elif opcion == '3':
        print(' ')
        a = int(input('Ingresa el primer número: '))
        b = int(input('Ingresa el segundo número: '))
        print('Multiplicación = ', calculadora.multiplicacion(a, b))
        print(' ')
    elif opcion == '4':
        print(' ')
        a = int(input('Ingresa el primer número: '))
        b = int(input('Ingresa el segundo número: '))
        print('Divisiín real = ', calculadora.division_real(a, b))
        print(' ')        
    elif opcion == '5':
        print('Saliendo')
        break

