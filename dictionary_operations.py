# Creating a dictionary
my_dict = {
    'name': 'Ram',    # Key 'name' with value 'Ram'
    'age': 25,        # Key 'age' with value 25
    'city': 'India'   # Key 'city' with value 'India'
}

# Accessing a value using a key
name = my_dict['name']  # Retrieve the value associated with the key 'name'
print("Name:", name)     # Output the name

# Adding a new key-value pair
my_dict['job'] = 'Engineer'  # Add a new key 'job' with the value 'Engineer'
print("After adding job:", my_dict)  # Output the updated dictionary

# Updating an existing value
my_dict['age'] = 31  # Update the value of the key 'age' to 31
print("After updating age:", my_dict)  # Output the updated dictionary

# Removing a key-value pair
removed_value = my_dict.pop('city')  # Remove the key 'city' and store its value in removed_value
print("Removed value:", removed_value)  # Output the removed value
print("After removing city:", my_dict)   # Output the updated dictionary

# Checking if a key exists
has_job = 'job' in my_dict  # Check if 'job' is a key in the dictionary
print("Has job key:", has_job)  # Output the result

# Iterating through keys
print("Keys in the dictionary:")
for key in my_dict:  # Loop through each key in the dictionary
    print(key)        # Output the current key

# Iterating through key-value pairs
print("Key-Value pairs in the dictionary:")
for key, value in my_dict.items():  # Loop through each key-value pair
    print(key, ":", value)  # Output the current key and its associated value

# Clearing all items from the dictionary
my_dict.clear()  # Remove all items from the dictionary
print("After clearing the dictionary:", my_dict)  # Output the empty dictionary
