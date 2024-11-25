num = int(input('Enter an integer '))
string = input('Enter a string ')
num2 =''
for a in string:
	if a.isdigit():
		num2 += a
num3 = num + int(num2)
print(num,'+',num2,'=',num3)