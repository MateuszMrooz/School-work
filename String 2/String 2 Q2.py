string = input('Enter something ')
num = 0
nums = ''
if any(b.isdigit() for b in string):
	for a in string:
		if a.isdigit():
			num = num + int(a)
			nums = nums + a
	print(string)
	print(nums)
	print(num)
else:
	print('There are no numbers')