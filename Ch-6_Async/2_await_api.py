# Normal Sync API Calls
import time

# def api_call():
#     time.sleep(3)
#     return "orders data"

# def execute():
#     print("Executing API Call")
#     result = api_call()
#     print("Data Fetched: ", result)

# execute()

# Async API Calls
import asyncio

async def api_call():
    await asyncio.sleep(3)
    return "orders data"



async def execute():
    print("Executing API Call")
    result = await api_call()
    print("Data Fetched: ", result)


asyncio.run(execute())