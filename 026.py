word = input('Enter a word ')
word = word.lower()
vowels = ['a','e','i','o','u']
if word[0] in vowels:
    print(word+'way')
else:
    firstletter = word[0]
    print(word[1]+firstletter+'ay')