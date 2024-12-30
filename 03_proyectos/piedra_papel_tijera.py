import random

emojis = { 'r': '🪨', 'p': '📄', 't': '✂️' }
opciones = ('r', 'p', 't') #tupla con las opciones válidas

while True:
    eleccion_usuario = input('Piedra, papel o tijera? (r/p/t): ').lower()
    if eleccion_usuario not in opciones:
        print('Elección inválida! ')
        continue

    eleccion_computadora = random.choice(opciones)

    print(f'Tu elegiste: {emojis[eleccion_usuario]}')
    print(f'La computadora eligió: {emojis[eleccion_computadora]}')
        
    if eleccion_usuario == eleccion_computadora:
        print('Empate! ')
    elif (
        (eleccion_usuario == 'r' and eleccion_computadora == 't') or
        (eleccion_usuario == 't' and eleccion_computadora == 'p') or
        (eleccion_usuario == 'p' and eleccion_computadora == 'r')):
        print('Ganaste! ')
    else:
        print('Perdiste! ')
        
    continuar = input('Continuar? (s/n): ').lower()
    if continuar == 'n':
        print('Gracias por jugar! ')
        break
    
