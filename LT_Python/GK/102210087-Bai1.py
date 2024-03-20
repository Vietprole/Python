countAm = 0
countDuong = 0
sumAm = 0
sumDuong = 0

with open('E:/Viet/Python/LT_Python/GK/InpAvg.txt', 'r') as file:
    line = file.readlines()
    for i in range(0, len(line)):
        if(int(line[i]) < 0):
            countAm += 1
            sumAm += int(line[i])
        else:
            countDuong += 1
            sumDuong += int(line[i])
AvgAm = int(sumAm / countAm) if countAm != 0 else 0
AvgDuong = int(sumDuong / countDuong) if countDuong != 0 else 0

with open('E:/Viet/Python/LT_Python/GK/OutAvg.txt', 'w') as file:
    file.write(str(AvgAm) + " " + str(AvgDuong))
    