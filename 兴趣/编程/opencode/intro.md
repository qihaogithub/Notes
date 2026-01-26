# 简介

欢迎使用 OpenCode。
[OpenCode](https://opencode.ai/) 是一款开源的 AI 编程助手。它提供终端界面、桌面应用或 IDE 扩展。
让我们开始吧。

#### [前提条件](https://opencode.ai/docs/#prerequisites)
要在终端中使用 OpenCode，你需要：
1. 一个现代的终端模拟器，例如：
   - [WezTerm](https://wezterm.org) (跨平台)
   - [Alacritty](https://alacritty.org) (跨平台)
   - [Ghostty](https://ghostty.org) (Linux 和 macOS)
   - [Kitty](https://sw.kovidgoyal.net/kitty/) (Linux 和 macOS)
2. 你想要使用的 LLM 提供商的 API 密钥。

## [安装](https://opencode.ai/docs/#install)
安装 OpenCode 最简单的方法是通过安装脚本：

```bash
curl -fsSL https://opencode.ai/install | bash
```

你也可以使用以下命令安装：

**使用 Node.js**
- **npm**: `npm install -g opencode-ai`
- **Bun**: `bun install -g opencode-ai`
- **pnpm**: `pnpm install -g opencode-ai`
- **Yarn**: `yarn global add opencode-ai`

**在 macOS 和 Linux 上使用 Homebrew**
```bash
brew install anomalyco/tap/opencode
```
我们建议使用 OpenCode 的 tap 以获取最新版本。

**在 Arch Linux 上使用 Paru**
```bash
paru -S opencode-bin
```

#### [Windows](https://opencode.ai/docs/#windows)
- **Chocolatey**: `choco install opencode`
- **Scoop**: `scoop install opencode`
- **NPM**: `npm install -g opencode-ai`
- **Mise**: `mise use -g github:anomalyco/opencode`
- **Docker**: `docker run -it --rm ghcr.io/anomalyco/opencode`

## [配置](https://opencode.ai/docs/#configure)
通过配置 API 密钥，你可以使用任何 LLM 提供商。
如果你是第一次使用，建议使用 [OpenCode Zen](https://opencode.ai/docs/zen)。它是经过 OpenCode 团队测试和验证的精选模型列表。

1. 在 TUI 中运行 `/connect` 命令，选择 opencode，然后访问 [opencode.ai/auth](https://opencode.ai/auth)。
2. 登录，添加账单详情，并复制你的 API 密钥。
3. 粘贴你的 API 密钥。

你也可以选择其他提供商。[了解更多](https://opencode.ai/docs/providers#directory)。

## [初始化](https://opencode.ai/docs/#initialize)
配置好提供商后，进入你想要工作的项目目录：

```bash
cd /path/to/project
```

运行 OpenCode：

```bash
opencode
```

然后，运行以下命令为项目初始化 OpenCode：

```bash
/init
```

这将让 OpenCode 分析你的项目并在根目录创建 `AGENTS.md` 文件。
**提示**：你应该将项目的 `AGENTS.md` 文件提交到 Git。这有助于 OpenCode 理解项目结构和编码模式。

## [使用](https://opencode.ai/docs/#usage)
现在你已经准备好使用 OpenCode 来处理项目了。

### [提出问题](https://opencode.ai/docs/#ask-questions)
你可以要求 OpenCode 为你解释代码库。
**提示**：使用 `@` 键可以模糊搜索项目中的文件。
例如：`How is authentication handled in @packages/functions/src/api/index.ts`

### [添加功能](https://opencode.ai/docs/#add-features)
你可以要求 OpenCode 为项目添加新功能。建议先让它创建一个计划。
1. **创建计划**：按 `Tab` 键切换到 **Plan** 模式。描述你想要实现的功能。
2. **迭代码计划**：它给出计划后，你可以提供反馈或添加更多细节。
   **提示**：你可以将图片拖放到终端中作为参考。
3. **构建功能**：对计划满意后，再次按 `Tab` 键切换回 **Build** 模式，让它进行更改。

### [进行更改](https://opencode.ai/docs/#make-changes)
对于简单的更改，你可以直接要求 OpenCode 构建而无需先审查计划。

### [撤销更改](https://opencode.ai/docs/#undo-changes)
如果你不满意当前的更改，可以使用 `/undo` 命令撤销。
你可以多次运行 `/undo` 来撤销多次更改，或运行 `/redo` 来重做。

## [分享](https://opencode.ai/docs/#share)
你可以与团队分享对话：
```bash
/share
```
这将创建一个链接并复制到剪贴板。

## [自定义](https://opencode.ai/docs/#customize)
你可以[选择主题](https://opencode.ai/docs/themes)、[自定义快捷键](https://opencode.ai/docs/keybinds)、[配置代码格式化程序](https://opencode.ai/docs/formatters)、[创建自定义命令](https://opencode.ai/docs/commands)或调整 [OpenCode 配置](https://opencode.ai/docs/config)。
