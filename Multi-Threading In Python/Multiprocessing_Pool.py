from multiprocessing import Pool
import time
import os

def square(n):
    for i in range(n):
        print("Worker process id for {0}: {1}".format(n, os.getpid()))
        print(f"Square of {i} is {i * i}")
    

if __name__ == "__main__":
    t = time.time()
    n = 100
    with Pool(processes=4) as pool:
        pool.map(square, [n] * 4)  # Map the square function to a list of n values

    print("Finished printing squares with multiprocessing.")
    print(f"Time taken: {time.time() - t:.2f} seconds")