sen = input('Enter a sentence ')
wordcount = 1
charcount = 0
alnumcount = 0
for a in sen:
	if a == ' ':
		wordcount += 1
	charcount +=1
	if a.isalnum():
		alnumcount += 1
print(sen)
print(wordcount)
print(charcount)
print((alnumcount/charcount)*100,'%',sep='')