# Creating an array
my_array = [1, 2, 3, 4, 5]

# Accessing array elements
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 3

# Modifying array elements
my_array[1] = 10
print(my_array)  # Output: [1, 10, 3, 4, 5]

# Length of the array
print(len(my_array))  # Output: 5

# Iterating over an array
for element in my_array:
    print(element, end=" ")  # Output: 1 10 3 4 5

# Now with index
for i in range(len(my_array)):
    print(my_array[i], end=" ")  # Output: 1 10 3 4 5

# Reverse an array
reversed_array = my_array[::-1]
print(reversed_array)  # Output: [5, 4, 3, 10, 1]

# Slicing an array
sliced_array = my_array[1:4]
print(sliced_array)  # Output: [10, 3, 4]

# Searching for an element in an array
if 3 in my_array:
    print("Element found")
else:
    print("Element not found")

# Sorting an array
my_array.sort()

# Adding elements to an array
my_array.append(6)

# Removing elements from an array
my_array.remove(3)