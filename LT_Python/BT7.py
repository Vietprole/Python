x = []
y = []
with open('E:/Viet/Python/LT Python/fin.txt', 'r') as file:
    line = file.readlines()
    N = line[0]
    for i in range(1, len(line)):
        [a,b]=line[i].split()
        x.append(float(a))
        y.append(float(b))

for i in range(0, len(x)):
    for j in range(0, len(x)):
        for k in range(0, len(x)):
            if (x[k] - x[i])*(x[k] - x[j]) + (y[k] - y[i])*(y[k] - y[j]) == 0:
                print(x[i], y[i], x[j], y[j], x[k], y[k])
