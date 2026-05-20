

## 智能体 (Agents)

Oh-My-OpenAgent 提供了 11 个专门的 AI 智能体。每个智能体都拥有独特的专业知识、经过优化的模型以及特定的工具权限。

### 核心智能体 (Core Agents)

核心智能体标签页的循环顺序由注入的运行时顺序字段决定。固定优先级顺序为：Sisyphus (0)、Hephaestus (1)、Prometheus (2) 和 Atlas (3)。其余智能体紧随其后。

| 智能体                            | 模型                  | 用途                                                                     |
| :----------------------------- | :------------------ | :--------------------------------------------------------------------- |
| **Sisyphus (西西弗斯)**            | `claude-opus-4-7`   | 默认调度器。计划、委派并执行复杂任务，支持子智能体的高强度并行执行。采用待办事项（Todo）驱动的工作流，具有扩展思考能力（32k 预算）。 |
| **Hephaestus (赫菲斯托斯)**         | `gpt-5.5`           | 合法工匠。受 AmpCode 深度模式启发的自主深度工作者。以目标为导向，在行动前进行彻底研究。探索代码库模式，端到端完成任务，不提前中止。 |
| **Oracle (先知)**                | `gpt-5.5`           | 架构决策、代码审查、调试。只读咨询，具有卓越的逻辑推理和深度分析能力。                                    |
| **Librarian (馆长)**             | `gpt-5.4-mini-fast` | 多仓库分析、文档查询、开源实现示例。对代码库有深度理解，提供基于证据的回答。                                 |
| **Explore (探索者)**              | `gpt-5.4-mini-fast` | 快速代码库探索和上下文 Grep。                                                      |
| **Multimodal-Looker (多模态查看者)** | `gpt-5.5`           | 视觉内容专家。分析 PDF、图像、图表以提取信息。                                              |
|                                |                     |                                                                        |

### 规划智能体 (Planning Agents)

| 智能体 | 模型 | 用途 |
| :--- | :--- | :--- |
| **Prometheus (普罗米修斯)** | `claude-opus-4-7` | 战略规划者，具备访谈模式。通过迭代提问创建详细的工作计划。 |
| **Metis (墨提斯)** | `claude-sonnet-4-6` | 计划顾问 —— 预规划分析。识别潜在意图、歧义和 AI 可能失败的点。 |
| **Momus (摩摩斯)** | `gpt-5.5` | 计划审查者 —— 根据清晰度、可验证性和完整性标准验证计划。 |

### 编排智能体 (Orchestration Agents)

| 智能体 | 模型 | 用途 |
| :--- | :--- | :--- |
| **Atlas (阿特拉斯)** | `claude-sonnet-4-6` | 待办事项编排者。有系统地执行计划任务，管理待办项并协调工作。 |
| **Sisyphus-Junior (小西西弗斯)** | _(取决于类别)_ | 类别生成的执行者。模型根据任务类别（视觉工程、快速、深度等）自动选择。 |

### 调用智能体

主智能体会自动调用这些智能体，但你也可以显式调用：

```
Ask @oracle to review this design and propose an architecture
(请 @oracle 审查此设计并提出架构建议)
Ask @librarian how this is implemented - why does the behavior keep changing?
(询问 @librarian 这是如何实现的 - 为什么行为一直在变？)
Ask @explore for the policy on this feature
(询问 @explore 关于此功能的策略)
```

### 工具限制

| 智能体 | 限制 |
| :--- | :--- |
| oracle | 只读：无法写入、编辑或委派（禁用：write, edit, task, call_omo_agent） |
| librarian | 无法写入、编辑或委派 |
| explore | 无法写入、编辑或委派 |
| multimodal-looker | 仅允许 `read` |
| atlas | 无法委派（禁用：task, call_omo_agent） |
| momus | 无法写入、编辑或委派 |

### 后台智能体 (Background Agents)

在后台运行智能体并继续你的工作：

- 让 GPT 调试的同时，Claude 尝试不同的方案。
- 让 Gemini 编写前端，Claude 处理后端。
- 发起大规模并行搜索，继续实现功能，在结果就绪时直接使用。

```
# 后台启动
task(subagent_type="explore", load_skills=[], prompt="Find auth implementations", run_in_background=true)

# 继续工作...
# 系统在完成时会通知

# 需要时检索结果
background_output(task_id="bg_abc123")
```

#### 带有 Tmux 的可视化多智能体

启用 `tmux.enabled` 以在独立的 tmux 窗格中查看后台智能体：

```json
{
  "tmux": {
    "enabled": true,
    "layout": "main-vertical"
  }
}
```

### 团队模式 (Team Mode - 实验性，默认关闭)

模仿 Claude Code 的实验性智能体团队（Agent Teams）开发的并行多智能体协作模式。通过 `team_mode.enabled: true` 启用。

## 类别系统 (Category System)

类别是针对特定领域优化的智能体配置预设。

- **类别 (Category)**: “这是什么样的工作？”（决定模型、温度、提示词心态）
- **技能 (Skill)**: “需要什么工具和知识？”（注入专门知识、MCP 工具、工作流）

