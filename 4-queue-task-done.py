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
    print(f'{time.ctime()} Consumer: Running')

    while True:
        item = await queue.get()
        print(f'{time.ctime()} >got {item}')
        if item:
            await asyncio.sleep(item)
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    _ = asyncio.create_task(consumer(queue))
    await asyncio.create_task(producer(queue))
    await queue.join()

asyncio.run(main())


# Wed Aug 23 14:31:00 2023 Consumer: Running
# ProduverL Running
# Wed Aug 23 14:31:01 2023 >got 0.8915453395917043
# Wed Aug 23 14:31:02 2023 >got 0.6086486420912988
# Wed Aug 23 14:31:03 2023 >got 0.7808031934258906
# Wed Aug 23 14:31:03 2023 >got 0.48677744855333693
# Wed Aug 23 14:31:04 2023 >got 0.9015933984244916
# Wed Aug 23 14:31:05 2023 >got 0.13522388255070483
# Wed Aug 23 14:31:05 2023 >got 0.6469685176922576
# Wed Aug 23 14:31:06 2023 >got 0.9845674741748212
# Wed Aug 23 14:31:07 2023 >got 0.9850372623198271
# Wed Aug 23 14:31:07 2023 Producer: Done
# Wed Aug 23 14:31:08 2023 >got 0.517