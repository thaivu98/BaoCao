# Project4: Project 4: Dựng mô hình Graph monitor (Grafana + InfluxDB + Telegraf + Kapacitor)


sơ đồ:


admin===========>granafa<==================influxDB<===============Telegraf

Với cấu trúc sơ đồ này các telegraf sẽ đẩy các thông số theo dõi lên influxDB và sau đó granafa sẽ lấy thông số từ influx chuyển qua dạng sơ đồ và các hiển thị cho người quản trị dễ theo dõi và biết được các thông báo. 

## Cài telegraf

Tải telegraf qua lệnh sau:

>       wget https://dl.influxdata.com/telegraf/releases/telegraf_1.14.3-1_amd64.deb

Sau khi tải xong thì chúng ta tiến hành cài đặt.

>           dpkg -i telegraf_1.14.3-1_amd64.deb

Tải thêm một số repo:

>           wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -

>       source /etc/lsb-release

>       echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

>   apt install telegraf

Bật nó khởi động cùng hệ thống.
>       systemctl enable --now telegraf


Do telegraf có chức năng gửi các biến số về influxdb nên là máy chủ nào cần theo dõi thì chúng ta cái telegraf trên máy chủ đó và add vào với influxdb.

## Cài InfluxDB

>       wget https://dl.influxdata.com/influxdb/releases/influxdb_1.8.0_amd64.deb

Tải về rồi tiến hành cài đặt.

>       dpkg -i influxdb_1.8.0_amd64.deb

sau khi tải và cài đặt Influxdb xong thì tạo 1 database:

>   influx
>
>   create database telegraf
>
>   create user telegraf with password 'myP@SSword'
>
>   grant all on telegraf to telegraf

Sau khi tạo xong database thì thoát ra.

Vào sửa file vi /etc/telegraf/telegraf.conf

> #Configuration for sending metrics to InfluxDB
> [[outputs.influxdb]]
>
>   urls = ["http://127.0.0.1:8086"]
>
>   database = "telegraf"
>
>   username = "telegraf"
>
>   password = "myP@SSword"

Sau khi sửa xong thì tiến hành khởi động lại dịch vụ.

Chạy thử nghiệm.
> telegraf --config /etc/telegraf/telegraf.conf --test
>
>telegraf -test -config /etc/telegraf/telegraf.conf --input-filter system

Sau khi thử nghiệm thành công không có lỗi phát sinh thì chúng ta cấu hình firewall
> ufw allow 3000/tcp

Sau đó vào http://ipserver:3000

Sau khi vào thì chọn phần `data source`

Sửa `URL        http://localhost:8086`

Thêm tài khoản và mật khẩu 
 
Xuống cuối chọn nguồn Data. là InfluxDB Sau đó save và test.


Ấn vào dấu cộng bên trái  vào phần `import` điền ID via  vào và `load` ta sẽ có một giao diện cùng với các thông số cần theo dõi.


## Cài đặt thông báo.
### Telegram
Vào biểu tượng cái chuông bên trái màn hình sau đó kích vào `Notifycation_chanels`====> `New chanel`

Phần type chọn kiểu là Telegram

Tạo một con bot và lấy token channel vào

Sau đó là thêm ID của người cần được nhận thông báo.

### Email

Giống telegram chỉ khác chọn type là email.


##### Link tham khảo

1. https://kifarunix.com/install-and-setup-tig-stack-on-ubuntu-20-04/
2. https://kifarunix.com/monitor-system-metrics-with-tick-stack-on-ubuntu-20-04/
3. https://galaxyz.net/cach-theo-doi-cac-chi-so-he-thong-bang-tick-stack-tren-centos-7.259.anews