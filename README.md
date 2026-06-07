# Network-Based Drug Discovery for Gout

#ổng quan dự án
Dự án xây dựng một mạng tương tác protein–protein (PPI) để phân tích mối quan hệ giữa dược liệu và bệnh gout thông qua dữ liệu gene, protein và triệu chứng.
Mục tiêu:
- Mô hình hóa bệnh học theo hướng network medicine
- Đánh giá hiệu quả dược liệu dựa trên khoảng cách mạng sinh học
- Kiểm định giả thuyết bằng thống kê và machine learning

# Ý tưởng chính

Thay vì phân tích dược liệu theo hướng truyền thống, dự án giả định rằng: Dược liệu hiệu quả sẽ có target protein nằm gần module protein của bệnh trong mạng PPI.

#Phương pháp

#1. Xây dựng mạng PPI
- Xây dựng đồ thị từ dữ liệu protein–protein interaction
- Loại bỏ các thành phần không liên thông
- Giữ largest connected component để đảm bảo tính nhất quán của khoảng cách

#2. Xác định module bệnh (symptom module)
- Map triệu chứng → gene/protein
- Lọc các protein có trong mạng PPI
- Giữ các module có ≥ 10 protein để đảm bảo độ tin cậy thống kê
# 3. Network Proximity

# 4.Proximity d
Đo khoảng cách trung bình từ target dược liệu đến protein gần nhất trong module bệnh:
- Giá trị càng nhỏ → dược liệu càng liên quan đến bệnh.
- 
# Sab (Menche et al., Science 2015)
\[
S_{AB} = D_{AB} - \frac{D_{AA} + D_{BB}}{2}
\]

- Sab < 0: hai module có xu hướng chồng lấp trong mạng
- Sab > 0: hai module tách biệt

# 4. Đánh giá thống kê
- ROC-AUC: đánh giá khả năng phân biệt dược liệu hiệu quả

=> Kết quả

- ROC-AUC (proximity d): 0.66
- Dược liệu có hiệu quả có khoảng cách mạng nhỏ hơn đáng kể so với nhóm không hiệu quả
- Sab cho thấy mức độ tương tác rõ ràng giữa các module bệnh trong mạng PPI

# Dữ liệu sử dụng

- HIT Herbal Target Database
- GeneCards (gout-related genes)
- TCM symptom–gene dataset
- Protein–Protein Interaction network (Interactome)



