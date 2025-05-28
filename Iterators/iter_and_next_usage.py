nums = [1,2,3,4,5,6,7,8,9,10]

# Using iter() to create an iterator from the list
nums_iter = iter(nums)
# Using next() to get the next item from the iterator
print(next(nums_iter))  # Output: 1
print(next(nums_iter))  # Output: 2

# Using a for loop to iterate through the rest of the items
for num in nums_iter:
    print(num)  # Output: 3, 4, 5, 6, 7, 8, 9, 10

# Using next() again will raise StopIteration if there are no more items
try:
    print(next(nums_iter))  # This will raise StopIteration
except StopIteration:
    print("No more items in the iterator.")

    