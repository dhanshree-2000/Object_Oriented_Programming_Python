def outer():
    print("Outer function")
    def inner():
        print("Inner function")

    inner()  # Call the inner function

outer()  # Call the outer function
# This code defines a nested function structure where the outer function calls the inner function.
# inner()  # This will raise an error because inner is not defined in the global scope
# outer.inner()  # This will also raise an error because inner is not accessible outside of outer