import requests
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


def fetch_data(url, number):
    print(f'{number}) Fetching data from {url}')
    response = requests.get(url)
    data = response.json()
    process_title(data, number)
    process_body(data, number)


def process_title(data, number):
    print(f'{number}) Title: {data["title"]}')


def process_body(data, number):
    print(f'{number}) Body: {data["body"]}')
    time.sleep(1)
    print(f'{number}) Url processed')


def main():
    start_time = time.time()

    for i, url in enumerate(urls, start=1):
        fetch_data(url, i)

    duration = time.time() - start_time
    print(f'Fetched and processed all data in {duration:.2f} seconds')

if __name__ == "__main__":
    main()
