
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

o_my_range = my_range(3,6)
iter_my_range = iter(o_my_range)
print(type(o_my_range))
print(type(iter_my_range))
print(next(iter_my_range))
print(next(iter_my_range))

iter_my_range2 = iter(o_my_range)
print("range2")
print(next(iter_my_range2))
# for p in my_range(3,14):
#     print(p)

##################################################
# subgenerator concept
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

# wrap = reader_wrapper1(reader())
# for i in wrap:
#     print(i)

##############################################################
### generator recusion, It use subgenerator concept:
# the code below won't work if just using yeild. 
# It need yield from to work.

def generator_recursion(n):
    if n < 0:
        return
    else:
        n = yield from generator_recursion(n-1)
        #yield n
    
# gr = generator_recursion(4)
# for g in gr:
#     print(g)

##################################################
### permutations
def permutations(lst, i=0):
    if i == len(lst):
      #print (lst)
      yield lst
    for j in range(i, len(lst)):
      # need to create new memory
      tmp = [p for p in lst]
      # swap
      tmp[i], tmp[j] = tmp[j], tmp[i]
      yield from permutations(tmp, i+1)

# for i in permutations(['a','b','c']):
#    print (i)

# Recursive Generators, no yield from
# ### permutations
def permutation_generator(word):
    if len(word) == 0:
        yield word
    else:
        for m in range(len(word)):
            for n in permutation_generator(word[:m] + word[m+1:]):
                yield word[m] + n

# pg = permutation_generator("hoe")
# for k in pg:
#     print (k)
