---
创建日期: 2026-02-25T13:36:40+08:00
修改日期: 2026-02-25T15:50:11+08:00
---
<div align="center">
  <h1>Kaku</h1>
  <p><em>一款为 AI 编程而生的快速、开箱即用的终端。</em></p>
</div>

<p align="center">
  <a href="https://github.com/tw93/Kaku/stargazers"><img src="https://img.shields.io/github/stars/tw93/Kaku?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/tw93/Kaku/releases"><img src="https://img.shields.io/github/v/tag/tw93/Kaku?label=version&style=flat-square" alt="Version"></a>
  <a href="LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="https://github.com/tw93/Kaku/commits"><img src="https://img.shields.io/github/commit-activity/m/tw93/Kaku?style=flat-square" alt="Commits"></a>
  <a href="https://twitter.com/HiTw93"><img src="https://img.shields.io/badge/follow-Tw93-red?style=flat-square&logo=Twitter" alt="Twitter"></a>
</p>

<p align="center">
  <img src="assets/kaku.jpeg" alt="Kaku Screenshot" width="1000" />
  <br/>
  Kaku 是 <a href="https://github.com/wez/wezterm">WezTerm</a> 的深度定制分支，旨在提供开箱即用的体验。
</p>

## 特性

- **零配置**：默认使用 JetBrains Mono 字体、opencode 主题、macOS 字体渲染和低分辨率字体大小。
- **精选 Shell 套件**：内置 zsh 插件，以及用于提示符、差异对比和导航工作流的可选 CLI 工具。
- **快速轻量**：二进制文件体积减少 40%，启动瞬间完成，支持懒加载，精简了 GPU 加速核心。
- **兼容 WezTerm 配置**：可直接使用 WezTerm 的 Lua 配置文件，具有完整的 API 兼容性，无需迁移。

## 快速开始

