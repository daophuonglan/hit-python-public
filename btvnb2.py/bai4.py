n=int(input("Nhập số xu:"))
sochai= n//28
bottle=sochai
while bottle>=3:
    doiduoc= bottle//3
    sochai+= doiduoc
    bottle=bottle%3 +doiduoc 
print("Số chai bia có thể mua được là:",sochai)