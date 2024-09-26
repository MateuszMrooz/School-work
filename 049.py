compnum = 50
x = float(input('Guess a number '))
y = 1
while x != compnum:
    if x > compnum:
        print('Too high')
        x = 0
    elif x < compnum:
        print('Too low')
    x = float(input('Guess another number '))
    y = y + 1
print('Well done. That took',y,'attempt(s)')