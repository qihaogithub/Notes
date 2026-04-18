---
创建日期: 2026-01-26T16:21:28+08:00
修改日期: 2026-01-26T16:21:40+08:00
---
在 Linux 上开启 FTP 服务，最常用的是 vsftpd。以下是主要步骤：

## 安装 vsftpd

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install vsftpd
```

**CentOS/RHEL:**
```bash
sudo yum install vsftpd
```

## 配置 vsftpd

编辑配置文件：
```bash
sudo nano /etc/vsftpd.conf
```

确保以下配置项已设置（取消注释）：
```ini
listen=YES
anonymous_enable=NO
local_enable=YES
write_enable=YES
local_umask=022
dirmessage_enable=YES
xferlog_enable=YES
connect_from_port_20=YES
xferlog_std_format=YES
listen_ipv6=NO
pam_service_name=vsftpd
userlist_enable=YES
```

## 启动服务

```bash
sudo systemctl start vsftpd
sudo systemctl enable vsftpd
```

## 配置防火墙

**UFW (Ubuntu):**
```bash
sudo ufw allow 20/tcp
sudo ufw allow 21/tcp
```

**firewalld (CentOS):**
```bash
sudo firewall-cmd --permanent --add-service=ftp
sudo firewall-cmd --reload
```

## 创建 FTP 用户（可选）

```bash
sudo useradd -m ftpuser
sudo passwd ftpuser
```

完成后，即可使用 FTP 客户端连接服务器。