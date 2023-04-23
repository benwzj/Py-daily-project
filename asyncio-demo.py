
import asyncio
import datetime
import random
import time
##########################################################
# basic one 
# coroutine example

async def basic_one():
    print("Hello")
    await asyncio.sleep(3)
    print("World")

# asyncio.run(basic_one())

##########################################################
# nested one 
# coroutine example
async def nested():
    print("42")
    await asyncio.sleep(1)
    print("100")

async def gather_demo():
    print("let's start! " + str(datetime.datetime.now()))
    task = asyncio.gather(nested(), nested(), nested())
    await task
    print("end at " + str(datetime.datetime.now()))

# asyncio.run(gather_demo())
############################################################
# This example runs 3 coroutines concurrently. 
# The makerandom conroutine is trying to simulate some jobs 
# need to be completed.

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)
async def makerandom(idx: int, threshold: int) -> int:
    print(c[idx + 1] + f"Initiated idx({idx}), threshold({threshold}).")
    int_ran = random.randint(0, 10)
    while int_ran <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {int_ran} too low; retrying.")
        await asyncio.sleep(idx + 1)
        int_ran = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {int_ran}" + c[0])
    return int_ran

async def gather_makerandom():
    threshold = [5,7,3]
    res = await asyncio.gather(*(makerandom(i, threshold[i]) for i in range(3)))
    return res

# random.seed(444)
# r1, r2, r3 = asyncio.run(gather_makerandom())
# print()
# print(f"r1: {r1}, r2: {r2}, r3: {r3}")

###################################################
# create_task () example
# understand why we need task

async def say_hello():
    await asyncio.sleep(2)
    print("Hello")

async def not_task():
    print(f"started at {time.strftime('%X')}")
    await say_hello()
    await say_hello()
    print(f"started at {time.strftime('%X')}")

async def is_task():
    t1 = asyncio.create_task(say_hello())
    t2 = asyncio.create_task(say_hello())
    print(f"started at {time.strftime('%X')}")
    await t1
    await t2
    print(f"started at {time.strftime('%X')}")

asyncio.run(is_task())
asyncio.run(not_task())

###################################################
# event_loop () example:
# @asyncio.coroutine exmaple:

@asyncio.coroutine
def countdown(name, n):
    while n > 0:
        print('T-minus', n, '({})'.format(name))
        yield from asyncio.sleep(1)
        n -= 1

# loop = asyncio.get_event_loop()
# tasks = [
#     asyncio.ensure_future(countdown("A", 2)),
#     asyncio.ensure_future(countdown("B", 3))]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

