import threading
import multiprocessing
import time

def cpu_bound_task(n=100000):
    count = 0
    for num in range(2, n):
        prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                prime = False
                break
        if prime:
            count += 1
    return count

def io_bound_task(n=5):
    for _ in range(n):
        time.sleep(1)

def run_task(method, task_type):
    start_time = time.time()

    workers = []
    num_tasks = 4

    if method == "thread":
        for _ in range(num_tasks):
            if task_type == "cpu":
                t = threading.Thread(target=cpu_bound_task)
            else:
                t = threading.Thread(target=io_bound_task)
            t.start()
            workers.append(t)
        for w in workers:
            w.join()

    elif method == "process":
        for _ in range(num_tasks):
            if task_type == "cpu":
                p = multiprocessing.Process(target=cpu_bound_task)
            else:
                p = multiprocessing.Process(target=io_bound_task)
            p.start()
            workers.append(p)
        for w in workers:
            w.join()

    end_time = time.time()
    return round(end_time - start_time, 2)

def count_threads():
    return threading.active_count()

def count_processes():
    return len(multiprocessing.active_children())
