# Project3: Setup Nagios và viết Bash Script phục vụ cảnh báo NRPE cho Nagios



## Dựng Nagios Server
Trước tiên cần cài đặt những gói phụ thuộc để phục vụ cho cài đặt nagios như apache2 php mysql,... 

> `apt install autoconf gcc libc6 make wget unzip apache2 php libapache2-mod-php`
 

Sau đó là tải Nagios Server về.Tải xong thì ta giải nén ra.

> wget https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.4.5.tar.gz
>
Giải nén.
> tar -zxvf /tmp/nagios-4.4.5.tar.gz

Tiếp theo đó ta biên dịch mã nguồn Nagios và xác định cấu hình máy chủ ảo Apache cho Nagios.

>sudo ./configure --with-httpd-conf=/etc/apache2/sites-enabled
>sudo make all

Tạo người dùng và nhóm Nagios và thêm người dùng Apache 'www-data' vào nhóm 'nagios'.
> sudo make install-groups-users
>
> sudo usermod -a -G nagios www-data

Sau đó tiến hành cài đặt 

> sudo make install
>
> sudo make install-daemoninit
>
> sudo make install-commandmode

Sau đó cài cấu hình scrip
> sudo make install-config

Sau đó cài đặt cấu hình Apache cho Nagios và kích hoạt các mô-đun mod_rewrite và mode_cgi.

> sudo make install-webconf
>
> sudo a2enmod rewrite cgi

restart lại apache.

Tạo User "nagiosadmin"và password "1"
> sudo htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin

Sau khi xong thì ta cài firewall cho phép nagios hoạt động.

### Thêm NRPE Plugin

Cả hai plugin Nagios và NRPE đều có sẵn theo mặc định trên kho lưu trữ Ubuntu. Bạn có thể cài đặt các gói đó bằng lệnh sau:

> sudo apt install monitoring-plugins nagios-nrpe-plugin

Sau đó di chuyển vào "/usr/local/nagios/etc" tạo 1 file 
> mkdir -p /usr/local/nagios/etc/servers

Sửa file config "nagios.cfg"
> vi nagios.cfg

Bỏ Comment dòng 
> cfg_dir=/usr/local/nagios/etc/servers

Sau đó sửa file "resource.cfg"
> vi resource.cfg

Sửa dòng sau:
> $USER1$=/usr/lib/nagios/plugins

Sau đó đi sửa trong file contact để lúc hệ thống có quá tải thì sẽ có cảnh báo về mail.
> vi objects/contacts.cfg

Thêm Mail để gửi cảnh báo vào.
Sau đó khởi động nagios và enable nó.
restart lại apache.

Bây giờ có thể vào trình duyệt vào http://IP máy server/nagios
### Thêm host vào server
Ta cần sửa file sau:
> cd /usr/local/nagios/etc
>
> vim servers/client01.cfg
>
# Ubuntu Host configuration file1

>       define host {
>            use                          linux-server
>            host_name                    client01
>            alias                        Ubuntu Host
>            address                      IP máy NRPE server
>            register                     1
>     }
> 
>       define service {
>
>            host_name                       client01
>            service_description             PING
>            check_command                   check_nrpe!check_ping
>            max_check_attempts              2
>            check_interval                  2
>            retry_interval                  2
>            check_period                    24x7
>            check_freshness                 1
>            contact_groups                  admins
>            notification_interval           2
>            notification_period             24x7
>            notifications_enabled           1
>            register                        1
>     }
> 
>       define service {
>            host_name                       client01
>            service_description             Check Users
>            check_command                   check_nrpe!check_users
>            max_check_attempts              2
>            check_interval                  2
>            retry_interval                  2
>            check_period                    24x7
>            check_freshness                 1
>            contact_groups                  admins
>            notification_interval           2
>            notification_period             24x7
>            notifications_enabled           1
>            register                        1
>     }
> 
>       define service {
>            host_name                       client01
>            service_description             Check SSH
>            check_command                   check_nrpe!check_ssh
>            max_check_attempts              2
>            check_interval                  2
>            retry_interval                  2
>            check_period                    24x7
>            check_freshness                 1
>            contact_groups                  admins
>            notification_interval           2
>            notification_period             24x7
>            notifications_enabled           1
>            register                        1
>     }
> 
>       define service {
>           host_name                       client01
>           service_description             Check Root / Disk
>           check_command                   check_nrpe!check_root
>           max_check_attempts              2
>           check_interval                  2
>           retry_interval                  2
>           check_period                    24x7
>           check_freshness                 1
>           contact_groups                  admins
>           notification_interval           2
>           notification_period             24x7
>           notifications_enabled           1
>           register                        1
>     }
> 
>       define service {
>           host_name                       client01
>           service_description             Check APT Update
>           check_command                   check_nrpe!check_apt
>           max_check_attempts              2
>           check_interval                  2
>           retry_interval                  2
>           check_period                    24x7
>           check_freshness                 1
>           contact_groups                  admins
>           notification_interval           2
>           notification_period             24x7
>           notifications_enabled           1
>           register                        1
>     }
> 
>       define service {
>           host_name                       client01
>           service_description             Check HTTP
>           check_command                   check_nrpe!check_http
>           max_check_attempts              2
>           check_interval                  2
>           retry_interval                  2
>           check_period                    24x7
>           check_freshness                 1
>           contact_groups                  admins
>           notification_interval           2
>           notification_period             24x7
>           notifications_enabled           1
>           register                        1
>     }


 Sau đó khởi động lại nagios.
 
