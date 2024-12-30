import random

numero_a_adivinar = random.randint(1, 100)

while True:
    try:
        adivinar = int(input('Adivina el número entre 1 y 100: '))

        if adivinar < numero_a_adivinar:
            print('Demasiado bajo! ')
        elif adivinar > numero_a_adivinar:
            print('Demasiado alto! ')
        else:
            print('Felicitaciones, adivinasta el número! ')
            break

    except ValueError:
        print('Por favor ingresa un número válido ')

print('Fin del juego! ')
    
