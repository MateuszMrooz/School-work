count= 0
avg = 0
num = 0
num1 = 0
while num != '':
	num = input('Enter an integer ')
	if num !='':
		num = int(num)
		num1 += num
		count += 1
		avg = num1/count
print(avg)