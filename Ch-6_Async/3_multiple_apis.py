import asyncio

async def api_call(url:str,delay:int):
    print("Fetching data from: ", url)
    await asyncio.sleep(delay)
    print("Data fetched from: ", url)
    return f"{url} data"





async def main():

    # Creating Tasks with Gather
    tasks = await asyncio.gather(
        api_call("https://api1.com", 2),
        api_call("https://api2.com", 3),
        api_call("https://api3.com", 1)
    )

    # Another way to create tasks with list comprehension
    # tasks = [api_call(url, delay) for url, delay in [("https://api1.com", 2), ("https://api2.com", 3), ("https://api3.com", 1)]]
    # results = await asyncio.gather(*tasks)

    print("All API calls completed.")

asyncio.run(main())