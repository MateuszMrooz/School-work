finalnum = input('Enter a 9 digit number ')
count = 1
total = 0
num = int(finalnum)
while count <= 9:
	count = count + 1
	num1 = num%10
	num = num//10
	total = total + num1*count
num2 = 11
while num2 < total:
	num2 = num2 + 11
checksum = num2 - total
if checksum == 10:
	checksum = X
print(finalnum,checksum,sep='')

#020131452