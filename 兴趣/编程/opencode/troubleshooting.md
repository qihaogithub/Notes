# 故障排除 (Troubleshooting)

常见问题及解决方法。
要调试 OpenCode 的任何问题，你可以检查日志或存储在本地的会话数据。

### [日志 (Logs)](https://opencode.ai/docs/troubleshooting/#logs)
日志文件写入位置：
- macOS/Linux: `~/.local/share/opencode/log/`
- Windows: `%USERPROFILE%\.local\share\opencode\log\`

日志文件以时间戳命名 (例如 `2025-01-09T123456.log`)，保留最近的 10 个日志文件。
你可以使用 `--log-level DEBUG` 命令行选项获取更详细的调试信息。

### [存储 (Storage)](https://opencode.ai/docs/troubleshooting/#storage)
OpenCode 在磁盘上存储会话数据和其他应用数据：
- macOS/Linux: `~/.local/share/opencode/`
- Windows: `%USERPROFILE%\.local\share\opencode\`

目录包含：
- `auth.json`: 身份验证数据 (如 API 密钥)。
- `log/`: 应用日志。
- `project/`: 项目特定数据。

## [获取帮助](https://opencode.ai/docs/troubleshooting/#getting-help)
1. **GitHub 报告问题**：[github.com/anomalyco/opencode/issues](https://github.com/anomalyco/opencode/issues)
2. **加入 Discord**：[opencode.ai/discord](https://opencode.ai/discord)

## [常见问题](https://opencode.ai/docs/troubleshooting/#common-issues)

### [OpenCode 无法启动](https://opencode.ai/docs/troubleshooting/#opencode-wont-start)
1. 检查日志中的错误信息。
2. 尝试使用 `--print-logs` 运行以在终端查看输出。
3. 确保使用 `opencode upgrade` 升级到最新版本。

### [身份验证问题](https://opencode.ai/docs/troubleshooting/#authentication-issues)
1. 尝试在 TUI 中使用 `/connect` 命令重新验证。
2. 检查 API 密钥是否有效。
3. 确保网络允许连接到提供商的 API。

### [模型不可用](https://opencode.ai/docs/troubleshooting/#model-not-available)
1. 检查是否已与提供商连接。
2. 验证配置中的模型名称是否正确。标准格式为 `<providerId>/<modelId>` (例如 `openai/gpt-4o`)。
3. 运行 `opencode models` 查看你拥有访问权限的模型列表。

### [ProviderInitError](https://opencode.ai/docs/troubleshooting/#provideriniterror)
这通常表示配置无效或损坏。
1. 检查 `providers` 指南。
2. 尝试清除存储的配置：`rm -rf ~/.local/share/opencode` (Windows 下对应路径)。
3. 使用 `/connect` 重新验证。

### [AI_APICallError 和提供商包问题](https://opencode.ai/docs/troubleshooting/#ai_apicallerror-and-provider-package-issues)
如果遇到 API 调用错误，可能是由于过时的提供商包。
1. 清除提供商包缓存：`rm -rf ~/.cache/opencode`。
2. 重启 OpenCode 以重新安装最新的包。

### [Linux 下无法复制/粘贴](https://opencode.ai/docs/troubleshooting/#copypaste-not-working-on-linux)
需要安装剪贴板实用程序：
- **X11**: `xclip` 或 `xsel`
- **Wayland**: `wl-clipboard`
- **无头环境**: `xvfb`
