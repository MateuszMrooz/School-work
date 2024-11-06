start = int(input('Enter the start value '))
end = int(input('Enter the end value '))
mul = int(input('Enter the multiple to ignore '))

while start <= end:
	if (start % mul) != 0 and (start % 2) == 1:
		print(start)
	start = start + 1