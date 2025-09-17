## 确保 Apache 正在运行
首先，确保您的 Apache 服务器正在运行。您可以使用以下命令来检查：
```bash
sudo systemctl status apache2
```
如果 Apache 没有运行，启动它：
```bash
sudo systemctl start apache2
```
如果没有安装：
```bash
sudo apt update
sudo apt install apache2
```
## 配置 Apache
接下来，您需要配置 Apache 服务器以服务您的网站。您可以创建一个新的 Apache 配置文件：
```bash
sudo nano /etc/apache2/sites-available/sites.conf
```
sites.conf 内容示例：[[Apache配置文件写法]]
[[配置文件示例]] 

## 修改完成后
重新加载 Apache 配置：

```
sudo systemctl reload apache2
```

重启 Node.js 服务：
```
pm2 restart server.js
```

## 错误排查
### 查看apache2 日志
```
sudo tail -f /var/log/apache2/error.log
```
### 测试前端页面
 curl -v http://10.130.35.137/temppix
### 测试图片列表接口
curl http://localhost:3003/images
### 查看文件权限
```bash
ls -l /var/www
```