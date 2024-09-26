x = float(input('Enter a number '))
y = float(input('Enter a number '))
x = x + y
a = 'y'
while a == 'y':
    a = input('Do you want to add another number?')
    if a == 'y':
        h = float(input('Enter another number '))
        x = x+h
print(x)