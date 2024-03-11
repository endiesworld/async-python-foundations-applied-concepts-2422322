import asyncio
from datetime import datetime
import click


async def sleep_five():
    print("Start sleep 5")
    await asyncio.sleep(5)
    return "Finished sleep 5"


async def sleep_three_then_five():
    print("Start sleep 3 then five")
    await asyncio.sleep(3)
    await sleep_five()
    return "Finished sleep 3 then five"
    


async def main():
    results = await asyncio.gather(sleep_five(), sleep_three_then_five())
    print(results)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
