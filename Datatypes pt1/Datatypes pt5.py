num1 = list(input('Enter a 3 digit number '))
num2 = num1[::-1]
print(''.join(num2) )

num = int(input('Enter a 3 digit number '))
num3 = num % 10
num5 = num // 100
num4 = int( (num - num3 - (num5 * 100))/10 )

print(str(num3)+str(num4)+str(num5))