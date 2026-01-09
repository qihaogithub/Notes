在宝塔面板中配置Docker的代理需要通过修改Docker的配置文件来实现，因为宝塔面板本身并没有直接提供Docker代理配置的图形化界面。以下是详细的步骤：

---

### 1. 确认Clash代理的地址和端口

在配置Docker代理之前，确保你已经知道Clash代理的地址和端口。通常，Clash的默认代理地址是：

- HTTP/HTTPS 代理：`http://127.0.0.1:7899
    
- SOCKS5 代理：`socks5://127.0.0.1:7898

你可以通过Clash的配置文件或日志确认这些信息。

---

### 2. 配置Docker的代理

Docker的代理配置是通过修改Docker服务的配置文件来实现的。以下是具体步骤：

#### 步骤 1：创建或编辑Docker的代理配置文件

1. 使用以下命令创建或编辑Docker的代理配置文件：

```bash
   sudo mkdir -p /etc/systemd/system/docker.service.d
   sudo nano /etc/systemd/system/docker.service.d/http-proxy.conf
```

2. 在文件中添加以下内容（根据你的Clash代理配置修改`HTTP_PROXY`和`HTTPS_PROXY`）：

```ini
   [Service]
   Environment="HTTP_PROXY=http://127.0.0.1:7899"
   Environment="HTTPS_PROXY=http://127.0.0.1:7899"
   Environment="NO_PROXY=localhost,127.0.0.1,.docker.io,.docker.com"
```

- `HTTP_PROXY` 和 `HTTPS_PROXY`：设置为Clash的HTTP/HTTPS代理地址。
    
- `NO_PROXY`：设置不需要代理的地址或域名（如本地地址和Docker官方镜像地址）。

1. 保存并退出编辑器（按 `Ctrl + X`，然后按 `Y` 确认保存）。

---

#### 步骤 2：重新加载Docker配置并重启服务

4. 重新加载Docker的systemd配置：

```bash
   sudo systemctl daemon-reload
```

5. 重启Docker服务以应用代理配置：

```bash
   sudo systemctl restart docker
```

---

#### 步骤 3：验证代理配置是否生效

查看Docker服务的环境变量，确认代理配置已加载： 

```bash 
sudo systemctl show --property=Environment docker
```

输出应该包含你设置的代理环境变量，例如：

```bash 
qihao@qihao:~$ sudo systemctl show --property=Environment docker
Environment=HTTP_PROXY=http://127.0.0.1:7899 HTTPS_PROXY=http://127.0.0.1:7899 NO_PROXY=localhost,127.0.0.1,.docker.io,.docker.com
```

2. 尝试拉取一个镜像，测试代理是否生效：

```bash
   docker pull ubuntu
```

如果代理配置正确，Docker应该能够通过代理拉取镜像。

---

### 3. 配置宝塔面板的Docker管理插件

宝塔面板的Docker管理插件本身并不直接支持代理配置，因此你需要通过命令行配置Docker的代理（如上所述）。配置完成后，宝塔面板的Docker管理插件也会使用这些代理设置。

---

### 4. 其他注意事项

#### Clash的代理模式
确保Clash的代理模式是全局模式（Global）或规则模式（Rule），并且规则中包含Docker相关的域名（如 `docker.io`、`docker.com` 等）。
#### DNS问题
如果拉取镜像时仍然失败，可能是DNS解析问题。可以尝试修改Docker的DNS配置。

1. 创建或编辑 `/etc/docker/daemon.json` 文件：

```bash
sudo nano /etc/docker/daemon.json
```

2. 添加以下内容：

```json
{
"dns": ["8.8.8.8", "8.8.4.4"]
}
```

添加后的示例：

```
{
  "registry-mirrors": [
    "https://docker.1ms.run"
  ],
    "dns": ["8.8.8.8", "8.8.4.4"]
}
```

3. 保存并退出编辑器。
4. 重启 Docker 服务：

```bash
sudo systemctl restart docker
```

#### 防火墙问题

确保防火墙没有阻止Docker的网络流量。可以暂时关闭防火墙进行测试：

```bash
  sudo ufw disable
```

**使用 `curl` 测试网络连接**：
在终端尝试使用 `curl` 命令直接访问 `https://registry-1.docker.io/v2/`，看看是否可以正常访问。

```bash
curl https://registry-1.docker.io/v2/
```

如果 `curl` 也失败，则说明是网络或代理的问题，不是 Docker 的问题。
