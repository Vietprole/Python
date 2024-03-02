import yfinance as yf

# Thay thế 'TICKER' với mã cổ phiếu của công ty bạn quan tâm
ticker = yf.Ticker("ACB.VN")

# Lấy báo cáo tài chính
financials = ticker.financials
balance_sheet = ticker.balance_sheet
cashflow = ticker.cashflow

# Hiển thị báo cáo lợi nhuận
print("Báo cáo lợi nhuận:")
print(financials)

# Hiển thị bảng cân đối kế toán
print("\nBảng cân đối kế toán:")
print(balance_sheet)

# Hiển thị báo cáo dòng tiền
print("\nBáo cáo dòng tiền:")
print(cashflow)
