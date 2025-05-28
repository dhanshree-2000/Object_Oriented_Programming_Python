import os
# Check if the file exists
if os.path.exists("Object_Oriented_Programming_Python\File_Handling\demo.txt"):
    print("File exists.")
else:
    print("File does not exist.")

file_path ="Object_Oriented_Programming_Python\File_Handling\demo.txt"
file = open(file_path, 'r')
content = file.read()
print(content)
file.close()

file = open(file_path, 'r')
line1= file.readline()
line2 = file.readline()
print(line1)
print(line2)
file.close()

file = open(file_path, 'r')
for line in file:
    print(line, end='')
file.close()


try:
    with open("demo.txt", 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found")