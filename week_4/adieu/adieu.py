import sys

names = []
while True:
    try:
        name = input('Name: ')
        names.append(name)
    except EOFError:
        print() # \n

        output = 'Adieu, adieu, to '

        if len(names) == 1:
            output += names[0]
        elif len(names) == 2:
            output += f'{names[0]} and {names[1]}'
        else:
            output += ', '.join(names[:-1]) + f', and {names[-1]}' # Add The Names Except The Last One by names[:-1]
                                                                   # Then The Last Name Which is names[-1]
        print(output)
        sys.exit(0)