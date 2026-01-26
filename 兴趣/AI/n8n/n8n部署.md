

# N 8 n 本地安装与配置指南（Linux & macOS）

## 简介

本指南详细介绍如何在 Linux (Ubuntu) 和 macOS 系统上将 n 8 n 安装到指定目录，并配置为后台运行的服务。这种安装方式提供了更高的隔离性、可维护性和可移植性。

## 1. 准备工作

### Linux (Ubuntu)

| 要求 | 检查命令 | 安装命令 |
|------|---------|---------|
| Node. Js 和 npm | `node -v`<br>`npm -v` | `sudo apt update`<br>`sudo apt install nodejs npm -y` |

### MacOS

| 要求             | 检查命令                  | 安装命令                                                                                              |
| -------------- | --------------------- | ------------------------------------------------------------------------------------------------- |
| Homebrew       | `brew -v`             | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| Node. Js 和 npm | `node -v`<br>`npm -v` | `brew install node`                                                                               |

## 2. 创建项目目录

### Linux (Ubuntu)

```bash
# 创建目标目录
sudo mkdir -p /www/wwwroot/n8n

# 设置目录权限
sudo chown -R $USER:$USER /www/wwwroot/n8n

# 进入目录
cd /www/wwwroot/n8n

# 初始化 npm 项目
npm init -y
```

### MacOS

```bash
# 创建目标目录（在用户目录下）
mkdir -p ~/n8n

# 进入目录
cd ~/n8n

# 初始化 npm 项目
npm init -y
```

## 3. 安装 n 8 n

### Linux (Ubuntu)

```bash
# 修复缓存目录权限
sudo chown -R $USER:$USER /www/server/nodejs/cache

# 安装 n8n
npm install n8n
```

### MacOS

```bash
# 安装 n8n
npm install n8n
```

## 4. 配置启动脚本

### Linux 和 macOS

编辑 `package.json` 文件，添加启动脚本：

```json
{
  "scripts": {
    "start": "node ./node_modules/n8n/bin/n8n"
  }
}
```

现在可以通过 `npm start` 命令启动 n 8 n。

## 5. 设置用户数据目录

### Linux (Ubuntu)

为了避免默认路径冲突，将 n 8 n 的用户数据目录设置为 `/www/wwwroot/n8n/data`。

#### 方法 1：临时设置（仅当前会话有效）

```bash
N8N_USER_FOLDER=/www/wwwroot/n8n/data npm start
```

#### 方法 2：永久设置

```bash
# 创建 .env 文件
echo 'N8N_USER_FOLDER=/www/wwwroot/n8n/data' > .env

# 安装 dotenv 包
npm install dotenv

# 修改 package.json 的启动脚本
sed -i 's/"start": "node \.\/node_modules\/n8n\/bin\/n8n"/"start": "node -r dotenv\/config .\/node_modules\/n8n\/bin\/n8n"/' package.json
```

### MacOS

为了避免默认路径冲突，将 n 8 n 的用户数据目录设置为 `~/n8n/data`。

#### 方法 1：临时设置（仅当前会话有效）

```bash
N8N_USER_FOLDER=~/n8n/data npm start
```

#### 方法 2：永久设置

```bash
# 创建 .env 文件
echo "N8N_USER_FOLDER=~/n8n/data" > .env

# 安装 dotenv 包
npm install dotenv

# 修改 package.json 的启动脚本
sed -i '' 's/"start": "node \.\/node_modules\/n8n\/bin\/n8n"/"start": "node -r dotenv\/config .\/node_modules\/n8n\/bin\/n8n"/' package.json
```

## 6. 服务管理

### Linux (使用 PM 2)

```bash
# 安装 PM2
sudo npm install -g pm2

# 启动服务
pm2 start "npm start" --name n8n

# 设置开机自启
pm2 save
pm2 startup

# 查看 PM2 状态
pm2 list

# 查看日志
pm2 logs n8n
```

### MacOS (使用 launchd)

```bash
# 创建 plist 文件
cat > ~/Library/LaunchAgents/com.n8n.plist << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.n8n</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/npm</string>
        <string>start</string>
    </array>
    <key>WorkingDirectory</key>
    <string>$HOME/n8n</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>$HOME/n8n/logs/n8n.log</string>
    <key>StandardErrorPath</key>
    <string>$HOME/n8n/logs/n8n-error.log</string>
</dict>
</plist>
EOF

# 创建日志目录
mkdir -p ~/n8n/logs

# 加载服务
launchctl load ~/Library/LaunchAgents/com.n8n.plist

# 启动服务
launchctl start com.n8n

# 查看服务状态
launchctl list | grep n8n

# 查看日志
tail -f ~/n8n/logs/n8n.log
```

