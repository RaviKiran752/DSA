# Basic operations on lists (arrays in Python)
arr = [1, 2, 3, 4, 5]

# Insert
arr.append(6)  # Add at end
arr.insert(2, 10)  # Insert 10 at index 2

# Delete
arr.pop()  # Remove last element
arr.remove(10)  # Remove specific value

# Access
print(arr[2])  # Indexing
print(arr[:3])  # Slicing

# Searching
print(arr.index(3))  # Find index of element 3
