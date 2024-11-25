num = input('Enter a phone number ')
if num[3] == '-' and num[7] == '-' and len(num) == 12 and num[0:3].isdigit() and num[4:7].isdigit() and num[9:]:
	print('Valid number')
else:
	print('Invalid number')