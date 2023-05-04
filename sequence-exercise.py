
#################################################################
### question1: reverse a string.

str1 = "abcdefghijklmnopqrstuvwxyz"

def str_rev(s, start, end) -> str:
    # code here...
    lst = list(s)
    while start <= end:
      lst[start], lst[end] = lst[end], lst[start]
      start += 1
      end -= 1

    return ''.join(lst)

#print (str_rev(str1, 4, 18))

def str_rev2(s) -> str:
  s = list(s)
  r_s = ''
  for i in s:
    r_s = i + r_s
  return r_s

# print (str_rev2(str1))

def str_rev3(s):
   return s[::-1]

# print(str_rev3(str1))

#################################################################
"""
Write a Python function find the length of the longest 
increasing sub-sequence in a said list, which contains numbers.
for example the list: [10,100,1,3,5,7,888,70,80,90]
the answer should 5.
"""

test_list = [10,100,1,3,5,7,8,9,10,888,70,80,90]
def longest_increasing1(l):
  longest = 0
  long = 0
  current = l[0]
  for i in l:
    if i > current:
        long += 1
    else:
        long = 1
    current = i
    if long > longest:
        longest = long
  return longest

# print(longest_increasing1(test_list))

## the following way have some problem. but it make another picture 
## for resolving the problem. 
def longest_increasing2(nums):
    n = len(nums)
    arr = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                arr[i] = max(arr[i], arr[j]+1)
    print(arr)
    return max(arr)

#print(longest_increasing2(test_list))

#################################################################
### permutations
## Write a Python function that finds all the permutations of the members of a list.

"""
you don't have to remember the algorithm. Getting to know the permutations() method
in itertools is enough.  
"""

# method1: 
from itertools import permutations

permutation_result = [p for p in permutations('pro')]
#print(permutation_result)

# method2
def permutation_fun1(l, count = 0):
  if count == len(l):
    print (l)
  
  for i in range(count, len(l)):
    # need to create new memory
    # tmp = [p for p in l]
    tmp = list(l)
    tmp[i], tmp[count] = tmp[count], tmp[i]
    permutation_fun1(tmp, count+1)
  
# permutation_fun1([1,3,5])

# method3: 
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

print(permutations1([1,3,5]))

#################################################################
"""
We have a matrix = [[1,2], [3,4], [5,6], [7,8]]
Now need to turn matrix into [[1, 3, 5, 7], [2, 4, 6, 8]]
"""
matrix = [[1,2], [3,4], [5,6], [7,8]]
# nested list complihension
re_matrix1 = [[row[i] for row in matrix ] for i in range(2)]

re_matrix2 = []
for i in range(2):
  row = []
  for j in matrix:
    row.append(j[i])
  re_matrix2.append(row)

#################################################################
### Question: Remove Duplicates From a Python List
# use dict.fromkeys(), don't use set, because set is unordered
keywords = ['foo', 'bar', 'bar', 'foo', 'baz', 'foo']
print (list(dict.fromkeys(keywords)))
print (list(set(keywords)))



