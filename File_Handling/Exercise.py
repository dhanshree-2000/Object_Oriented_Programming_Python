with open('program.txt','r') as file:
    data= file.read()

new_data = data.replace('multiple','single')    

with open('program.txt','w') as file:
    file.write(new_data)

def check_word(file_content,word):
    if not file_content:
        return False
    elif word not in file_content:
        return False
    else:
        return True

def check_word(file_content, word):
    if not file_content:
        return 0
    else:
        return file_content.count(word)
    
with open('program.txt', 'r') as file:
    data = file.read()
    status=check_word(data, 'single')
    print(f"The word 'single' appears {status} times in the file.")







