S = {'red', 'green', 'blue', 'red'}
print(S)

S1 = {1, 'red', ('a', 'b'), True}
print(S1)

A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}
# by operator
print(A | B)
# {'green', 'red', 'yellow', 'blue', 'orange’}
# by method
print(A.union(B))
# {'green', 'red', 'yellow', 'blue', 'orange'}

# by operator
print(A & B)
# {'red’}
# by method
print(A.intersection(B))
# {'red'}

# by operator
print(A- B)
# {'blue', 'green'}
# by method
print(A.difference(B))
# {'blue', 'green'}

# by operator
print(A ^ B)
# {'green', 'yellow', 'blue', 'orange'}
# by method
print(A.symmetric_difference(B))
# {'green', 'yellow', 'blue', 'orange'}

# by operator
print(A <= B)
# False
