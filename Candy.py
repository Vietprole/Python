t = int(input())
for i in range(t):
    count = 0
    amount = input().split()
    n = int(amount[0])
    m = int(amount[1])
    arr = input().split()
    a = [int(num) for num in arr]
    for j in range(n):
        if a[j] + 1 == m:
            count += 1
        elif a[j] + 1 > m:
            count += m
        elif m % (a[j] + 1) == 0: 
            count += int(m/(a[j]+1))
        else: count += m - int(m/(a[j]+1)) * a[j]
    print(count)