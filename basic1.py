
### question1: reverse a string.

# operate it as an array
str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = ""
length = len(str1)
while length:
  str2 += str1[length-1]
  length = length-1

# print(str2)

# using slice syntax:
# print(str1[::-1])
# print(str1.index('z'))

# using for
tmp = ""
for i in str1:
  tmp = i + tmp

# print (tmp)

# a function Reverse a string at a specific location
def reverse_string_in_location(string, start_pos, end_pos):
  if (start_pos >= end_pos):
    return string
  string_lenght = len(string)
  string_re = string[start_pos: end_pos]
  string_re = string_re[::-1]
  if start_pos > 0:
    string_re = string[0:start_pos] + string_re
  if end_pos < string_lenght-1:
    string_re = string_re + string[end_pos:string_lenght]
  return string_re

#print(reverse_string_in_location(str1, 4, 20))

# a function Reverse a list at a specific location
def reverse_list_in_location(lst, start_pos, end_pos):
  while start_pos < end_pos:
    lst[start_pos], lst[end_pos] = lst[end_pos], lst[start_pos]
    start_pos += 1
    end_pos -= 1
  return lst

#print ( reverse_list_in_location(list(str1), 4, 20) )

## Write a Python function find the length of the longest 
## increasing sub-sequence in a said list, which contains numbers.
def longest_increasing_subsequence1(nums):
  longest = 1
  length = 1
  start = nums[0]
  for i in nums:
    if i > start:
      length += 1
    else:
      length = 1
    start = i      
    if length > longest: 
      longest = length
  return longest

## the following way have some problem. but it make another picture 
## for resolving the problem. 
def longest_increasing_subsequence2(nums):
    n = len(nums)
    arr = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                arr[i] = max(arr[i], arr[j]+1)
    print(arr)
    return max(arr)

nums = [10,100,1000,1,3,5,1,30,40,50,60,70,80,909,10,2]

print( longest_increasing_subsequence1(nums))
print( longest_increasing_subsequence2(nums))


## Write a Python function that finds all the permutations of the members of a list.
def permutations(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        m = nums[i]
        rem_list = nums[:i] + nums[i+1:]
        for p in permutations(rem_list):
            result.append([m] + p)
    return result

nums1 = [10,30,20]
print(permutations(nums1))

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

