# TUI (终端用户界面)

使用 OpenCode 终端用户界面。
OpenCode 提供了一个交互式的终端界面，用于与 LLM 协作处理项目。
运行 `opencode` 即可启动当前目录下的 TUI。

```bash
opencode
```

或者为特定目录启动：
```bash
opencode /path/to/project
```

## [文件引用](https://opencode.ai/docs/tui/#file-references)
你可以在消息中使用 `@` 来引用文件。这会在当前工作目录中进行模糊文件搜索。
例如：`How is auth handled in @packages/functions/src/api/index.ts?`
文件的内容会自动添加到对话中。

## [Bash 命令](https://opencode.ai/docs/tui/#bash-commands)
以 `!` 开头的消息可以运行 shell 命令。
例如：`!ls -la`
命令的输出将作为工具结果添加到对话中。

## [斜杠命令 (Commands)](https://opencode.ai/docs/tui/#commands)
你可以输入 `/` 后跟命令名称来快速执行操作。大多数命令也可以使用快捷键 (`ctrl+x` 作为前缀键)。

### 常用命令列表
- **/connect**: 添加模型提供商。
- **/compact**: 压缩当前会话 (别名: `/summarize`)。
- **/details**: 切换工具执行细节的显示。
- **/editor**: 打开外部编辑器编写消息 (基于 `EDITOR` 环境变量)。
- **/exit**: 退出 OpenCode (快捷键: `ctrl+x q`)。
- **/export**: 将当前对话导出为 Markdown 并打开。
- **/help**: 显示帮助对话框。
- **/init**: 创建或更新 `AGENTS.md` 文件。
- **/models**: 列出可用模型。
- **/new**: 开始新会话 (别名: `/clear`)。
- **/undo**: 撤销上一条消息及相关文件更改。
- **/sessions**: 列出并切换会话。
- **/share**: 分享当前会话。
- **/theme**: 列出可用主题。
- **/thinking**: 切换思考/推理块的显示。

## [编辑器设置 (Editor setup)](https://opencode.ai/docs/tui/#editor-setup)
`/editor` 和 `/export` 命令使用 `EDITOR` 环境变量指定的编辑器。

**常见编辑器选项**：
- `code --wait` (VS Code)
- `cursor --wait` (Cursor)
- `nvim` (Neovim)
- `vim`
- `nano`
- `notepad` (Windows)

## [配置 (Configure)](https://opencode.ai/docs/tui/#configure)
你可以在配置文件中自定义 TUI 行为：
- `scroll_acceleration`: 启用 macOS 风格的滚动加速。
- `scroll_speed`: 控制滚动速度 (默认 3)。
- `Username display`: 切换是否在聊天中显示用户名。
