"""
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

### Question2: Remove Duplicates From a Python List
# use dict.fromkeys(), don't use set, because set is unordered
keywords = ['foo', 'bar', 'bar', 'foo', 'baz', 'foo']
print (list(dict.fromkeys(keywords)))
print (list(set(keywords)))
"""
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
