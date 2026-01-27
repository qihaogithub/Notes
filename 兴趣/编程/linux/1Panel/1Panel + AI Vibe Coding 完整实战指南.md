---
创建日期: 2026-01-27T12:19:02+08:00
修改日期: 2026-01-27T13:20:12+08:00
---

> **核心哲学**：
> 
> - **Linux Mint (宿主机)** = **指挥舱** (写代码、Git、AI 指令)
>     
> - **1Panel (容器)** = **引擎室** (运行环境、数据库、Nginx)
>     
> - **挂载 (Volume)** = **传送门** (连接两个世界的唯一通道)
>     

---

## 🔒 为什么要“把代码关进笼子”？

_(这是给强迫症开发者的福音)_

1. **系统洁癖保卫战**：
    
    - 您在 Mint 上不需要装 `node_modules`，不需要装 `pip`，不需要装 `mysql`。
        
    - **后果**：您的 Mint 系统永远像刚装好一样干净。删掉容器 = 删掉一切垃圾。
        
2. **消灭“环境玄学”**：
    
    - **容器 = 比特级一致性**。本地容器里的环境 = 服务器上的环境。
        
    - 再也不会出现 _“我本地明明能跑，服务器上怎么挂了”_ 这种鬼故事。
        
3. **AI 的安全气囊**：
    
    - Claude 如果发疯删错了库，或者把环境搞乱了，点击 1Panel 的**“重建”**按钮，3秒钟满血复活。
        

---

## 🛠️ 第一阶段：基建初始化 (一次性设置)

### 1. 建立“基地” (宿主机)

在 Mint 终端执行，建立统一的工作区：

Bash

```
mkdir -p ~/Projects/vibe-workspace
cd ~/Projects/vibe-workspace
```

### 2. 创建“不死的”开发容器 (1Panel)

> 💡 **Vibe 技巧**：很多新手在创建容器时，因为项目还没代码，容器启动就会报错退出。我们用一个**“空转命令”**先把它养着。

- **进入 1Panel** -> **容器** -> **创建容器**。
    
- **镜像**：选 `node:18` 或 `python:3.10`。
    
- **必填配置**：
    
    - **名称**：`dev-project-alpha`
        
    - **网络**：`1panel-network` (关键！为了连数据库)
        
    - **端口**：`3000:3000` (外部访问)
        
    - **挂载 (Volume)**：
        
        - 主机: `/home/qihao/Projects/vibe-workspace/my-app`
            
        - 容器: `/app`
            
- **⚠️ 关键的一手 (启动命令)**：
    
    - 在 **“运行命令”** 栏，填入：`tail -f /dev/null`
        
    - _解释：这会让容器一直活着，哪怕里面什么代码都没有。等 Claude 把代码写好了，我们再改回 `npm start`。_
        


## 🤖 第二阶段：AI 开发流 (日常循环)

### 1. 启动 Claude Code

进入目录：

Bash

```
cd ~/Projects/vibe-workspace/my-app
claude
```

### 2. 注入“上帝视角” (Context Injection)

**这是 Vibe Coding 成功的关键。** 第一次对话时，请直接发送以下卡片，让 Claude 瞬间理解它的处境：

Markdown

