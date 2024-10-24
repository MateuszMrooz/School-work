n = int(input('Enter a number less then 20 '))
if n > 11:
	c = range(11,n+1)
elif n < 11:
	c= range(-11,-n+1)
for i in c:
	print(abs(i))
	i+1
if n%3 == 0:
	print('Tipsy')
if n%7 == 0:
	print('Topsy')