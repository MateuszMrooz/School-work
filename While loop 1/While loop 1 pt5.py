num = int(input('Enter an integer '))
num1 = 0
if num > 0:
	while num1 <= num:
		if (num1 % 2) == 0:
			print(num1)
		num1 = num1 + 1
elif num < 0:
	while num1 >= num:
		if (num1 % 2) == 0:
			print(num1)
		num1 = num1 - 1