import time
from prettytable import PrettyTable
import asyncio
from threading_version import calculate_sum_with_threading
from multiprocessing_version import calculate_sum_with_multiprocessing
from asyncio_version import calculate_sum_with_asyncio

if __name__ == '__main__':

    num = 100000000
    start_time = time.time()
    threading_sum = calculate_sum_with_threading(num)
    threading_time = time.time() - start_time

    start_time = time.time()
    multiprocessing_sum = calculate_sum_with_multiprocessing(num)
    multiprocessing_time = time.time() - start_time

    start_time = time.time()
    asyncio_sum = asyncio.run(calculate_sum_with_asyncio(num))
    asyncio_time = time.time() - start_time

    table = PrettyTable()
    table.field_names = ["Approach", "Total Sum", "Execution Time (s)"]
    table.add_row(["Threading", threading_sum, threading_time])
    table.add_row(["Multiprocessing", multiprocessing_sum, multiprocessing_time])
    table.add_row(["Asyncio", asyncio_sum, asyncio_time])

    print(table)
