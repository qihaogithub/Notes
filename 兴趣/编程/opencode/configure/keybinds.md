# 快捷键设置 (Keybinds)

自定义你的快捷键。
OpenCode 允许你通过配置文件中的 `keybinds` 字段自定义各项操作。

## [前缀键 (Leader Key)](https://opencode.ai/docs/keybinds/#leader-key)
为了避免与终端原有快捷键冲突，OpenCode 使用前缀键。
- 默认前缀键为 `ctrl+x`。
- 大多数操作需要先按下前缀键，然后再按快捷键。例如：开始新会话先按 `ctrl+x` 再按 `n`。

## [自定义示例](https://opencode.ai/docs/keybinds/#disable-keybind)
你可以通过将操作的值设置为 `"none"` 来禁用某个快捷键。

```json
{
  "keybinds": {
    "leader": "ctrl+x",
    "app_exit": "ctrl+c,ctrl+d,<leader>q",
    "session_new": "<leader>n",
    "session_compact": "none"
  }
}
```

## [部分常用操作列表](https://opencode.ai/docs/keybinds/)
- `app_exit`: 退出应用。
- `editor_open`: 打开编辑器 (`<leader>e`)。
- `theme_list`: 列出主题 (`<leader>t`)。
- `sidebar_toggle`: 切换侧边栏 (`<leader>b`)。
- `session_new`: 新会话 (`<leader>n`)。
- `session_list`: 会话列表 (`<leader>l`)。
- `messages_undo`: 撤销 (`<leader>u`)。
- `messages_redo`: 重回 (`<leader>r`)。
- `agent_cycle`: 循环切换代理 (`tab`)。

## [换行符 (Shift+Enter)](https://opencode.ai/docs/keybinds/#shiftenter)
某些终端默认不发送 `Shift+Enter`。你可能需要为终端配置转义序列（如 `\u001b[13;2u`）来正确处理换行。
对于 **Windows Terminal**，需在 `settings.json` 中添加相应的 `actions` 和 `keybindings`。
