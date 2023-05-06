
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

# print(permutations1([1,3,5]))

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
# print (list(dict.fromkeys(keywords)))
# print (list(set(keywords)))

#################################################################
# Write a Python a function to find the union and intersection of two lists
# Set type provide a range of method for mathematical 
# operation: intersection, union, difference, and symmetric difference

intersection1 = [1, 2, 3, 4, 5]
intersection2 = [3, 4, 5, 6, 7, 8]

def find_intersection (l1, l2):
  return l1, l2

# print(type(find_intersection(intersection1, intersection2)))
# print(set(intersection1) & set(intersection2))
  

#################################################################
# maximum minimum sum sub-sequence problems:
"""
Question:
Find the maximum sum sub-sequence in a list, and return the maximum sum value.
Like:
nums =  [-4,-1,100,-4,3,5,4,6,9,2,-10]
maximum sum sub-sequence should be:
sum([100,-4,3,5,4,6,9,2])
"""
"""
Conclusion:
Sum sub-sequence knowlodge basic:
-- Rule1: 
   If sum of sub-sequence smaller than the current value. 
   that means it should stop for maximum
-- Rule2: 
   If Sum of sub-sequence bigger than 0. that means it will be part of Maximum.
-- vice versa for minimum
"""

# According to Rule1
def max_sum_subsequence1(arr):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
      dp[i] = max(arr[i], dp[i-1] + arr[i])
    return max(dp)
    # return dp

# According to Rule2:
def max_sum_subsequence2(arr):
  max_value, sum_value = 0, 0
  for i in range (len (arr)):
    sum_value += arr[i]
    if sum_value < 0:
      sum_value = 0
    if sum_value > max_value:
      max_value = sum_value
  if max_value == 0:
    max_value = max(arr)
  return max_value

# nums = [12,-1,-100,4,3,-5,1000,9,2,10,-1]
# print(max_sum_subsequence1(nums))
# print(max_sum_subsequence2(nums))

"""
Question: 
find the maximum sum sub-sequence in a list, and return that sub-sequence.
"""

# According to Rule1: 
def max_sum_subsequence3(arr):
    n = len(arr)
    dp = [(arr[0],1)]
    for i in range(1, n):
      value = dp[i-1][0]
      count = dp[i-1][1]
      if arr[i] > value + arr[i]:
        count = 1
      else:
        count += 1
      value = max (value+arr[i], arr[i])
      dp.append ((value, count))
    #print(dp)
    max_index = 0
    max_value = dp[0][0]
    for j in range(1,len(dp)):
      if dp[j][0] > max_value:
        max_index = j
        max_value = dp[j][0]
    print(max_value)
    return arr[max_index+1-dp[max_index][1]: max_index+1]

# According to Rule2: 
# if current_sum if smaller than 0, then update current_start 
def max_sum_subsequence4(arr):
  max_value, sum_value = 0, 0
  start, end, current_start = 0, 0, 0

  for i in range(len(arr)):
    sum_value += arr[i]
    if sum_value > max_value: 
      max_value = sum_value
      start = current_start
      end = i
    if sum_value < 0:
      sum_value = 0
      current_start = i + 1
  print(max_value)
  return arr[start: end+1]

# nums = [98,-12,1,10,-4,3,-500,4,10,5,-10, 9]
# print( max_sum_subsequence3(nums) )
# print( max_sum_subsequence4(nums) )

"""
Quention: 
Find the minimum sum sub-sequence in a list, and return that sub-sequence.
"""
def minimum_sum_subsequence(lst):
    min_sum = float('inf')
    start, end = 0, 0
    curr_start, curr_sum = 0, 0
    
    for i in range(len(lst)):
        curr_sum += lst[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
            start = curr_start
            end = i
        if curr_sum > 0:
            curr_sum = 0
            curr_start = i + 1
    
    return lst[start:end+1]

# nums = [8,-12,1,1000,-4,3,5,4,-1000,9,2,-12,11]
# print(minimum_sum_subsequence(nums))

#################################################################

