x=int(input("Nhập số lương:"))
while x<=0:
    x=int(input("Nhập lại số lương:"))
if(x<7000000):
    print("Thuế:",int(x*0.1))
    print("Thu nhập:",int(x-(x*0.1)))
elif(x<15000000 and x>=7000000):
    print("Thuế:",int(x*0.2))
    print("Thu nhập:",int(x-(x*0.2)))
else:
    print("Thuế:",int(x*0.3))
    print("Thu nhập:",int(x-(x*0.3)))