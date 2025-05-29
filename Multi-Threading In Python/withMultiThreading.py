#print the squares of numbers from 1 to 10 with using multithreading
#print the cubes of numbers from 1 to 10 with using multithreading

import time
from threading import *
result = []
def print_squares():
    global result
    for i in range(1, 11):
        time.sleep(0.5)  # Simulating a time-consuming task
        print(f"Square of {i} is {i * i}")
        result.append(i * i)
    

def print_cubes():
    for i in range(1, 11):
        time.sleep(0.5)  # Simulating a time-consuming task
        print(f"Cube of {i} is {i * i * i}")


t= time.time()
t1 = Thread(target=print_squares)
t2 = Thread(target=print_cubes)

t1.start()
t2.start()

t1.join()
t2.join()
print("Final result of squares:", result)
print("Finished printing squares and cubes without multithreading.")
print(time.time()-t)


# Cube of 1 is 1
# Square of 1 is 1
# Cube of 2 is 8
# Square of 2 is 4
# Cube of 3 is 27
# Square of 3 is 9
# Cube of 4 is 64
# Square of 4 is 16
# Cube of 5 is 125
# Square of 5 is 25
# Cube of 6 is 216
# Square of 6 is 36
# Cube of 7 is 343
# Square of 7 is 49
# Cube of 8 is 512
# Square of 8 is 64
# Cube of 9 is 729
# Square of 9 is 81
# Cube of 10 is 1000
# Square of 10 is 100
# Finished printing squares and cubes without multithreading.
# 5.01190447807312