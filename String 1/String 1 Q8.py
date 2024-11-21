word = input('Enter something ')
count = 1
word2 = ''
while count < len(word):
	if count % 2 == 0 and count != 0:
		word2 += word[count].upper()
	else:
		word2 += word[count]
	count = count+1
print(word2)
