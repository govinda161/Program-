# Example of handling file errors
try:
    with open('C:/Users/admin/Desktop/hellos.txt','r') as file:
        content = file.read()  # Attempt to read a non-existent file
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist!")  # Handle the error gracefully
