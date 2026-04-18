---
创建日期: 2026-04-08T14:17:10+08:00
修改日期: 2026-04-08T14:28:29+08:00
---

### 第一步：服务器端部署 CouchDB (Docker 方式)

在你的 Linux 服务器上创建一个目录（如 `obsidian-sync`），编写 `docker-compose.yml`：

```yaml
version: '3'
services:
  couchdb:
    image: couchdb:3.3.3
    container_name: obsidian-couchdb
    restart: always
    environment:
      - COUCHDB_USER=qihao     # 修改为你的用户名
      - COUCHDB_PASSWORD=0015   # 修改为你的强密码
    ports:
      - "5984:5984"
    volumes:
      - ./data:/opt/couchdb/data
      - ./etc:/opt/couchdb/etc/local.d
```

**运行命令：**
```bash
docker-compose up -d
```

---

### 第二步：使用 Cloudflare Tunnel 实现内网穿透

这是最关键的一步，它能给你的内网服务一个公网可访问的域名，且自带 HTTPS。

1.  **前提条件**：你需要在 Cloudflare 有一个账号，并托管了一个域名（哪怕是最便宜的 .top 域名）。
2.  **创建 Tunnel**：
    *   登录 [Cloudflare Zero Trust](https://one.dash.cloudflare.com/) 仪表板。
    *   点击 **Networks** -> **Tunnels** -> **Create a tunnel**。
    *   选择 **cloudflared**，给 Tunnel 起个名字（如 `obsidian-sync`）。
3.  **安装 cloudflared**：
    *   在面板上选择你的服务器系统（Linux/AMD 64），复制它提供的安装命令并在服务器上执行。
4.  **配置 Hostname**：
    *   在 **Public Hostname** 界面：
        *   **Subdomain**: 输入你想用的前缀（如 `sync`）。
        *   **Domain**: 选择你的域名。
        *   **Service**: 类型选 `HTTP`，URL 输入 `localhost:5984`。
5.  **保存**。现在你可以通过 `https://sync.yourdomain.com` 访问你的 CouchDB 了。

---

### 第三步：CouchDB 的初始化配置

为了让 Obsidian 插件正常工作，需要对 CouchDB 进行简单的设置：

1.  打开浏览器，访问 `http://服务器内网IP:5984/_utils/`（或者通过刚才配置好的域名访问）。
2.  使用你设置的管理员账号登录。
3.  **配置单节点**：点击左侧“扳手”图标 (Setup) -> 选择 **Configure a Single Node**，确认管理员信息并提交。
4.  **开启 CORS**：
    *   点击左侧“设置”图标 (Configuration) -> 右上角 **CORS**。
    *   选择 **Enable CORS**。
    *   **Origins** 选择 `Allow all domains (*)` 或者手动填入 `app://obsidian.md, obsidian://obsidian.md, http://localhost`。
    *   **Credentials** 勾选为 `True`。

---

### 第四步：Obsidian 插件配置

1.  在 Obsidian 中安装社区插件：**Self-hosted LiveSync**。
2.  打开插件设置，点击 **Remote Dashboard** (卫星图标)：
    *   **URI**: 输入你的公网域名 `https://sync.yourdomain.com`。
    *   **Username / Password**: 你的 CouchDB 管理员信息。
    *   **Database**: 随便起个名字（如 `obsidian-vault`）。
3.  点击 **Check configuration**。插件会提示你数据库不存在，选择 **Create it**。
4.  接着插件会提示进行初始化设置，一直点下一步即可。
5.  **同步模式**：建议选择 **LiveSync** 实现实时同步。

---

### 第五步：同步其他设备（iOS/Android/PC）

这是该方案最省心的地方：
1.  在第一台设备配置好后，在插件设置里找到 **Setup Wizard**，点击 **Copy setup URI**。
2.  设置一个加密密码，它会生成一个以 `obsidian://setuplivesync...` 开头的极长链接。
3.  将链接发给手机或其他电脑，在 Obsidian 插件里选择 **Import from setup URI**，粘贴进去即可完成全部配置。

### 为什么这个方案目前“最好”？
*   **免费且高性能**：除了域名的那点小钱，所有软件和穿透服务都是免费的。
*   **实时同步**：你在一端改一个字，另一端几乎瞬间同步，不需要像 Remotely Save 那样等待触发。
*   **移动端友好**：Cloudflare 提供的 HTTPS 解决了 iOS 必须加密连接的硬性要求。
*   **隐私安全**：数据存在你自己的服务器上，传输经过 Cloudflare 的加密通道。




```
curl -X PUT http://qihao:0015@127.0.0.1:5984/_node/nonode@nohost/_config/httpd/enable_cors -d '"true"'
curl -X PUT http://qihao:0015@127.0.0.1:5984/_node/nonode@nohost/_config/cors/origins -d '"*"'
curl -X PUT http://qihao:0015@127.0.0.1:5984/_node/nonode@nohost/_config/cors/credentials -d '"true"'
curl -X PUT http://qihao:0015@127.0.0.1:5984/_node/nonode@nohost/_config/cors/methods -d '"GET, PUT, POST, HEAD, DELETE"'
```