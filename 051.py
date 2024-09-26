x = 10
while x>0 :
    print('There are',x,'green bottles hanging on the wall',x,'green bottles hanging on the wall, and if 1 green bottle should acidently fall')
    y = int(input('how many green bottles should be hanging on the wall? '))
    if y == x-1:
        print('There will be',y,'green bottles hanging on the wall')
        x = x-1
    else:
        print('No try again')
print('There are no more green bottles hanging on the wall')