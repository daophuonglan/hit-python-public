x=int( input("Nhập tháng:"))
y=int( input("Nhập năm:"))
while x<=0 or x>12:
    x= int(input("Nhập lại tháng:"))
while y<=0:
    y=int(input("Nhập lại năm:"))
if(x==2 and y%4==0):
    print("Có 29 ngày")
elif(x==2 and y%4!=0):
    print("Có 28 ngày")
elif(x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12):
    print("Có 31 ngày")
else:
    print("Có 30 ngày")
