#mayorDe3: int int int -> int
#devuelve el mayor de tres numeros enteros
#ejemplo: mayorDe3(7,9,3) devuelve 9
def mayorDe3(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
assert mayorDe3(7,9,3) == 9
assert mayorDe3(8,1,3) == 8
assert mayorDe3(1,2,3) == 3
assert mayorDe3(-1,-2,-3) == -1
assert mayorDe3(7,7,7) == 7

