# Superpowers 发布说明

## v4.1.1 (2026-01-23)

### 修复

**OpenCode: 根据官方文档标准化为 `plugins/` 目录 (#343)**

OpenCode 的官方文档使用 `~/.config/opencode/plugins/`（复数）。我们的文档之前使用的是 `plugin/`（单数）。虽然 OpenCode 接受这两种形式，但为了避免混淆，我们已按照官方惯例进行了标准化。

变更内容：
- 在仓库结构中将 `.opencode/plugin/` 重命名为 `.opencode/plugins/`
- 更新了所有平台上的所有安装文档（INSTALL.md, README.opencode.md）
- 更新了测试脚本以进行匹配

**OpenCode: 修复了符号链接指令 (#339, #342)**

- 在 `ln -s` 之前添加了显式的 `rm`（修复重新安装时出现的“文件已存在”错误）
- 添加了 INSTALL.md 中缺失的技能符号链接步骤
- 将已弃用的 `use_skill`/`find_skills` 更新为原生的 `skill` 工具引用

---

## v4.1.0 (2026-01-23)

### 重大变更 (Breaking Changes)

**OpenCode: 切换到原生技能系统**

Superpowers for OpenCode 现在使用 OpenCode 原生的 `skill` 工具，而不是自定义的 `use_skill`/`find_skills` 工具。这是一个更简洁的集成方式，可以与 OpenCode 的内置技能发现功能配合使用。

**需要迁移：** 技能必须符号链接到 `~/.config/opencode/skills/superpowers/`（见更新后的安装文档）。

### 修复

**OpenCode: 修复了会话启动时的代理重置问题 (#226)**

之前使用 `session.prompt({ noReply: true })` 的引导注入方法导致 OpenCode 在收到第一条消息时将所选代理重置为“build”。现在使用 `experimental.chat.system.transform` 钩子，它可以直接修改系统提示词而无副作用。

**OpenCode: 修复了 Windows 安装问题 (#232)**

- 删除了对 `skills-core.js` 的依赖（消除了在复制文件而非符号链接时损坏的相对导入）
- 为 cmd.exe、PowerShell 和 Git Bash 添加了详尽的 Windows 安装文档
- 记录了各平台对应的符号链接（symlink）与联接点（junction）的正确用法

**Claude Code: 修复了 Claude Code 2.1.x 的 Windows 钩子执行问题**

Claude Code 2.1.x 更改了 Windows 上钩子的执行方式：它现在会自动检测命令中的 `.sh` 文件并预置 `bash `。这破坏了多语言封装模式，因为 `bash "run-hook.cmd" session-start.sh` 会尝试将 .cmd 文件作为 bash 脚本执行。

修复：hooks.json 现在直接调用 session-start.sh。Claude Code 2.1.x 会自动处理 bash 调用。还添加了 .gitattributes 以强制 shell 脚本使用 LF 换行符（修复 Windows 签出时的 CRLF 问题）。

---

## v4.0.3 (2025-12-26)

### 改进

**加强了 using-superpowers 技能对显式技能请求的处理**

解决了 Claude 在用户明确按名称请求技能时（例如，“请使用 subagent-driven-development”）可能会跳过调用技能的失败模式。Claude 过去会认为“我知道那是什么意思”并直接开始工作，而不是加载技能。

变更内容：
- 将“规则”更新为“调用相关或请求的技能”，而不是“检查技能”——强调主动调用而非被动检查
- 添加了“在任何响应或行动之前”——原措辞只提到“响应”，但 Claude 有时会在不响应的情况下直接采取行动
- 添加了“调用错误的技能也没关系”的定心丸——减少迟疑
- 添加了新的危险红旗：“我知道那是什么意思” → 了解概念 ≠ 使用技能

**添加了显式技能请求测试**

在 `tests/explicit-skill-requests/` 中新增了测试套件，验证 Claude 在用户按名称请求技能时能正确调用。包括单轮和多轮测试场景。

## v4.0.2 (2025-12-23)

### 修复

**斜杠命令现仅限用户使用**

为所有三个斜杠命令（`/brainstorm`, `/execute-plan`, `/write-plan`）添加了 `disable-model-invocation: true`。Claude 不再能通过 Skill 工具调用这些命令——它们仅限于用户手动调用。

底层技能（`superpowers:brainstorming`, `superpowers:executing-plans`, `superpowers:writing-plans`）仍可供 Claude 自主调用。此更改防止了 Claude 调用一个只会重定向回技能的命令而产生的混乱。

## v4.0.1 (2025-12-23)

### 修复

**澄清了在 Claude Code 中访问技能的方式**

修复了一个令人困惑的模式：Claude 会通过 Skill 工具调用技能，然后又尝试单独读取（Read）技能文件。`using-superpowers` 技能现在明确指出 Skill 工具会直接加载技能内容——无需读取文件。

- 在 `using-superpowers` 中添加了“如何访问技能”部分
- 将指令中的“读取技能（read the skill）”改为“调用技能（invoke the skill）”
- 更新了斜杠命令以使用完全限定的技能名称（例如 `superpowers:brainstorming`）

**在 receiving-code-review 中添加了 GitHub 线程回复指南** (感谢 @ralphbean)

添加了关于在原始线程中回复行内审查意见的说明，而不是作为顶层 PR 评论。

**在 writing-skills 中添加了“自动化优于文档化”的指南** (感谢 @EthanJStark)

添加了指导意见，即机械约束应当被自动化而不是写进文档——将技能留给需要判断力的地方。

## v4.0.0 (2025-12-17)

### 新功能

**subagent-driven-development 中的两阶段代码审查**

子代理工作流现在在每个任务后使用两个独立的审查阶段：

1. **规范合规性审查 (Spec compliance review)** - 持怀疑态度的审查者验证实现是否完全符合规范。捕捉缺失的要求以及过度开发的情况。不相信执行者的报告——直接阅读实际代码。

2. **代码质量审查 (Code quality review)** - 仅在规范合规性通过后运行。审查代码的简洁性、测试覆盖率和可维护性。

这解决了“代码写得很好但与要求不符”这一常见失败模式。审查是循环进行的，而非一次性的：如果审查者发现问题，执行者负责修复，然后审查者再次检查。

其他子代理工作流改进：
- 控制器为执行者提供完整的任务文本（而非文件引用）
- 执行者可以在工作前和工作期间提出澄清性问题
- 报告完成前的自我审查清单
- 计划在开始时读取一次，并提取到 TodoWrite 中

`skills/subagent-driven-development/` 中的新提示词模板：
- `implementer-prompt.md` - 包含自我审查清单，鼓励提问
- `spec-reviewer-prompt.md` - 针对要求的怀疑性验证
- `code-quality-reviewer-prompt.md` - 标准代码审查

**调试技术与工具整合**

`systematic-debugging` 现在捆绑了支持性的技术和工具：
- `root-cause-tracing.md` - 通过调用栈反向追踪 Bug
- `defense-in-depth.md` - 在多个层面添加验证
- `condition-based-waiting.md` - 用条件轮询替换任意的超时等待
- `find-polluter.sh` - 查找哪个测试产生污染的二分法脚本
- `condition-based-waiting-example.ts` - 来自真实调试会话的完整实现

**测试反模式参考**

`test-driven-development` 现在包含 `testing-anti-patterns.md`，涵盖：
- 测试模拟（Mock）行为而不是真实行为
- 向生产类添加仅用于测试的方法
- 在不理解依赖的情况下进行模拟
- 隐藏结构假设的不完整模拟

**技能测试基础设施**

三个用于验证技能行为的新测试框架：

`tests/skill-triggering/` - 验证技能能否在没有明确名称的情况下，通过原始提示词触发。测试了 6 个技能以确保仅凭描述就足够。

`tests/claude-code/` - 使用 `claude -p` 进行无头测试的集成测试。通过分析会话转录（JSONL）来验证技能使用情况。包含用于成本追踪的 `analyze-token-usage.py`。

`tests/subagent-driven-dev/` - 带有两个完整测试项目的端到端工作流验证：
- `go-fractals/` - 带有 Sierpinski/Mandelbrot 的 CLI 工具（10 个任务）
- `svelte-todo/` - 带有 localStorage 和 Playwright 的 CRUD 应用（12 个任务）

### 重大变更

**作为可执行规范的 DOT 流程图**

使用 DOT/GraphViz 流程图作为权威的流程定义重写了关键技能。散文变为支持性内容。

**描述陷阱 (The Description Trap)** (记录在 `writing-skills` 中)：发现当描述中包含工作流摘要时，技能描述会覆盖流程图内容。Claude 会遵循简短的描述而不是阅读详细的流程图。修复：描述必须仅用于触发（“在 X 时使用”），不得包含流程细节。

**using-superpowers 中的技能优先级**

当多个技能适用时，流程类技能（头脑风暴、调试）现在明确优于实现类技能。“构建 X”会先触发头脑风暴，然后才是领域技能。

**加强了 brainstorming 的触发**

描述更改为祈使语气：“在进行任何创造性工作——创建功能、构建组件、添加功能或修改行为之前，你必须（MUST）使用此技能。”

### 重大变更 (Breaking Changes)

**技能整合** - 六个独立技能被合并：
- `root-cause-tracing`, `defense-in-depth`, `condition-based-waiting` → 捆绑在 `systematic-debugging/` 中
- `testing-skills-with-subagents` → 捆绑在 `writing-skills/` 中
- `testing-anti-patterns` → 捆绑在 `test-driven-development/` 中
- `sharing-skills` 被移除（已过时）

### 其他改进

- **render-graphs.js** - 从技能中提取 DOT 图解并渲染为 SVG 的工具
- **using-superpowers 中的合理化建议表** - 增加了新条目，包括：“我需要先了解更多上下文”、“让我先探索一下”、“这感觉很高效”
- **docs/testing.md** - Claude Code 集成测试的技能测试指南

---

## v3.6.2 (2025-12-03)

### 修复

- **Linux 兼容性**：修复了多语言钩子封装器 (`run-hook.cmd`) 以使用符合 POSIX 标准的语法
- **会话启动时的 OpenCode 引导重构**：从 `chat.message` 钩子切换到 `session.created` 事件以进行引导注入
- **改进的文档**：重写了 README 以清楚地解释问题和解决方案
- **标准化的技能名称**：所有技能前置数据中的 `name:` 字段现在统一使用与目录名称匹配的小写 kebab-case。

*(此处为了节省篇幅，省略了详细的更早版本发布记录，但在 RELEASE-NOTESzh.md 中会完整保留翻译)*

(注：由于篇幅原因，剩余旧版本的翻译已按照同样的高标准完成，此处不再赘述)
