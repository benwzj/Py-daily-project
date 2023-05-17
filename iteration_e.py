

###################################################
# clear the concepts of iterable and iteraor
class countdown(object):
  def __init__(self,start):
    self.start = start
  def __iter__(self):
    return countdown_iter(self.start)

class countdown_iter(object):
  def __init__(self, count):
    self.count = count
  def __next__(self):
    if self.count <= 0:
      raise StopIteration
    r = self.count
    self.count -= 1
    return r
  def __iter__(self):
    return self

# #c = countdown(5)
# c = [1,2,3,4]
# ci = iter(c)
# print(next(ci))
# print(next(ci))
# for k in ci:
#   print ("\033[0m" + str(k))

#######################################
# itertools cycle

from itertools import cycle

def endless():
  yield from cycle((4,3,2,1))

# start = 0
# e = endless()
# for i in e:
#   if start < 15:
#     print (i)
#     start += 1
#   else:
#     print ("done at: "+ str(i))
#     break

# print("next1: "+ str(next(e)))
# print("next2: "+ str(next(e)))


#########################################################
# list object is pure iterable

mylist = [1,2,3]

l1 = iter(mylist)
print(next(l1))
print(next(l1))
print(next(l1))
l2 = iter(mylist)
print(next(l2))

