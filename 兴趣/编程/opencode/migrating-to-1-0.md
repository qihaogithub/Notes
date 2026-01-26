# 迁移到 1.0 (Migrating to 1.0)

OpenCode 1.0 的新变化。
OpenCode 1.0 对 TUI 进行了重写。我们从基于 Go + bubbletea 的 TUI (存在性能和功能瓶颈) 迁移到了自研的 OpenTUI 框架 (使用 Zig + SolidJS 编写)。
新的 TUI 与旧版具有相同的工作原理，因为它连接到相同的 OpenCode 服务器。

## [升级](https://opencode.ai/docs/1-0/#upgrading)
如果你正在使用之前的版本，不应该被自动升级到 1.0。
要手动升级：
```bash
opencode upgrade 1.0.0
```
要降级回 0.x：
```bash
opencode upgrade 0.15.31
```

## [UX 变更](https://opencode.ai/docs/1-0/#ux-changes)
- **会话历史更压缩**：仅显示 `edit` 和 `bash` 工具的完整细节。
- **添加了命令栏 (Command Bar)**：几乎所有操作都流经此处。在任何上下文中按 `Ctrl + P` 呼出。
- **添加了会话侧边栏**。
- **删除了部分低频功能**。

## [破坏性变更](https://opencode.ai/docs/1-0/#breaking-changes)

### [快捷键重命名](https://opencode.ai/docs/1-0/#keybinds-renamed)
- `messages_revert` -> `messages_undo`
- `switch_agent` -> `agent_cycle`
- `switch_agent_reverse` -> `agent_cycle_reverse`
- `switch_mode` -> `agent_cycle`
- `switch_mode_reverse` -> `agent_cycle_reverse`

### [快捷键删除](https://opencode.ai/docs/1-0/#keybinds-removed)
删除了诸如 `messages_layout_toggle`、`file_diff_toggle`、`file_search`、`app_help` 等快捷键。
如果发现某些重要功能缺失，请在 GitHub 上开启 Issue。
