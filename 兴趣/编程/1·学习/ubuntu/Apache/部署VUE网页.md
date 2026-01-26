在 Ubuntu 上部署 Vue. Js 应用程序到 Apache 服务器，您可以按照以下步骤进行：
### 1. 确保 Apache 正在运行
首先，确保您的 Apache 服务器正在运行。您可以使用以下命令来检查：
```bash
sudo systemctl status apache2
```
如果 Apache 没有运行，启动它：
```bash
sudo systemctl start apache2
```
### 2. 构建 Vue. Js 项目
在部署之前，您需要构建您的 Vue. Js 项目。如果您还没有进行这一步，请切换到您的 Vue. Js 项目目录，并运行以下命令：
```bash
npm run build
```
这将创建一个 `dist` 文件夹，其中包含了可以部署到生产环境的文件。
### 2. 配置 Ubuntu 服务器

#### 2.1 创建一个用于存放网页的目录
登录到您的 Ubuntu 服务器，并创建一个目录来存放您的网页文件：
```
sudo mkdir -p /var/www/uipreview
sudo chown -R $USER:$USER /var/www/uipreview
```
#### 2.2 配置 Apache
接下来，您需要配置 Apache 服务器以服务您的网站。您可以创建一个新的 Apache 配置文件：
```bash
sudo nano /etc/apache2/sites-available/uipreview.conf
```
在打开的文件中，添加以下内容：
```apache
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName qihao-Standard-PC-i440FX-PIIX-1996   
    ServerAlias 10.130.35.137   
    DocumentRoot /var/www/uipreview/dist
    <Directory /var/www/uipreview/dist>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
        Require all granted
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>      
```
请确保将 `ServerName` 和 `DocumentRoot` 路径更改为您的实际域名和 Vue. Js 项目构建输出目录。
#### 2.3启用新配置和重载 Apache
启用刚才创建的配置文件，并确保 Apache 重新加载新的配置：
```bash
sudo a2ensite uipreview.conf
sudo a2enmod rewrite
sudo systemctl reload apache2
```

### 3. 部署 Vue 项目
现在，您需要将 Vue 项目构建的 `dist` 文件夹内容上传到 Ubuntu 服务器的网页目录中。您可以使用 `scp` 或 `rsync` 命令来传输文件：
```bash
scp -r path/to/your/vue-project/dist/* username@your-ubuntu-server:/var/www/your-website
```
或者[[使用 rsync 传输文件]]
### 4. 测试网站
最后，您需要在局域网中的另一台设备上测试网站是否可以访问。在浏览器中输入您的 Ubuntu 服务器的 IP 地址或域名（例如 `http://your-ubuntu-server-ip` 或 `http://your-website.local`），您应该能够看到您的 Vue 网站正在运行。
如果网站无法访问，请检查 Apache 的错误日志以获取更多信息：
```bash
sudo cat /var/log/apache2/error.log
```
根据日志中的信息调整配置或文件权限，直到网站可以正常运行。
