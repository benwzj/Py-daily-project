
# clone python's built-in range() function:
def my_range(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step

# for p in my_range(3,14):
#     print(p)

### permutations
def permutations(lst, i=0):
    if i == len(lst):
      print (lst)
      #yield lst
    for j in range(i, len(lst)):
      # need to create new memory
      tmp = [p for p in lst]
      # swap
      tmp[i], tmp[j] = tmp[j], tmp[i]
      permutations(tmp, i+1)

permutations(['a','b','c'])
# for i in permutations(['a','b','c']):
#    print (i)

# Recursive Generators
# ### permutations
def permutation_generator(word):
    if len(word) == 0:
        yield ""
    else:
        for m in range(len(word)):
            for n in permutation_generator(word[:m] + word[m + 1:]):
                yield word[m] + n

# for x in permutation_generator("hoe"):
#     print(x)