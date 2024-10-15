height  = int(input('Enter your height in cm '))
height_inch = height /2.54
feet = height_inch // 12
inch = round(height_inch % 12)
print('Your height is',feet,'feet and',inch,'inches')