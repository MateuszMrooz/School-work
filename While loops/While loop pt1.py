n = int(input('Enter a number '))
count = 1
while count <= n:
	if (count % 5) != 0:
		print(count)
	count = count + 1
while count >= n:
	if count == 0:
		print(0)
	elif (count % 5) != 0:
		print(count)
	count = count - 1