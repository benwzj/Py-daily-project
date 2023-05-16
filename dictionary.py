
import operator
#################################################################
# Sorting Dictionaries in Python

# Basic way: convert to list, sorted(), then convert back to dict
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

sorted_people_bykey = dict(sorted(people.items()))
sorted_people_byvalue = dict(sorted(people.items(), key=lambda item: item[1]))

# print(people.items())
# print(sorted_people_byvalue)
# print(sorted_people_bykey)

# Using operator module for helper function

sorted_people_byvalue2 = dict(
    sorted(people.items(), key=operator.itemgetter(1)))

# print(sorted_people_byvalue2)

#################################################################
# Write a Python program to get the maximum and minimum values of a dictionary.
dict_mm = {1: 2, 3: 4, 4: 3, 2: 1, 0: 11}


def get_max_min(d):
    minimun_value = float('inf')
    maximun_value = float('-inf')
    for key, value in d.items():
        if value < minimun_value:
            minimun_value = value
        if value > maximun_value:
            maximun_value = value
    return maximun_value, minimun_value

# print(get_max_min(dict_mm))


def get_max_min1(d):
    key_max = max(d.values())
    key_min = min(d.values())
    return key_max, key_min


# print(get_max_min1(dict_mm))

#################################################################
# add items

my_dict = {'x': 500, 'y': 5874, 'z': 560}
# 1 directly
my_dict[3] = "xyz"

# 2 update()
# my_dict.update({4: 5})
dict_list = ((11, 22), (33, 44))
my_dict.update(dict_list)

# 3 using keyword parameter
my_dict.update(iii=111)
print(my_dict)
