### what is decorator in python
# we have a decorator function:
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

# we can wrag function like this:
def say_hi():
    return "Hello There"

print(uppercase_decorator(say_hi)())

# also we can use decorator, same result as above:
@uppercase_decorator
def de_say_hi():
    return "Hello There using decorator"

print(de_say_hi())
