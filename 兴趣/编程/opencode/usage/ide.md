# IDE 扩展

适用于 VS Code、Cursor 及其他 IDE 的 OpenCode 扩展。
OpenCode 可以与 VS Code、Cursor 或任何支持终端的 IDE 集成。只需在终端中运行 `opencode` 即可开始。

## [用法](https://opencode.ai/docs/ide/#usage)
- **快速启动**: 使用 `Cmd+Esc` (Mac) 或 `Ctrl+Esc` (Windows/Linux) 在拆分终端视图中打开 OpenCode。
- **新会话**: 使用 `Cmd+Shift+Esc` (Mac) 或 `Ctrl+Shift+Esc` (Windows/Linux) 开启新的 OpenCode 会话。你也可以点击界面上的 OpenCode 按钮。
- **上下文感知**: 自动与 OpenCode 共享你当前的选择或标签页。
- **文件引用快捷键**: 使用 `Cmd+Option+K` (Mac) 或 `Alt+Ctrl+K` (Linux/Windows) 插入文件引用，例如 `@File#L37-42`。

## [安装](https://opencode.ai/docs/ide/#installation)
要在 VS Code 及其流行分支 (Cursor、Windsurf、VSCodium) 上安装 OpenCode：
1. 打开 VS Code。
2. 打开集成终端。
3. 运行 `opencode` —— 扩展会自动安装。

如果你想在运行 `/editor` 或 `/export` 时使用自己的 IDE，需要设置 `export EDITOR="code --wait"`。

### [手动安装](https://opencode.ai/docs/ide/#manual-install)
在扩展市场中搜索 **OpenCode** 并点击安装。

### [故障排除](https://opencode.ai/docs/ide/#troubleshooting)
如果扩展未能自动安装：
- 确保你在集成终端中运行 `opencode`。
- 确认 IDE 的 CLI 已安装：
  - VS Code: `code` 命令
  - Cursor: `cursor` 命令
  - Windsurf: `windsurf` 命令
  - VSCodium: `codium` 命令
- 如果没安装，请按 `Cmd+Shift+P` (Mac) 或 `Ctrl+Shift+P` (Windows/Linux) 并搜索 “Shell Command: Install 'code' command in PATH” (或对应的 IDE 名称)。
- 确保 VS Code 有权限安装扩展。
