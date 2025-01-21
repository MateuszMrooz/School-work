#1a
print('''
1
 2
  3
  ''')
#1b
text = 'Test.\nNextline.'
print(text)
#1c
print('one','two'*2)
print('one'+'two'*2)
print(len('0123456789'))
#1d
s = '0123456789'
print(s[3],',','-',s[2:5])
print(s[:3],'-',s[3:],',',s[3:100])
print(s[20:],s[2:1],s[1:1])
#1e
s = '987654321'
print(s[-1],s[-3])
print(s[-3],s[:-3])
print(s[-100:-3],s[-100:3])
#2a
y = str(123)
x = 'hello'*3
print(x,y)
x = 'hello'+'world'
y=len(x)
print(y,x)
#2b
x='hello'+\
   'to python' +\
   'world'
for char in x:
	y = char
	print(y,':',end='')
#2c
x = 'hello world'
print(x[:2],x[:-2],x[-2:])
print(x[6],x[2:4])
print(x[2:-3],x[-4:-2])
#3
theStr = 'This is a test'
inputInt = int(input('Enter an integer '))
testStr = theStr
while inputInt >= 0:
	testStr= testStr[1:-1]
	inputInt -= 1
testBool = 't' in testStr
print(theStr)
print(testStr)
print(inputInt)
print(testBool)
#4
testStr = 'abcdefghi'
inputInt = int(input('Enter an integer '))
count = 2
newStr = ''
while count <= inputInt:
	newStr += testStr[0:count]
	testStr= testStr[2:]
	count += 1
print(newStr)
print(testStr)
print(count)
print(inputInt)