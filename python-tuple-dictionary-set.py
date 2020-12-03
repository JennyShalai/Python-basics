# TUPLES, DICTIONARY, SET

a_tuple = 1, 2
another_tuple = (1, 2)
yet_another_tuple = tuple([1, 2])

# tuple is immutable, new items can't be added,
# but if the tuple's item is a mutable it can be extand:
tuple = (1, [2,3])
tuple[1].append(4) # (1,[2,3,4])

tuple[index] # element on given index
len(tuple) # number of elements in the tuple
tuple.count(value)  # how many times value in the tuple
tuple.index(value)  # index of the first time seen value



dictionary = {key1: value1, key2: value2}
dictionary[key] = value # create new key-value
dictionary[key]         # return value for that key

for key in dictionary:
    print(key)

for value in dictionary.values():
    print(value)

for key, value in dictionary.items():
    print(key, value)

for pair in dictionary.items():
    print(pair)
# print out key-value pairs as tuple:
# (key1, value1)
# (key2, value2)
# (key3, value3)

if key in dictionary:
    # do something

for word in words:
    # some restrictions if needed
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

# DICTIONARY
# Definition
x = {key1:value1, key2:value2} 

# Operations
len(dictionary) # Returns the number of items in the dictionary
for key in dictionary # Iterates over each key in the dictionary
for key, value in dictionary.items() # Iterates over each key,value pair in the dictionary
if key in dictionary # Checks whether the key is in the dictionary
dictionary[key] # Accesses the item with key key of the dictionary
dictionary[key] = value # Sets the value associated with key
del dictionary[key] # Removes the item with key key from the dictionary

# Methods
dict.get(key, default) # Returns the element corresponding to key, or default if it's not present
dict.keys() # Returns a sequence containing the keys in the dictionary
dict.values() # Returns a sequence containing the values in the dictionary
dict.update(other_dictionary) # Updates the dictionary with the items coming from the other dictionary. 
                              # Existing entries will be replaced; new entries will be added.
dict.clear() # Removes all the items of the dictionary        
        
        
        
        
# SET
a_set = set([1, 2, 3])
other_set = {1, 2, 3}

set.add(value)
set.intersection(other_set)  # return only elements that are in both sets
set.remove(value)
set.clear
set.intersection_update
set.symmetric_difference
set.copy
set.isdisjoint
set.symmetric_difference_update
set.difference
set.issubset
set.union(other_set)
set.difference_update
set.issuperset
set.update
set.discard
set.pop


===
# COMPREHENSION

dictionary = {key:value for key in array}

# create a dictionary that has keys that are the original word and values
# that are the uppercase version of the word.
# {'organic': 'ORGANIC', 'kale': 'KALE', 'chip': 'CHIP', 'snack': 'SNACK'}
words = input('Enter words:')
words_dictionary = {word: word.upper() for word in words.split()}
print(words_dictionary)


# Create tuples that have a word of mixed case as the first element
# and an entirely lowercase string as the second element.
# (('RADIO', 'radio'), ('aStRoNoMy', 'astronomy'), ('Pulsar', 'pulsar'))
words = input('Enter words:')
result = tuple(i for i in ({key:key.lower() for key in words.split()}.items()))
print(result)
# OR result = tuple((word, word.lower()) for word in words.split())
