
#################################################################
# Sorting Dictionaries in Python

# Basic way: convert to list, sorted(), then convert back to dict
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

sorted_people_bykey = dict(sorted(people.items()))
print(sorted_people_bykey)
sorted_people_byvalue = dict(sorted(people.items(), key=lambda item: item[1]))
print(sorted_people_byvalue)
