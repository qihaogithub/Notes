---
创建日期: 2026-01-27T12:19:02+08:00
修改日期: 2026-01-27T15:39:57+08:00
---


> **核心哲学**：
> 
> - **Linux Mint (宿主机)** = **指挥舱** (写代码、Git、AI 指令)
>     
> - **1 Panel (容器)** = **引擎室** (运行环境、数据库、Nginx)
>     
> - **挂载 (Volume)** = **传送门** (连接两个世界的唯一通道)
>     

---

## 🌳 核心决策树：我该走哪条路？

在开始 coding 之前，先看您的项目属于哪一类：

### 🅰️ 光速流 (静态/前端)
- **技术栈**：Vue, React, Vite, Next. Js (SSG), 纯 HTML/CSS
- **特征**：不需要数据库，不需要后端服务，最终产物是一堆 html/js 文件
- **策略**：拒绝容器。直接用 Nginx (OpenResty) 托管

### 🅱️ 堡垒流 (后端/全栈)
- **技术栈**：Node. Js (Express/Nest), Python (Flask/Django), PHP, Go
- **特征**：需要连接数据库，需要常驻进程，需要特定的系统环境
- **策略**：必须容器。环境隔离，保护 Mint 系统

---

## 🏗️ 0. 基建准备 (通用)

无论走哪条路，先在您的 Linux Mint 上把"地基"打好。

### 1. 统一工作区

在您的主目录建立代码仓库：

```bash
mkdir -p ~/Projects/vibe-workspace
```

### 2. 权限神器 (防止 AI 搞乱权限)

Claude Code 生成的文件有时删不掉？在 `~/Projects/vibe-workspace` 下创建一个 `fix.sh`：

```bash
#!/bin/bash
# 运行这个脚本，瞬间把所有文件的所有权拿回来
echo "🔧 正在修复当前目录权限..."
sudo chown -R $USER:$USER .
echo "✅ 权限已归还给 $USER"
```

**用法**：遇到 Permission Denied 就运行 `./fix.sh`

---

## 🅰️ 路径一：光速流 (Vue/React/Static)

**核心理念**：前端开发最重"热更新" (HMR)。不要把 Vue 放进 Docker，那会变慢。

### 1. 开发阶段 (Dev Mode)

完全不要用 1 Panel。直接在 Mint 终端配合 Claude。

**初始化**：
> "Claude, 在当前目录帮我用 Vite 创建一个 Vue 3 + Tailwind 项目。"

**启动**：
```bash
npm run dev
```

**Vibe 体验**：Claude 改完代码，您按 Ctrl+S，浏览器毫秒级刷新。这是容器给不了的快感。

### 2. 本地托管/预览 (Prod Mode)

如果您想通过 1 Panel 模拟上线，或者想用自定义域名访问：

**构建**：
```bash
npm run build
# 这会生成 dist 目录
```

**1 Panel 设置 (静态网站)**：
- 进入 **网站** -> **创建网站** -> **类型**：静态网站
- **主域名**：填一个假域名，如 `mysite.local`
- **网站目录**：1 Panel 默认会建在 `/opt/1panel/...`



### 3. 给 AI 的指令 (Prompt)

```plaintext
# Context: 前端开发模式
我是前端开发者。请直接在宿主机执行 `npm` 命令。不要使用 docker 指令。
项目是 Vue/Vite，构建输出在 ./dist 目录。
```

---

## 🅱️ 路径二：堡垒流 (Node/Python + 数据库)

**核心理念**：后端环境太容易脏，必须关进笼子 (容器) 里。

### 1. 1 Panel 创建"空容器"

**网站** -> **创建网站** -> **运行环境** (Node/Python)

**配置**：
- **名称**：`backend-api`
- **镜像**：`node:18`
- **端口**：`3000:3000`
- **挂载 (Volume)** [关键]：
    - 主机：`/home/qihao/Projects/vibe-workspace/my-api`
    - 容器：`/app`
- **网络**：`1panel-network` (为了连数据库)
- **启动命令**：`tail -f /dev/null` (先让它空转，活着就行)

### 2. 数据库准备

在 1 Panel 创建 MySQL/Redis，记下账号密码。

**Host**：直接填 `mysql` (因为在同一个网络里)

### 3. AI 开发循环

**进入目录**：
```bash
cd ~/Projects/vibe-workspace/my-api
```

**启动 Claude**

**注入 AI 上下文 (复制这段)**：
```plaintext
# Context: 后端容器模式
1. 代码在本地 `/home/qihao/...`，但运行在 Docker 容器 `/app` 中。
2. 数据库 Host 是 `mysql`，端口 3306。
3. 安装依赖：请生成 `npm install` 命令并在宿主机执行（我会确认）。
4. 运行服务：请帮我把 package.json 的 start 命令改为 `node server.js`。
```

**让容器跑起来**：代码写好后，去 1 Panel 修改容器启动命令为 `npm start` 并重建。

---

## 🚀 部署上线 (GitOps 通用流)

不管您是 Vue 还是 Node，部署到服务器（VPS）的流程是一样的：**推 Git，自动拉**。

### 本地
> "Claude, git commit and push."

### 服务器 (1 Panel)

**如果是 Vue (静态)**：
- 创建静态网站 -> 来源选 Git
- 构建命令填 `npm install && npm run build`
- 目录设为 `dist`

**如果是 Node (容器)**：
- 创建运行环境 -> 来源选 Git
- 构建命令填 `npm install`
- 启动命令 `npm start`

**勾选"自动构建"**：Done. 以后您只管在 Mint 上写代码，服务器自动更新。

---

## 📊 总结：您的 Vibe Coding 备忘录

| 特性 | Vue / React (前端) | Node / Python (后端) |
|------|-------------------|---------------------|
| 开发地点 | Linux Mint 终端直接跑 | 1 Panel 挂载的 Docker 容器 |
| 运行命令 | `npm run dev` | 1 Panel 容器启动 |
| 1 Panel 作用 | 仅用于生产环境预览 (Nginx) | 提供运行环境 + 数据库 |
| AI 禁忌 | 不要让 AI 写 Dockerfile | 不要让 AI 装系统级依赖 (apt) |
| 部署方式 | 1 Panel 静态网站 (Git) | 1 Panel 运行环境 (Git) |

**一句话口诀**：前端直接跑，后端进笼子；代码存本地，Git 走天下。


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
