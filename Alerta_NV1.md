### Tổng quan
##### Giới thiệu
   Alerta là một hệ thống giám sát cảnh báo, là một công cụ để hợp nhất và loại bỏ các cảnh báo trùng lặp từ nhiều nguồn để nhanh chóng đưa ra các thông báo chính xác.

##### Chức năng nhiệm vụ
  > Tổng hợp các thông báo từ nhiều nguồn
  >
  > Loại bỏ các thông báo trung lặp
   
### Tài liệu vận hành
#####  Trên Docker
Tải mongodb, alerta/alerta-web về sau đó khởi chạy dịch vụ.

Sau khi tải về thì khởi chạy mongo trước:

> docker run --name alerta-db -d mongo

Sau đó chạy lệnh 
> $ export DATABASE_URL=mongodb://db:27017/monitoring
>
> $ docker run --name alerta-web -e DATABASE_URL=$DATABASE_URL -e ADMIN_USERS=username -e ADMIN_PASSWORD=password -e ADMIN_KEY=api_key -e PLUGINS=reject,heartbeat,blackout,normalise -e DEBUG=1 --link alerta-db:db -d -p 8080:8080 alerta/alerta-web

Sau đó truy cập vào `http://ipdocker:port` là ta đã thấy giao diện web .


Để tạo cảnh báo trong giao diện người dùng web thì chúng ta dùng lệnh sau:

`docker exec -ti idcontainer alerta send -E Development -S Web -r web01 -e http5xx -s warning -t 'Too many 5xx responses'`

-E là tùy chọn môi trường(Production, Development)

-S là tùy chọn dịch vụ(app name, Web,Network, Storage, Database, Security)

-r là tùy chọn nguồn tài nguyên

-e là tùy chọn tên lỗi 

-s là tình trạng như nào(critical, major, minor, warning)

-t là tùy chọn thêm mô tả cảnh báo

![Thêm cảnh báo](Lệnh%20thêm%20cảnh%20báo.PNG)

Kết quả trên web

![](../Kết%20quả%20trên%20web.PNG)

### Trêm server Nagios 
Cài đặt git, curl,gcc,make,libcurl4-openssl-devel

Sau đó git clone `https://github.com/alerta/nagios-alerta.git` 
Sau đó di chuyển tới thư mục nagios-alerta 
Thiếu thư viện của glib chúng ta cài gói glib, sau đó sẽ báo lỗi thiếu thư viện jansson thì chúng ta cài gói libjansson-dev
Chạy lệnh `make nagios4` tiếp đó là `sudo make install`

##### Cấu hình Nagios-to-Alerta 

 `sudo vi /usr/local/nagios/etc/nagios.cfg` 
 
 thêm 
 
 `broker_module=/usr/lib/nagios/alerta-neb.o http://your_alerta_server_ip/api key=ALERTA_API_KEY env=Production hard_only=1 debug=1...`

vào trước `#broker_module=/somewhere/module1.o`

URL:Địa chỉ được sử dụng để giao tiếp với  Alerta API

KEY là API key tạo lúc đầu

env: Tên môi trường, mặc định là Production

hard_only: Chỉ phản hồi kết quả ở trạng thái Hard , bạn có thể tìm hiểu thêm Nagios State Types ở tài liệu. Cài nấc 1 để bật trạng thái.

debug: - sửa lỗi cho module. cài nấc 1 để bật trạng thái.

Sau đó sửa file: ` sudo vi /usr/local/nagios/etc/objects/localhost.cfg `

Thêm `_Environment Production_Service Nagios ` cuối `define host`

thêm 
> service_description Root Partition

> check_command check_local_disk!20%!10%!/

> _Service System }...

Vào cuối `define service` lưu lại thoát ra khởi động lại Nagios

Chowf 1 lúc sẽ có cảnh báo gửi tới web.





### Kế hoạch phát triển

Thêm cảnh báo từ nhiều nguồn và gửi cảnh báo tới khách hàng một cách chính xác qua telegram, email và sms.

##### Tài liệu tham khảo.
1. https://github.com/alerta/docker-alerta
2. https://docs.alerta.io/en/latest/gettingstarted/tutorial-10-docker.html#tutorial-10
3. https://buildmedia.readthedocs.org/media/pdf/alerta/latest/alerta.pdf
4. https://vicloud.vn/community/lam-the-nao-de-giam-sat-nagios-alerts-su-dung-alerta-tren-centos-7-344.html