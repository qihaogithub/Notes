# CLI (命令行界面)

OpenCode CLI 选项和命令。
默认情况下，运行不带参数的 `opencode` 会启动 [TUI](https://opencode.ai/docs/tui)。

```bash
opencode
```

但它也接受各种命令，允许你以编程方式与 OpenCode 交互。
例如：`opencode run "Explain how closures work in JavaScript"`

## [TUI 命令](https://opencode.ai/docs/cli/#tui)
启动 OpenCode 终端用户界面。

**标志位 (Flags)**:
- `--continue`, `-c`: 继续上一次会话。
- `--session`, `-s`: 指定会话 ID。
- `--prompt`: 提供初始提示词。
- `--model`, `-m`: 指定使用的模型。
- `--agent`: 指定使用的代理。

## [常用命令 (Commands)](https://opencode.ai/docs/cli/#commands)

### [agent](https://opencode.ai/docs/cli/#agent)
管理 OpenCode 代理。
- `opencode agent list`: 列出所有代理。
- `opencode agent create`: 引导创建新代理。

### [attach](https://opencode.ai/docs/cli/#attach)
将终端连接到已运行的 OpenCode 后端服务器 (由 `serve` 或 `web` 启动)。
例如：`opencode attach http://10.20.30.40:4096`

### [auth](https://opencode.ai/docs/cli/#auth)
管理凭据和登录。
- `opencode auth login`: 配置 API 密钥。
- `opencode auth list`: 列出已认证的提供商。
- `opencode auth logout`: 登出。

### [github](https://opencode.ai/docs/cli/#github)
管理 GitHub 代理以进行仓库自动化。
- `opencode github install`: 在仓库中安装 GitHub 代理。
- `opencode github run`: 运行 GitHub 代理 (通常用于 GitHub Actions)。

### [mcp](https://opencode.ai/docs/cli/#mcp)
管理模型上下文协议 (MCP) 服务器。
- `opencode mcp add`: 添加 MCP 服务器。
- `opencode mcp list`: 列出已配置的服务器。
- `opencode mcp auth [name]`: 对支持 OAuth 的服务器进行身份验证。

### [models](https://opencode.ai/docs/cli/#models)
列出所有可用模型。
- `opencode models [provider]`: 按提供商过滤。
- `--refresh`: 更新缓存的模型列表。

### [run](https://opencode.ai/docs/cli/#run-1)
以非交互模式运行 OpenCode（直接传递提示词）。
适合脚本编写和自动化。
例如：`opencode run "Explain the use of context in Go"`

### [serve](https://opencode.ai/docs/cli/#serve)
启动一个无界面的 OpenCode 服务器。

### [session](https://opencode.ai/docs/cli/#session)
管理 OpenCode 会话。
- `opencode session list`: 列出所有会话。

### [stats](https://opencode.ai/docs/cli/#stats)
显示 Token 使用情况和成本统计。

### [export / import](https://opencode.ai/docs/cli/#export)
导出或导入会话数据 (JSON 格式或分享 URL)。

### [web](https://opencode.ai/docs/cli/#web)
启动一个带有 Web 界面的 OpenCode 服务器。

### [upgrade / uninstall](https://opencode.ai/docs/cli/#upgrade)
升级 OpenCode 到最新或特定版本，或卸载。

## [全局标志 (Global Flags)](https://opencode.ai/docs/cli/#global-flags)
- `--help`, `-h`: 显示帮助。
- `--version`, `-v`: 显示版本。
- `--print-logs`: 打印日志。
- `--log-level`: 设置日志级别。

## [环境变量](https://opencode.ai/docs/cli/#environment-variables)
可以使用环境变量配置 OpenCode，如 `OPENCODE_CONFIG`、`OPENCODE_AUTO_SHARE`、`OPENCODE_SERVER_PASSWORD` 等。
