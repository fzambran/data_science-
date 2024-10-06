#invertir :: int -> int
#devuelve un entero positivo de dos cifras al reves
#ejemplo: invertir(28) devuelve 82
def invertir(N):
    unidades = N % 10
    decenas = N // 10
    return unidades * 10 + decenas
assert invertir(28) == 82 #prueba de caso nominal
assert invertir(33) == 33 #prueba de caso borde o caso limite