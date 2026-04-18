---
创建日期: 2026-02-10T10:34:03+08:00
修改日期: 2026-02-10T10:55:02+08:00
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

# 允许来自 Mac IP 的所有访问（最直接有效） 
sudo ufw allow from 10.130.33.34 

# 刷新防火墙 
sudo ufw reload

# 验证命令：看到输出路径即代表 Linux 准备好了 
showmount -e localhost
```

### 第三步：在 macOS 上挂载

**注意：** 如果你的 Mac 开启了 **iCloud 云端同步文档**，挂载在 ~/Documents 可能会触发同步冲突或图标显示异常。  
建议：如果遇到奇怪的权限问题，请改到 ~/nfs_shares/Linux_Home 这种不被 iCloud 监控的目录。

1.  **创建挂载入口：**
```bash
mkdir -p ~/Documents/Linux_Home
mkdir -p ~/Documents/Linux_1Panel
```

2.  **手动挂载测试（使用你测试成功的命令）：**
```bash
# 挂载 qihao 目录
sudo mount -t nfs -o resvport,rw,nolock,vers=3,tcp 10.130.33.131:/home/qihao ~/Documents/Linux_Home

# 挂载 1panel 目录
sudo mount -t nfs -o resvport,rw,nolock,vers=3,tcp 10.130.33.131:/opt/1panel ~/Documents/Linux_1Panel
```

### 第四步：设置开机自动挂载

**关键修改点：** Mac 修改 fstab 的专用命令是 vifs 不是 vips，而且由于 macOS 的安全机制，目录路径建议加引号或确保无空格。

1. 在 Mac 终端执行：

```codeBash
sudo vifs
```

vifs 是 macOS 官方工具，它会调用 vim 编辑器并检查语法。按 i 进入编辑模式，按 Esc 后输入 :wq 保存退出。

1. 加入以下内容（**注意：Mac 的 fstab 不支持带空格的路径，也不支持 ~ 缩写，必须写全路径**）：

```codeText
10.130.33.131:/home/qihao /Users/qh2/Documents/Linux_Home nfs rw,resvport,nolock,vers=3,tcp,hard,bg,intr 0 0
10.130.33.131:/opt/1panel /Users/qh2/Documents/Linux_1Panel nfs rw,resvport,nolock,vers=3,tcp,hard,bg,intr 0 0
```

- **参数补全说明**：
- vers=3,tcp: 确保自动挂载时也使用你测试成功的协议。
- bg: 背景挂载。如果开机时 Linux 没开，Mac 会在后台继续尝试，不会卡在开机画面。
- hard,intr: 确保如果网络断开，程序在尝试读写时可以被“中断”，不会导致整个 Finder 永久死掉。


---

### 特别提醒

1. **权限风险**：/opt/1panel 映射为 root 后具有极高危险性。
2. **IDE 配置 (JetBrains)**：关闭 Safe Write 极其重要，否则保存文件时可能会导致文件清空或 Permission Denied。
3. **macOS 权限弹窗**：当你第一次通过 VS Code 访问挂载目录时，Mac 可能会弹出“终端想要访问文稿文件夹”，务必点**允许**。
4. **软链接限制**：如果在 Linux 目录下有指向 /home 之外的软链接，NFS 默认可能无法跟随（Follow symlinks），这在开发时需留意。