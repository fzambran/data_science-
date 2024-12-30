#suma :: int int -> int
#devuelve la suma de dos numeros enteros
#ejemplo: suma(4,3) devuelve 7
def suma(a, b):
    return a + b
    
#Test
assert suma(4,3) == 7

#resta :: int int -> int
#devuelve la resta de dos numeros enteros
#ejemplo: resta (4,3) devuelve 1
def resta(a, b):
    return a - b

#Test
assert resta(4, 3) == 1

#multiplicacion :: int int -> int
#devuelve la multiplicacion de dos numeros enteros
#ejemplo: multiplicacion(4, 3) devuelve 12
def multiplicacion(a, b):
    return a * b

#Test
assert multiplicacion(4, 3) == 12

#division real :: int int -> float
#devuelve la division real entre dos numeros enteros 
#ejemplo: division_real(1, 2) devuelve 0.5
def division_real(a, b):
    return a / b

#Test
assert division_real(1, 2) == 0.5