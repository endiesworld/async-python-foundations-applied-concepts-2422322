import asyncio
from datetime import datetime
import click


async def sleep_and_print(seconds):
    print(f"starting async {seconds} sleep 😴")
    await asyncio.sleep(seconds)
    print(f"finished async {seconds} sleep ⏰")
    return seconds

def ordinary_func(arg):
    print('Running ordinary function')
    return arg

async def main():
    # using arguments
    coroutines_list_1 = [ordinary_func(i) for i in range(1, 11)]
    print('created a list comprehension fir ordinary function')
    print(coroutines_list_1)
    # building list
    coroutines_list = [sleep_and_print(i) for i in range(1, 11)]
    print('created a list comprehension')
    results = await asyncio.gather(*coroutines_list)
    print(results)


start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
