g1 = int(input('Enter grade 1 '))
g2 = int(input('Enter grade 2 '))
g3 = int(input('Enter grade 3 '))
g4 = int(input('Enter grade 4 '))
average = (g1 + g2 + g3 + g4) / 4
if average > 50:
	print('Pass')
else:
	print('Fail')