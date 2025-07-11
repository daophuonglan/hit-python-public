Bài 1:
- Python là ngôn ngữ thông dịch vì mã nguồn được chạy qua trình thông dịch (như CPython), không biên dịch trực tiếp thành mã máy như C/C++.
Bài 2:
- Các kiểu dữ liệu trong Python:
1. Kiểu dữ liệu số
Python hỗ trợ nhiều loại số học khác nhau, bao gồm:

int: Số nguyên (ví dụ: 1, 2, 3)
float: Số thực, hay số có dấu chấm động (ví dụ: 1.5, 2.75)
complex: Số phức (ví dụ: 3+4j, 5+6j)

2. Kiểu dữ liệu chuỗi
Chuỗi là một dãy các ký tự Unicode. Chuỗi có thể được đặt trong dấu ngoặc đơn ('') hoặc dấu ngoặc kép ("").

Ví dụ:

a = "Hello"
b = 'Python'
3. Kiểu dữ liệu danh sách
Danh sách là một cấu trúc dữ liệu có thứ tự, có thể chứa nhiều kiểu dữ liệu khác nhau. Các phần tử trong danh sách được đặt trong dấu ngoặc vuông [] và phân cách bởi dấu phẩy.

Ví dụ:

a = [1, 2, 3, "Python", 4.5]
4. Kiểu dữ liệu tuple
Tuple tương tự như danh sách nhưng không thể thay đổi được (immutable). Các phần tử trong tuple được đặt trong dấu ngoặc đơn () và phân cách bởi dấu phẩy.

Ví dụ:

a = (1, 2, 3, "Python", 4.5)
5. Kiểu dữ liệu từ điển
Từ điển là một cấu trúc dữ liệu không có thứ tự, lưu trữ các cặp khóa-giá trị (key-value). Các phần tử trong từ điển được đặt trong dấu ngoặc nhọn {} và phân cách bởi dấu phẩy.

Ví dụ:

a = {"name": "John", "age": 30, "city": "New York"}
6. Kiểu dữ liệu tập hợp
Tập hợp là một tập hợp không có thứ tự các phần tử duy nhất. Các phần tử trong tập hợp được đặt trong dấu ngoặc nhọn {}.

Ví dụ:
a = {1, 2, 3, 4, 5}
- Các toán tử trong Python:
1. Toán tử số học: +, -, *, /, //, %, **

2. So sánh: ==, !=, <, >, <=, >=

3. Logic: and, or, not

4. Gán: =, +=, -=, *=, ...

5. Membership: in, not in

6. Nhận dạng: is, is not

7. Toán tử thao tác bit trong Python: &, |, ^, ~, >>, <<
- Mệnh đề điều kiện và vòng lặp trong python:
1. Mệnh đề điều kiện (if, elif, else):
Cú pháp:
if điều_kiện:
    # mã lệnh nếu đúng
elif điều_kiện_khác:
    # mã lệnh nếu điều_kiện_khác đúng
else:
    # mã lệnh nếu tất cả điều kiện sai
2. Vòng lặp trong Python:
a. Vòng lặp for – Lặp qua dãy số, chuỗi, list,...
b. Vòng lặp while – Lặp khi điều kiện còn đúng
3. Thoát vòng lặp:
break: dừng vòng lặp
continue: bỏ qua lần lặp hiện tại, tiếp tục vòng tiếp theo
- Kiểu dữ liệu True, False:
Kiểu bool chỉ có 2 giá trị: True và False
Thường dùng trong so sánh và điều kiện
