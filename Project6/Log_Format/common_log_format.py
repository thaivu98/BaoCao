# Dau tien mo file log ra
from os import access


r=open("access.log","r")
f=open("access.txt","w+")
for s in r:
    # s =s.replace("\n","")
    list= s.split('"')
    list.pop(6)
    list.pop(5)
    list.pop(4)
    list.pop(3)
    f.write(str(list))
    f.write("\n")
f.close()
r.close()
# Ghi vao file moi nhung can loai bo ki tu dau va ki tu cuoi trong chuoi( su dung lstrip va rstrip de lam viec)

a=open("access.txt","r")
b=open("test.txt","w+")
for s in a:
    s=s.replace("'",'')
    s=s.replace(",","")
    s=s.replace("[","")
    s=s.replace("]","")
    b.write(s)
    print(s)
a.close()
b.close()
import os                           #Xong file nao xoa file day.
os.remove("access.txt")






