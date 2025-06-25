import asyncio
import time


async def add(a,b): # coroutine
    await asyncio.sleep(1)
    return a+b

async def main():
    start = time.perf_counter()
    # a = 2
    # print(a)
    # c = await add(2,3)
    # print(c)
    coroutines = [add(3,4),add(1,4),add(2,4),add(3,5)]
    
    results = await asyncio.gather(*coroutines)
    # results = await asyncio.gather(add(3,4),add(1,4),add(2,4),add(3,5))
    print(results)
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')    

    end = time.perf_counter()
    print(f"{end-start:.3}s")

if __name__ == '__main__':
    # event loop
    asyncio.run(main())
    


