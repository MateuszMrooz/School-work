num = 0
total = 0
while num >= 0:
	num = int(input('Enter a number '))
	total = total + num
print(total-num)

num = int(input('Enter a number '))
total = 0
if num >=0:
	while num>0:
		total = total + num
		num = int(input('Enter a number '))
	else:print(total)
else:
	print(total)