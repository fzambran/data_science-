import calculadora

def ejecutar_operacion(opcion):
    operaciones = {
        '1' : ('Suma', calculadora.suma),
        '2' : ('Resta', calculadora.resta),
        '3' : ('Multiplicación', calculadora.multiplicacion),
        '4' : ('División real', calculadora.division_real),
    }
    
    if opcion in operaciones:
        operacion_nombre, operacion_funcion = operaciones[opcion]
        print(f'\n{operacion_nombre}')
        a = int(input('Ingresa el primer número: '))
        b = int(input('Ingresa el segundo número: '))
        resultado = operacion_funcion(a, b)
        print(f'{operacion_nombre} = {resultado}\n')
    elif opcion == '5':
        print('Saliendo...')
        return False
    else:
        print('Opción inválida. Por favor, elige una opción válida.\n')
    return True

def main():
    print('Calculadora')
    print('===========')
    
    while True:
        print('1.- Suma')
        print('2.- Resta')
        print('3.- Multiplicación')
        print('4.- División real')
        print('5.- Salir')
        print(' ')
        
        opcion = input('Ingresa una opción: ')
        
        if not ejecutar_operacion(opcion):
            break

if __name__ == '__main__':
    main()
        
