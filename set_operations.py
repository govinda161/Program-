# Creating two sets
a = {1, 2, 3, 4}  # Set A contains the numbers 1 through 4
b = set([3, 4, 5, 6])  # Set B contains the numbers 3 through 6

# Union: Combine elements from both sets
union_set = a | b   # Alternatively, you can use a.union(b)
print("Union:", union_set) # Output the union of a and b

# Intersection: Common elements in both sets
intersection_set = a & b  # Alternatively, use a.intersection(b)
print("Intersection:", intersection_set)  # Output the intersection

# Difference: Elements in a but not in b
difference_set = a - b  # Alternatively, use a.difference(b)
print("Difference:", difference_set)  # Output the difference

# Symmetric Difference: Elements in either set but not in both
symmetric_difference_set = a ^ b  # Alternatively, use a.symmetric_difference(b)
print("Symmetric Difference:", symmetric_difference_set)  # Output the symmetric difference

# Adding an element to a
a.add(5)  # Add the number 5 to a
print("After adding 5:", a)  # Output the updated a

# Removing an element from set_a
a.remove(1)  # Remove the number 1 from a (raises KeyError if not found)
print("After removing 1:", a)  # Output the updated a

# Discarding an element from a
a.discard(2)  # Remove the number 2 from set_a (does not raise error if not found)
print("After discarding 2:", a)  # Output the updated a

# Clearing all elements from a
a.clear()  # Remove all elements from a
print("After clearing:", a) # Output the empty set
    
