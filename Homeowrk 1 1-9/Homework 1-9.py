#2
temp = 50
if temp < 32:
	print('ice')
elif temp < 212:
	print('water')
else:
	print('steam')

#3
x = 1
if x>3:
	if x>4:
		print('A',end='')
	else:
		print('B',end='')
elif x<2:
	if(x != 0):
		print('C',end='')
print('D',end='')

#4
weather = 'raining'
if weather == 'sunny':
	print('wear sunvblock')
elif weather == 'snow':
	print('going skiing')
else:
	print(weather)

#5
if 'zero' == 0:
	print('zero')
elif str(0) == 'zero':
	print(0)
elif str(0) == '0':
	print(str(0))
else:
	print('none of the above')

#6
n = 1
if n==0:
	print('zero')
elif n ==1:
	print('one')
elif n==2:
	print('two')
else:
	print('none of the above')

#7
n = int(input('Enter an integer '))
if n<1:
	print('invalid value')
else:
	for i in range(1,n+1):
		print(i**2)

#8
n = int(input('Enter an integer '))
if n > 0:
	for a in range(1,n+n):
		print(a/(n/2))
	else:
		print('Now quitting')

n = int(input('Enter an integer '))
if n > 0:
	for a in range(1,n+n):
		print(a/(n/2))
else:
	print('Now quitting')

#9(a)
for i in range (100,0,-3):
	print(i)
#(b)
num = 10
for i in range(0,i+1):
	print(num%10)
	num = num/10
	if num <= 0:
		break
#(c)
sum1 = 0
num = 31
for i in range(0,11):
	if num <= 0:
		break
	sum1 += num
	num -=2
	if i == 10:
		print(sum1/float(i))