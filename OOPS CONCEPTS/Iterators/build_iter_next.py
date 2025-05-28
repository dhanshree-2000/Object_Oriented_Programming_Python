class IterNext:
    def __init__(self):
        self.data= 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.data <= 10:
            value= self.data
            value += 1
            self.data = value
            return value
        else:
            raise StopIteration("No more items in the iterator.")
        
# Example usage
nums= IterNext()
print(next(nums))  # Output: 2
print(next(nums))  # Output: 3

# Using a for loop to iterate through the rest of the items
for num in nums:
    print(num)  # Output: 4, 5, 6, 7, 8, 9, 10

