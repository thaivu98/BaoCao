# Project2: Dựng NFS server
Chuẩn bị 1 máy server và 1 máy Client.

## NFS server
Cài đặt NFSS server.

Sau khi cài xong thì chúng ta tiến hành tạo thư mục chia sẻ.

Sau khi tạo xong thư mục chia sẻ thì cấp quyền truy cập cho nó.

Sau đó vào sửa file `sudo nano /etc/exports`
Thêm IP máy khách và quyền cho nó

/var/testshare 192.168.255.137(rw,sync,no_subtree_check)

Đường dẫn    --------IP---------------Phân quyền

`rw` Phân quyền đọc và ghi 
`sync`  Tùy chọn này buộc NFS ghi các thay đổi vào đĩa trước khi trả lời.
`no_subtree_check` Ngăn việc kiểm tra cây con

Sau đó lưu vào thoát ra khỏi động lại dịch vụ

`sudo systemctl restart nfs-kernel-server`

## NFS client

Cài đặt NFS

Sau khi cài đặt xong thì ta tiến hành tạo 1 folder dùng chung 

`sudo mount ip:<đường dẫn bên server> <đường dẫn client>`

## Test 

Bên máy server tạo một file test.txt sau đó sang bên máy client viết "hello" vào file test.txt  đó.



##### Tài Liệu tham khảo
1. https://congdonglinux.com/how-to-install-nfs-client-and-server-on-ubuntu-20-04/
2. https://www.linuxtechi.com/install-nfs-server-on-ubuntu/