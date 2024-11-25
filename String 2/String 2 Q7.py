num = int(input('Enter a number up to 4 digits '))
ans = ''
if num >= 1000:
	M = num//1000
	ans = 'M'*M
if (num//100)%10 >= 5:
	ans = ans + 'D'
	if (num//100)%10 >= 6:
		ans = ans + 'C'*(((num//100)%10)-5)
if (num//100)%10 == 4:
	ans = ans + 'CD'
if 4 > (num//100)%10 > 0:
	ans = ans + 'C'*((num//100)%10)
if ((num//10)%100)%10 >= 5:
	ans = ans + 'L'
	if ((num//10)%100)%10 >= 6:
		ans = ans + 'X'*((((num//10)%100)%10)-5)
if ((num//10)%100)%10 == 4:
	ans = ans + 'XL'
if 4 > ((num//10)%100)%10 > 0:
	ans = ans + 'X'*(((num//10)%100)%10)
if num%10 >= 5:
	ans = ans + 'V'
	if num%10 >= 6:
		ans = ans + 'I'*((num%10)-5)
if num%10 == 4:
	ans = ans + 'IV'
if 4 > num%10 > 0:
	ans = ans + 'I'*(num%10)
print(ans)