## 7. 配置防火墙

### Linux (Ubuntu)

N 8 n 默认监听端口 5678，如需通过公网访问，请确保防火墙允许该端口：

```bash
sudo ufw allow 5678
```

### MacOS

MacOS 默认没有启用防火墙，如需启用：

```bash
# 启用防火墙
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on

# 允许端口 5678
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --addport 5678
```

## 8. 访问 n 8 n

N 8 n 启动后，可通过以下地址访问：
- 本地访问：`http://localhost:5678`
- 外网访问：`http://<服务器IP>:5678`

## 9. 备份与迁移

### Linux (Ubuntu)

#### 备份项目

```bash
tar -czvf n8n_backup.tar.gz /www/wwwroot/n8n
```

#### 迁移到新服务器

```bash
# 解压备份文件
tar -xzvf n8n_backup.tar.gz -C /www/wwwroot/

# 进入目录并安装依赖
cd /www/wwwroot/n8n
npm install

# 重新启动服务
pm2 start "npm start" --name n8n
```

### MacOS

#### 备份项目

```bash
tar -czvf n8n_backup.tar.gz ~/n8n
```

#### 迁移到新服务器

```bash
# 解压备份文件
tar -xzvf n8n_backup.tar.gz -C ~/

# 进入目录并安装依赖
cd ~/n8n
npm install

# 重新启动服务
launchctl load ~/Library/LaunchAgents/com.n8n.plist
launchctl start com.n8n
```

## 10. 配置 Webhook URL（反向代理场景）

### Linux 和 macOS

如果 n 8 n 运行在反向代理后面（如 Nginx），需要设置 WEBHOOK_URL：

```bash
# 临时设置
export WEBHOOK_URL=https://你的域名.com/

# 永久设置（添加到 .env 文件）
echo 'WEBHOOK_URL=https://你的域名.com/' >> .env

# 重启服务使配置生效
# Linux
pm2 restart n8n

# macOS
launchctl stop com.n8n
launchctl start com.n8n
```

## 11. 升级 n 8 n

### Linux 和 macOS

```bash
# 进入项目目录
# Linux: cd /www/wwwroot/n8n
# macOS: cd ~/n8n

# 更新 n8n
npm update n8n

# 重启服务
# Linux: pm2 restart n8n
# macOS: launchctl stop com.n8n && launchctl start com.n8n

# 验证版本
npm list n8n
```

## 12. 汉化

### Linux 和 macOS

1. [下载中文语言包](https://github.com/other-blowsnow/n8n-i18n-chinese/releases)，注意版本需要和 n 8 n 相同
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20250819101755147.png)

2. 找到路径：
   - Linux: `/www/wwwroot/n8n/node_modules/n8n-editor-ui/dist`
   - macOS: `~/n8n/node_modules/n8n-editor-ui/dist`
4. 下载对应版本的 editor-ui. Tar. Gz 文件
5. 解压到 dist 目录下替换
6. 设置环境变量 `N8N_DEFAULT_LOCALE=zh-CN`：

   ```bash
   echo 'N8N_DEFAULT_LOCALE=zh-CN' >> .env
   ```

7. 重启 n 8 n 服务：
   - Linux: `pm2 restart n8n`
   - macOS: `launchctl stop com.n8n && launchctl start com.n8n`

## 常用命令参考

| 操作          | Linux (PM 2)                            | macOS (launchd)                                     |              |
| ----------- | --------------------------------------- | --------------------------------------------------- | ------------ |
| 启动 n 8 n    | `pm2 start n8n`                         | `launchctl start com.n8n`                           |              |
| 停止 n 8 n    | `pm2 stop n8n`                          | `launchctl stop com.n8n`                            |              |
| 重启 n 8 n    | `pm2 restart n8n`                       | `launchctl stop com.n8n && launchctl start com.n8n` |              |
| 查看 n 8 n 状态 | `pm2 list`                              | `launchctl list                                     | grep n 8 n ` |
| 查看 n 8 n 日志 | `pm2 logs n8n`                          | `tail -f ~/n8n/logs/n8n.log`                        |              |
| 更新 n 8 n    | `cd /www/wwwroot/n8n && npm update n8n` | `cd ~/n8n && npm update n8n`                        |              |