vowels = ['a', 'e', 'o', 'i', 'u']

word = input('Input: ')
new_word = ''
for char in word:
    if char.lower() in vowels:
        pass
    else:
        new_word += char

print(new_word)