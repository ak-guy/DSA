import requests
import time
import asyncio
import aiohttp

url = "https://api.genderize.io?name={}"


async def makeASyncCalls1():
    res = []
    async with aiohttp.ClientSession() as session:
        for i in range(50):
            response = await session.get(url.format("arpit"))
            res.append(await response.json())


def makeAsyncCalls2Helper(session):
    task = []
    for _ in range(50):
        task.append(session.get(url.format("arpit")))
    return task


async def makeAsyncCalls2():
    res = []
    async with aiohttp.ClientSession() as session:
        tasks = makeAsyncCalls2Helper(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            res.append(await response.json())


def makeSyncCalls():
    res = []
    for _ in range(50):
        response = requests.get(url.format("arpit"))
        res.append(response)


# # iteration 1
start = time.time()
asyncio.run(makeASyncCalls1())
print(f"Total time taken for makeASyncCalls1() = {time.time() - start}")


# # iteration 2
start = time.time()
asyncio.run(makeAsyncCalls2())
print(f"Total time taken for makeAsyncCalls2() = {time.time() - start}")


# # iteration 3
start = time.time()
makeSyncCalls()
print(f"Total time taken for makeSyncCalls() = {time.time() - start}")


"""
Total time taken for makeASyncCalls1() = 15.636098623275757
Total time taken for makeAsyncCalls2() = 12.700150728225708
Total time taken for makeSyncCalls() = 62.56667351722717
"""
