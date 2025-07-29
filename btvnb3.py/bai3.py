s1=input("Nhập chuối s1:")
s2=input("Nhập chuỗi s2:")
reversed_s1= s1[::-1]
print("Đảo ngược của chuỗi s1:",reversed_s1)
while True:
    a = int(input("Nhập số nguyên a (>=1): "))
    b = int(input("Nhập số nguyên b (>a và <= độ dài chuỗi s2): "))
    
    if 1 <= a < b <= len(s2):
        break
    else:
        print(f"Giá trị không hợp lệ. Nhập lại (1 <= a < b <= {len(s2)})")
start = a - 1
end = b
reversed_s2 = s2[:start] + s2[start:end][::-1] + s2[end:]
print("Chuỗi s2 sau khi đảo ngược chuỗi từ vị trí ",a," đến ",b,"là:",reversed_s2)
s3 = ''.join([s1[i] for i in range(len(s1)) if i % 2 != 0])
print("s3:", s3)
s4 = ''
min_len = min(len(s1), len(s2))
for i in range(min_len):
    s4 += s1[i] + s2[i]
s4 += s1[min_len:] + s2[min_len:]
print("s4:", s4)