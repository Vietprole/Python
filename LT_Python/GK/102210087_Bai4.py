def min_cost(v1, v2):
    v1.sort()
    v2.sort(reverse=True)
    return sum(a * b for a, b in zip(v1, v2))

n = int(input())
v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))
print(min_cost(v1, v2))