m = int(input('Enter a number '))
n = int(input('Enter a number '))
for i in range(1,m):
	if i%n == 0 and i%2 == 0:
		print(i,'even')
	elif i%n == 0:
		print(i,'odd')