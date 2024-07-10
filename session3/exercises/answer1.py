import random
import multiprocessing
import time


def bubble_sort(arr):
    n = len(arr)
    for _ in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def generate_and_sort_numbers():
    numbers = []
    for _ in range(10000):
        numbers.append(random.uniform(0, 100))
    bubble_sort(numbers)


def serial_runner():
    start = time.perf_counter()
    for _ in range(3):
        generate_and_sort_numbers()
    end = time.perf_counter()

    print(f'Serial: {end-start} second(s)')


def parallel_runner2():
    start = time.perf_counter()
    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=generate_and_sort_numbers)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    end=time.perf_counter()

    print(f'Parallel: {end-start} second(s)')


if __name__ == '__main__':
    serial_runner()
    parallel_runner2()
