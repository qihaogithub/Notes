# 主题设置 (Themes)

选择内置主题或定义你自己的主题。
默认情况下，OpenCode 使用自带的 `opencode` 主题。

## [终端要求](https://opencode.ai/docs/themes/#terminal-requirements)
为了正确显示主题颜色，你的终端必须支持 **Truecolor (24-bit color)**。
- **检查支持**: 运行 `echo $COLORTERM`，应输出 `truecolor` 或 `24bit`。
- **开启**: 在 shell 配置文件中设置 `export COLORTERM=truecolor`。

## [内置主题](https://opencode.ai/docs/themes/#built-in-themes)
OpenCode 提供了多种内置主题：
- `system`: 自动适应终端颜色。
- `tokyonight`, `everforest`, `catppuccin`, `gruvbox`, `nord` 等。

## [使用主题](https://opencode.ai/docs/themes/#using-a-theme)
在 TUI 中输入 `/theme` 指令呼出选择菜单，或者在配置文件中指定：
```json
{
  "theme": "tokyonight"
}
```

## [自定义主题 (Custom Themes)](https://opencode.ai/docs/themes/#custom-themes)
OpenCode 支持基于 JSON 的主题系统。

### 存放目录 (优先级由高到低)
1. 项目目录：`./.opencode/themes/*.json`
2. 用户配置目录：`~/.config/opencode/themes/*.json`
3. 内置主题。

### JSON 格式
支持：
- 十六进制颜色 (`"#ffffff"`)
- ANSI 颜色 (`0-255`)
- 引用定义 (`"primary"`)
- 暗黑/明亮变体 (`{"dark": "#000", "light": "#fff"}`)
- 特殊值 `"none"`：继承终端默认背景或文字颜色。

### 创建主题
在上述任一目录创建 `.json` 文件即可。文件名将作为主题名称。
可以在 `defs` 字段定义可重复使用的颜色。
