# Opening the file in binary mode (e.g., for images)
# This example assumes you have a binary file named 'image.png' to read
with open('C:/Users/admin/Pictures/Saved Pictures/brain.png', 'rb') as file:
    binary_content = file.read()  # Read the entire binary file
    print("Binary file read successfully!")
