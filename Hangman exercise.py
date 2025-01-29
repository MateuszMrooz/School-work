#version where one letter can be guessed at a time
word = 'helloworld'
count = 0
life = 7
line =''
while count < len(word) and life > 0:
	print(line,(len(word)-count)*'_ ')
	guess = input('Guess the next letter: ')
	if guess.lower() == word[count]:
		print('Correct ',end='')
		count += 1
		line += guess
	else:
		life -= 1
		print('Incorrect, lives remaining:',life)
print('The answer was',word)
print('GAME OVER')
#Improved version
word = 'helloworld'
life = 7
count = 0
letters = ''
clues =' '+len(word)*'_ '
a = input('Would you like to play? ')
while a.lower() == 'yes':
	while count < len(word) and life > 0:
		print('Letters guessed:',letters,' ')
		guess = input('Guess a letter: ')
		letters += guess+' '
		count1 = 0
		while count1 < len(word):
			if word[count1] == guess:
				clues = clues[:2*count1 + 1] + guess + clues[2*count1 + 2:]
			count1 += 1
		print(clues)
		if clues == word:
			break
		count2 = 0
		for i in word:
			if i != guess:
				count2+=1
		if count2 == len(word):
			life -= 1
			print('Incorrect, lives remaining:',life)
		else:
			print('Correct')
		if life == 6:
			print('     |')
			print('     |')
			print('     |')
			print('     |')
			print(' ""')
		elif life == 5:
			print(' +---+')
			print(' |   |')
			print('     |')
			print('     |')
			print('     |')
			print(' ""')
		elif life == 4:
			print(' +---+')
			print(' |   |')
			print(' 0   |')
			print(' |   |')
			print('     |')
			print(' ""')
		elif life == 3:
			print(' +---+')
			print(' |   |')
			print(' 0   |')
			print(' |\  |')
			print('     |')
			print(' ""')
		elif life == 2:
			print(' +---+')
			print(' |   |')
			print(' 0   |')
			print('/|\  |')
			print('     |')
			print(' ""')
		elif life == 1:
			print(' +---+')
			print(' |   |')
			print(' 0   |')
			print('/|\  |')
			print(' \   |')
			print(' ""')
		elif life == 0:
			print(' +---+')
			print(' |   |')
			print(' 0   |')
			print('/|\  |')
			print('/\   |')
			print(' ""')
	print('GAME OVER')
	a = input('Would you like to play again? ')
print('Thank you for playing')