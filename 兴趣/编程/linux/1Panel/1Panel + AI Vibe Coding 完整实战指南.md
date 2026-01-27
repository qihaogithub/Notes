---
创建日期: 2026-01-27T12:19:02+08:00
修改日期: 2026-01-27T12:26:29+08:00
---
这份指南专为您在 **Linux Mint** 上结合 **Claude Code** (AI) 和 **1Panel** (可视化管理) 而设计。

我们要达成的是 **"Vibe Coding" 的终极形态**：

- **AI 负责**：写代码、跑测试、修 Bug。
    
- **1Panel 负责**：管环境、管数据库、管 SSL、管备份。
    
- **你负责**：指挥和确认。
    


# 🚀 1Panel + AI Vibe Coding 完整实战指南

### 核心哲学：内外分治 (The Separation)

- **宿主机 (Your Mint)**：这是 **代码** 的家。AI 在这里读写文件，你在这里提交 Git。
    
- **容器 (1Panel Docker)**：这是 **运行** 的家。代码被“投影”到这里运行。
    

---

### 第一阶段：基建初始化 (一次性设置)

在开始写代码前，我们要打通“宿主机”和“容器”的任督二脉。

#### 1. 规划你的“基地”

不要把代码乱放。在你的 Mint 主目录下建立统一的工作区：

Bash

```
mkdir -p ~/Projects/vibe-workspace
cd ~/Projects/vibe-workspace
```

#### 2. 在 1 Panel 中创建"开发容器"

不要直接用 AI 手搓 Docker 命令，去 1 Panel 点鼠标，这更稳。

##### 📌 开发容器是什么？为什么需要它？

**开发容器**是一个隔离的运行环境，用于执行和测试你的代码，同时通过目录挂载与宿主机保持实时同步。

**核心作用：**

- **运行环境隔离**：提供纯净的 Node. Js、Python 等运行环境，不影响宿主机系统，避免依赖冲突和版本问题。
    
- **代码同步开发**：通过挂载宿主机目录（如 `~/Projects/vibe-workspace/my-app`），容器内可以直接读写代码。你在宿主机用 Claude Code 写代码，容器内立即生效。
    
- **网络互联**：容器加入 `1panel-network` 后，可直接访问 1 Panel 创建的数据库（如通过 `mysql` 主机名连接）。
    
- **端口映射**：将容器内的服务端口（如 `3000`）映射到宿主机，让你在浏览器通过 `localhost:3000` 直接访问应用。
    
- **依赖管理**：在容器内执行 `npm install` 或 `pip install`，确保依赖与运行环境匹配，避免因宿主机与容器架构不同导致的兼容性问题。

> **一句话总结**：你在宿主机写代码（Claude 负责），容器负责跑代码（1 Panel 管理），两者通过挂载目录实时同步。

##### 🛠️ 具体创建步骤

- **进入 1 Panel** -> **容器** -> **创建容器**。
    
- **选择镜像**：例如 `node:18-alpine` 或 `python:3.10`。
    
- **关键设置 (必做)**：
    
    - **名称**：例如 `dev-project-alpha`。
        
    - **端口映射**：`3000:3000` (把容器里的 web 端口暴露出来，方便你在浏览器看)。
        
    - **挂载 (Volume) - 最重要的一步！**
        
        - **本机路径**：`/home/qihao/Projects/vibe-workspace/my-app` (手动填入你刚才建的目录)。
            
        - **容器路径**：`app` (这是容器里的工作目录)。
            
    - **网络**：选择 `1panel-network` (这样它能直接连上 1 Panel 创建的数据库)。
        
    - **命令 (Command)**：如果是 Node，填 `npm run dev`；如果是 Python，填 `python app.py` (这一步可以先填 `tail -f /dev/null` 让容器空转，等代码写好了再改)。
        


### 第二阶段：AI 开发流 (日常循环)

现在环境搭好了，开始 Vibe Coding。

#### 1. 启动 Claude Code

打开 Mint 终端，进入你的代码目录：

Bash

```
cd ~/Projects/vibe-workspace/my-app
claude
```

<!-- ... existing content ... -->
#### 2. 注入上下文 (Context Injection)

第一次对话时，把这段话发给 Claude，让它知道自己在哪里：

