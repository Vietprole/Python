N = 0
M = 0
K = []
array = []
result = []
with open('E:/Viet/Python/LT_Python/GK/inpLN.txt', 'r') as file:
    line = file.readlines()
    N = int(line[0])  
    array = list(map(int, line[1].split()))
    M = int(line[2])
    for i in range(3, len(line)):
        element = int(line[i])
        K.append(element)

for element in K:
    max_smaller_K = max((x for x in array if x < element), default=None)
    if max_smaller_K is None:
        result.append(-1)
    else:
        index = array.index(max_smaller_K)
        result.append(array[index])
        
with open('E:/Viet/Python/LT_Python/GK/outLN.txt', 'w') as file:
    for j in result:
        file.write(str(j) + "\n")