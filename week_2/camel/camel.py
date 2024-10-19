camelcase = input('camelCase: ')

snake = ''
for char in camelcase:
    if char.isupper():
        snake += '_' + char.lower()
    else:
        snake += char

print(snake)