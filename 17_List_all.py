# Create a list of student names
students = ['Ram', 'Sanjay', 'Rahul', 'Ranjeet', 'Rohit']

# 1. Accessing elements
print("List of students:", students)
print("First student:", students[0])
print("Last student:", students[-1])

# 2. Slicing
print("First three students:", students[:3])
print("Last three students:", students[-3:])

# 3. Length of the list
print("Number of students:", len(students))

# 4. Append
students.append('Ravi')
print("List after appending :", students)

# 5. Insert
students.insert(2, 'Ankit')
print("List after inserting :", students)

# 6. Remove
students.remove('Ranjeet')
print("List after removing :", students)

# 7. Pop
removed_student = students.pop(4)
print("List after popping last element ('{}'):", students)

# 8. Concatenate lists
more_students = ['Harshit', 'Sunil']
all_students = students + more_students
print("List after concatenating :", all_students)

# 9. Sorting (alphabetical order)
all_students.sort()
print("List after sorting :", all_students)

# 10. Reverse sorting
all_students.sort(reverse=True)
print("List after sorting reverse :", all_students)

# 11. Clear the list
all_students.clear()
print("List after clearing all elements:", all_students)
