## Các ví dụ về bài toán regression **trong thực tế**

### Dự đoán doanh thu thông qua chi phí quảng cáo

**Input**: chi phí quảng cáo (kiểu số nguyên - đơn vị tính là VND)

**Output**: doanh thu dự đoán sẽ đạt được thông qua việc quảng cáo(kiểu số nguyên - đơn vị tính là VND)

**Cách thu thập data**: tạo trang sheet (file .csv) thu thập chi phí đã dùng cho quảng cáo sản phẩm và doanh thu của sản phẩm của những tháng (hoặc năm) trước đó.

**Cách xử lý data**: 
* Loại bỏ những thông tin có giá trị NULL 
* Không cần loại bỏ những giá trị âm ở cột doanh thu, vì nếu giá trị âm chứng tỏ việc quảng cáo không đem lại lợi nhuận (bị lỗ vốn); giá trị gần = 0 thì hòa vốn

**Cách tính**:
Y = B*0* + B*1*X

Y: Doanh thu dự đoán

X: Chi phí dành cho việc quảng cáo

B*0*: tổng doanh thu dự kiến đạt được khi chi phí dành cho quảng cáo = 0

B*1*: sự thay đổi trung bình trong tổng doanh thu khi chi tiêu cho quảng cáo được tăng thêm một đơn vị (trường hợp ở đây là VND)

### Dự đoán huyết áp của người bệnh dựa trên lượng thuốc được cho

**Input**: liều lượng thuốc cho người bệnh (kiểu số thực - miligram)

**Output**: huyết áp của người bệnh (gồm 2 số nguyên - đơn vị tính là mi-li-mét thủy ngân)( *huyết áp thường được xác định bởi tỉ số của 2 chỉ số*)

**Cách thu thập data**: thu thập thông tin từ bệnh viện, các cơ sở y tế và ghi nhận lại 2 thông tin: liều lượng thuốc được bác sĩ kê và huyết áp của bệnh nhân. Tổng hợp lại thành file .csv

**Cách xử lý data**: 
* Loại bỏ những thông tin có giá trị NULL 
* Loại bỏ những thông tin có giá trị âm

**Cách tính**:
Y = B*0* + B*1*X

Y: Huyết áp dự đoán

X: Liều lượng thuốc

B*0*: Huyết áp khi liều lượng thuốc = 0

B*1*: sự thay đổi trung bình của huyết áp khi tăng liều lượng thuốc lên một đơn vị (miligram)

### Dự đoán sản lượng cây trồng dựa trên lượng nước tưới và phân bón

**Input**: lượng nước tưới cây (kiểu số thực - đơn vị lít) và lượng phân bón đã bón cho cây (kiểu số thực - đơn vị kg)

**Output**: sản lượng của cây trồng (kiểu số thực - đơn vị kg)

**Cách thu thập data**: thu thập bằng cách đo cụ thể, liên hệ với những người nông dân. Tổng hợp thành file .csv

**Cách xử lý data**: 
* Loại bỏ những thông tin có giá trị NULL 
* Loại bỏ những thông tin có giá trị âm
* Chuẩn hóa dữ liệu về khoảng giá trị [0, 1]

**Cách tính**:

Z = B*0* + B*1*X + B*2*Y

Z: Sản lượng cây trồng dự đoán

X: Lượng phân bón

Y: Lượng nước tưới cho cây

B*0*: sản lượng của cây khi không bón phân và tưới nước

B*1*: sự thay đổi trung bình của sản lượng khi lượng phân bón tăng lên 1 đơn vị và giả sử lượng nước không thay đổi

B*2*: sự thay đổi trung bình của sản lượng khi lượng nước tăng lên 1 đơn vị và giả sử lượng phân bón không thay đổi

### Dự đoán tác động của chế độ tập luyện lên các cầu thủ ở NBA

**Input**: số lượng buổi tập yoga (kiểu số nguyên) và số lượng buổi tập nâng tạ (kiểu nguyên)

**Output**: số điểm dự đoán có thể ghi được (kiểu số nguyên)

**Cách thu thập data**: thu thập thông tin tập luyện hằng tuần của các cầu thủ. Tổng hợp thành file .csv

**Cách xử lý data**: 
* Loại bỏ những thông tin có giá trị NULL 
* Loại bỏ những thông tin có giá trị âm
* Đưa những giá trị về trong khoảng [0, 1]

**Cách tính**:

Z = B*0* + B*1*X + B*2*Y

Z: Số điểm dự đoán đạt được

X: Số lượng bài tập yoga

Y: Số lượng bài tập nâng tạ

B*0*: số điểm đạt được khi không tham gia bất kỳ buổi tập nào

B*1*: sự thay đổi trung bình của điểm số khi tăng số buổi tập yoga và giả sử số buổi tập nâng tạ không đổi

B*2*: sự thay đổi trung bình của điểm số khi tăng số buổi tập nâng tạ và giả sử số buổi tập yoga không đổi

### Dự đoán số tiền cần phải bỏ ra để đổ xăng cho xe khi muốn đi trên 1 đoạn đường

**Input**: số kilomet cần phải đi (kiểu nguyên - đơn vị km)

**Output**: số tiền dự đoán để đổ xăng (số nguyên - đơn vị VND)

**Cách thu thập data**: ghi lại thông tin của chính bản thân và những người xung quanh về số quãng được đã đi được và số tiền đổ xăng trong từng tuần

**Cách xử lý data**: 
* Loại bỏ những thông tin có giá trị NULL 
* Loại bỏ những thông tin có giá trị âm

**Cách tính**:

Y = B*0* + B*1*X

Y: Số tiền dự đoán

X: Số km đã đi được

B*0*: Số tiền phải bỏ ra khi số km đi được = 0

B*1*: sự thay đổi trung bình của số tiền phải trả khi tăng số km đã đi được lên 1 đơn vị



