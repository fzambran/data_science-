#es_par :: num -> string
#devuelve "es par" si el numero es par, en otro caso, devuelve "impar"
#ejemplo: es_par(2) devuelve "es par"
def es_par(num):
    if num % 2 == 0:
        return "es par"
    else:
        return "impar"
assert es_par(2) == "es par"

a = int(input("Ingresa un número: "))
resultado = es_par(a)

print(resultado)