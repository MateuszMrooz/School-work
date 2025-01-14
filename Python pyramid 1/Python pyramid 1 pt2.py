n = 5
a = n-1
b = 1
while a >= 0:
	print(' '*a,'*'*b)
	a -= 1
	b = 2*(n-a) - 1