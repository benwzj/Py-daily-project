
### permutations
## Write a Python function that finds all the permutations of the members of a list.
# method1: 
def permutations1(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        m = nums[i]
        rem_list = nums[:i] + nums[i+1:]
        for p in permutations1(rem_list):
            result.append([m] + p)
    return result

# method2
  
def permutations2(lst, i=0):
    if i == len(lst):
      print (lst)
    for j in range(i, len(lst)):
      # need to create new memory
      tmp = [p for p in lst]
      # swap
      tmp[i], tmp[j] = tmp[j], tmp[i]
      permutations2(tmp, i+1)

nums1 = ['a','b','c']
print(permutations1(nums1))
permutations2(nums1)

# permutations function in itertools lib
from itertools import permutations

words = [''.join(p) for p in permutations('pro')]
word = [p for p in permutations('pro')]
#print(word)

"""
### Question2: Remove Duplicates From a Python List
# use dict.fromkeys(), don't use set, because set is unordered
keywords = ['foo', 'bar', 'bar', 'foo', 'baz', 'foo']
print (list(dict.fromkeys(keywords)))
print (list(set(keywords)))

### Question3: nonlocal concept
def test_scopes():
  x = 'spam'
  def change_local():
    x = 'local_spam'
  def change_nonlocal():
    nonlocal x
    x = 'nonlocal_spam'
  def change_global():
    global x
    x = "global_spam"
  
  x = "test_spam"
  change_local()
  print (x)
  change_nonlocal()
  print(x)
  change_global()
  print(x)

test_scopes()
print(x)
"""

