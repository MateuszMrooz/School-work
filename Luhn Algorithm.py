num = input('Enter a credit card number ')
count = 0
total = 0
num1 = int(num)
while count <= len(num):
	count = count + 1
	num2 = num1%10
	num1 = num1//10
	if (count % 2) == 0:
		num2 = num2*2
		if num2 >= 10:
			total = total + (num2%10) + 1
		else:
			total = total + num2
	else:
		total = total + num2
	print (total)
if total%10 == 0:
	print('Valid credit card',total)
else:
	print('Invalid credit card',total)