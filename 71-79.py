#71
L = ['basketball','baseball']
x = input('Input your favourite sport ')
L.append(x)
L.sort()
print(L)
#72
L = ['chemistry','biology','physics','maths','woodwork','english']
print(L)
x = input('Which of these do you not like? ')
L.remove(x)
print(L)
#74
Colours = ['blue','green','yellow','orange','red','pink','navy','aqua','purple','white']
num1 = int(input('Enter a number between 0-4 '))
num2 = int(input('Enter a number between 5-9 '))
print(Colours[num1:num2+1])
#75
numbers = [123,124,125]
print(*numbers,sep='\n')
num = int(input('Enter a 3 digit number '))
if num in numbers:
	print(numbers.index(num)+1)
#76
List = [input('Who do you want to invite ')]
List.append(input('Who do you want to invite '))
List.append(input('Who do you want to invite '))
x = input('Do you want to invite more? (Y/N) ')
while x == 'Y':
	List.append(input('Who else do you want to invite '))
	x = input('Do you want to invite more? (Y/N) ')
print('There are',len(List),'invited')
#77
print(List)
x = input('Enter a name from the list ')
print(List.index(x)+1)
y = input('Do you still want them to come?(Y/N) ')
while y == 'N':
	List.remove(x)
	print(List)
	x = input('Enter a name from the list ')
	y = input('Do you still want them to come?(Y/N) ')
#78
Tv = ['channel','radio','tv2','tv1']
print(*Tv,sep='\n')
x = input('Enter another Tv program ')
y = int(input('Enter its position '))
Tv.insert(y-1,x)
print(Tv)
#79
nums = []
for a in range(0,2):
	x = int(input('Enter a number '))
	nums.append(x)
y = input('Do you want to keep the last number?(Y/N) ')
if y == 'N':
	nums.reverse()
	nums.remove(0)
	nums.reverse()
print(nums)