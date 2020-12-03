# INTRO TO PYTHON (numeric data and basic math operations )

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
strip() #returns a new string after removing any leading and trailing whitespaces including tabs (\t).
rstrip() #returns a new string with trailing whitespace removed. It’s easier to remember as removing white spaces from “right” side of the string.
lstrip() #returns a new string with leading whitespace removed, or removing whitespaces from the “left” side of the string.
capitalize()
upper()
lower()
replace(value, new_value)
split() 	# list (array) of words
isupper() 	# bool 
endswith()
len(string) # length
string[i] 	# chat at I position
count(value) # count words in string
isnumeric() #returns true if all characters in the string are numeric
"-".join("a", "b", "c") # return "a-b-c", join()

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
string.index("x") #method index() returning the position of the first "x" in the string

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


# list is an array in swift
list = [1, ‘hi’, 4.5]
list('hello')   # ['h', 'e', 'l', 'l', 'o']

append(value)   # add new value at the end of the list
pop()           # delete last element in list and return it’s value
remove()        # delete last element of the list
reverse()
sort()          # sort from small to big

list[index]
list[start_index:end_index] # sublist of elements from start_index till (end_index-1)
list[-1]    # last element
list[:]     # all elements
list[::3]   # every 3rd element

for element in list:
    print(element)

for index, element in enumerate(list):
    print(index, element)

# list comprehension
in_list = ['SPAM', 'Spam', 'spam']
answer = [value.lower() for value in in_list]
         # what to do    # with what #from where

