在 Windows 系统上安装 MySQL 数据库服务器，可以按照以下步骤进行：
### 1. 下载 MySQL 安装包
1. 访问 MySQL 官方网站的下载页面：[https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
2. 选择适合您系统的 MySQL 版本（通常选择“MySQL Community Server”）
3. 选择 Windows 平台，并下载对应的安装包（例如：MySQL Installer for Windows）
### 2. 安装 MySQL
1. 双击下载的安装包开始安装过程。
2. 选择“Custom”自定义安装，以便可以选择安装路径和其他选项。
3. 根据需要选择要安装的产品和功能。通常，您至少需要安装“MySQL Server”和“MySQL Workbench”（图形界面管理工具）。
4. 点击“Execute”开始安装过程。
5. 安装过程中，安装向导会要求您设置 root 用户的密码，请牢记这个密码，因为它将被用于管理 MySQL 服务器。
### 3. 配置 MySQL
1. 安装完成后，需要配置 MySQL 服务。
2. 可以通过“MySQL Installer”中的“MySQL Server”实例的“Configure Instance”来配置。
3. 在配置过程中，可以选择“Detailed Configuration”进行详细配置，也可以选择“Standard Configuration”进行标准配置。
4. 根据提示完成配置，包括但不限于：
   - 设置服务器类型（Developer Machine、Server Machine、Dedicated MySQL Server Machine）
   - 选择数据库类型（Multifunctional Database、Transactional Database Only、Non-Transactional Database Only）
   - 选择网络选项（启用或禁用 TCP/IP 网络，配置端口等）
   - 设置字符集（推荐使用 utf 8 或 utf 8 mb 4）
   - 设置 root 密码（如果之前未设置）
### 4. 启动 MySQL 服务
1. 在 Windows 服务管理器中，找到 MySQL 服务。
2. 右键点击服务，选择“启动”来启动 MySQL 服务。
### 5. 验证安装
1. 打开命令提示符或 PowerShell。
2. 输入以下命令来连接 MySQL 服务器：
   ```
   mysql -u root -p
   ```
3. 当提示输入密码时，输入您在安装过程中设置的 root 密码。
4. 如果成功连接到 MySQL 服务器，将显示 MySQL 命令提示符，表明安装成功。
请注意，安装和配置过程中可能会根据不同的 MySQL 版本和 Windows 版本有所不同。如果在安装过程中遇到任何问题，请参考 MySQL 官方文档或搜索相关错误信息。