### 内置类别

| 类别 | 默认模型 | 用途 |
| :--- | :--- | :--- |
| `visual-engineering` | `google/gemini-3.1-pro` | 前端、UI/UX、设计、样式、动画 |
| `ultrabrain` | `openai/gpt-5.5` (xhigh) | 深度逻辑推理，复杂的架构决策 |
| `deep` | `openai/gpt-5.5` (medium) | 针对棘手问题的自主解决。单次调用仅限一个目标。 |
| `quick` | `openai/gpt-5.4-mini` | 琐碎任务 —— 单文件更改、拼写修复等 |
| `writing` | `google/gemini-3-flash` | 文档、散文、技术写作 |

### 使用方法

在调用 `task` 工具时指定 `category` 参数。

```typescript
task({
  category: "visual-engineering",
  prompt: "Add a responsive chart component to the dashboard page",
});
```

## 高级配置

### 回退模型 (Fallback Models)

为每个智能体配置回退链：

```jsonc
{
  "agents": {
    "sisyphus": {
      "fallback_models": [
        "opencode/glm-5",
        { "model": "openai/gpt-5.5", "variant": "high" }
      ]
    }
  }
}
```

### 会话恢复 (Session Recovery)

系统会自动从常见的会话失败中恢复，无需用户干预：
- 修复缺失的工具结果
- 处理思考块 (Thinking block) 违规
- 自动压缩超出上下文窗口的消息

## 技能 (Skills)

技能提供了带有嵌入式 MCP 服务器和详细指令的专门工作流。

### 内置技能

| 技能 | 触发点 | 描述 |
| :--- | :--- | :--- |
| **git-master** | commit, rebase, squash 等 | Git 专家。检测提交风格，拆分原子提交，制定变基策略。 |
| **playwright** | 浏览器任务、测试、截图 | 通过 Playwright MCP 进行浏览器自动化。 |
| **frontend-ui-ux** | UI/UX 任务、样式 | 设计师兼开发者人格。即便没有原型也能创作出精美的 UI。 |
| **review-work** | "review work" 等 | 审查编排者。启动 5 个并行后台智能体进行代码质量、安全等全方位检查。 |
| **ai-slop-remover**| "remove AI slop" | 移除文件中的 AI 生成痕迹（冗余注释、过度工程等），同时保留功能。 |

## 命令 (Commands)

命令是由斜杠 (`/`) 触发的预定义工作流。

| 命令 | 描述 |
| :--- | :--- |
| `/init-deep` | 初始化分层级的 AGENTS.md 知识库 |
| `/ralph-loop` | 开启自引用开发循环，直到任务完成 |
| `/ulw-loop` | 以最高强度开启循环（Ultrawork 模式） |
| `/refactor` | 利用 LSP、AST-grep 等工具进行智能重构 |
| `/handoff` | 创建详细的上下文摘要，以便在新会话中继续工作 |

## 工具 (Tools)

### 代码编辑工具
- **edit**: 基于哈希锚点的编辑工具。使用 `LINE#ID` 格式进行精确、安全的修改，防止在过时的代码版本上操作。

### LSP 工具 (智能 IDE 功能)
- **lsp_rename**: 全局重命名。
- **lsp_goto_definition**: 跳转到定义。
- **lsp_find_references**: 查找引用。

### AST-Grep 工具
- **ast_grep_search**: 感知语法树的代码模式搜索（支持 25 种语言）。

### 任务管理工具 (Task System)
需要开启 `experimental.task_system: true`。不同于简单的 Todo，它支持任务间的依赖关系（`blockedBy`）和并行执行。

## 钩子 (Hooks)

钩子在智能体生命周期的关键点拦截并修改行为。

- **comment-checker**: 运行评论检查器，阻止 AI 风格的废话评论。
- **write-existing-file-guard**: 防止在未读取文件的情况下意外覆盖现有文件。
- **runtime-fallback**: 在遇到 API 错误或限流时自动切换到备选模型。

## MCP (Model Context Protocol)

支持三层架构：
1. 内置远程 MCP（websearch, context7, grep_app）。
2. Claude Code 风格的 `.mcp.json` 加载器（支持环境变量）。
3. `SKILL.md` 中声明的嵌入式 MCP 服务器。

### 带有 OAuth 的 MCP
技能可以定义受 OAuth 保护的远程 MCP 服务器，支持自动发现、PKCE 和动态客户端注册。

## 上下文注入 (Context Injection)

### 目录 AGENTS.md
读取文件时会自动注入该目录及上级目录的 `AGENTS.md` 文件：
`项目根目录/AGENTS.md` -> `src/AGENTS.md` -> `src/components/AGENTS.md`。

### 条件规则
从 `.claude/rules/` 注入匹配 glob 模式的规则。

## Claude Code 兼容性

完全兼容 Claude Code 的配置层。可以加载其命令、技能、智能体和 `settings.json` 中的钩子。可以通过配置禁用特定的兼容项。