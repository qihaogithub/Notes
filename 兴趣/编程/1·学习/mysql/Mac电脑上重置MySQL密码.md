在macOS上重置MySQL密码的步骤如下：

1. **停止MySQL服务**：
   打开终端，输入以下命令来停止MySQL服务：
   ```
   sudo /usr/local/mysql/support-files/mysql.server stop
   ```
   你也可以在系统偏好设置中手动关闭MySQL服务。

2. **以跳过授权认证模式登录MySQL**：
   在终端中输入以下命令以跳过授权认证模式登录MySQL：
   ```
   sudo /usr/local/mysql/bin/mysqld_safe --skip-grant-tables &
   ```
   这将启动MySQL服务并跳过权限表认证。

3. **使用ALTER USER语句重置密码**：
   在另一个终端窗口中，输入以下命令来重置MySQL root密码：
   ```
   /usr/local/mysql/bin/mysql -u root
   ```
   由于跳过了授权认证，你可以直接按回车键进入MySQL shell。

1. **在MySQL shell中输入以下命令来重置MySQL root密码**：
```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'qh9189';
```
由于权限认证没有重新加载，执行修改密码语句后会报错。
![](https://i-blog.csdnimg.cn/blog_migrate/239e78b9dca76fe645951b9d345a07c9.png)
输入命令 flush privileges；，重新加载权限。
修改root账户密码的命令
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202411111720789.png)

**退出MySQL shell并重启MySQL服务**：
在MySQL shell中输入以下命令来退出MySQL shell：
```
exit
```
   然后，输入以下命令来重启MySQL服务，输入电脑登录密码
```
sudo /usr/local/mysql/support-files/mysql.server start
```
通过这些步骤，你可以在macOS上成功地重置MySQL root密码。记得在MySQL里面使用强密码来保护您的数据库。
