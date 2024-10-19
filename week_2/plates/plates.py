def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(plate):
    # Check if the first two characters are letters     
    if not plate[0:2].isalpha():
        return False
    
    # Check if the plate has between 2 and 6 characters
    if len(plate) > 6 or len(plate) < 2:
        return False
    
    # Ensure that the plate contains only letters and numbers
    if not plate.isalnum():
        return False
    
    for i, char in enumerate(plate):
        if char.isdigit():
            if char == '0' and (i == 2 or i == 1): #Leading zero not allowed
                return False
            if not plate[i:].isdigit():
                return False
            break

    return True
    
main()