import random
import string

print('Random name generator')
print
print

name=""
for i in range(0,5):
	letter=random.choice(string.ascii_uppercase)
	name= name+letter
print name

print("test")
print('marios')
