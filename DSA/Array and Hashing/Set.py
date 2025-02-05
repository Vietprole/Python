# Creating a set
my_set = set([1, 2, 3, 2])
print(my_set)  # Output: {1, 2, 3} - Duplicates are removed

# Adding an element to a set
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Removing an element from a set (if the element does not exist, this will raise a KeyError)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# Discarding an element from a set (if the element does not exist, nothing happens)
my_set.discard(3)
print(my_set)  # Output: {1, 4}

# Checking if an element is in a set
print(1 in my_set)  # Output: True
print(2 in my_set)  # Output: False

# Set operations
# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)  # Output: {3}

# Difference
print(set1 - set2)  # Output: {1, 2}
print(set2 - set1)  # Output: {4, 5}

# Symmetric Difference (elements in either set1 or set2 but not in both)
print(set1 ^ set2)  # Output: {1, 2, 4, 5}