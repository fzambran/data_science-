print("Votos por tangananica? ")
tangananica = int(input())

print("Votos por tanganana?" )
tanganana = int(input())

total = tangananica + tanganana
porcentaje = tangananica / total * 100

print("Porcentaje tangananica: " + str(porcentaje) + "%")
print("Porcentaje tanganana: " + str(100 - porcentaje) + "%")
