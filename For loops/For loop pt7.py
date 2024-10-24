temp = float(input('Enter a temperature in Celcius '))
if temp < -273.15:
	print('Invalid temperature')
elif temp == -273.15:
	print('The temperatue is absolute zero')
elif 0 > temp > -273.15:
	print('The temperature is below freezing')
elif temp == 0:
	print('The temperature is at freezing point')
elif 100 > temp > 0:
	print('The temperature is in the normal range')
elif temp == 100:
	print('The temperature is at boiling')
elif temp > 100:
	print('The temperature is above the boiling point')