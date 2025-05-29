import multiprocessing
import time

def workers(q, lst):
    for item in lst:
        print(f"item: {item}")
        q.put(item *item)

if __name__ == "__main__":
    q= multiprocessing.Queue()
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t= time.time()
    p = multiprocessing.Process(target=workers, args=(q, lst))
    p.start()
    p.join()

    while not q.empty():
        item = q.get()
        print(f"Square: {item}")
    print("Finished processing items in the queue.")
    print(f"Time taken: {time.time() - t:.2f} seconds")