> 你现在是一个 **Vibe Coding 助手**，正在协助我进行开发。请严格遵守以下规则：
> 
> **【环境信息】**
> - 我的工作目录：`/home/qihao/Projects/vibe-workspace/my-app` (宿主机)
> - 运行环境：Docker 容器 `dev-project-alpha`，容器内工作目录为 `/app`
> - 管理工具：1 Panel (用于容器、数据库、反向代理管理)
> 
> **【核心原则 - 必须遵守】**
> 1. **文件操作只能在宿主机进行**：所有创建、修改、删除文件的操作都在 `/home/qihao/Projects/vibe-workspace/my-app` 执行
> 2. **不要在容器内安装系统包**：禁止运行 `apt-get`、`yum` 等系统包管理命令
> 3. **依赖安装优先在宿主机执行**：运行 `npm install` 或 `pip install` 时，优先在宿主机终端执行（因为目录已挂载）
> 4. **如需在容器内执行命令**：使用完整格式 `docker exec -it dev-project-alpha <命令>`
> 5. **数据库连接配置**：
>    - Host: `mysql` (容器名，因为同在 1 panel-network)
>    - Port: `3306`
>    - 用户名: `root`
>    - 密码: 从 `.env` 文件读取
> 
> **【禁止事项】**
> - ❌ 不要修改 `/opt/1panel` 目录下的任何文件
> - ❌ 不要尝试通过 SSH 连接到其他服务器
> - ❌ 不要直接修改 Nginx 配置文件（如有需要，请告知我在 1 Panel 面板中操作）
> 

#### 3. 数据库连接 (The Connection)

在 1Panel 里创建一个数据库，获取密码。

让 Claude 创建一个 `.env` 文件：

代码段

```
DB_HOST=mysql        # 在容器内部，直接用容器名连接
DB_PORT=3306
DB_USER=root
DB_PASS=你的1Panel数据库密码
```

#### 4. 解决“权限打架” (The Fix)

Claude 生成文件后，Docker 容器可能因为权限问题读不到，或者 Docker 生成的文件（如 `__pycache__` 或 `node_modules`）你在 Mint 下删不掉。

**让 Claude 写一个 `fix_perm.sh` 脚本放在根目录：**

Bash

```
#!/bin/bash
# 强行把所有权拿回给当前用户
sudo chown -R $USER:$USER .
```

_每当遇到 Permission Denied，运行一下这个脚本。_

---

### 第三阶段：运维与调试

#### 1. 安装依赖

不要让 Claude 试图去 Docker 里运行 `apt-get`。

- **Node/Python 依赖**：让 Claude 在 Mint 终端运行 `npm install` 或 `pip install`。因为目录是挂载的，宿主机装了，容器里也就有了（注意 `node_modules` 最好在容器内重新 rebuild，但通常开发环境通用）。
    
    - _更优雅的做法_：让 Claude 写 `docker exec -it dev-project-alpha npm install`。
        

#### 2. 查看日志

- **Vibe 方式**：问 Claude _"My container is failing, please check the logs."_ (前提是你开启了 Claude 的命令执行权限)。
    
- **1Panel 方式**：去面板 -> 容器 -> 点击日志图标。
    

#### 3. Nginx 反向代理 (可选，为了好看的域名)

如果你不想用 `localhost:3000`，想用 `dev.local`：

1. 修改 Mint 的 `/etc/hosts`，添加 `127.0.0.1 dev.local`。
    
2. 去 1Panel -> **网站** -> **创建反向代理**。
    
3. 域名填 `dev.local`，代理地址填 `127.0.0.1:3000`。
    

---

### 第四阶段：部署上线 (GitOps)

当你开发完成，准备部署到服务器（VPS）上的 1Panel 时：

1. **推送到 Git**：
    
    > "Claude, git add all, commit with message 'v1.0 release', and push."
    
2. **服务器端 1Panel 设置**：
    
    - 进入服务器的 1Panel -> **网站** -> **运行环境** -> **创建 Node/Python 环境**。
        
    - **代码来源**：选择 **Git**。
        
    - 填入 URL，勾选 **自动构建**。
        
3. **触发**：
    
    以后你在 Mint 上一推代码，服务器自动拉取、构建、重启。
    

---

### ⚠️ 避坑指南 (Vibe Killers)

1. **绝对不要**：手动去修改 `/opt/1panel` 里的文件。那是雷区。
    
2. **绝对不要**：在 1Panel 的图形界面里改了 Nginx 配置，又让 Claude 去改 `nginx.conf` 文件。这会导致配置被覆盖。**配置听 1Panel 的，代码听 Claude 的。**
    
3. **关于 node_modules**：如果你在 Linux Mint (宿主机) 执行 `npm install`，而在容器里跑不起来（架构不同），请使用以下命令让容器自己装依赖：
    
    Bash
    
    ```
    docker exec -it <容器名> npm install
    ```
    

### 🎯 总结你的工作流

1. **新建项目** -> `mkdir` -> 1Panel 挂载容器。
    
2. **写代码** -> `claude` (在 Mint 终端)。
    
3. **看效果** -> 浏览器访问 `localhost:端口`。
    
4. **修 Bug** -> 截图报错给 Claude -> Claude 改代码 -> 刷新浏览器。
    
5. **上线** -> `git push`。
    

现在，享受你的 Vibe Coding 吧！这就是目前最现代化的单兵作战方案。