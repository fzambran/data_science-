#es par :: int -> bool
#devuelve "es par" si el numero es par e "impar" si no lo es
#ejemplo: es_par(4) devuelve "es par"

def main():
    x = int(input("Ingresa un número: "))
    if es_par(x):
        print("es par")
    else:
        print("impar")

def es_par(n):
    return n % 2 == 0
assert es_par(4) == True

main()

    