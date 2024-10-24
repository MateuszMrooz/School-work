n = int(input('Enter a number '))
i = range(1,n+1,2)
g = 0
for c in i:
	c = c**2
	g = c+g
print(g)