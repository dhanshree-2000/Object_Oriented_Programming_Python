file_path ="Object_Oriented_Programming_Python/File_Handling/demo.txt"

# Writing to a file
with open(file_path, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.write("Goodbye!\n")

with open(file_path, 'a') as file:
    file.write("Appending a new line.\n")
    file.write("This is the second appended line.\n")

with open(file_path,'r') as file:
    content=file.read()
    
print("File content after writing and appending:")
print(content)