1. [下载 Kaku DMG](https://github.com/tw93/Kaku/releases/latest) 并拖拽到“应用程序”文件夹。
2. 或使用 Homebrew 安装：`brew install tw93/tap/kakuku`。
3. 打开 Kaku。该应用已通过 Apple 公证，因此打开时不会出现安全警告。
4. 首次启动时，Kaku 将自动设置你的 Shell 环境。

## 使用指南

Kaku 配备了直观的 macOS 原生快捷键：

| 操作          | 快捷键                                               |
| :---------- | :------------------------------------------------ |
| 新建标签页       | `Cmd + T`                                         |
| 新建窗口        | `Cmd + N`                                         |
| 关闭标签页/窗格    | `Cmd + W`                                         |
| 切换标签页       | `Cmd + Shift + [`、`Cmd + Shift + ]` 或 `Cmd + 1-9` |
| 切换窗格        | `Cmd + Opt + 方向键`                                 |
| 垂直分割窗格      | `Cmd + D`                                         |
| 水平分割窗格      | `Cmd + Shift + D`                                 |
| 切换分割方向      | `Cmd + Shift + S`                                 |
| 放大/还原窗格     | `Cmd + Shift + Enter`                             |
| 调整窗格大小      | `Cmd + Ctrl + 方向键`                                |
| 清屏          | `Cmd + K`                                         |
| Kaku AI 设置  | `Cmd + Shift + A`                                 |
| Kaku 助手应用建议 | `Cmd + Shift + E`                                 |
| 打开 Lazygit  | `Cmd + Shift + G`                                 |
| Yazi 文件管理器  | `Cmd + Shift + Y` 或 `y`                           |
| 字体大小        | `Cmd + +`、`Cmd + -`、`Cmd + 0`                     |
| 智能跳转        | `z <目录>`                                          |
| 智能选择        | `z -l <目录>`                                       |
| 最近目录        | `z -t`                                            |

## 配置

Kaku 配备了精心挑选的 Shell 栈，可实现即时生产力，让你无需打开 VSCode 即可专注于 AI 编程：

默认捆绑的内置 zsh 插件：

- **z**：一个更智能的 cd 命令，能学习你最常使用的目录以实现即时导航。
- **zsh-completions**：扩展的命令和子命令补全定义。
- **语法高亮**：实时命令验证和着色。
- **自动建议**：类似 Fish shell 的智能、基于历史的补全建议。

在 `kaku init` 期间通过 Homebrew 安装的可选 CLI 工具：

- **Starship**：一个快速、可定制的提示符，显示 Git 状态、包版本和执行时间。
- **Delta**：用于 Git、diff 和 grep 输出的语法高亮分页器。
- **Lazygit**：一个用于快速、可视化 Git 工作流的终端 UI，无需离开 Shell。
- **Yazi**：一个终端文件管理器。使用 `y` 启动它，并在退出时同步 Shell 目录。

Kaku 使用 `~/.config/kaku/kaku.lua` 进行配置，完全兼容 WezTerm 的 Lua API，内置默认配置位于 `Kaku.app/Contents/Resources/kaku.lua` 作为后备。

在终端中运行 `kaku` 可查看所有可用命令，例如 `kaku update`、`kaku reset`、`kaku config` 和 `kaku ai`。

## Kaku AI

Kaku 包含一个内置助手，用于命令行错误恢复，以及一个用于外部 AI 编程工具的统一设置界面。

- **Kaku 助手**：自动分析失败的命令并准备安全的命令建议。
- **AI 工具配置**：管理如 Claude Code、Codex、Gemini CLI、Copilot CLI、Factory Droid、OpenCode 和 OpenClaw 等工具的设置。

使用 `kaku ai` 打开 AI 设置，然后在一个地方配置 **Kaku 助手**（启用、模型、基础 URL、API 密钥）和你的外部 AI 工具。

提示：DeepSeek-V 3.2 是开始日常 AI 编码任务的绝佳低成本选择。

当 Kaku 助手在命令出错后准备好建议时，按 `Cmd + Shift + E` 应用它。

## 为什么选择 Kaku？

我在工作和个人项目中都严重依赖 CLI。我构建的工具，如 [Mole](https://github.com/tw93/mole) 和 [Pake](https://github.com/tw93/pake)，都反映了这一点。

我使用 Alacritty 多年，学会了重视速度和简洁性。随着我的工作流程转向 AI 辅助编程，我想要更强的标签页和窗格人体工程学。我也探索了 Kitty、Ghostty、Warp 和 iTerm 2。每个工具在不同领域都很强大，但我仍然想要一个匹配我个人在性能、默认设置和控制权之间平衡的设置。

WezTerm 功能强大且高度可定制，我非常感谢它的引擎和生态系统。Kaku 在此基础上构建，为第一天使用提供了实用的默认设置，同时保持了完整的基于 Lua 的定制和快速、轻量的感觉。

所以我构建了 Kaku 来成为这样的环境：快速、精致、随时可以工作。

### 性能

| 指标 | 上游版本 | Kaku | 方法论 |
| :--- | :--- | :--- | :--- |
| **可执行文件大小** | ~67 MB | ~40 MB | 激进的符号剥离和功能裁剪 |
| **资源体积** | ~100 MB | ~80 MB | 资源优化和懒加载资源 |
| **启动延迟** | 标准 | 瞬间 | 即时初始化 |
| **Shell 启动时间** | ~200 ms | ~100 ms | 优化的环境配置 |

通过激进地剥离未使用功能、懒加载配色方案和 Shell 优化实现。

## 常见问题

1. **为什么 Homebrew cask 的名字是 `kakuku` 而不是 `kaku`？**

   因为 `kaku` 这个名字与 Homebrew 官方仓库中的另一个包（一个未维护的音乐播放器）冲突。`kakuku` 是一个容易记住的可爱变体。

2. **有 Windows 或 Linux 版本吗？**

   目前没有。Kaku 目前是 macOS 专属，我们专注于打磨 macOS 体验。一旦 macOS 版本成熟，可能会推出 Windows 和 Linux 版本。

3. **Kaku 能在 macOS 上使用透明窗口吗？**

   可以。你可以在 `~/.config/kaku/kaku.lua` 中设置 `window_background_opacity` 和可选的 `macos_window_background_blur`。透明模式现在会保持顶部/右侧/底部填充区域的视觉一致性，以避免出现透明间隙。

4. **如何关闭选中即复制？**

   Kaku 默认启用选中即复制；要禁用自动剪贴板复制和选中后的复制提示，请在 `~/.config/kaku/kaku.lua` 中添加 `config.copy_on_select = false`。

## 贡献者

衷心感谢所有帮助构建 Kaku 的贡献者。去