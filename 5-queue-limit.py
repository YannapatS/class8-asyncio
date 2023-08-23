from random import random
import asyncio
import time

# coroutine to generate work


async def producer(queqe):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queqe
        await queqe.put(value)
    print(f'{time.ctime()} Producer: Done')


async def consumer(queqe):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit for work
        item = await queqe.get()
        # report
        print(f'{time.ctime()} >got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark as completed
        queqe.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine


async def main():
    # create the shared queqe
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many product
    product = [producer(queue) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*product)
    # wait for the consumer to process all item
    await queue.join()
# start the asyncio program
asyncio.run(main())



# Wed Aug 23 14:39:51 2023 Consumer: Running
# Wed Aug 23 14:39:51 2023 Producer: Running
# Wed Aug 23 14:39:51 2023 Producer: Running
# Wed Aug 23 14:39:51 2023 Producer: Running
# Wed Aug 23 14:39:51 2023 Producer: Running
# Wed Aug 23 14:39:51 2023 Producer: Running
# Wed Aug 23 14:39:51 2023 >got 0.17045570419547174
# Wed Aug 23 14:39:51 2023 >got 0.240150535489272
# Wed Aug 23 14:39:52 2023 >got 0.31383397944749614
# Wed Aug 23 14:39:52 2023 >got 0.5201779478783041
# Wed Aug 23 14:39:52 2023 >got 0.4281710186463089
# Wed Aug 23 14:39:53 2023 >got 0.3923676669921927
# Wed Aug 23 14:39:53 2023 >got 0.8993054955736901
# Wed Aug 23 14:39:54 2023 >got 0.34061770014370074
# Wed Aug 23 14:39:55 2023 >got 0.7182299598351819
# Wed Aug 23 14:39:55 2023 >got 0.8452780452248625
# Wed Aug 23 14:39:56 2023 >got 0.5550255434345923
# Wed Aug 23 14:39:57 2023 >got 0.6379021807950358
# Wed Aug 23 14:39:57 2023 >got 0.6527911219801725
# Wed Aug 23 14:39:58 2023 >got 0.2658427417213214
# Wed Aug 23 14:39:58 2023 >got 0.3215666752967453
# Wed Aug 23 14:39:59 2023 >got 0.9056780704915234
# Wed Aug 23 14:39:59 2023 >got 0.4219110308888515
# Wed Aug 23 14:40:00 2023 >got 0.10049923910985326
# Wed Aug 23 14:40:00 2023 >got 0.6497646166595784
# Wed Aug 23 14:40:01 2023 >got 0.03458000089134883
# Wed Aug 23 14:40:01 2023 >got 0.9797348249784954
# Wed Aug 23 14:40:02 2023 >got 0.383503158796783
# Wed Aug 23 14:40:02 2023 >got 0.516430895208591
# Wed Aug 23 14:40:03 2023 >got 0.6254163228639298
# Wed Aug 23 14:40:03 2023 >got 0.3032216407410373
# Wed Aug 23 14:40:03 2023 >got 0.9259689907337391
# Wed Aug 23 14:40:04 2023 >got 0.5711448714895236
# Wed Aug 23 14:40:05 2023 >got 0.8227674999179291
# Wed Aug 23 14:40:06 2023 >got 0.7556270726829994
# Wed Aug 23 14:40:07 2023 >got 0.5329387759094724
# Wed Aug 23 14:40:07 2023 >got 0.5934496840106022
# Wed Aug 23 14:40:08 2023 >got 0.28215511636102175
# Wed Aug 23 14:40:08 2023 >got 0.8448469785571853
# Wed Aug 23 14:40:09 2023 >got 0.501271260138228
# Wed Aug 23 14:40:09 2023 >got 0.914464516900588
# Wed Aug 23 14:40:10 2023 >got 0.9081586415615786
# Wed Aug 23 14:40:11 2023 >got 0.37751390646241667
# Wed Aug 23 14:40:12 2023 >got 0.7832575113547824
# Wed Aug 23 14:40:12 2023 >got 0.6584366128770144
# Wed Aug 23 14:40:13 2023 >got 0.7981351418790726
# Wed Aug 23 14:40:13 2023 Producer: Done
# Wed Aug 23 14:40:14 2023 >got 0.4191398430226084
# Wed Aug 23 14:40:14 2023 >got 0.5059226755276037
# Wed Aug 23 14:40:15 2023 >got 0.04969273598681878
# Wed Aug 23 14:40:15 2023 Producer: Done
# Wed Aug 23 14:40:15 2023 >got 0.40661242564303035
# Wed Aug 23 14:40:15 2023 >got 0.8845384347327953
# Wed Aug 23 14:40:15 2023 Producer: Done
# Wed Aug 23 14:40:16 2023 >got 0.3550241238636219
# Wed Aug 23 14:40:16 2023 Producer: Done
# Wed Aug 23 14:40:16 2023 >got 0.3453547946761891
# Wed Aug 23 14:40:17 2023 >got 0.857672767275187
# Wed Aug 23 14:40:17 2023 Producer: Done
# Wed Aug 23 14:40:18 2023 >got 0.6675355343711776
# Wed Aug 23 14:40:18 2023 >got 0.6524643472409271