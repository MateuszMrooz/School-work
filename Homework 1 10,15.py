#10
minimum = 0
num = -1
maximum = num
count = 0
sum1 = 0
if num < 0:
	minimum = num
	maximum = 0
	while count <= maximum - minimum:
		sum1 += count
		count += 1

#15
count = 0 # New code
a = int(input('Enter a value: '))
while a != 0:
	count = count+1
	a = int(input('Enter a value: '))
print('You entered',count,'values')