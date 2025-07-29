k=int(input("Nhập k:"))
a=[]
for i in range(k):
    x=int(input())
    a.append(x)
print("List a vừa nhập là:",a)
n=int(input("Nhập số dòng của ma trận:"))
m=int(input("Nhập số cột của ma trận:"))
if n * m <= k:
    X = []
    index = 0
    for i in range(n):
        row = a[index:index + m]
        X.append(row)
        index += m

    print("Ma trận X:")
    for row in X:
        print(row)
else:
    print("NO")
