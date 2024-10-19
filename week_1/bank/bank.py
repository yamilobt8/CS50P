greet = input('Greeting: ').lower().replace(' ', '')

if greet == 'hello' or greet == 'hello,newman':
    print('$0')
elif greet == 'howyoudoing?':
    print('$20')
else:
    print('$100')