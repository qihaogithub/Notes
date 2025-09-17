## 1、ssh 连接群晖
## 2、切换到 root 用户
前两步参考[[NAS]]
## 3、输入命令
```
docker exec -it [容器名称] ./alist admin
```
## 4、设置密码
若出现以下提示, 是由于密码在首次启动后会被存储为哈希值，所以无法直接查看密码，
```
root@mynas:~# docker exec -it xhofe-alist-1 ./alist admin
INFO[2024-11-10 12:16:23] reading config file: data/config.json
INFO[2024-11-10 12:16:23] load config from env with prefix: ALIST_
INFO[2024-11-10 12:16:23] init logrus...
INFO[2024-11-10 12:16:23] Admin user's username: qihao
INFO[2024-11-10 12:16:23] The password can only be output at the first startup, and then stored as a hash value, which cannot be reversed
INFO[2024-11-10 12:16:23] You can reset the password with a random string by running [alist admin random]
INFO[2024-11-10 12:16:23] You can also set a new password by running [alist admin set NEW_PASSWORD]
```
但可以通过以下两种方式来重置或设置新密码：
1. **随机生成新密码**：
   如果您忘记了密码，可以随机生成一个新的密码。使用以下命令：
```bash
docker exec -it xhofe-alist-1 ./alist admin random
```
   这将生成一个随机密码，并显示在命令行中。

2. **手动设置新密码**：
   如果您想要设置一个特定的新密码，可以使用以下命令：
```bash
docker exec -it xhofe-alist-1 ./alist admin set NEW_PASSWORD
```
   将`NEW_PASSWORD`替换为您想要设置的新密码。
