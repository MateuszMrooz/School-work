#5
inputStr = input('Give me a string: ')
bigInt = 0
littleInt = 0
otherInt = 0
for ele in inputStr:
	if ele >= 'a' and ele <='m':
		littleInt += 1
	elif ele > 'm' and ele <= 'z':
		bigInt += 1
	else:
		otherInt += 1
print(bigInt)
print(littleInt)
print(otherInt)
print(inputStr.isdigit())
#6
in1Str = input('Enter a string of digits: ')
in2Str = input('Enter a string of digits: ')
if len(in1Str) > len(in2Str):
	small = in2Str
	big = in1Str
else:
	big = in2Str
	small = in1Str
newStr = ''
for element in small:
	result = int(element) + int(big[0])
	newStr += str(result)
	big = big[1:]
print(len(newStr))
print(newStr)
print(big)
print(small)
#7(a)
S = input('Enter a string: ')
RS = ''
for ch in S:
	RS += ch
print(S + RS)
#7(b)
S = input('Enter a string: ')
RS = ''
#for ch in S:
	# RS = ch + 2 + RS Cannot add string to int
print(RS + S)
#8(a)
S = 'PURA VIDA'
#print(S[9] +S[9:15])
#8(b)
S = 'PURA VIDA'
S1 = S[:10] + S[10:]
#S2 = S[10]+s[-10]
#8(c)
S = 'PURA VIDA'
S1 = S*2
#S2 = S1[-19] + S1[-20]
S3 = S1 [-19:]
#8(d)
S = 'PURA VIDA'
S1 = S[:5]
S2 = S[5:]
#S3 = S1*S2
S4 = S2 + '3'
#S5 = S1 + 3
#9
print('whenever'.find('never'))
print('whenever'.find('what'))