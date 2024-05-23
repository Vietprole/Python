import time
start_time = time.time()

N = 0
M = 0
Q = 0
array = []
temp_list = []

with open('E:/Viet/Python/LT_Python/GK-practice/inpTB1.txt', 'r') as file:
    line = file.readlines()
    N = int(line[0])  
    array = list(map(int, line[1].split()))
    M = int(line[2])
    array = sorted(array)
    for i in range(3, len(line)):
        Q = int(line[i])
        if Q == -1:
            temp_list.append(array[0])
            array.pop(0)
        else:
            array.append(Q)
            array = sorted(array)

with open('E:/Viet/Python/LT_Python/GK-practice/outTB.txt', 'w') as file:
    for j in temp_list:
        file.write(str(j) + "\n")

endtime = time.time()
print("Execution time: ", endtime - start_time)
    
