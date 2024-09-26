a = 'yes'
y = 0
while a == 'yes':
    x = input('Who do you want to invite? ')
    print(x,'has now been invited')
    y = y + 1
    a = input('Do you want to invite more people? ')
    a = a.lower()
print(y,'people are invited')