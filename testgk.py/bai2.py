n= input("Nhập chuỗi ký tự:")
words = n.split()
s = set()
for word in words:
    for char in word:
        s.add(char)
print(list(s))
