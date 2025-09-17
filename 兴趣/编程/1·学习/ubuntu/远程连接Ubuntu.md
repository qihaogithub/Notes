要在局域网中远程控制一台安装了Ubuntu Desktop的电脑，您可以使用多种方法。以下是一些常见的方法：
### 1. VNC (Virtual Network Computing)
VNC是一种广泛使用的远程桌面协议。以下是安装和配置VNC服务器的步骤：
#### 在Ubuntu上安装VNC服务器：
1. 打开终端。
2. 安装VNC服务器软件包
   ```bash
   sudo apt-get update
   sudo apt install tightvncserver
   ```
3. 启动VNC服务器并设置密码：
   ```bash
  vncserver :1
   ```
   这将提示您输入并确认密码。
4. 当您启动VNC服务器时，它会创建一个以`:1`结尾的会话。例如，`:1`表示第一个VNC会话。
#### 在Mac上使用VNC客户端连接
1. Mac OS X自带了VNC客户端，名为“屏幕共享”。您可以在“应用程序”>“实用工具”中找到它。
2. 打开“屏幕共享”，然后点击“+”按钮来添加一个新的VNC服务器。
3. 输入Ubuntu电脑的IP地址，后跟`:1`（如果您使用的是第一个VNC会话）。例如：`192.168.1.100:1`。
4. 点击“连接”，系统将提示您输入密码。
5. 输入密码后，您应该能够看到Ubuntu桌面的远程控制界面。
6. 
### 2. XRDP
XRDP是另一个远程桌面协议，它允许您使用Windows的远程桌面客户端连接到Ubuntu桌面。
#### 在Ubuntu上安装XRDP：
1. 打开终端。
2. 安装XRDP：
   ```bash
   sudo apt update
   sudo apt install xrdp
   ```
3. 启动XRDP服务：
   ```bash
   sudo systemctl start xrdp
   ```
   如果您希望XRDP随系统启动，可以使用以下命令：
   ```bash
   sudo systemctl enable xrdp
   ```
#### 在另一台电脑上连接XRDP服务器：
1. 在Windows上，打开“远程桌面连接”应用程序。
2. 输入Ubuntu电脑的IP地址。
3. 如果一切正常，您应该会被提示输入Ubuntu的用户名和密码。
### 注意事项：
- 确保两台电脑在同一个局域网内，并且可以相互通信。
- 您需要知道Ubuntu电脑的IP地址。您可以在Ubuntu上使用`ip addr show`命令来查找。
- 如果您的网络设置了防火墙，确保允许远程桌面协议（VNC或XRDP）所需的端口。
使用上述任何一种方法，您应该能够从局域网中的另一台电脑远程控制Ubuntu桌面。
