n= int(input("Nhập n:"))
count=0
total=0
if(n==0):
    count=1
    total=0
else:
    while n!=0:
        x=n%10
        count+=1
        total+=x
        n=n//10
print("Số chữ số:",count)
print("Tổng chữ số:",total)
