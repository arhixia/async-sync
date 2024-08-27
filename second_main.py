import asyncio
import aiohttp
import time


urls = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3',
    'https://jsonplaceholder.typicode.com/posts/4',
    'https://jsonplaceholder.typicode.com/posts/5',
    'https://jsonplaceholder.typicode.com/posts/6',
    'https://jsonplaceholder.typicode.com/posts/7',
    'https://jsonplaceholder.typicode.com/posts/8',
    'https://jsonplaceholder.typicode.com/posts/9',
    'https://jsonplaceholder.typicode.com/posts/10',
    'https://jsonplaceholder.typicode.com/posts/11',
]


async def fetch_data(session, url, number):
    print(f'{number}) Fetching data from {url}')
    async with session.get(url) as response:
        data = await response.json()
        await process_title(data, number)
        await process_body(data, number)


async def process_title(data, number):
    print(f'{number}) Title: {data["title"]}')


async def process_body(data, number):
    print(f'{number}) Body: {data["body"]}')
    await asyncio.sleep(1)
    print(f'{number}) Url processed')


async def main():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url, i+1) for i, url in enumerate(urls)]
        await asyncio.gather(*tasks)

    duration = time.time() - start_time
    print(f'Fetched and processed all data in {duration:.2f} seconds')

if __name__ == "__main__":
    asyncio.run(main())

