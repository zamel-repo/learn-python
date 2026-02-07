import asyncio

async def task(name, delay): 
    print(f"Start task {name}")
    await asyncio.sleep(delay)
    print(f"End task {name}")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3),
        task("D", 4)
    )

asyncio.run(main())