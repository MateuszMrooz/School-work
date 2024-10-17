hour = int(input('Enter an hour between 1 and 12 '))
ahead = int(input('How many hours ahead would you like to know the time '))
ahead1 = ahead % 12
time = hour + ahead1
print('in',ahead,'hours it will be',time,"o'clock")