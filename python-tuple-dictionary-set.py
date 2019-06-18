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



