grade,count,avg = 0,0,0
while grade >=0:
	grade = int(input('Enter your grade '))
	count =+ 1
	avg = grade/count
if avg >= 90:
	print('Your average is A',avg)
elif avg >= 80:
	print('Your average is B',avg)
elif avg >= 70:
	print('Your average is C',avg)
elif avg >= 60:
	print('Your average is D',avg)
elif avg <= 56:
	print('Your average is F',avg)