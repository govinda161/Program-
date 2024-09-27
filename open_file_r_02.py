# Using with statement
with open('C:/Users/admin/Desktop/hello.txt', 'r') as file: # 'r' means read mode
    # Read the content
    content = file.read()
    print(content)
