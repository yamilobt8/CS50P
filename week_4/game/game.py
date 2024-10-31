import random

while True:
    try:
        level = int(input('Level: '))
        number_to_guess = random.randint(1, level)
        break
    except ValueError:
        pass
     
while True:
    try:
        n = int(input('Guess: '))
        if n == number_to_guess:
            print('Just right!')
            break
        elif n > number_to_guess:
            print('Too large!')
        else:
            print('Too small!')
    except ValueError:
        pass