Apache HTTP服务器是一个开源的网页服务器软件，它可以通过配置文件来设定服务器的行为。在Linux系统中，Apache的配置文件通常位于 `/etc/httpd/`（CentOS/RHEL）或 `/etc/apache2/`（Debian/Ubuntu）目录下。以下是一些基本的配置文件写法：

## 配置文件位置 **：
   - 对于CentOS/RHEL系统，主配置文件通常是`/etc/httpd/httpd.conf`。
   - 对于Debian/Ubuntu系统，主配置文件通常是`/etc/apache2/apache2.conf`。
## 编辑配置文件
**使用文本编辑器编辑文件**：你可以使用 `nano` 或 `vim` 等命令行编辑器来编辑配置文件。
[[Linux中nano的使用教程]]

```
nano /etc/apache2/sites-available/site1.conf
```

或者

```
vim /etc/apache2/sites-available/site1.conf
```

[[配置文件示例]]

## 权限和重启：
   - 修改配置文件后，需要检查语法是否正确：

     ```bash
     sudo apachectl configtest
     ```

   - 如果没有错误，重启Apache服务以应用更改：

     ```bash
     sudo systemctl restart httpd  # CentOS/RHEL
     sudo systemctl restart apache2  # Debian/Ubuntu
     ```

请注意，具体的配置可能会根据你的具体需求和Apache的版本有所不同。在进行任何更改之前，建议备份原始的配置文件。


```
sudo a2dissite 000-default.conf
```