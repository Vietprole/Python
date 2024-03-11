while True:
    N = int(input("Nhap so nguyen duong N: "))
    if N > 0:
        break
    else:
        print("N phai la so nguyen duong. Vui long nhap lai.")

#cal S = 1/1 - 1/2 + ...
S = 0
i = 1
while i <= N:
    S += (-1)**(i+1)/i
    i += 1
print("S = ", S)
