ho_ten=input("Nhập họ tên:")
ho_ten = ho_ten.strip().lower()
print(ho_ten)
cac_tu = ho_ten.split()
print(cac_tu)
for i in range(len(cac_tu)):
    cac_tu[i] = cac_tu[i].capitalize()
ho_ten_chuan = ' '.join(cac_tu)
print("Họ tên chuẩn:",ho_ten_chuan)
