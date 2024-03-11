while True:
    N = int(input("Nhap so nguyen duong N: "))
    if N > 0:
        break
    else:
        print("N phai la so nguyen duong. Vui long nhap lai.")

#cal S = 1/1 + 1/2! + ... + 1/N!
S = 0
i = 1
GiaiThua = 1
while i <= N:
    GiaiThua *= i
    S += 1/GiaiThua
    i += 1
print("S = ", S)
