sen = input('Enter a sentence ')
count = 0
count1 = 1
count2 = 0
space = ' '
while count < len(sen):
	if sen[count] == space and sen[count+1] != space:
		if count2 == 0:
			word1 = (sen[0:1].upper() + sen[1:count])
			print(word1)
		else:
			print(sen[len(word1) + 1:len(word1)+2].upper() + sen[len(word1)+2:count])
		count2 = count2 + 1
	count = count + 1
while count1 <len(sen):
	count1 = count1 + 1
	if sen[-count1] == space and sen[-count1+1] != space:
		word2 = (sen[-count1-1].upper() + sen[-count])
		print(word2)
		break