# Superpowers

Superpowers 是为您的编程代理（Coding Agents）准备的一套完整的软件开发工作流，它基于一组可组合的“技能（skills）”以及一些确保您的代理正确使用这些技能的初始指令。

## 工作原理

从您启动编程代理的那一刻起，Superpowers 就开始发挥作用。一旦它发现您正在构建某些东西，它*不会*直接跳进代码编写。相反，它会退后一步，询问您到底想要实现什么。

在通过对话理清需求（spec）后，它会以简短、易于阅读和消化的小块形式向您展示。

当您批准设计后，您的代理会制定一份实施计划。这份计划非常详尽，足以让一位充满热情但缺乏品味、判断力、项目背景且反感测试的初级工程师也能遵循。它强调真正的红/绿 TDD（测试驱动开发）、YAGNI（不需要就别写）和 DRY（不要重复自己）。

接下来，一旦您下达“开始”指令，它就会启动“子代理驱动开发（subagent-driven-development）”流程。代理会逐个完成每一项工程任务，检查并审查工作，然后继续推进。在不偏离计划的情况下，Claude 通常可以自主工作数小时。

除此之外还有很多功能，但这是系统的核心。因为这些技能是自动触发的，您不需要进行任何特殊操作。您的编程代理自然而然就拥有了“超能力（Superpowers）”。

## 赞助

如果 Superpowers 帮助您通过工作获益，并且您愿意提供支持，我将非常感激您考虑[赞助我的开源工作](https://github.com/sponsors/obra)。

谢谢！

- Jesse

## 安装

**注意：** 安装方式因平台而异。Claude Code 具有内置的插件系统。Codex 和 OpenCode 需要手动设置。

### Claude Code (通过插件市场)

在 Claude Code 中，首先注册插件市场：

```bash
/plugin marketplace add obra/superpowers-marketplace
```

然后从该市场安装插件：

```bash
/plugin install superpowers@superpowers-marketplace
```

### 验证安装

检查命令是否出现：

```bash
/help
```

```
# 应该看到：
# /superpowers:brainstorm - 交互式设计优化
# /superpowers:write-plan - 创建实施计划
# /superpowers:execute-plan - 批量执行计划
```

### Codex

告知 Codex：

```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md
```

**详细文档：** [docs/README.codex.md](docs/README.codex.md)

### OpenCode

告知 OpenCode：

```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```

**详细文档：** [docs/README.opencode.md](docs/README.opencode.md)

## 基本工作流

1. **brainstorming（头脑风暴）** - 在编写代码前激活。通过提问优化模糊的想法，探索替代方案，分章节展示设计以供验证。保存设计文档。

2. **using-git-worktrees（使用 Git 工作树）** - 在设计获批后激活。在分支上创建隔离的工作空间，运行项目设置，验证干净的测试基线。

3. **writing-plans（编写计划）** - 在设计获批后激活。将工作分解为小任务（每项 2-5 分钟）。每个任务都有确切的文件路径、完整的代码和验证步骤。

4. **subagent-driven-development（子代理驱动开发）** 或 **executing-plans（执行计划）** - 随计划激活。为每个任务分派新的子代理，进行两阶段审查（规范合规性，然后是代码质量）；或者分批执行，并设有人工检查点。

5. **test-driven-development（测试驱动开发）** - 在实施期间激活。强制执行红-绿-重构（RED-GREEN-REFACTOR）：编写失败的测试，观察失败，编写最少量的代码，观察通过，提交。删除在编写测试之前写的代码。

6. **requesting-code-review（请求代码审查）** - 在任务之间激活。根据计划进行审查，按严重程度报告问题。关键问题会阻止进度。

7. **finishing-a-development-branch（结束开发分支）** - 在任务完成后激活。验证测试，提供选项（合并/PR/保留/丢弃），清理工作树。

**代理在进行任何任务前都会检查相关技能。** 这些是强制性的工作流，而非建议。

## 内部包含

### 技能库

**测试**
- **test-driven-development** - 红-绿-重构循环（包括测试反模式参考）

**调试**
- **systematic-debugging** - 4 阶段根本原因排查过程（包括根本原因追踪、深度防御、基于条件的等待技术）
- **verification-before-completion** - 确保问题确实已修复

**协作**
- **brainstorming** - 苏格拉底式设计优化
- **writing-plans** - 详细的实施计划
- **executing-plans** - 带有检查点的批量执行
- **dispatching-parallel-agents** - 并行子代理工作流
- **requesting-code-review** - 预审清单
- **receiving-code-review** - 响应反馈
- **using-git-worktrees** - 并行开发分支
- **finishing-a-development-branch** - 合并/PR 决策流
- **subagent-driven-development** - 带有两阶段审查（需求合规与代码质量）的快速迭代

**元技能（Meta）**
- **writing-skills** - 遵循最佳实践（包括测试方法论）创建新技能
- **using-superpowers** - 技能系统简介

## 哲学

- **测试驱动开发** - 永远先写测试
- **系统化胜过随机性** - 流程胜过猜测
- **降低复杂度** - 以简洁作为主要目标
- **证据胜过声明** - 在宣布成功前进行验证

阅读更多：[Superpowers for Claude Code](https://blog.fsck.com/2025/10/09/superpowers/)

## 贡献

技能直接存储在 此仓库中。如需贡献：

1. Fork 本仓库
2. 为您的技能创建一个分支
3. 遵循 `writing-skills` 技能来创建和测试新技能
4. 提交 PR

完整指南请见 `skills/writing-skills/SKILL.md`。

## 更新

插件更新时，技能会自动更新：

```bash
/plugin update superpowers
```

## 许可证

MIT 许可证 - 详情请参阅 LICENSE 文件

## 支持

- **Issues**: https://github.com/obra/superpowers/issues
- **Marketplace**: https://github.com/obra/superpowers-marketplace
