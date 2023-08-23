from random import random
import asyncio
import time

async def producer(queue):
    print('ProduverL Running')

    for i in range(10):
        value = random()
        await asyncio.sleep(value)
        await queue.put(value)
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')

async def consumer(queue):
    print('Consumer: Running')

    while True:
        try:
            get_await = queue.get()
            item = await asyncio.wait_for(get_await, 0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Concumer: gave up waiting...')
            continue
        if item is None:
            break
        print(f'{time.ctime()} >got {item}')
    print('Concumer: Done')

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue)),

asyncio.run(main())


# ProduverL Running
# Wed Aug 23 14:26:09 2023 Producer: Done