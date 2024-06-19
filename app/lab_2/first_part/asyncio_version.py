import asyncio
import time


async def calculate_partial_sum(start, end):
    return sum(range(start, end))


async def calculate_sum_with_asyncio(num):
    num_tasks = 5
    range_per_task = num // num_tasks
    tasks = []

    for i in range(num_tasks):
        start = i * range_per_task + 1
        end = (i + 1) * range_per_task + 1
        tasks.append(calculate_partial_sum(start, end))
    results = await asyncio.gather(*tasks)

    total_sum = sum(results)
    return total_sum


if __name__ == '__main__':
    start_time = time.time()
    total_sum = asyncio.run(calculate_sum_with_asyncio(1000000))
    asyncio_time = time.time() - start_time

    print(f"Total sum (asyncio): {total_sum}")
    print(f"Execution time (asyncio): {asyncio_time} seconds")
