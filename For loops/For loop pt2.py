num1 = int(input('Enter an integer that ends in 4 or 8 '))
if num1%10 == 4:
	print('ends with 4')
elif num1%10 == 8:
	print('ends with 8')
else:
	print('ends with neither')