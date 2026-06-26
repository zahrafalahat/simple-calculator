print('welcome to simple calcutalor')
num1 = int(input('enter first number'))
num2 = input('enter operator')
num3 = int(input('enter second number'))

if num2 == '+':
    print(num1 + num3)
elif num2 == '-':
    print(num1 - num3)  
elif num2 == '*':
    print(num1 * num3)
elif num2 == '/':
    print(num1 / num3)
else:
    print('invalid operator ')

