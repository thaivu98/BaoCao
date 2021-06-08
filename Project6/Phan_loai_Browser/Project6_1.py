# Doc file sau do xuat file thanh list .
#Sau do loc list lay phan tu thu 5 chinh la user agent 
# Xuat vao 1 file de de lam viec.




from os import remove, write


r = open("gistfile1.txt","r")        # doc file
f = open("Browser.txt", "w+")            # mo tep ghi vao cuoi
for s in r:
    list= s.split('"')              # Tach chuoi thanh list dua tren ki tu nao do
    tmp= list[5].replace('(','"')                   # sua 1 ki tu thanh 1 ki tu khac
    tmp= tmp.replace(')','"')
    f.write(tmp)       # Tach chuoi thanh list dua tren ki tu nao do
    f.write('\n')
f.close()        
r.close()
# sau khi dong 2 file xong ta se lam viec voi file Browser. Quay laij nhung buoc dau tien.
# Doc file va xuat chung thanh chuoi 
f = open("Browser.txt", "r")   # Do dong 9 chi mo cho ghi khong cho doc nen ta mo file cho doc duoi nay
# do dinh dang file chua on dinh nen sua dau ()= "


#Tach xong ma User Agent



b= open("Browser1.txt", "w+")
for s in f:
    list= s.split('"')              # Tach chuoi thanh list dua tren ki tu nao do
    try:
        b.write(list[-1])
    except:
        b.write("Khong xac dinh browser \n ") 
 
b.close()
f.close()
import os
os.remove('Browser.txt')
b= open("Browser1.txt", "r")
c= open ("Baocaotylesudungtrinhduyet.txt","w+")
tmp =[]
for s in b:
    s= s.replace("\n","")
    s= s.replace("/"," ")
    list= s.split(" ")
    list.pop(0)
    tmp = tmp + list

import os
os.remove("Browser1.txt")
# Dem tong Safari se la tong luot truy cap con lai sex dem theo so lan xuat hien cua ten trinh duyet
# Ti le se la so lan xuat hien/safari
# Co nhung truong hop khong xac dinh duoc safari 
#Do chua xac dinh duoc so lan truy cap nen de laf 882
# Tong=tmp.count("Safari")
# print("Tong luot truy cap xac dinh duoc la: ",Tong)
cho=tmp.count("Chrome")
print("Chorme",cho,"luot truy cap")
ch=float(cho/882)*100
ch=round(ch,3)
print("Ty le su dung Chorme la: ",ch,"%")
c.write(str(ch))
c.write(" % truy cap bang chorme \n")
coc=tmp.count("coc_coc_browser")
print("cococ",coc,"luot truy cap")
cc=float(coc/882)*100
cc=round(cc,3)
c.write(str(cc))
c.write(" % truy cap bang CocCoc \n")
print("Ty le su dung CocCoc la: ",cc,"%")
fif=tmp.count("Firefox")
print("Firefox",fif,"luot truy cap")
ff=float(fif/882)*100
ff=round(ff,3)
c.write(str(ff))
c.write(" % truy cap bang Firefox \n")
print("Ty le su dung Firefox la: ",ff,"%")
cor=tmp.count("CoRom")
print("CoRom",cor,"luot truy cap")
cr=float(cor/882)*100
cr=round(cr,3)
c.write(str(cr))
c.write(" % truy cap bang CoRom \n")
print("Ty le su dung CoRom la: ",cr,"%")
b.close()
c.close()