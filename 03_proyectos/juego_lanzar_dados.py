import random

while True:
    opcion = input('¿Lanzar los datos? (s/n): ').lower()
    if opcion == 's':
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        print(f'({dado1}, {dado2})')
    elif opcion == 'n':
        print('Gracias por jugar! ')
        break
    else:
        print('Opción incorrecta! ')