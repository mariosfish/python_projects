import math
import random
import string

code = ''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
digits = ''

print('Random Code Generator')
digits = input('Enter the desire number of digits of your code: ')

while digits.isalpha():
    digits = input('Enter the desire number of digits of your code: ')
else:
    for i in range(0, int(digits)):
        if i % random.choice(numbers) == 0:
            code = code + random.choice(string.ascii_letters)
        else:
            code = code + str(random.choice(numbers))
print(code)
print((len(code)))  # for debugging
