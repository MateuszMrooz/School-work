x = float(input('Enter a number between 10 and 20 '))
while x< 10 or x >20:
    x = float(input('Enter a number between 10 and 20 '))
    if x > 20:
        print('Too high')
    elif x < 10:
        print('Too low')
print('Thank you')
