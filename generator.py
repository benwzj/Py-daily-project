
##################################################
# If you create a list to sum the first n. When n is really big, 
# then it consume lots of memory. Not acceptable. 
# Using generator pattern is better. (an iterable)
class first_n(object):
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        raise StopIteration()

#sum_of_first_n = sum(first_n(1000000))

# iterator looks too much detail. 
# a generator fucntion can provide simpler way and same result as above.
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

#sum_of_first_n = sum(firstn(1000000))

##################################################
### clone python's built-in range() function:
def my_range(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step

# for p in my_range(3,14):
#     print(p)

##################################################
# understand yield from

def reader():
    """A generator that fakes a read from a file, socket, etc."""
    for i in range(4):
        yield '<< %s' % i

def reader_wrapper(g):
    # Manually iterate over data produced by reader
    for v in g:
        yield v

# Instead of manually iterating over reader(), we can just yield from it.
def reader_wrapper1(g):
    yield from g

wrap = reader_wrapper1(reader())
for i in wrap:
    print(i)

##################################################
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

# permutations(['a','b','c'])
# for i in permutations(['a','b','c']):
#    print (i)

# Recursive Generators
# ### permutations
def permutation_generator(word):
    if len(word) == 0:
        yield "1"+word
    else:
        for m in range(len(word)):
            for n in permutation_generator(word[:m] + word[m+1:]):
                yield word[m] + n

# pg = permutation_generator("hoe")
# for k in pg:
#     print (k)
