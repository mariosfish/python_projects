import random
import string
import math

print('Random Code Generator')

digits= int(input('Enter the desire number of digits of your code: '))
code = ''
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, digits):
	if i % random.choice(numbers) == 0:
		code = code + random.choice(string.ascii_letters)
	else:
		code = code + str(random.choice(numbers))

print (code)
print (len(code))
