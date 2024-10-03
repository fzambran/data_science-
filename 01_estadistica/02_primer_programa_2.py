# print("Votos por tangananica? ")
#tangananica = int(input())
tangananica = int(input("Votos por tangananica? "))

#print("Votos por tanganana? ")
#tanganana = int(input())
tanganana = int(input("Votos por tanganana? "))

total = tangananica + tanganana
porcentaje = tangananica / total * 100

print("Porcentaje tangananica: " + str(porcentaje) + "%")
print("Porcentaje tanganana: " + str(100 - porcentaje) + "%")