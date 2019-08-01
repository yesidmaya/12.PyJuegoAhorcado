#-*- coding: utf-8 -*-
import random

IMAGES = ['''

    +-----+
    |     |
          |
          |
          |
          |
          =========''', '''
          
    +-----+
    |     |
    0     |
          |
          |
          |
          =========''', '''

    +-----+
    |     |
    0     |
    |     |
          |
          |
          =========''', '''

    +-----+
    |     |
    0     |
   /|     |
          |
          |
          =========''', '''

    +-----+
    |     |
    0     |
   /|\    |
          |
          |
          =========''', '''

    +-----+
    |     |
    0     |
   /|\    |
    |     |
          |
          =========''', '''

    +-----+
    |     |
    0     |
   /|\    |
    |     |
   /      |
          =========''', '''

    +-----+
    |     |
    0     |
   /|\    |
    |     |
   / \    |
          =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def random_word():
    idx = random.randint(0, len(WORDS) - 1) # asignamos un numero aleatorio entre 0 y la longitud de la lista de palabras - 1 porque podemos salir del indice
    return WORDS[idx] #accedemos con el indice -> y tenemos una palabra

def display_board(hidden_word, tries):
    print(IMAGES[tries]) #dependiendo los intentos muestra una determinada imagen
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- *')

def run():
    word = random_word() # Escogemos una palabra al azar de nuestra lista de palabras
    hidden_word = ['-'] * len(word) # generamos la palabra escondida y multiplicamos la lista por la longitud de la palabra
    tries = 0 # guarda el numero de errores

    while True:
        display_board(hidden_word, tries) # desplegamos el tablero. va a recibir dos parametros la palabra escondida y el numero de intentos
        current_letter = str(input('Escribe una letra: '))

        # verificamos si la letra del usuario esta dentro de la palabra
        letter_indexes = [] 
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx) # metemos la letra
        # verificamos si la letra del usuario esta dentro de la palabra

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('PERDISTE !!! La palabra correcta era {}'.format(word))
                break #salimos 

        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            
            letter_indexes = []

        try:
            hidden_word.index('-') # pregunta si nos queda este signo dentro de la lista de palabras?
        except ValueError:
            print('')
            print('Felicidades!!! GANASTE. La palabra es {}'.format(word))
            break



if __name__ == "__main__":
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()