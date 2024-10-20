while True:
    try:
        fraction = input('Fraction: ')
        x, y = fraction.split('/')
        x, y = int(x), int(y)
        if y == 0:
            raise ZeroDivisionError
        
        if x > y:
            raise ValueError
        
        percentage = round((x / y) * 100)

        if percentage <= 1:
            print("E")

        elif percentage >= 99:
            print("F")

        else:
            print(f"{percentage}%")
            
        break
    except(ValueError, ZeroDivisionError):
        pass
