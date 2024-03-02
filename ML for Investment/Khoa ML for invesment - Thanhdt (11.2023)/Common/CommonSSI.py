#######################################################################################################################################
# symbol = 'VCB'
# from_date = '2023-11-01'
# to_date = '2023-11-30'
# data = Common.Common.loaddataSSI(symbol, from_date, to_date)
class CommonSSI:

    @staticmethod   
    def loaddataSSI(symbol, from_date, to_date):
    # Import các module cần thiết
        from ssi_fc_data import fc_md_client, model
        from datetime import datetime
        import pandas as pd
        import json
        import configDataSSL

        # Tạo Market Data Client
        # from_date = "01/11/2023"
        # to_date = "17/11/2023"

        # Sử dụng datetime để phân tích chuỗi ngày tháng
        from_date_new = datetime.strptime(from_date, '%Y-%m-%d')
        to_date_new = datetime.strptime(to_date, '%Y-%m-%d')

        # Định dạng lại ngày tháng sang định dạng 'dd/mm/yyyy'
        from_date_new = from_date_new.strftime('%d/%m/%Y')
        to_date_new = to_date_new.strftime('%d/%m/%Y')

        client = fc_md_client.MarketDataClient(configDataSSL)

        req = model.daily_ohlc(symbol, from_date_new, to_date_new)

        data_dict = client.daily_ohlc(configDataSSL, req)
        print(type(data_dict))

        data_list = data_dict['data']
  
        data = pd.DataFrame(data_list)
   
        data = data.rename(columns={'TradingDate': 'Datetime'})       

        data = pd.DataFrame(data, columns=['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume'])

        return data
    
    @staticmethod
    def loaddataSSI_Ext(symbol, from_date, to_date):
        from ssi_fc_data import fc_md_client, model
        from datetime import datetime, timedelta
        import pandas as pd
        import json
        import configDataSSL
        
        client = fc_md_client.MarketDataClient(configDataSSL)

        # Chuyển đổi chuỗi ngày tháng sang đối tượng datetime
        from_date = datetime.strptime(from_date, '%Y-%m-%d')
        to_date = datetime.strptime(to_date, '%Y-%m-%d')

        # Tạo một DataFrame rỗng để lưu trữ dữ liệu
        data = pd.DataFrame()

        while from_date < to_date:
            # Tính to_date_new là ngày cuối cùng của khoảng thời gian ba tháng kế tiếp
            to_date_new = from_date + timedelta(days=90)
            # Đảm bảo không vượt quá to_date gốc
            if to_date_new > to_date:
                to_date_new = to_date

            # Định dạng lại ngày tháng để phù hợp với API
            from_date_str = from_date.strftime('%d/%m/%Y')
            to_date_new_str = to_date_new.strftime('%d/%m/%Y')

            # Tạo request và lấy dữ liệu
            req = model.daily_ohlc(symbol, from_date_str, to_date_new_str)
            data_dict = client.daily_ohlc(configDataSSL, req)
            data_list = data_dict['data']

            # Thêm dữ liệu vào DataFrame
            data = pd.concat([data, pd.DataFrame(data_list)], ignore_index=True)

            # Cập nhật from_date để lấy dữ liệu cho khoảng thời gian tiếp theo
            from_date = to_date_new

        # Đổi tên cột và chỉ định cột
        data = data.rename(columns={'TradingDate': 'Datetime'})
        # Chuyển đổi cột 'Datetime' sang định dạng datetime
        data['Datetime'] = pd.to_datetime(data['Datetime'], format='%d/%m/%Y')

        data = pd.DataFrame(data, columns=['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume'])

        return data