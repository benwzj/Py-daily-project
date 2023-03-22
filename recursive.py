
##############################################################
# Understand Recursive function
# Clear the flow of recursive function execution: 
# keep variable value during enter and withdraw process
##############################################################
### simple one:
def test_recursion(n):
    if n < 0:
        return
    else:
        test_recursion(n-1)
        print(n)
    
#test_recursion(4)

### factorial
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

#print(factorial (4))

##############################################################
# You can find out what Python’s recursion limit is with a function 
# from the sys module called getrecursionlimit():
from sys import getrecursionlimit
# print(getrecursionlimit())


