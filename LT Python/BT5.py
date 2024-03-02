
x, y = map(int, input("Nhap toa do C:").split())
x1, y1 = map(int, input("Nhap toa do P:").split())
print("Nhap ban kinh R:")
R = int(input())
if (x1-x)**2 + (y1-y)**2 < R**2:
    print(f"P({x},{y}) nam trong duong tron C({x1},{y1}) ban kinh R = {R}")
else: 
    print(f"P({x},{y}) nam ngoai duong tron C({x1},{y1}) ban kinh R = {R}")