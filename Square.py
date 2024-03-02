import math
N = int(input())
for i in range(N):
    a = int(input())
    var = int(math.sqrt(a))
    while a % var != 0:
        var -= 1
    print(var, int(a/var))