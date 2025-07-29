tmp =[1,10,100]
tmp[1]=100
print(tmp)

list=[1,3,'a']
list.append(1)
print(list)
list.insert(1,60)
print(list)
list.insert(-1,'python')
print(list)

a=[1,2,3]
a.insert(40,200)
print(a)
a.insert(-10,100)
print(a)
list1=[1,2,3]
list1.extend([10])
print(list1)
list2=[1,2,3]
list2.append([10])
print(list2)
list3=[1,10,'a',100]
value_dele=list3.pop(1)
print(value_dele)
print(list3)
list4=['a','b',2,5,7]
# list4.remove('a')
# print(list4)
list4.clear
print(list4)
list5=[1,2,'a',2.3,4,5,'b']
# print(len(list5))
# for i in range(len(list5)):
#     print(list5[i], end =' ')
# print('\n')
# for x in list5:
#     print(x, end=' , ')
# for x in range(len(list5)):
#     if x < 4:
#         print(list5[x], sep='-', end=' ')
#         print('\n')
#     else:
#         print(list5[x],sep='\n', end='#')
a=[1,2,5]
b=a*2
print(b)
c=[1,3,5,7,5,8,12,5]
print(c.count(5))
print(c.index(8))
d=[4,5,6]
d.reverse()
print(d)
# sap xep tang
e=[4,2,8,9,6,7,5]
e.sort()
print(e)
#sapxep giam
e.sort(reverse=True)
print(e)
# nhap mang
# n=int(input())
# arr=[]
# for i in range(n):
#     x=int(input())
#     arr.append(x)
# print(arr)
list6=[1,2,3,4,5,'a','b','c']
print(list6[2:5:1])
print(list6[2:5:2])
print(list6[2:5])
print(list6[3:])
print(list6[-4:-2])
# dao nguoc ma khong thay doi a
a1=[1,2,3,4,5]
# b1=a1[::-1]
# print(b1)
list6[1:3]=[8,9]
print(list6)
# copy mang
b1=a1[:]
print(b1)
# xoa ptu
a1[1:3]=[]
print(a1)
# b2 [x**2 for x in a1]
# print(b2)
a2=[i for i in range(10)]

