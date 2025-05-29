#print the squares of numbers from 1 to 10 without using multithreading
#print the cubes of numbers from 1 to 10 without using multithreading

import time

def print_squares():
    for i in range(1, 11):
        time.sleep(0.5)  # Simulating a time-consuming task
        print(f"Square of {i} is {i * i}")

def print_cubes():
    for i in range(1, 11):
        time.sleep(0.5)  # Simulating a time-consuming task
        print(f"Cube of {i} is {i * i * i}")
t= time.time()
print_squares()
print_cubes()
print("Finished printing squares and cubes without multithreading.")
print(time.time()-t)
# The above code will print the squares of numbers from 1 to 10 followed by the cubes of numbers from 1 to 10
# without using multithreading, which means it will complete the squares first and then the cubes.


# Square of 1 is 1
# Square of 2 is 4
# Square of 3 is 9
# Square of 4 is 16
# Square of 5 is 25
# Square of 6 is 36
# Square of 7 is 49
# Square of 8 is 64
# Square of 9 is 81
# Square of 10 is 100
# Cube of 1 is 1
# Cube of 2 is 8
# Cube of 3 is 27
# Cube of 4 is 64
# Cube of 5 is 125
# Cube of 6 is 216
# Cube of 7 is 343
# Cube of 8 is 512
# Cube of 9 is 729
# Cube of 10 is 1000
# Finished printing squares and cubes without multithreading.
# 10.017821788787842