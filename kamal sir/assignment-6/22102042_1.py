
while True:
    op = input('What to do: ')
    
    if op == '+':
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f'The sum is = {a + b}')
        
        
    elif op == '-':
        a = int(input("Enter number 1: "))P
        b = int(input("Enter number 2: "))
        print(f'The sub is = {a - b}')
        
        
    elif op == '*':
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        print(f'The multiplication is = {a * b}')
        
    
    elif op == '/': 
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))
        if b != 0:
            print(f'The division is = {a / b}')
        else:
            print("Division by zero is not allowed.")
        
        
    else:
        print('It\'s not possible')

    print('\n')
    n = input('Do you want to do more calculations? (y/n): ')
    n = n.lower()
    if n != 'y':
        print('The program is closed')
        break
