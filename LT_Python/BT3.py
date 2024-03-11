S = 0
# input 2 integer N and k
while True:
    N = int(input("Nhap so nguyen duong N: "))
    if N > 0:
        break
    else:
        print("N phai la so nguyen duong. Vui long nhap lai.")

i = 1
while i <= N:
    if i % k == 0:
        S += i
    i += 1
print("S = ", S)