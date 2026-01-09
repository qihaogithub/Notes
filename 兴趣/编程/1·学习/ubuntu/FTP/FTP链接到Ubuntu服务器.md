要通过FTP连接到`/var/www/`目录并传输网站文件，你需要设置一个FTP服务器。以下是使用vsftpd（一个流行的FTP服务器软件）在Ubuntu上设置FTP服务器的步骤：
**一、安装vsftpd**
1. 更新包列表：

   ```bash
   sudo apt update
   ```

2. 安装vsftpd：

   ```bash
   sudo apt install vsftpd
   ```

**二、配置vsftpd**
1. 备份默认配置文件：

   ```bash
   sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.default
   ```

2. 编辑配置文件：

   ```bash
   sudo nano /etc/vsftpd.conf
   ```

3. 在配置文件中做出以下更改：

```
#确保FTP服务启用：
listen=YES
listen_ipv6=NO
#禁用匿名登录（提高安全性）：
anonymous_enable=NO
#启用本地用户登录：
local_enable=YES
#允许用户写入文件：
write_enable=YES
#禁用chroot限制，允许用户访问整个文件系统
chroot_local_user=NO
#设置FTP用户的根目录为 `/`，这样用户就可以访问所有目录
local_root=/

#启用被动模式（如果需要）：
pasv_enable=YES
pasv_min_port=10000
pasv_max_port=10100
```

在这个配置中，`chroot_local_user` 被设置为 `NO`，这意味着本地用户不会被限制在他们的主目录中，而是可以访问整个文件系统。`local_root` 被设置为根目录 `/`，这样用户就可以访问 `/home` 和 `/etc` 目录。

**三、重启vsftpd服务**

```bash
sudo systemctl restart vsftpd
```

**四、配置防火墙**
确保防火墙允许FTP流量（端口21）以及你为被动模式设置的端口范围（例如10000-10100）。

```bash
sudo ufw allow 21/tcp
sudo ufw allow 10000:10100/tcp
```

**五、创建FTP用户**
1. 创建一个新用户（例如`ftpuser`），该用户将用于FTP登录：

   ```bash
   sudo adduser ftpuser
   ```

2. 设置用户密码（在提示时输入）。
3. 确保用户对`/var/www/`目录有适当的权限：

   ```bash
   sudo chown -R www-data:www-data /var/www/
   sudo usermod -aG www-data ftpuser
   ```

**六、测试FTP连接**
使用FTP客户端（如FileZilla、WinSCP等）连接到服务器：
* 主机：服务器的IP地址或域名
* 用户名：你创建的FTP用户名（例如`ftpuser`）
* 密码：你设置的密码
* 端口：21（默认FTP端口）
连接成功后，你应该能够看到`/var/www/`目录的内容，并可以上传和下载文件。
**七、注意事项**
* 确保FTP用户没有不必要的权限，以保持服务器的安全性。
* 定期更新vsftpd和系统以获取最新的安全补丁。
* 考虑使用SFTP（SSH File Transfer Protocol）作为更安全的替代方案，它通过SSH加密传输数据。
通过以上步骤，你应该能够通过FTP连接到`/var/www/`目录，并方便地传输网站文件。
