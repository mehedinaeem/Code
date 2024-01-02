def do_sum():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print(f'The sum is = {a + b}')

def do_sub():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print(f'The sub is = {a - b}')

def do_multi():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print(f'The multiplication is = {a * b}')

def do_divide():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    if b != 0:
        print(f'The division is = {a / b}')
    else:
        print("Division by zero is not allowed.")

# Main code starts from here

while True:
    op = input('What to do: ')
    if op == '+':
        do_sum()
    elif op == '-':
        do_sub()
    elif op == '*':
        do_multi()
    elif op == '/': 
        do_divide()
    else:
        print('It\'s not possible')

    print('\n')
    n = input('Do you want to do more calculations? (y/n): ')
    n = n.lower()
    if n != 'y':
        print('The program is closed')
        break
