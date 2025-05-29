import time
from multiprocessing import *

result =[]
def print_squares():
    global result
    for i in range(1,11):
        # time.sleep(0.5)
        print(f"Square of {i} is {i * i}")
        result.append(i * i)
    print("Final result of squares:", result)

def print_cubes():
    for i in range(1,11):
        # time.sleep(0.5)
        print(f"Cube of {i} is {i * i * i}")

if __name__ == "__main__":
    t = time.time()
    p1 = Process(target=print_squares)
    p2 = Process(target=print_cubes)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final result of squares:", result)

    print("Finished printing squares and cubes with multiprocessing.")
    print(time.time() - t)
