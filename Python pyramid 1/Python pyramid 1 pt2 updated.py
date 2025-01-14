n = 5
a = n-1
b = 1
while a >= 0:
	print(' '*a,'*'*b)
	a -= 1
	b = 2*(n-a) - 1

for i in range(1,n+1):
	print(' '*(n-i),end='')
	for j in range(1,2*(i-1)+1):
		print('*',end='')
	print('*')