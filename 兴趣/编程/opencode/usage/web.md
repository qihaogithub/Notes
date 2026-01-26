# Web (浏览器界面)

在浏览器中使用 OpenCode。
OpenCode 可以作为 Web 应用程序运行，提供与终端相同的强大 AI 编程体验。

## [快速入门](https://opencode.ai/docs/web/#getting-started)
运行以下命令启动 Web 界面：

```bash
opencode web
```

这将在 `127.0.0.1` 启动一个本地服务器 (使用随机可用端口)，并自动在默认浏览器中打开 OpenCode。

**注意**：如果未设置 `OPENCODE_SERVER_PASSWORD` 环境变量，服务器将是不安全的。本地使用没问题，但如果需要通过网络访问，请务必设置密码。

## [配置](https://opencode.ai/docs/web/#configuration)
你可以通过命令行标志或配置文件进行配置。

- **端口 (Port)**: `opencode web --port 4096`
- **主机名 (Hostname)**: 默认绑定到 `127.0.0.1`。若要通过局域网访问，请使用 `0.0.0.0`：
  ```bash
  opencode web --hostname 0.0.0.0
  ```
- **mDNS 发现**: `opencode web --mdns` 使服务器在局域网内可被发现 (地址为 `opencode.local`)。
- **CORS**: `opencode web --cors https://example.com` 允许跨域请求。
- **身份验证**: 使用 `OPENCODE_SERVER_PASSWORD` 设置密码。用户名默认为 `opencode`，可以通过 `OPENCODE_SERVER_USERNAME` 更改。

## [使用 Web 界面](https://opencode.ai/docs/web/#using-the-web-interface)
启动后，你可以在主页查看和管理会话，启动新会话，以及查看连接的服务器状态。

## [连接终端](https://opencode.ai/docs/web/#attaching-a-terminal)
你可以将终端 TUI 连接到正在运行的 Web 服务器：
```bash
# 启动 Web 服务器
opencode web --port 4096

# 在另一个终端连接 TUI
opencode attach http://localhost:4096
```
这允许你同时使用 Web 界面和终端，并共享相同的会话和状态。
