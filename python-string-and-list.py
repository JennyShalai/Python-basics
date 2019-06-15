INTRO TO PYTHON (numeric data and basic math operations )

int, float, complex
snake_case_naming_convention
if elif else
while
continue, break, pass

# STRINGS AND LISTS
str
str(value) # casting to string
+ 	# concatenate strings
*n 	#repeat string n times
strip()	#removes the trailing space 
capitalize()
upper()
lower()
replace(value, new_value)
split() 	# list (array) of words
isupper() 	# bool 
endswith()
len(string) # length
string[i] 	# chat at I position

string[i,j] # chars from i to j-1 positions
string[N:]	# remover first N chars
string[:N]	# leaves first N chars
string[:-N]	# removes last N chars
string[-N:]	# leaves last N chars
'012345'[:2]  # 01
'012345'[2:]  # 2345
'012345'[:-2] # 0123
'012345'[-2:] # 45
'012345'[::2] # 024 - every second char
'012345'[1:5:2] #135 in range from 1 to (5-1) position take every second char

# !!! So ‘:’ is a separator to set a range for string slicing, 
# if no number is given it mean “from the beginning of the sting 
# till N position” like so [:N], or “from N position till the end 
# of the sting” like so [N:]

while index < len(string):
	print(string[index])
	index += 1

for index in range(len(string)):
	print(string[index])

for char in string:
	print(char)

format(parameter) # string formatting 
# print(‘Hello, {}!’.format(‘John’))
# print(‘Hello, {0}! I am {1}’.format(‘John’, ‘Jen’))
# print('%d %s %.4f.' % (2, 'formatting', 3.1415)) -> 2 formatting 3.1415.

