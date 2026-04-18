import asyncio
import time

# Coroutine function
async def main():
    print("Hello") # This will print immediately
    await asyncio.sleep(3) # The thread is idle here
    print("World") # This will be executed right after the thread is idle

# Run the main coroutine
asyncio.run(main())