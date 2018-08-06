import random
import string

print('Random Code Generator')

code = ''
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, 26):
	if i % 3 == 0:
		code = code + random.choice(string.ascii_letters)
	else:
		code = code + str(random.choice(numbers))

print code
