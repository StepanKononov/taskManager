import threading
import time


def calculate_partial_sum(start, end, result, index):
    partial_sum = sum(range(start, end))
    result[index] = partial_sum


def calculate_sum_with_threading(num):
    num_threads = 5
    range_per_thread = num // num_threads
    threads = []
    results = [0] * num_threads

    for i in range(num_threads):
        start = i * range_per_thread + 1
        end = (i + 1) * range_per_thread + 1
        thread = threading.Thread(target=calculate_partial_sum, args=(start, end, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = sum(results)
    return total_sum


if __name__ == '__main__':
    start_time = time.time()
    total_sum = calculate_sum_with_threading(1000000)
    threading_time = time.time() - start_time

    print(f"Total sum (threading): {total_sum}")
    print(f"Execution time (threading): {threading_time} seconds")
