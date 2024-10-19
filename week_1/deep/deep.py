question = input('What is the answer to the Great Question of Life, the Universe and Everything? ').lower().replace('-', '').replace(' ', '')
if question == '42' or question == 'fortytwo':
    print('Yes')
else:
    print('No')