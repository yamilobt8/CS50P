import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        tries = 0
        while tries < 3:
            try:
                answer = int(input(f'{x} + {y} = '))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print('EEE')
            except ValueError:
                pass
            tries += 1
        if tries == 3:
            print(f'{x} + {y} = {x + y}')
    print(f'Score: {score}')

def get_level():
    while True:
        try:
            level = int(input('Level: '))  
            if level in range(1, 4):  
                return level
        except ValueError:
            pass  

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    return random.randint(10 ** (level - 1), 10 ** level - 1)

if __name__ == '__main__':
    main()
