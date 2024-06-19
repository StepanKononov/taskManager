import multiprocessing
import time


def calculate_partial_sum(start, end):
    return sum(range(start, end))


def calculate_sum_with_multiprocessing(num):
    num_processes = 5
    range_per_process = num // num_processes
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = []
        for i in range(num_processes):
            start = i * range_per_process + 1
            end = (i + 1) * range_per_process + 1
            results.append(pool.apply_async(calculate_partial_sum, (start, end)))
        total_sum = sum(result.get() for result in results)
    return total_sum


if __name__ == '__main__':
    start_time = time.time()
    total_sum = calculate_sum_with_multiprocessing(1000000)
    multiprocessing_time = time.time() - start_time

    print(f"Total sum (multiprocessing): {total_sum}")
    print(f"Execution time (multiprocessing): {multiprocessing_time} seconds")