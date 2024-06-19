import asyncio
import multiprocessing
import threading
from time import time

import aiohttp
import requests
import sqlalchemy
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from sqlalchemy.orm import sessionmaker

from app.database import engine
from app.models.page import Page

SessionLocal = sessionmaker(bind=engine)

urls = ["https://www.example.com", "https://www.python.org", "https://www.github.com"]


def parse_and_save_threading(url):
    open_session = SessionLocal()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title"
        page = Page(url=url, title=title)
        open_session.add(page)
        open_session.commit()
        print(f"Threading - URL: {url}, Title: {title}")
    except sqlalchemy.exc.IntegrityError:
        open_session.rollback()
        print(f"Threading - URL: {url} already exists in database")
    finally:
        open_session.close()


def threading_main(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=parse_and_save_threading, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def parse_and_save_multiprocessing(url):
    open_session = SessionLocal()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title"
        page = Page(url=url, title=title)
        open_session.add(page)
        open_session.commit()
        print(f"Multiprocessing - URL: {url}, Title: {title}")
    except sqlalchemy.exc.IntegrityError:
        open_session.rollback()
        print(f"Multiprocessing - URL: {url} already exists in database")
    finally:
        open_session.close()


def multiprocessing_main(urls):
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=parse_and_save_multiprocessing, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def parse_and_save_async(url):
    open_session = SessionLocal()
    async with aiohttp.ClientSession() as aio_session:
        try:
            html = await fetch(aio_session, url)
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else "No title"
            page = Page(url=url, title=title)
            open_session.add(page)
            open_session.commit()
            print(f"Async - URL: {url}, Title: {title}")
        except sqlalchemy.exc.IntegrityError:
            open_session.rollback()
            print(f"Async - URL: {url} already exists in database")
        finally:
            open_session.close()


async def async_main(urls):
    tasks = [parse_and_save_async(url) for url in urls]
    await asyncio.gather(*tasks)


def run_async(urls):
    asyncio.run(async_main(urls))


def measure_performance():
    results = []

    start_time = time()
    threading_main(urls)
    threading_time = time() - start_time
    results.append(("Threading", threading_time))

    start_time = time()
    multiprocessing_main(urls)
    multiprocessing_time = time() - start_time
    results.append(("Multiprocessing", multiprocessing_time))

    start_time = time()
    run_async(urls)
    async_time = time() - start_time
    results.append(("Async", async_time))

    table = PrettyTable()
    table.field_names = ["Method", "Time (s)"]
    for method, t in results:
        table.add_row([method, t])

    print(table)


if __name__ == "__main__":
    measure_performance()
