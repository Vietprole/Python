#######################################################################################################################################
# Su dung cac ham ben duoi
# import sys
# sys.path.append("../Common")
# import Common

#######################################################################################################################################
# data = CommonBacktest.CommonBacktest.backtest(databacktest, initial_capital, shares_per_signal)
class CommonBacktest:

    @staticmethod
    def backtest(data, initial_capital, shares_per_signal): # Chung khoan
        import pandas as pd
        import matplotlib.pyplot as plt
        import plotly.graph_objects as go
        import plotly.express as px

        capital = initial_capital
        shares_held = 0

        # Xác định vị thế mua/ bán
        data['Position_Buy'] = data['Buy_Signal'].shift()
        data['Position_Sell'] = data['Sell_Signal'].shift()

        data['Trade_Action'] = ''
        data['Capital'] = capital
        data['Shares_Held'] = shares_held

        # Lặp qua mỗi hàng trong DataFrame
        for index, row in data.iterrows():
            # Nếu có tín hiệu mua và có đủ vốn để mua
            if row['Position_Buy'] == 1 and capital >= row['Close'] * shares_per_signal and row['Trade_Action'] == '':
                # Mua cổ phiếu và cập nhật vốn và số cổ phiếu được giữ
                data.at[index, 'Trade_Action'] = 'Buy'
                capital -= row['Close'] * shares_per_signal
                data.at[index, 'Capital'] = capital
                shares_held += shares_per_signal
                data.at[index, 'Shares_Held'] = shares_held
            elif row['Position_Sell'] == 1 and shares_held > 0 and row['Trade_Action'] == '':
                data.at[index, 'Trade_Action'] = 'Sell'
                capital += row['Close'] * shares_held
                data.at[index, 'Capital'] = capital
                shares_held = 0
                data.at[index, 'Shares_Held'] = shares_held  # Giảm số lượng cổ phiếu 0
            else:
                data.at[index, 'Capital'] = capital
                data.at[index, 'Shares_Held'] = shares_held

            # Cập nhật giá trị hiện tại của vốn dựa trên số cổ phiếu đang giữ và giá đóng cửa hiện tại
            current_value = capital + shares_held * row['Close']

        # Ngày vào lệnh
        first_entry_date = data[data['Position_Buy'] == 1].index.min()
        # Tính lợi nhuận
        profit = current_value - initial_capital
        # Tính lợi nhuận thị trường
        market_return = (data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0]
        # Tính lợi nhuận chiến lược
        strategy_return = (current_value - initial_capital) / initial_capital

        print(f"Ngày vào lệnh đầu tiên: {first_entry_date}")
        print(f'Tổng lợi nhuận: {profit}')
        print(f'Tổng giá trị tài khoản: {current_value}')
        print(f'Lợi nhuận thị trường: {market_return * 100}%')
        print(f'Lợi nhuận chiến lược: {strategy_return * 100}%')

        # Tính toán lợi nhuận thị trường và chiến lược
        data['Market_Return'] = data['Close'].pct_change()
        data['Cumulative_Market_Returns'] = (1 + data['Market_Return']).cumprod()

        # Tính toán lợi nhuận lũy kế từ chiến lược
        data['Strategy_Value'] = data['Capital'] + data['Shares_Held'] * data['Close']
        data['Cumulative_Strategy_Returns'] = data['Strategy_Value'] / initial_capital

        # Vẽ biểu đồ so sánh lợi nhuận lũy kế từ thị trường và từ chiến lược
        plt.figure(figsize=(12, 6))
        plt.plot(data['Cumulative_Market_Returns'], label='Market Returns')
        plt.plot(data['Cumulative_Strategy_Returns'], label='Strategy Returns')
        plt.title('Comparison of Cumulative Returns: Market vs Strategy')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.legend()
        plt.show()

        # Tạo biểu đồ sử dụng Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Cumulative_Market_Returns'], mode='lines', name='Market Returns'))
        fig.add_trace(go.Scatter(x=data.index, y=data['Cumulative_Strategy_Returns'], mode='lines', name='Strategy Returns'))

        fig.update_layout(
            title='Comparison of Cumulative Returns: Market vs Strategy',
            xaxis_title='Date',
            yaxis_title='Cumulative Returns',
        )
        fig.show()

        return data
    
    @staticmethod
    def backtest_ext(data, initial_capital, shares_per_signal): # Chung khoan
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import plotly.graph_objects as go
        import plotly.express as px

        capital = initial_capital
        shares_held = 0

        # Xác định vị thế mua/ bán
        data['Position_Buy'] = data['Buy_Signal'].shift()
        data['Position_Sell'] = data['Sell_Signal'].shift()

        data['Trade_Action'] = ''
        data['Capital'] = capital
        data['Shares_Held'] = shares_held

        # Lặp qua mỗi hàng trong DataFrame
        for index, row in data.iterrows():
            # Nếu có tín hiệu mua và có đủ vốn để mua
            if row['Position_Buy'] == 1 and capital >= row['Close'] * shares_per_signal and row['Trade_Action'] == '':
                # Mua cổ phiếu và cập nhật vốn và số cổ phiếu được giữ
                data.at[index, 'Trade_Action'] = 'Buy'
                capital -= row['Close'] * shares_per_signal
                data.at[index, 'Capital'] = capital
                shares_held += shares_per_signal
                data.at[index, 'Shares_Held'] = shares_held
            elif row['Position_Sell'] == 1 and shares_held > 0 and row['Trade_Action'] == '':
                data.at[index, 'Trade_Action'] = 'Sell'
                capital += row['Close'] * shares_held
                data.at[index, 'Capital'] = capital
                shares_held = 0
                data.at[index, 'Shares_Held'] = shares_held  # Giảm số lượng cổ phiếu 0
            else:
                data.at[index, 'Capital'] = capital
                data.at[index, 'Shares_Held'] = shares_held

            # Cập nhật giá trị hiện tại của vốn dựa trên số cổ phiếu đang giữ và giá đóng cửa hiện tại
            current_value = capital + shares_held * row['Close']

        # Ngày vào lệnh
        first_entry_date = data[data['Position_Buy'] == 1].index.min()
        # Tính lợi nhuận
        profit = current_value - initial_capital
        # Tính lợi nhuận thị trường
        market_return = (data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0]
        # Tính lợi nhuận chiến lược
        strategy_return = (current_value - initial_capital) / initial_capital

        print(f"Ngày vào lệnh đầu tiên: {first_entry_date}")
        print(f'Tổng lợi nhuận: {profit}')
        print(f'Tổng giá trị tài khoản: {current_value}')
        print(f'Lợi nhuận thị trường: {market_return * 100}%')
        print(f'Lợi nhuận chiến lược: {strategy_return * 100}%')

        # Tính toán lợi nhuận thị trường và chiến lược
        data['Market_Return'] = data['Close'].pct_change()
        data['Cumulative_Market_Returns'] = (1 + data['Market_Return']).cumprod()

        # Tính toán lợi nhuận lũy kế từ chiến lược
        data['Strategy_Value'] = data['Capital'] + data['Shares_Held'] * data['Close']
        data['Cumulative_Strategy_Returns'] = data['Strategy_Value'] / initial_capital

        # Tính toán chỉ số Sharpe Ratio
        risk_free_rate = 0.01  # Risk-free rate, thay đổi theo tình hình thị trường thực tế
        strategy_return_daily = data['Strategy_Value'].pct_change()
        excess_return = strategy_return_daily - risk_free_rate / 252  # Chia cho 252 ngày giao dịch trong năm
        sharpe_ratio = np.sqrt(252) * excess_return.mean() / excess_return.std()

        # Tính toán Max Drawdown
        rolling_max = data['Strategy_Value'].cummax()
        daily_drawdown = data['Strategy_Value']/rolling_max - 1.0
        max_drawdown = daily_drawdown.cummin().min()

        # Tính toán CAGR (Compound Annual Growth Rate)
        days = (data.index[-1] - data.index[0]).days
        cagr = ((data['Strategy_Value'].iloc[-1] / data['Strategy_Value'].iloc[0]) ** (365.0/days)) - 1

        # In các chỉ số
        print(f"Sharpe Ratio: {sharpe_ratio}")
        print(f"Max Drawdown: {max_drawdown * 100}%")
        print(f"CAGR: {cagr * 100}%")

        # Vẽ biểu đồ so sánh lợi nhuận lũy kế từ thị trường và từ chiến lược
        plt.figure(figsize=(12, 6))
        plt.plot(data['Cumulative_Market_Returns'], label='Market Returns')
        plt.plot(data['Cumulative_Strategy_Returns'], label='Strategy Returns')
        plt.title('Comparison of Cumulative Returns: Market vs Strategy')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.legend()
        plt.show()

        # Tạo biểu đồ sử dụng Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Cumulative_Market_Returns'], mode='lines', name='Market Returns'))
        fig.add_trace(go.Scatter(x=data.index, y=data['Cumulative_Strategy_Returns'], mode='lines', name='Strategy Returns'))

        fig.update_layout(
            title='Comparison of Cumulative Returns: Market vs Strategy',
            xaxis_title='Date',
            yaxis_title='Cumulative Returns',
        )
        fig.show()

        return data
    
    @staticmethod
    def backtestForex(data, initial_capital, lot_per_trade, leverage, tp_point, sl_point):  # Forex
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import plotly.graph_objects as go

        capital = initial_capital  # Vốn ban đầu
        lot_size = 100000  # Kích cỡ chuẩn của một lot là 100,000 đơn vị

        positions = []  # Danh sách để theo dõi các vị thế mua vào

        # Định nghĩa vị thế mua và bán dựa trên tín hiệu mua và bán
        data['Position_Buy'] = data['Buy_Signal'].shift()  # Lấy tín hiệu mua của ngày trước
        data['Position_Sell'] = data['Sell_Signal'].shift()  # Lấy tín hiệu bán của ngày trước

        # Chuyển đổi TP và SL từ point sang tỷ lệ thay đổi giá
        tp_price = tp_point * 0.00001  # chẳng hạn: 100 points = 0.0010 thay đổi giá
        sl_price = sl_point * 0.00001  # chẳng hạn: 200 points = 0.0020 thay đổi giá

        # Khởi tạo cột cho kết quả giao dịch và số vốn
        data['Trade_Action'] = ''
        data['Capital'] = capital

        # Lặp qua từng dòng dữ liệu
        for index, row in data.iterrows():
            # Kiểm tra tín hiệu mua và đủ vốn
            if row['Position_Buy'] == 1 and capital >= (row['Close'] * lot_size * lot_per_trade) / leverage:
                entry_price = row['Close']
                positions.append({'type': 'long', 'entry_price': entry_price, 'lot': lot_per_trade})
                data.at[index, 'Trade_Action'] = 'Buy'
                capital -= entry_price * lot_per_trade * lot_size / leverage

            # Kiểm tra tín hiệu bán và đủ vốn
            elif row['Position_Sell'] == 1 and capital >= (row['Close'] * lot_size * lot_per_trade) / leverage:
                entry_price = row['Close']
                positions.append({'type': 'short', 'entry_price': entry_price, 'lot': lot_per_trade})
                data.at[index, 'Trade_Action'] = 'Sell'
                capital -= entry_price * lot_per_trade * lot_size / leverage

            # Kiểm tra cho mỗi vị thế nếu cần chốt lời hoặc cắt lỗ
            for position in positions[:]:
                if position['type'] == 'long':
                    if row['Close'] >= position['entry_price'] + tp_price:
                        capital += position['lot'] * lot_size * (row['Close'] - position['entry_price']) / leverage
                        positions.remove(position)
                        data.at[index, 'Trade_Action'] += ', Take Profit Long'
                    elif row['Close'] <= position['entry_price'] - sl_price:
                        capital -= position['lot'] * lot_size * (position['entry_price'] - row['Close']) / leverage
                        positions.remove(position)
                        data.at[index, 'Trade_Action'] += ', Stop Loss Long'

                elif position['type'] == 'short':
                    if row['Close'] <= position['entry_price'] - tp_price:
                        capital += position['lot'] * lot_size * (position['entry_price'] - row['Close']) / leverage
                        positions.remove(position)
                        data.at[index, 'Trade_Action'] += ', Take Profit Short'
                    elif row['Close'] >= position['entry_price'] + sl_price:
                        capital -= position['lot'] * lot_size * (row['Close'] - position['entry_price']) / leverage
                        positions.remove(position)
                        data.at[index, 'Trade_Action'] += ', Stop Loss Short'

            data.at[index, 'Capital'] = capital  # Cập nhật số vốn sau mỗi giao dịch

        # Tính giá trị hiện tại của các vị thế chưa chốt
        for position in positions:
            if position['type'] == 'long':
                current_value = position['lot'] * lot_size * (data['Close'].iloc[-1] - position['entry_price']) / leverage
                capital += current_value
            elif position['type'] == 'short':
                current_value = position['lot'] * lot_size * (position['entry_price'] - data['Close'].iloc[-1]) / leverage
                capital += current_value

        # Tính toán lợi nhuận cuối cùng và lợi nhuận chiến lược
        final_capital = capital  # Số vốn cuối cùng
        profit = final_capital - initial_capital  # Lợi nhuận tổng cộng
        market_return = (data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0]  # Lợi nhuận thị trường
        strategy_return = profit / initial_capital  # Lợi nhuận chiến lược

        # In thông tin lợi nhuận và lợi nhuận chiến lược
        print(f"Ngày vào lệnh đầu tiên: {data[data['Position_Buy'] == 1].index.min()}")
        print(f'Tổng lợi nhuận: {profit}')
        print(f'Tổng giá trị tài khoản cuối cùng: {final_capital}')
        print(f'Lợi nhuận thị trường: {market_return * 100}%')
        print(f'Lợi nhuận chiến lược: {strategy_return * 100}%')

        # Tính toán và vẽ biểu đồ lợi nhuận lũy kế từ thị trường và chiến lược
        data['Market_Return'] = data['Close'].pct_change()
        data['Cumulative_Market_Returns'] = (1 + data['Market_Return']).cumprod()
        data['Strategy_Value'] = data['Capital']
        data['Cumulative_Strategy_Returns'] = data['Strategy_Value'] / initial_capital

        # Vẽ biểu đồ lợi nhuận lũy kế từ thị trường và từ chiến lược
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data['Cumulative_Market_Returns'], label='Lợi nhuận Thị trường')
        plt.plot(data.index, data['Cumulative_Strategy_Returns'], label='Lợi nhuận Chiến lược')
        plt.title('So sánh Lợi nhuận Lũy kế: Thị trường và Chiến lược')
        plt.xlabel('Ngày')
        plt.ylabel('Lợi nhuận Lũy kế')
        plt.legend()
        plt.show()

        # Sử dụng Plotly cho biểu đồ tương tác
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Cumulative_Market_Returns'], mode='lines', name='Lợi nhuận Thị trường'))
        fig.add_trace(go.Scatter(x=data.index, y=data['Cumulative_Strategy_Returns'], mode='lines', name='Lợi nhuận Chiến lược'))
        fig.update_layout(
            title='So sánh Lợi nhuận Lũy kế: Thị trường và Chiến lược',
            xaxis_title='Ngày',
            yaxis_title='Lợi nhuận Lũy kế'
        )
        fig.show()

        return data



