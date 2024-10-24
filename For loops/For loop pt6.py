temp = int(input('Enter the temperature '))
unit = input('Celcius or Farenheit? ')
if unit.lower() == 'celcius':
	temp = 9/5*temp + 32
	print('The temperature in Ferenheit is',temp)
elif unit.lower() == 'ferenheit':
	temp = 5/9*(temp-32)
	print('The temperature in Celcius is',temp)