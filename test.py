import os
from unidecode import unidecode

def create_folders(folder_path, folder_names):
    for name in folder_names:
        folder = os.path.join(folder_path, name)
        os.makedirs(folder)

# Example usage
folder_path = 'E:/Viet(1)'

text = u"Khoa học dữ liệu, Lập trình Python, Lịch sử Đảng Cộng sản Việt Nam, PBL 5 Dự án Kỹ thuật máy tính, Pháp luật đại cương, Quản lý dự án CNTT, Chương trình dịch, Công nghệ Web, Kinh tế chính trị Mác - Lênin, Lập trình mạng, Lập trình trên Linux, Mạng máy tính, PBL 4 Dự án hệ điều hành và mạng máy tính, Vi điều khiển, Xử lý tín hiệu số, Chủ nghĩa Xã hội khoa học, Công nghệ phần mềm, Đồ họa máy tính, GDTC 4 CL Nam, Lập trình .NET, Lập trình Java, PBL 3 Dự án Công nghệ phần mềm, Phân tích & T.kế hướng đối tượng, Trí tuệ nhân tạo, Cơ sở dữ liệu, Lập trình hướng đối tượng, Nguyên lý hệ điều hành, PBL 2 Dự án cơ sở lập trình, Phân tích & thiết kế giải thuật, TN Vật lý (Cơ-Nhiệt), Toán ứng dụng Công nghệ thông tin, Xác suất thống kê, Anh văn CLC_T700, Cấu trúc dữ liệu, Cấu trúc máy tính và vi xử lý, Giải tích 2, Giáo dục thể chất 2, PBL1 Dự án lập trình tính toán, Phương pháp tính, Toán rời rạc, Tư tưởng Hồ Chí Minh, Vật lý 1, Anh văn A2.1 (CLC), Anh văn A2.2 (CLC), Đại số tuyến tính, Giải tích 1, Giáo dục thể chất 1, Kỹ thuật lập trình, Nhập môn ngành, TH kỹ thuật lập trình, Triết học Mác - Lênin"
text_without_diacritics = unidecode(text)
folder_names = text_without_diacritics.split(", ")
print(folder_names)
create_folders(folder_path, folder_names)