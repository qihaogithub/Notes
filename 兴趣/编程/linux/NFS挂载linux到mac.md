---
创建日期: 2026-02-10T10:34:03+08:00
修改日期: 2026-02-10T10:37:51+08:00
---
针对你的具体路径和权限需求，我们需要在 Linux Mint 上配置两个不同的 NFS 导出规则，分别处理“普通用户权限”和“Root 权限”。

你的 Mac IP 是 `10.130.33.34`。

### 第一步：在 Linux Mint 上配置 `/etc/exports`

打开终端，编辑配置文件：
```bash
sudo nano /etc/exports
```

在文件末尾添加以下两行：

```text
# 第一个路径：映射为 qihao 用户 (1000:1000)
/home/qihao 10.130.33.34(rw,sync,no_subtree_check,all_squash,anonuid=1000,anongid=1000,insecure)

# 第二个路径：映射为 root 用户 (0:0)，因为 1panel 是系统管理级目录
/opt/1panel 10.130.33.34(rw,sync,no_subtree_check,all_squash,anonuid=0,anongid=0,insecure)
```

**配置解析：**
*   **`all_squash`**: 关键参数。无论你在 Mac 上是用什么用户登录，都会被强制映射为下方指定的 ID。
*   **`anonuid/anongid`**: 
    *   第一个路径设为 `1000`，这样你在 Mac 上新建的文件，在 Linux 上看所有者就是 `qihao`。
    *   第二个路径设为 `0`，因为 `/opt/1panel` 下很多文件只有 root 能写。这样映射后，你在 Mac 上对该文件夹有最高权限。
*   **`insecure`**: 必须加，否则 Mac 无法连接。

### 第二步：让配置生效

在 Linux 终端执行以下命令：
```bash
# 重新加载配置
sudo exportfs -ra

# 重启 NFS 服务确保状态刷新
sudo systemctl restart nfs-kernel-server
```

### 第三步：在 macOS 上挂载

在 Mac 上，建议将这两个目录挂载到桌面的文件夹中，方便编程。

1.  **创建挂载入口：**
```bash
mkdir -p ~/Documents/Linux_Home
mkdir -p ~/Documents/Linux_1Panel
```

2.  **手动挂载测试（请替换 `LinuxIP` 为你的 Mint 实际地址）：**
```bash
# 挂载 qihao 目录
sudo mount -t nfs -o resvport,rw,nolock 10.130.33.131:/home/qihao ~/Documents/Linux_Home

# 挂载 1panel 目录
sudo mount -t nfs -o resvport,rw,nolock 10.130.33.131:/opt/1panel ~/Documents/Linux_1Panel
```

### 第四步：设置开机自动挂载（推荐）

为了避免每次开机都要敲命令，修改 Mac 的 `/etc/fstab`：

1.  在 Mac 终端执行：`sudo vips /etc/fstab` （或者 `sudo nano /etc/fstab`）
2.  加入以下内容（注意将 `LinuxIP` 和 `你的Mac用户名` 替换掉）：
    ```text
    LinuxIP:/home/qihao /Users/你的Mac用户名/Documents/Linux_Home nfs rw,resvport,nolock,hard,bg,intr 0 0
    LinuxIP:/opt/1panel /Users/你的Mac用户名/Documents/Linux_1Panel nfs rw,resvport,nolock,hard,bg,intr 0 0
    ```

---

### 特别提醒：针对 1 panel 和编程开发

1.  **权限风险**：由于我帮你把 `/opt/1panel` 映射成了 `root`，你在 Mac 上操作该文件夹时，拥有破坏 Linux 系统文件的能力（比如误删配置文件）。**请务必谨慎操作该目录下的文件。**
2.  **IDE 配置**：
    *   如果你用 **VS Code**：直接打开挂载后的桌面文件夹即可。
    *   如果你用 **JetBrains (IntelliJ/PyCharm)**：在设置中关闭 `Safe Write` 功能（`Appearance & Behavior` -> `System Settings` -> 勾选掉 `Use "safe write"`）。因为 NFS 协议下，“安全写入”有时会导致文件清空。
3.  **Git 性能**：如果你的项目里 `.git` 文件夹非常大，Mac 的 Finder 或 IDE 扫描索引时可能会有短暂延迟。这是由于 NFS 需要频繁同步小文件元数据，属正常现象。