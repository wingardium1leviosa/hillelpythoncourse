num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
act = input('Enter the operation: ')
if act == '+':
    print(num1 + num2)
elif act == '-':
    print(num1 - num2)
elif act == '*':
    print(num1 * num2)
elif act == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("The second number cannot be zero")





