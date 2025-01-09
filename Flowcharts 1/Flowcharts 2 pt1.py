import math
a = int(input('Enter a '))
b = int(input('Enter b '))
c = int(input('Enter c '))
root1 = (-b + math.sqrt(b**2-4*a*c))/2
root2 = (-b - math.sqrt(b**2-4*a*c))/2
print(root1)
print(root2)