value = input().split()
N = int(value[0])
X = int(value[1])
numbers_string = input().split()
numbers = [int(num) for num in numbers_string]
count = 0
for i in range(0,N):
    ai = numbers[i] * numbers[i]
    for j in range(i,N):
        aj = numbers[j]
        if (ai + aj) == X: count += 1
print(count)