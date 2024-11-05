count= 0
avg = 0
num = 0
num1 = 0
while num >= 0:
	num = input('Enter an integer ')
	num = int(num)
	if num >= 0:
		num1 += num
		count += 1
		avg = num1/count
print(avg)