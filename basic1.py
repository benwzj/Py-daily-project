
str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = ""
len = len(str1)
while len:
  str2 += str1[len-1]
  len = len-1

print(str2)