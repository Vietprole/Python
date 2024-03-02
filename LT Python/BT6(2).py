print('Nhap N:')
N = int(input())
x = []
y = []
for i in range(0, N):
    print('Nhap diem thu ', i+1, ':')
    x_value, y_value = map(int, input().split())
    x.append(x_value)
    y.append(y_value)

x_max = [min(x), max(x)]
y_max = [min(y), max(y)]

print(f"Hai diem ({x_max[0]},{y_max[0]}) va ({x_max[1]},{y_max[1]}) tao thanh doan thang dai nhat")
