import numpy as np

with open("LT_Python/Numpy/fin.txt", "r") as file:
    lines = file.readlines()

points = np.array([list(map(int, line.split())) for line in lines])

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        # Tính toán hệ số góc và hệ số tự do của đường thẳng đi qua 2 điểm
        a = points[j, 1] - points[i, 1] # y2 - y1
        b = points[i, 0] - points[j, 0] # x1 - x2
        c = points[i, 1] * points[j, 0] - points[i, 0] * points[j, 1] # x1*y2 - x2*y1

        # Đếm số điểm nằm ở mỗi nửa mặt phẳng
        count1 = count2 = 0
        for k in range(len(points)):
            if k != i and k != j:
                if a * points[k, 0] + b * points[k, 1] + c > 0:
                    count1 += 1
                elif a * points[k, 0] + b * points[k, 1] + c < 0:
                    count2 += 1

        # Kiểm tra xem có tồn tại cặp điểm thỏa mãn yêu cầu hay không
        if count1 == count2:
            print("Cặp điểm thỏa mãn yêu cầu:")
            print(points[i])
            print(points[j])
            exit()

with open('LT_Python/Numpy/fout.txt', 'w') as file:
    #write pointi, j to file
    file.write(str(points[i][0]) + " " + str(points[i][1]) + "\n")
print("Không tìm thấy cặp điểm thỏa mãn yêu cầu.")