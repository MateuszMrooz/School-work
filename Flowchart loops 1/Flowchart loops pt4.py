r = int(input('Enter the number of rows '))
c = int(input('Enter the number of columns '))
for a in range(0,c):
	print('#'*r)

print('       ')

b = 0
while b < c:
	print('#'*r)
	b += 1