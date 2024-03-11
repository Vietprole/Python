print('Nhap N:')
N = int(input())
x = []
y = []
for i in range(0, N):
    print('Nhap diem thu ', i+1, ':')
    x_value, y_value = map(int, input().split())
    x.append(x_value)
    y.append(y_value)

max_distance = 0
for i in range(0, N):
    for j in range(i+1, N):
        distance = (x[i]-x[j])**2 + (y[i]-y[j])**2
        if distance > max_distance:
            max_distance = distance
            max_xi = x[i]
            max_yi = y[i]
            max_xj = x[j]
            max_yj = y[j]
print('Do dai lon nhat la:', max_distance)
print(f"Hai diem ({max_xi},{max_yi}) va ({max_xj},{max_yj}) tao thanh doan thang dai nhat")
