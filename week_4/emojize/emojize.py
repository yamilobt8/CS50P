import emoji # pip install emoji

emojie = input('Input: ')
print(f"Output: {emoji.emojize(emojie, language='alias')}")