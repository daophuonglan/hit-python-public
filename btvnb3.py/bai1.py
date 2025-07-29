n=int(input("Nhập n:"))
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
print("List vừa nhâp:",arr)
x=int(input("Nhập x:"))
print("Số lần ",x," xuất hiện trong list là: ",arr.count(x))
arr[1:7]=[8, 5, 4, 0, 1, 3]
print("List sau khi thay thế là:",arr)
print("Số lớn nhất:",max(arr))
print("Số nhỏ nhất:",min(arr))
y=int(input("Nhập y:"))
arr.insert(0,y)
print("List sau khi thêm ",y," vào vị trí đầu tiên:",arr)
if arr == sorted(arr):
    print("TĂNG")
elif arr == sorted(arr, reverse=True):
    print("GIẢM")
else:
    print("NO")
