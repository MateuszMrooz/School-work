sen = input('Enter a sentence or q to quit ')
sen1 = ''
while sen != 'q':
	for a in sen:
		if a == a.upper():
			sen1 += a.lower()
		elif a == a.lower():
			sen1 += a.upper()
	print(sen1)
	sen1 = ''
	sen = input('Enter a sentence or q to quit ')