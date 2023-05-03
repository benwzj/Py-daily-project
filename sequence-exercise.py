
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
# method1: 

permutation_list = 'abcefg'

def factorial(n):
  r = 1
  for i in range(1,n+1):
    r = r * i
  return r


def permutation_fun1(l, count = 0):
  if count == len(l):
    print (l)
  
  for i in range(count, len(l)):
    tmp = [p for p in l]
    tmp[i], tmp[count] = tmp[count], tmp[i]
    permutation_fun1(tmp, count+1)
  
permutation_fun1([1,3,5])
  
