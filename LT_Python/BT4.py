while True:
    N = int(input("Nhap so nguyen duong N: "))
    if N > 0:
        break
    else:
        print("N phai la so nguyen duong. Vui long nhap lai.")

#cal S = N!!
S = 1
if N % 2 == 0:
    i = 2
else:
    i = 1
while i <= N:
    S *= i
    i += 2
print("S = ", S)