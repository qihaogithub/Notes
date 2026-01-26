# Superpowers for Codex

在 OpenAI Codex 中使用 Superpowers 的完整指南。

## 快速安装

告知 Codex：

```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md
```

## 手动安装

### 前提条件

- 拥有 OpenAI Codex 访问权限
- 拥有安装文件的 Shell 访问权限

### 安装步骤

#### 1. 克隆 Superpowers

```bash
mkdir -p ~/.codex/superpowers
git clone https://github.com/obra/superpowers.git ~/.codex/superpowers
```

#### 2. 安装引导（Bootstrap）

引导文件已包含在仓库中的 `.codex/superpowers-bootstrap.md`。Codex 会自动从克隆的位置使用它。

#### 3. 验证安装

告知 Codex：

```
Run ~/.codex/superpowers/.codex/superpowers-codex find-skills to show available skills
```

您应该看到带有描述的可用技能列表。

## 使用方法

### 查找技能

```
Run ~/.codex/superpowers/.codex/superpowers-codex find-skills
```

### 加载技能

```
Run ~/.codex/superpowers/.codex/superpowers-codex use-skill superpowers:brainstorming
```

### 引导所有技能

```
Run ~/.codex/superpowers/.codex/superpowers-codex bootstrap
```

这将加载包含所有技能信息的完整引导。

### 个人技能

在 `~/.codex/skills/` 中创建您自己的技能：

```bash
mkdir -p ~/.codex/skills/my-skill
```

创建 `~/.codex/skills/my-skill/SKILL.md`：

```markdown
---
name: my-skill
description: 当 [条件] 时使用 - [它的作用]
---

# My Skill

[此处填写您的技能内容]
```

同名的个人技能会覆盖 Superpowers 核心技能。

## 架构

### Codex CLI 工具

**位置：** `~/.codex/superpowers/.codex/superpowers-codex`

一个提供三个命令的 Node.js CLI 脚本：
- `bootstrap` - 加载包含所有技能的完整引导
- `use-skill <name>` - 加载特定技能
- `find-skills` - 列出所有可用技能

### 共享核心模块

**位置：** `~/.codex/superpowers/lib/skills-core.js`

Codex 实现使用共享的 `skills-core` 模块（ES 模块格式）进行技能发现和解析。这与 OpenCode 插件使用的是同一个模块，确保了跨平台行为的一致性。

### 工具映射

为 Claude Code 编写的技能通过以下映射适配 Codex：

- `TodoWrite` → `update_plan`
- 带有子代理的 `Task` → 告知用户子代理不可用，直接执行工作
- `Skill` 工具 → `~/.codex/superpowers/.codex/superpowers-codex use-skill`
- 文件操作 → Codex 原生工具

## 更新

```bash
cd ~/.codex/superpowers
git pull
```

## 故障排除

### 找不到技能

1. 验证安装：`ls ~/.codex/superpowers/skills`
2. 检查 CLI 是否工作：`~/.codex/superpowers/.codex/superpowers-codex find-skills`
3. 验证技能是否包含 SKILL.md 文件

### CLI 脚本不可执行

```bash
chmod +x ~/.codex/superpowers/.codex/superpowers-codex
```

### Node.js 错误

CLI 脚本需要 Node.js。请验证：

```bash
node --version
```

应显示 v14 或更高版本（建议使用 v18+ 以获得 ES 模块支持）。

## 获取帮助

- 报告问题：https://github.com/obra/superpowers/issues
- 主文档：https://github.com/obra/superpowers
- 博客文章：https://blog.fsck.com/2025/10/27/skills-for-openai-codex/

## 注意

Codex 支持目前处于实验阶段，可能需要根据用户反馈进行优化。如果您遇到问题，请在 GitHub 上报告。
