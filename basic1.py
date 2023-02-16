
### question1: reverse a string.

# operate it as an array
str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = ""
len = len(str1)
while len:
  str2 += str1[len-1]
  len = len-1

print(str2)

# using slice syntax:
print(str1[::-1])

### Remove Duplicates From a Python List
# use dict.fromkeys(), don't use set
keywords = ['foo', 'bar', 'bar', 'foo', 'baz', 'foo']
print (list(dict.fromkeys(keywords)))

