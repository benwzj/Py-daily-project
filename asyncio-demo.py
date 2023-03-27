##########################################################
# basic one

import asyncio
import datetime
import random

async def nested():
    print("42")
    await asyncio.sleep(1)
    print("100")

async def main():
    print("let's start! " + str(datetime.datetime.now()))
    task = asyncio.gather(nested(), nested(), nested())
    await task
    print("end at " + str(datetime.datetime.now()))

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

async def main():
    threshold = [5,7,3]
    res = await asyncio.gather(*(makerandom(i, threshold[i]) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
