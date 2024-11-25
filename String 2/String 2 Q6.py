str1 = input('Enter a string ')
str2 = input('Enter a string ')
if len(str1) >= len(str2):
	largestr = str1
	smallstr = str2
elif len(str1) < len(str2):
	largestr = str2
	smallstr = str1
print(smallstr)
print(largestr[0:1],'     ',largestr[-1:])
print('',largestr[1:2],'   ',largestr[-2:-1])
print(' ',largestr[2:3],' ',largestr[-3:-2])