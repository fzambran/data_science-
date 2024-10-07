import triangulo #guardado en el archivo 07_triangulo.py

a = int(input("lado 1? "))
b = int(input("lado 2? "))
c = int(input("lado 3? "))

print("Perimetro = ", triangulo.perimetro(a,b,c))
print("Area = ", triangulo.area(a,b,c))