## Thêm máy client cần theo dõi vào hệ thống Nagios.

Đầu tiên cần cài gói Nagios Plugin và NRPE Server.
> sudo apt install nagios-nrpe-server monitoring-plugins

 Sau đó là vào chỉnh sửa file nrpe.cfg

Bỏ comment dòng `server_address`
> server_address=IP máy NRPE Server.

Tiếp theo thêm IP máy Nagios Server
> allowed_hosts=IP máy Nagios Server,::1

Sau khi sửa xong file này thì chúng ta sửa tới file nrpe_local.cfg
Ở đây chúng ra viết những đoạn scrip để cho Nagios gửi cảnh báo khi máy tới giới hạn.


sau đó thì khởi động lại NRPE service

> systemctl restart nagios-nrpe-server
>
>systemctl enable nagios-nrpe-server

### Cảnh báo qua Mail.
Trước tiên cài Postfix để mail hoạt động.

Thêm một file khai báo mail `sasl_passwd` ở trong file này chúng ta khai báo email của mình và mật khẩu.

`[smtp.gmail.com]:587 mail:pass`

Sau đó vào sửa file: `vi /etc/postfix/main.cf`

> relayhost = [smtp.gmail.com]:587
>
> smtp_use_tls = yes
>
> smtp_sasl_auth_enable = yes
>
> smtp_sasl_security_options =
>
> smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
>
> smtp_tls_CAfile = /etc/ssl/certs/ca-bundle.crt

> https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NCnJC4KybbyP0n5PNsyhDEMqsbt9zV3DAGIPoh3YbH_3iB0Tc6SD-hN50teQ0iL5cX3lqPUM8SVKxr2s4feZXZ9CrjQQ

Truy cập link trên để chuyển sang có.

Sau khi đã xong thì ta khởi động Postfix

Điền mail vào file contact.cfg

Rồi sau đó khởi động lại Nagios.

### Cảnh báo qua telegram

Đầu tiênvaof chat với @botfather
> /newbot  

Để tạo bot mới. sau đó chúng ta sẽ đặt tên cho con bot mới này. Sau khi đặt tên cho bot mới xong thì nó sẽ gửi cho token

Sau đó chúng ta phải sửa command trong file contact.cfg

Thêm ID của telegram muốn nhận thông báo.
và sửa thêm phần ` service_notification_commands         notify-service-by-email, notify-service-by-telegram`

`host_notification_commands              notify-host-by-email, notify-host-by-telegram`

Để nhận thông báo từ cả telegram và gmail.

Trong file command.cfg ta thêm phần command sau:

> #'notify-host-by-telegram' command definition
> 
> define command{
>
> command_name notify-host-by-telegram
>
> command_line /usr/bin/curl -X POST --data chat_id=$CONTACTPAGER$ --data parse_mode="markdown" --data text="%60$HOSTNAME$%60 %0A%0A$NOTIFICATIONTYPE$ %0A%60$HOSTSTATE$%60 %0A%60$HOSTADDRESS$%60 %0A%60$HOSTOUTPUT$%60" https://api.telegram.org/bot`BOTAPI-KEY`/sendMessage
> }
> 
> #'notify-service-by-telegram' command definition
> 
> define command{
>
> command_name notify-service-by-telegram
>
> command_line /usr/bin/curl -X POST --data chat_id=$CONTACTPAGER$ --data parse_mode="markdown" --data text="%60$HOSTNAME$%60 %0A%0A$NOTIFICATIONTYPE$ %0A%60$SERVICEDESC$%60 %0A%60$HOSTADDRESS$%60 %0A%60$SERVICESTATE$%60 %0A%60$SERVICEOUTPUT$%60" https://api.telegram.org/bot`BOTAPI-KEY`/sendMessage
> }


##### Tài liệu tham khảo
1. https://www.howtoforge.com/tutorial/how-to-install-nagios-on-ubuntu-2004/
2. https://kifarunix.com/install-and-setup-nagios-core-on-ubuntu-20-04/
3. https://linuxhint.com/install_nagios_ubuntu/