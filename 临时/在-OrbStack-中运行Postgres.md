---
id: ABC6E13B-D20F-4CCE-96E2-4DE9315C3F79
title: 在 OrbStack 中运行Postgres
created: 2026-05-07T02:07:56Z
modified: 2026-05-07T02:10:10Z
---
# 在 OrbStack 中运行Postgres

### 步骤 1：打开终端 (Terminal)
你可以使用 macOS 自带的“终端”应用，也可以直接点击你截图右侧界面顶部的 **Terminal** 选项卡。

### 步骤 2：运行启动命令
在终端中输入以下命令并回车（你可以把 `your_password` 替换成你自己想要的数据库密码）：

```bash
docker run --name my-postgres -e POSTGRES_PASSWORD=your_password -p 5432:5432 -d postgres
```

**命令参数解释：**
*   `--name my-postgres`: 给你的容器起个名字，这里叫 `my-postgres`。
*   `-e POSTGRES_PASSWORD=your_password`: 设置 Postgres 的默认超级用户 (`postgres`) 的密码。**这是必填项**，否则容器会启动失败。
*   `-p 5432:5432`: 将你电脑（宿主机）的 5432 端口映射到容器内的 5432 端口。这样你就可以在电脑上直接连接数据库了。
*   `-d`: 让容器在后台运行 (detached mode)。
*   `postgres`: 使用你截图里已经下载好的那个镜像名称。

### 步骤 3：在 OrbStack 中查看运行状态
1. 回到 OrbStack 的界面。
2. 在左侧边栏点击 **Containers**（容器）选项卡。
3. 你应该能看到一个名为 `my-postgres` 的容器正在运行（前面会有一个绿色的点表示运行中）。

### 如何连接你的 Postgres 数据库？
现在数据库已经运行了，你可以使用任何数据库客户端（如 DBeaver、Navicat、DataGrip 等）进行连接：
*   **主机 (Host):** `127.0.0.1` 或 `localhost`
*   **端口 (Port):** `5432`
*   **用户名 (Username):** `postgres`
*   **密码 (Password):** 你在步骤2中设置的密码 (`your_password`)
*   **默认数据库 (Database):** `postgres`