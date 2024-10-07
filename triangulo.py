import math

#perimetro :: num num num -> num
#devuelve el perimetro de un triangulo de lados a, b y c
#ejemplo: perimetro(1,1,1) devuelve 3
def perimetro(a,b,c):
    return a + b + c
assert perimetro(1,1,1) == 3

#area :: num num num -> num
#devuelve el area de un triangulo de lados a, b y c
#ejemplo: area(3,4,5) devuelve 6
def area(a,b,c):
    S = perimetro(a,b,c) / 2
    return math.sqrt(S * (S-a) * (S-b) * (S-c))
assert area(3,4,5) == 6
