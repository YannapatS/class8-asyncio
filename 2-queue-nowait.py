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
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer: got nothing, waiting a while...')
            continue
        if item is None:
            break
    print(f'{time.ctime()} Consumer: Done')

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())
