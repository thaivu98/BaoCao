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
b=open("data.txt","w+")
for s in a:
    s=s.replace("'",'')
    s=s.replace(",","")
    s=s.replace("[","")
    s=s.replace("]","")
    s=s.replace("-","")
    b.write(s)
a.close()
b.close()
import os                           #Xong file nao xoa file day.
os.remove("access.txt")
# Da co file log_format. Bay gio lam viec voi file log_format nay.file log cu co the xoa.
c=open("data.txt","r")
d=open("Source_IP","w+")
list_ip={}                     # Tao ra 1  set rong de kiem tra
for line in c:
    list=line.split(" ") # Doc 1 dong
    ip = str(list[0]) # lay ip
    
    if(list_ip.get(ip) == None): # Kiem tra xem ip ton tai hay chua
        list_time=[str(list[3])]
        value = [1,list_time]

        list_ip[ip] = value # Them ip vao danh sach
    else:
        value = list_ip.get(ip) # Lay so lan xuat hien cua ip 
        count = int(value[0]) + 1
        list_time = value[1]
        list_time.append(str(list[3]))

        value = [count,list_time]
        list_ip[ip] = value  # Tang so lan len 1
for item in list_ip:
    d.write(str(item)+ ": "+str(list_ip[item])+"\n")
# Xem co baonhieu IP va so lan xuat hien trong log.