```
# SYSTEM CONTEXT: Vibe Coding Mode

你现在是我的 Vibe Coding 助手。请读取以下**物理规则**并严格遵守：

**[1] 空间架构**
- **我是谁**：用户 (User `qihao`)
- **我在哪**：Linux Mint 宿主机 (`/home/qihao/Projects/vibe-workspace/my-app`)
- **代码在哪**：通过 Volume 挂载到 Docker 容器内 (`/app`)
- **运行在哪**：容器 `dev-project-alpha` (由 1Panel 管理)

**[2] 行为准则 (铁律)**
- ✅ **文件操作**：你只能在当前目录下读写文件。
- ✅ **安装依赖**：
    - Python/Node: 请直接在当前终端执行 `npm install` 或 `pip install` (因为目录挂载，容器内会自动同步)。
    - 系统库: **严禁**执行 `apt-get`。如果必须安装系统库(如 libpng)，请告诉我 "请手动进入容器安装"。
- ✅ **运行命令**：如果需要重启服务或查看容器日志，请生成 `docker` 命令。
- ✅ **数据库**：Host 使用 `mysql` (容器名)，端口 `3306`，密码读 `.env`。

**[3] 禁止事项**
- ❌ **禁止**修改 `/opt/1panel` 或 Nginx 配置文件。
- ❌ **禁止**尝试 SSH 连接。

现在，请帮我初始化一个 [Node.js / Python] 项目结构。
```

### 3. 解决“权限地狱” (The Fix Script)

容器里生成的 `node_modules` 或 `__pycache__` 往往是 `root` 权限，导致你在 Mint 下删不掉。

让 Claude 创建一个 `fix.sh`：

Bash

```
#!/bin/bash
# 作用：将当前目录的所有权归还给当前用户
# 用法：./fix.sh
if [ "$PWD" == "$HOME/Projects/vibe-workspace/my-app" ]; then
    echo "🔧 正在修复当前目录权限..."
    sudo chown -R $USER:$USER .
    echo "✅ 修复完成！"
else
    echo "⚠️ 安全警告：请只在项目根目录下运行此脚本！"
fi
```

---

## 🔧 第三阶段：运维与调试

### 1. 数据库连接

在 1Panel 创建数据库后，让 Claude 生成 `.env`：

代码段

```
# 这里的 Host 填 1Panel 里的数据库容器名，通常是 'mysql' 或 'postgresql'
DB_HOST=mysql
DB_PORT=3306
DB_USER=root
DB_PASS=你的密码
```

### 2. 当容器报错时

不要去 1Panel 网页点日志，太慢。直接问 Claude：

> "App is crashing. Please check the docker logs for container 'dev-project-alpha' and fix the code."
> 
> _(Claude 会自动执行 `docker logs --tail 50 ...` 并分析错误)_

### 3. 从“空转”切换到“实战”

当代码写好了，想要容器自动运行 `npm start`？

1. 去 1Panel -> 容器 -> 编辑。
    
2. 把之前的 `tail -f /dev/null` 改成 `npm run dev` 或 `python app.py`。
    
3. **重建容器**。
    

---

## 🚢 第四阶段：部署上线 (GitOps)

不要手动传文件。

1. **推送到 Git**：
    
    > "Claude, git push origin main."
    
2. **服务器端 1Panel**：
    
    - 创建网站 -> 运行环境。
        
    - 代码来源选 **Git**。
        
    - 勾选 **“自动构建”** (Webhook)。
        
3. **效果**：
    
    你在 Mint 上一推代码，服务器自动拉取、构建、重启。**这就是 DevOps 的终极形态。**
    

---

## 🆘 紧急救援模版

如果遇到搞不定的问题，把下面这段发给 Claude，它能救你：

Markdown

```
🚨 **TECHNICAL INTERVENTION REQUIRED**

**环境快照：**
- OS: Linux Mint (Host)
- App Path: `/home/qihao/Projects/vibe-workspace/my-app`
- Container: `dev-project-alpha` (1Panel Managed)
- Issue: Permission Denied / Connection Refused / 依赖缺失

**我遇到的具体问题：**
[在此粘贴报错信息或截图]

**任务：**
请根据上述架构，分析是**宿主机文件权限问题**，还是**容器内环境缺失问题**，并给出修复命令。
```

---

### 🎯 Vibe Coding 总结

1. **1Panel** 是你的**房东**（提供房子和水电）。
    
2. **Claude** 是你的**管家**（负责装修和干活）。
    
3. **你** 只需要坐在 **Mint** 的客厅里（宿主机），喝着咖啡指挥即可。