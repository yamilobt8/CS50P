expression = input('Expression: ')
num_1, operation, num_2 = expression.split(' ')

if operation == '+':
    print(float(int(num_1) + int(num_2)))
elif operation == '*':
    print(float(int(num_1) * int(num_2)))
elif operation == '/':
    print(float(int(num_1) / int(num_2)))
elif operation == '-':
    print(float(int(num_1) - int(num_2)))
