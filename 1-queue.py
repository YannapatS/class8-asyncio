# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

from random import random
import asyncio
import time 

async def producer(queue):
    print(f'{time.ctime()} Producer: Running')

    for i in range(10):
        value = random()
        await asyncio.sleep(value)
        await queue.put(value)

    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')

async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')

    while True:
        item = await queue.get()
        if item is None:
            break
        print(f'{time.ctime()} Consumer: Done')

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())

# Wed Aug 23 14:09:45 2023 Producer: Running
# Wed Aug 23 14:09:45 2023 Consumer: Running
# Wed Aug 23 14:09:46 2023 Consumer: Done
# Wed Aug 23 14:09:46 2023 Consumer: Done
# Wed Aug 23 14:09:47 2023 Consumer: Done
# Wed Aug 23 14:09:47 2023 Consumer: Done
# Wed Aug 23 14:09:47 2023 Consumer: Done
# Wed Aug 23 14:09:48 2023 Consumer: Done
# Wed Aug 23 14:09:48 2023 Consumer: Done
# Wed Aug 23 14:09:48 2023 Consumer: Done
# Wed Aug 23 14:09:49 2023 Consumer: Done
# Wed Aug 23 14:09:50 2023 Producer: Done
# Wed Aug 23 14:09:50 2023 Consumer: Done


