#Type C
#1
l = (1,2,3,4)
print(l[-1::-1])
#2
l = list(input('Enter a list: '))
l1 = list(input('Enter a list: '))
l.extend(l1)
print(l)
#3
l =input('Enter a list containing numbers between 1 and 12: ').split()
count = 0
for a in l:
	if int(a) > 10:
		l.remove(a)
		l.insert(count,10)
	count += 1
print(l)
#4
l = input('Enter a list of strings: ').split()
count = 0
for a in l:
	l[count] = a[1:]
	count += 1
print(l)
#5(a)
l = list()
for a in range(50):
	l.append(a)
print(l)
#5(b)
l = list()
for a in range(51):
	l.append(a**2)
print(l)
#5(c)
l = list()
for a in range(26):
	l.append(chr(a+97)*(a+1))
print(l)
#6
L = input('Enter a list: ').split()
M = input('Enter a list: ').split()
N = list()
if len(L) > len(M):
	big = len(L)
else:
	big = len(M)
for a in range(big):
	N.append(int(L[a]) + int(M[a]))
print(N)