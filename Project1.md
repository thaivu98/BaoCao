# Project1: Dựng web Server trên linux

Chuẩn bị 3 server: 1 chạy nginx, 2 máy chạy apache

## Nginx
Đầu tiên ta cần tải Nginx về.

Sau đó vào `/etc/nginx/sites-available ` để coppy file default thành file web của mình.

Sau đó sửa nội dung file như sau:
>      upstream webnginx {
>         server 192.168.255.140:8080;
>         server 192.168.255.141:8080;
>      }
>      server {
>         listen 80;
> 
>         server_name webnginx;
> 
>         location / {
>             proxy_set_header X-Real-IP $remote_addr;
>             proxy_set_header X-Forwarded-For $remote_addr;
>             proxy_set_header Host $host;
>             proxy_pass http://webnginx;
>         }
>      }

Port mặc định của nginx là 80 nên không cần sửa

Phần ` upstream` là lệnh để đưa ra một tập hợp các server có chức năng xử lí yêu cầu. Rất tốt để sử dụng cho việc mở rộng cơ sở hạ tầng.
Sau khi cấu hình file xong t tiến hành cấu hình fie proxy_params để có thể có proxy reverse


> proxy_set_header Host $http_host;
>
> proxy_set_header X-Real-IP $remote_addr;
>
> proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
>
> proxy_set_header X-Forwarded-Proto $scheme;

Sau đó coppy file:

`sudo cp /etc/nginx/sites-available/webnginx.conf /etc/nginx/sites-enabled/webnginx.conf` 

Sau đó tiến hành reload nginx là xong: `sudo service nginx reload `

## Apache2

Ở trên 2 con server web thì chúng ta cài đặt apache2 và PHP để tạo 2 website cho bài lap.

Sau khi cài đặt xong thì chúng ta tiến hành đổi port lắng nghe sang port 8080 hoặc port bất kì k chạy service nào.
> cd /etc/apache2 

Sửa file ports.conf

> Listen 8080


Sau đó tiến hành cài  mariadb server và maria client trên cả 2 web server.
Sau đó chúng ta tiến hành cài PHP 
Sau đó  tạo database cho wordpress
sau khi khởi tạo database xong cho wordpress thì ta tiến hành tải wordpress bản mới nhất về.
sau đó tiến hành cấu hình file config
Vào sửa file sudo nano `/etc/apache2/sites-available/wordpress.conf`

Sửa port lắng nghe sang 8080 như lúc cài đặt ở upstream trong nginx

`<VirtualHost *:8080>` Và đường dẫn `DocumentRoot /var/www/wordpress` trỏ về thư mục wordpress.
Sau đó khởi động site `sudo a2ensite wordpress.conf` sau đó chúng ta restart lại apache2. `sudo systemctl restart apache2.service `
Sau khi hoàn thiện các các cài đặt trên thì chúng ta test . Vào trình duyệt gõ IP của máy chủ Nginx ra. Và thấy xuất hiện trang cài đặt của Wordpress. 



## Chứng thực
sudo htpasswd -cb /etc/apache2/user petblack1 1
Tạo 2 tài khoản để lát đăng nhập
Thêm 4 dòng sau vào file wordpress.conf trong sites-available

> AuthType Basic
> 
> AuthName "testweb"
> 
> AuthUserFile /etc/apache2/user
> 
> Require valid-user


Kích hoạt dịch vụ lên và restart lại apache2. Giờ thì vào web để xem điều kahcs biệt.
