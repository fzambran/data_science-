'''
La funcion area va a recibir un valor de tipo float y va a deolver un valor de tipo float que va a 
corresponder al area de un circulo de radio R.
'''
#area :: float -> float
#devuelve el area de un circulo de radio R
#ejemplo: area(10) devuelve 314
def area(radio):
    pi = 3.14
    return pi * radio ** 2
#Test
assert area(10) == 314 

exterior = float(input("Radio exterior? "))
interior = float(input("Radio interior? "))
anillo = area(exterior) - area(interior)

print("area anillo = " + str(anillo))