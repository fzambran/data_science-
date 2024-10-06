#area :: float -> float
#devuelve el area de un circulo de radio R
#ejemplo: area(10) devuelve 314
def area(radio):
    pi = 3.14
    return pi * radio ** 2
#Test
assert area(10) == 314 

interior = float(input("radio interior? "))
exterior = float(input("radio exterior? "))
anillo = area(exterior) - area(interior)
print("area anillo = " + str(anillo))