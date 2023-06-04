
from collections import Counter, defaultdict
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

# print(my_dict)


#################################################################
#  remove duplicates value from the dictionary.

student_data = {'id1':
                {'name': ['Sara'],
                 'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                'id2':
                {'name': ['David'],
                    'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                'id3':
                {'name': ['Sara'],
                    'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                'id4':
                {'name': ['Surya'],
                    'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                }


def remove_duplicated_values(d):
    result = {}
    for key, value in d.items():
        if value not in result.values():
            result[key] = value
    return result

# print(remove_duplicated_values(student_data))

#################################################################
# collections.Counter() exercise
# counter is subclass of dictionary.
# counter support operator '+'


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
dc = Counter(d1) + Counter(d2)
# print(dc)

# Sample data: [{'item': 'item1', 'amount': 400},
#               {'item': 'item2', 'amount': 300},
#               {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

data = [{'item': 'item1', 'amount': 400},
        {'item': 'item2', 'amount': 300},
        {'item': 'item1', 'amount': 750}]


def output_counter1(d):
    result = Counter()
    for i in d:
        result += Counter(dict([(i['item'], i['amount'])]))

    return result


def output_counter2(d):
    result = Counter()
    for i in d:
        result[i['item']] += i['amount']
    return result


# print(output_counter1(data))
# print(output_counter2(data))


# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
sample_string = "Track the count of the letters from the string"


def char_counter(s):
    return Counter(s)


def char_counter1(s):
    result = {}
    for i in s:
        if i != ' ':
            result[i] = result.get(i, 0) + 1
    r = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    return r


# print(char_counter1(sample_string))

#################################################################
# find the highest 3 values of corresponding keys in a dictionary.

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

sorted_lst = sorted(my_dict.items(), key=lambda item: item[1])

# print([i[0] for i in sorted_lst[len(sorted_lst)-3:]])

#################################################################
# print a dictionary in table format.
# table_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}
# C1 C2 C3
# 1 5 9
# 2 6 10
# 3 7 11

table_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}


def print_table_from_dict(d):
    length = 0
    for i in d:
        if len(d[i]) > length:
            length = len(d[i])
        print(i, end="")
    print('')
    for i in range(length):
        for j in d:
            print(d[j][i], end="")
        print('')


def print_table_from_dict1(d):
    for row in zip(*[(key, * item) for key, item in d.items()]):
        print_tuple_withoutbracket(row)


def print_tuple_withoutbracket(t):
    for i in t:
        print(i, end=' ')
    print('')


# print_table_from_dict1(table_dict)

#################################################################
# input: num_list = [1, 2, 3, 4]
# required output: {1: {2: {3: {4: {}}}}}

num_list = [1, 2, 3, 4]


def nested_dic1(l):
    result = {}
    for i in reversed(l):
        result = {i: result}
    return result


def nested_dic2(l):
    result = current_dic = {}
    for i in l:
        current_dic[i] = {}
        current_dic = current_dic[i]
    return result


# print(nested_dic1(num_list))
# print(nested_dic2(num_list))

#################################################################
# defaultdict example

# from:  [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# to : {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
# defaultdict is more efficient than setdefault()
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]


def use_defaultdic(l):
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)

    print(d)  # {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})


def use_setdefault(l):
    d = {}
    for k, v in s:
        d.setdefault(k, []).append(v)

    print(d)


def default_list():
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    print(d)


def constant_factory(value):
    return lambda: value


def default_int():
    s = 'mississippi'
    d = defaultdict(constant_factory(0))
    for c in s:
        d[c] += 1
    print(d)


default_int()

#################################################################
# dict.fromkeys(keys, value) example


def test_fromkeys():
    lst = [1, 2, 3, 4, 3, 4]
    lst2 = ['foo', 'bar']
    dct = {}
    print(dct.fromkeys(lst, lst2))


# test_fromkeys()

#################################################################
def dictvalue_set():

    x = {'key1': 1, 'key2': 3, 'key3': 2}
    y = {'key1': 1, 'key2': 3}
    for k, v in set(x.items()) & set(y.items()):
        print(k, v)


dictvalue_set()

ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/BenWordPress

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