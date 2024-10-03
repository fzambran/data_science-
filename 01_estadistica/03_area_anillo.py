exterior = float(input("Radio exterior? "))
interior = float(input("Radio interior? "))

pi = 3.14
areaExterior = pi * exterior ** 2
areaInterior = pi * interior ** 2
areaAnillo = areaExterior - areaInterior

print("Area anillo =", areaAnillo)