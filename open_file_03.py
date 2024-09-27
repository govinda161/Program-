# Opening a file for writing (this will create 'example.txt' if it doesn't exist)
with open('C:/Users/admin/Desktop/hello.txt', 'w') as file:
    # Write a few lines to the file
    file.write('Hello Sir\n')  # Write first line with a newline
    file.write('Welcome to my file.\n')  # Write second line
    file.write('I am Govinda Chauhan.\n')

    
# Opening the same file for reading
with open('C:/Users/admin/Desktop/hello.txt', 'r') as file:
    # Read the entire content of the file
    content = file.read()  
    print("File content:")
    print(content)  # Print the content read from the file


# Appending more text to the existing file
with open('C:/Users/admin/Desktop/hello.txt', 'a') as file:
    # Append a new line to the file
    file.write('This line is appended.\n')  # Add a new line at the end


# Reading lines from the file
with open('C:/Users/admin/Desktop/hello.txt', 'r') as file:
    print("Reading lines:")
    for line in file:
        print(line.strip())  # Print each line, stripping the trailing newline


