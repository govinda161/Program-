# Open a file for reading
file = open('C:/Users/admin/Desktop/hello.txt', 'r')  # 'r' means read mode

# Read the content
content = file.read()
print(content)

# Always close the file when done
file.close()
