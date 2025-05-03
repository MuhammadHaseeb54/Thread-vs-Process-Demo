import threading
import multiprocessing

# Thread memory sharing
shared_counter = 0

def increment_thread():
    global shared_counter
    for _ in range(1000):
        shared_counter += 1

# Process memory sharing using Value
def increment_process(shared_value):
    for _ in range(1000):
        shared_value.value += 1

def memory_sharing_demo():
    global shared_counter
    shared_counter = 0

    # Threads
    threads = []
    for _ in range(4):
        t = threading.Thread(target=increment_thread)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    thread_result = shared_counter

    # Processes
    shared_value = multiprocessing.Value('i', 0)
    processes = []
    for _ in range(4):
        p = multiprocessing.Process(target=increment_process, args=(shared_value,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    process_result = shared_value.value

    return {
        "Thread Counter Result": thread_result,
        "Process Shared Value Result": process_result
    }
