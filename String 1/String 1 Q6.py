word = input('Enter a palindrome ')
if word[0:len(word)//2] == word[-1:len(word)//2:-1]:
	print('This is a palindrome')
else:
	print('This is not a palindrome')