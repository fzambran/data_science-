import random
import string

#gen_pass :: int -> str
#devuelve una cadena de largo n
#ejemplo: gen_pass(4) devuelve una cadena de 4 caracteres

def gen_pass(n):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(n))
    return password

while True:
    length = int(input("Ingresa la longitud de la contraseña (o 0 para salir): "))
    if length == 0:
        break
    
    print(f"Contraseña generada: {gen_pass(length)}")
    
    
#assert gen_pass(4) ==

