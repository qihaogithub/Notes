以下是一个 **仅包含本地安装** 的详细教程，指导您如何在 Ubuntu 系统上将 n 8 n 安装到特定目录（如 `/www/wwwroot/n8n`），并配置为后台运行的服务。本教程适用于希望实现更高隔离性、可维护性和可移植性的用户。

---

## **本地安装 n 8 n 详细教程**

### **1. 准备工作**
确保您的系统满足以下条件：
- 已安装 Node. Js 和 npm（建议使用 LTS 版本）。
- 目标目录 `/www/wwwroot/n8n` 存在，并具有适当的权限。

#### 检查 Node. Js 和 npm 是否已安装：
```bash
node -v
npm -v
```

如果未安装，请运行以下命令安装 Node. Js 和 npm：

```bash
# 更新包管理器
sudo apt update

# 安装 Node.js 和 npm
sudo apt install nodejs npm -y

# 验证安装
node -v
npm -v
```

---

### **2. 创建项目目录**
创建目标目录 `/www/wwwroot/n8n` 并进入该目录：

```bash
mkdir -p /www/wwwroot/n8n
cd /www/wwwroot/n8n
```

初始化 npm 项目：

```bash
npm init -y
```

这将在当前目录生成一个 `package.json` 文件，用于记录项目的依赖和脚本。

---

### **3. 本地安装 n 8 n**
修复缓存目录权限
```
sudo chown -R $USER:$USER /www/server/nodejs/cache
```
在项目目录中安装 n 8 n：

```bash
npm install n8n
```

安装完成后，n 8 n 将位于 `node_modules/n8n` 中。

---

### **4. 配置启动脚本**
为了简化启动命令，在 `package.json` 中添加一个启动脚本：

```json
{
  "scripts": {
    "start": "node ./node_modules/n8n/bin/n8n"
  }
}
```

现在可以通过以下命令启动 n 8 n：

```bash
npm start
```

---

### **5. 设置用户数据目录**
为了避免默认路径冲突，可以指定 n 8 n 的用户数据目录为 `/www/wwwroot/n8n/data`。

#### 方法 1：临时设置环境变量
每次启动时手动设置环境变量：

```bash
N8N_USER_FOLDER=/www/wwwroot/n8n/data npm start
```

#### 方法 2：永久设置环境变量
在项目根目录下创建一个 `.env` 文件，并定义环境变量：

```bash
echo 'N8N_USER_FOLDER=/www/wwwroot/n8n/data' > .env
```

然后安装 `dotenv` 包以加载 `.env` 文件中的环境变量：

```bash
npm install dotenv
```

修改 `package.json` 的启动脚本：

```json
{
  "scripts": {
    "start": "node -r dotenv/config ./node_modules/n8n/bin/n8n"
  }
}
```

现在运行 `npm start` 时会自动加载 `.env` 文件中的环境变量。

---

### **6. 使用 PM 2 管理服务**
为了确保 n 8 n 在后台持续运行，可以使用 PM 2。

#### 安装 PM 2：
```bash
sudo npm install -g pm2
```

#### 启动服务：
```bash
pm2 start "npm start" --name n8n
```

#### 设置开机自启：
```bash
pm2 save
pm2 startup
```

#### 查看 PM 2 状态：
```bash
pm2 list
```

PM 2 的日志文件可以通过以下命令查看：

```bash
pm2 logs n8n
```

---

### **7. 配置防火墙**
n 8 n 默认监听端口 `5678`。如果需要通过公网访问，请确保防火墙允许该端口：

```bash
sudo ufw allow 5678
```

---

### **8. 访问 n 8 n**
n 8 n 启动后，默认监听 `http://localhost:5678`。如果服务器有外网 IP，可以通过浏览器访问：

```
http://<服务器IP>:5678
```

---

### **9. 备份与迁移**
由于 n 8 n 是本地安装，整个项目目录（包括 `node_modules` 和数据目录）都可以轻松打包并迁移到其他机器。

#### 打包项目：
```bash
tar -czvf n8n_backup.tar.gz /www/wwwroot/n8n
```

#### 迁移到新服务器：
将备份文件上传到新服务器，解压后重新安装依赖：

```bash
tar -xzvf n8n_backup.tar.gz -C /www/wwwroot/
cd /www/wwwroot/n8n
npm install
```

然后按照上述步骤重新启动 n 8 n。

---

### **10. 总结**
通过本地安装的方式，您可以实现以下目标：
1. **依赖隔离**：每个项目独立管理 n 8 n 的版本。
2. **可维护性**：通过 `package.json` 和 `.env` 文件，方便管理和配置。
3. **可移植性**：整个项目目录可以轻松打包并迁移到其他机器。

如果您对某个步骤有疑问，或者需要进一步的帮助，请随时补充说明！