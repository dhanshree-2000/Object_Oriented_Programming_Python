from multiprocessing import *
import time


def print_squares(result):
    for idx , i in enumerate(range(1, 11)):
        print(f"Square of {i} is {i * i}")
        result[idx] = i * i

def print_cubes(result):
    for idx, i in enumerate(range(1, 11)):
        print(f"Cube of {i} is {i * i * i}")
        result[idx + 10] = i * i * i

if __name__ == "__main__":
    t = time.time()
    result = Array('i', 20)  # Shared array for results

    p1 = Process(target=print_squares, args=(result,))
    p2 = Process(target=print_cubes, args=(result,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final result of squares and cubes:", list(result))
    print("Finished printing squares and cubes with multiprocessing.")
    print(time.time() - t)