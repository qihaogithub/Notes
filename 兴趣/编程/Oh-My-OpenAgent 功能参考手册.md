# Oh-My-OpenAgent 功能参考手册

## 智能体（Agents）
Oh-My-OpenAgent 提供 11 款专业级 AI 智能体，每款均具备专属专业能力、优化模型及工具使用权限。

### 核心智能体
核心智能体的标签切换机制通过注入运行时优先级字段实现确定性排序，固定优先级顺序为：西西弗斯（Sisyphus，优先级：0）、赫菲斯托斯（Hephaestus，优先级：1）、普罗米修斯（Prometheus，优先级：2）、阿特拉斯（Atlas，优先级：3）。其余智能体均遵循此核心稳定排序规则。

| 智能体名称                         | 模型                  | 用途说明                                                                                                                                              |                                      |                                              |                |                                                          |                               |                |                                               |                                          |
| ----------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | -------------------------------------------- | -------------- | -------------------------------------------------------- | ----------------------------- | -------------- | --------------------------------------------- | ---------------------------------------- |
| **西西弗斯（Sisyphus）**            | `claude-opus-4-7`   | 默认编排智能体。通过专业子智能体规划、委派并执行复杂任务，支持高并发并行执行。基于待办事项（Todo）驱动的工作流，具备扩展思考能力（32k 令牌预算）。降级备选模型链：`opencode-go/kimi-k2.6` → `kimi-for-coding/k2p5` → `opencode | moonshotai                           | moonshotai-cn                                | firmware       | ollama-cloud                                             | aihubmix/kimi-k2.5` → `openai | github-copilot | opencode/gpt-5.5 (medium)` → `zai-coding-plan | opencode/glm-5` → `opencode/big-pickle`。 |
| **赫菲斯托斯（Hephaestus）**         | `gpt-5.5`           | "正统工匠"智能体。受 AmpCode 深度模式启发的自主深度工作智能体。行动前开展充分调研，以目标为导向执行任务。深度探索代码库模式，端到端完成任务，杜绝提前终止。以希腊锻造与工艺之神命名，需兼容 GPT 系列的模型提供商支持。                               |                                      |                                              |                |                                                          |                               |                |                                               |                                          |
| **神谕者（Oracle）**               | `gpt-5.5`           | 负责架构决策、代码评审、调试工作。只读模式的咨询智能体，具备卓越的逻辑推理与深度分析能力。受 AmpCode 启发。降级备选模型链：`google                                                                         | github-copilot                       | opencode/gemini-3.1-pro (high)` → `anthropic | github-copilot | opencode/claude-opus-4-7 (max)` → `opencode-go/glm-5.1`。 |                               |                |                                               |                                          |
| **图书管理员（Librarian）**          | `gpt-5.4-mini-fast` | 多代码库分析、文档检索、开源项目实现案例参考。深度理解代码库，提供基于实证的答案。降级备选模型链：`opencode-go/qwen3.5-plus` → `opencode-go/minimax-m2.7` → `anthropic                             | opencode/claude-haiku-4-5` → `openai | opencode/gpt-5.4-nano`。                      |                |                                                          |                               |                |                                               |                                          |
| **探索者（Explore）**              | `gpt-5.4-mini-fast` | 快速代码库探索与上下文检索（grep）。降级备选模型链：`opencode-go/qwen3.5-plus` → `opencode-go/minimax-m2.7` → `anthropic                                                  | opencode/claude-haiku-4-5` → `openai | opencode/gpt-5.4-nano`。                      |                |                                                          |                               |                |                                               |                                          |
| **多模态观察者（Multimodal-Looker）** | `gpt-5.5`           | 视觉内容专业智能体。分析 PDF、图片、图表以提取信息。降级备选模型链：`opencode-go/kimi-k2.6` → `zai-coding-plan/glm-4.6v` → `openai                                                | github-copilot                       | opencode/gpt-5-nano`。                        |                |                                                          |                               |                |                                               |                                          |

### 规划类智能体

| 智能体名称       | 模型                  | 用途说明                                                                                                                                 |
| ---------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **普罗米修斯（Prometheus）** | `claude-opus-4-7`     | 带访谈模式的战略规划智能体。通过迭代式提问制定详细工作计划。降级备选模型链：`openai|github-copilot|opencode/gpt-5.5 (high)` → `opencode-go/glm-5.1` → `google|github-copilot|opencode/gemini-3.1-pro`。|
| **墨提斯（Metis）** | `claude-sonnet-4-6`   | 规划顾问——规划前分析。识别隐藏意图、模糊表述及 AI 失效风险点。降级备选模型链：`anthropic|github-copilot|opencode/claude-opus-4-7 (max)` → `openai|github-copilot|opencode/gpt-5.5 (high)` → `opencode-go/glm-5.1` → `kimi-for-coding/k2p5`。|
| **摩墨斯（Momus）** | `gpt-5.5`             | 规划评审员——验证计划是否符合清晰性、可验证性、完整性标准。降级备选模型链：`anthropic|github-copilot|opencode/claude-opus-4-7 (max)` → `google|github-copilot|opencode/gemini-3.1-pro (high)` → `opencode-go/glm-5.1`。|

### 编排类智能体

| 智能体名称               | 模型                  | 用途说明                                                                                                                                  |
| ------------------------ | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **阿特拉斯（Atlas）**    | `claude-sonnet-4-6`   | 待办事项编排智能体。系统化执行已规划任务，管理待办项并协调工作流程。降级备选模型链：`opencode-go/kimi-k2.6` → `openai|github-copilot|opencode/gpt-5.5 (medium)` → `opencode-go/minimax-m2.7`。|
| **小西西弗斯（Sisyphus-Junior）** | _(按任务类别适配)_ | 按类别生成的执行智能体。模型根据任务类别（视觉工程、快速任务、深度任务等）自动选择。内置通用降级备选模型链：`anthropic|github-copilot|opencode/claude-sonnet-4-6` → `opencode-go/kimi-k2.6` → `openai|github-copilot|opencode/gpt-5.5 (medium)` → `opencode-go/minimax-m2.7` → `opencode/big-pickle`。|

### 智能体调用方式
主智能体会自动调用上述子智能体，也可通过指令显式调用：

```
请 @oracle（神谕者）评审此设计并提出架构方案
请 @librarian（图书管理员）说明此功能的实现方式——为何行为频繁变化？
请 @explore（探索者）查询此功能的相关规范
```

### 工具使用限制

| 智能体名称              | 限制说明                                                                 |
| ----------------------- | ------------------------------------------------------------------------ |
| 神谕者（oracle）| 只读权限：禁止写入、编辑、委派任务（禁用工具：write、edit、task、call_omo_agent） |
| 图书管理员（librarian） | 禁止写入、编辑、委派任务（禁用工具：write、edit、task、call_omo_agent）    |
| 探索者（explore）| 禁止写入、编辑、委派任务（禁用工具：write、edit、task、call_omo_agent）    |
| 多模态观察者（multimodal-looker） | 仅允许列表：仅开放 `read` 权限                                           |
| 阿特拉斯（atlas）| 禁止委派任务（禁用工具：task、call_omo_agent）                            |
| 摩墨斯（momus）| 禁止写入、编辑、委派任务（禁用工具：write、edit、task）                    |

### 后台智能体
可在后台运行智能体并继续其他工作：

- 让 GPT 调试代码的同时，Claude 尝试不同解决方案
- Gemini 编写前端代码，Claude 处理后端逻辑
- 启动大规模并行检索任务，继续核心开发，待结果返回后直接使用

```
# 启动后台任务
task(subagent_type="explore", load_skills=[], prompt="查找认证功能实现方案", run_in_background=true)

# 继续其他工作...
# 任务完成时系统会发送通知

# 需要时获取结果
background_output(task_id="bg_abc123")
```

#### 基于 Tmux 的可视化多智能体
启用 `tmux.enabled` 配置后，可在独立 Tmux 面板中查看后台智能体运行状态：

```json
{
  "tmux": {
    "enabled": true,
    "layout": "main-vertical"
  }
}
```

在 Tmux 环境中运行时：
- 后台智能体在新面板中启动
- 实时查看多个智能体的工作过程
- 每个面板实时展示对应智能体的输出内容
- 智能体完成任务后自动清理面板
- **稳定的智能体排序**：核心智能体标签切换默认顺序为西西弗斯、赫菲斯托斯、普罗米修斯、阿特拉斯，可通过 `agent_order` 自定义

在 cmux 环境中运行时（`cmux omo`），面板集成功能通过 cmux 的 Tmux 兼容命令实现。OMO 会从 `CMUX_SOCKET_PATH` 环境变量或 cmux 提供的 `TMUX` 值检测 cmux 环境，因此即使未安装原生 `tmux` 二进制文件，`tmux.enabled` 仍可创建 cmux 面板。

可在 `oh-my-opencode.jsonc` 中自定义智能体模型、提示词及权限配置。

### 团队模式（实验性，默认关闭）
借鉴 Claude Code 实验性 Agent Teams 实现的并行多智能体协作模式。通过 `team_mode.enabled: true` 启用。提供 12 个 `team_*` 工具，支持创建 1 个主导智能体 + 最多 8 个成员智能体，包含共享延迟确认邮箱、带文件锁声明的共享任务列表、可选的成员专属 Git 工作区，以及可选的 Tmux 布局（将每个成员的会话输出流式传输至专属面板）。

详见 **[团队模式指南](../guide/team-mode.md)** 了解配置方式、团队规格格式、生命周期、边界限制及存储布局。

### 架构快照（当前版本）
- **功能模块**：`src/features/` 目录包含 20 个模块
- **工具系统**：`src/tools/` 目录包含 16 个工具目录，根据配置开关可生成 **20 至 39 个工具**
- **钩子系统**：5 层组合架构包含 **54 个基础钩子**；启用团队模式后增至 **61 个**（新增工具防护 + 转换逻辑 + 团队会话事件直接处理器）
- **MCP 系统**：3 层架构：内置远程 MCP（`websearch`、`context7`、`grep_app`）、`.mcp.json` 加载器、以及从 `SKILL.md` 前置元数据加载的技能嵌入式 MCP
- **管理器**：插件启动时创建 4 个管理器：TmuxSessionManager（Tmux 会话管理器）、BackgroundManager（后台任务管理器）、SkillMcpManager（技能 MCP 管理器）、ConfigHandler（配置处理器）
- **配置流水线**：6 个执行阶段（按顺序）：提供商配置 → 插件组件 → 智能体 → 工具 → MCP → 命令
- **标准核心智能体顺序**：西西弗斯、赫菲斯托斯、普罗米修斯、阿特拉斯
- **OpenClaw**：双向集成 Discord、Telegram、HTTP 及 Shell，含回复监听守护进程

## 任务分类系统（Category System）
任务分类是针对特定领域优化的智能体配置预设。相较于将所有任务委派给单一 AI 智能体，调用适配任务属性的专业智能体效率更高。

### 分类的定义与价值
- **分类（Category）**："这是何种类型的工作？"（决定模型选择、温度参数、提示词思维模式）
- **技能（Skill）**："需要哪些工具和知识？"（注入专业知识、MCP 工具、工作流程）

通过组合这两个维度，可通过 `task` 工具生成最优适配的智能体。

### 内置分类

| 分类名称            | 默认模型                  | 适用场景                                                                 |
| ------------------- | ------------------------- | ------------------------------------------------------------------------ |
| `visual-engineering`（视觉工程） | `google/gemini-3.1-pro`   | 前端开发、UI/UX 设计、样式开发、动画效果                                 |
| `ultrabrain`（超脑） | `openai/gpt-5.5` (xhigh)  | 深度逻辑推理、需大量分析的复杂架构决策                                   |
| `deep`（深度任务）| `openai/gpt-5.5` (medium) | 面向目标的自主解决复杂问题，需深度调研。每次调用仅含**一个目标 + 一个交付物**——多目标需拆分为并行 `deep` 调用，禁止合并为单次调用。 |
| `artistry`（创意设计） | `google/gemini-3.1-pro` (high) | 高创意/艺术性任务、创新想法生成                                           |
| `quick`（快速任务）| `openai/gpt-5.4-mini`     | 简单任务 - 单文件修改、拼写错误修复、简单功能调整                         |
| `unspecified-low`（未指定-低优先级） | `anthropic/claude-sonnet-4-6` | 不匹配其他分类、低工作量任务                                             |
| `unspecified-high`（未指定-高优先级） | `anthropic/claude-opus-4-7` (max) | 不匹配其他分类、高工作量任务                                             |
| `writing`（文档创作） | `google/gemini-3-flash`   | 文档编写、散文创作、技术文档撰写                                         |

### 使用方式
调用 `task` 工具时指定 `category` 参数：

```typescript
task({
  category: "visual-engineering",
  prompt: "为仪表盘页面添加响应式图表组件",
});
```

### 自定义分类
可在插件配置文件中定义自定义分类。在重命名过渡阶段，`oh-my-openagent.json[c]` 和旧版 `oh-my-opencode.json[c]` 文件名均会被识别。

#### 分类配置架构

| 字段名              | 类型    | 说明                                                                 |
| ------------------- | ------- | -------------------------------------------------------------------- |
| `description`       | 字符串  | 分类用途的易读描述，会显示在任务提示词中                             |
| `model`             | 字符串  | 使用的 AI 模型 ID（例如：`anthropic/claude-opus-4-7`）               |
| `variant`           | 字符串  | 模型变体（例如：`max`、`xhigh`）                                     |
| `temperature`       | 数字    | 创意度（0.0 ~ 2.0），值越低结果越确定                                |
| `top_p`             | 数字    | 核采样参数（0.0 ~ 1.0）                                              |
| `prompt_append`     | 字符串  | 选择此分类时追加到系统提示词的内容                                   |
| `thinking`          | 对象    | 思考模型配置（`{ type: "enabled", budgetTokens: 16000 }`）           |
| `reasoningEffort`   | 字符串  | 推理力度等级（`low`、`medium`、`high`）                              |
| `textVerbosity`     | 字符串  | 文本冗余度等级（`low`、`medium`、`high`）                            |
| `tools`             | 对象    | 工具使用控制（通过 `{ "tool_name": false }` 禁用特定工具）            |
| `maxTokens`         | 数字    | 最大响应令牌数                                                       |
| `is_unstable_agent` | 布尔值  | 标记智能体为不稳定状态 - 强制启用后台模式以便监控                    |

#### 配置示例

```jsonc
{
  "categories": {
    // 1. 定义全新自定义分类
    "korean-writer": {
      "model": "google/gemini-3-flash",
      "temperature": 0.5,
      "prompt_append": "你是一名韩语技术文档撰写师，保持友好且清晰的语气。",
    },

    // 2. 覆盖现有分类（修改模型）
    "visual-engineering": {
      "model": "openai/gpt-5.5",
      "temperature": 0.8,
    },

    // 3. 配置思考模型并限制工具使用
    "deep-reasoning": {
      "model": "anthropic/claude-opus-4-7",
      "thinking": {
        "type": "enabled",
        "budgetTokens": 32000,
      },
      "tools": {
        "websearch_web_search_exa": false,
      },
    },
  },
}
```

### 小西西弗斯（Sisyphus-Junior）：委派执行智能体
选择分类后，由专属智能体**小西西弗斯（Sisyphus-Junior）** 执行任务：
- **核心特征**：禁止将任务**二次委派**给其他智能体
- **设计目的**：防止无限委派循环，确保聚焦完成分配的任务

## 高级配置

### 重命名兼容性
发布包和二进制文件仍保留 `oh-my-opencode` 名称。在 `opencode.json` 中，兼容层优先读取插件配置项 `oh-my-openagent`，同时仍加载旧版 `oh-my-opencode` 配置项并给出警告。插件配置文件（`oh-my-openagent.json[c]` 或旧版 `oh-my-opencode.json[c]`）在过渡阶段均会被识别。运行 `bunx oh-my-opencode doctor` 可检查旧版包名相关警告。

### 降级备选模型
可为每个智能体配置降级备选模型链，支持混合纯模型字符串和模型配置对象：

```jsonc
{
  "agents": {
    "sisyphus": {
      "fallback_models": [
        "opencode/glm-5",
        { "model": "openai/gpt-5.5", "variant": "high" },
        { "model": "anthropic/claude-sonnet-4-6", "thinking": { "type": "enabled", "budgetTokens": 64000 } }
      ]
    }
  }
}
```

当某模型调用出错时，运行时会按配置的备选列表依次尝试。对象形式的配置项允许精细调优备用模型，而非仅替换模型名称。

插件采用两套独立的降级机制：
- **model-fallback（模型降级）**：在聊天参数中主动选择模型链
- **runtime-fallback（运行时降级）**：在提供商/API 行为导致运行时失败后被动恢复

### 文件式提示词
可通过 `prompt` 字段中的 `file://` 协议 URL 从外部文件加载智能体系统提示词，或通过 `prompt_append` 追加额外内容。`prompt_append` 字段同样适用于分类配置。

```jsonc
{
  "agents": {
    "sisyphus": {
      "prompt": "file:///path/to/custom-prompt.md"
    },
    "oracle": {
      "prompt_append": "file:///path/to/additional-context.md"
    }
  },
  "categories": {
    "deep": {
      "prompt_append": "file:///path/to/deep-category-append.md"
    }
  }
}
```

支持 `~` 符号展开为主目录，以及相对路径的 `file://` URL。

适用场景：
- 提示词与配置分离，便于版本控制
- 跨项目共享提示词
- 保持配置文件简洁
- 为特定分类添加专属上下文，无需重复编写基础提示词

文件内容会在运行时加载并注入智能体的系统提示词中。

### 会话恢复
系统可自动从常见会话故障中恢复，无需用户干预：
- **缺失工具结果**：重建可恢复的工具状态，跳过无效工具部件 ID，而非直接终止恢复流程
- **思考块冲突**：从 API 思考块不匹配错误中恢复
- **空消息**：内容缺失时重建消息历史
- **上下文窗口超限**：智能压缩内容，优雅处理 Claude 上下文窗口超限错误
- **JSON 解析错误**：从格式错误的工具输出中恢复

恢复过程在智能体执行时透明进行，用户仅能看到最终结果，不会感知到中间失败。

## 技能系统（Skills）
技能系统为特定领域提供内置 MCP 服务器和详细指令的专业工作流。技能是向智能体注入**专业知识（上下文）** 和**工具（MCP）** 的核心机制。

### 内置技能

| 技能名称           | 触发关键词                                   | 说明                                                                                                                                                                                                                                                                  |
| ------------------ | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **git-master**（Git 大师） | commit、rebase、squash、"who wrote"、"when was X added" | Git 专家技能。检测提交风格、拆分原子化提交、制定变基策略。包含三大专精方向：提交架构师（原子化提交、依赖排序、风格检测）、变基外科医生（历史重写、冲突解决、分支清理）、历史考古学家（定位特定变更的引入时间/位置）。|
| **playwright**（浏览器自动化） | 浏览器任务、测试、截图                       | 基于 Playwright MCP 的浏览器自动化。**必须使用**此技能完成浏览器验证、网页浏览、数据爬取、测试、截图等任务。|
| **agent-browser**（代理浏览器） | 在 agent-browser 上执行浏览器任务            | 基于 `agent-browser` 命令行工具的浏览器自动化。支持导航、快照、截图、网络监控、脚本交互。|
| **dev-browser**（开发浏览器） | 有状态浏览器脚本                             | 带持久页面状态的浏览器自动化，适用于迭代式工作流和认证会话。|
| **frontend-ui-ux**（前端UI/UX） | UI/UX 任务、样式开发                         | 设计师转型开发者的角色设定。即使无设计稿也能打造出色的 UI/UX。强调鲜明的美学方向、独特的排版、协调的配色方案。|
| **review-work**（工作评审） | "review work"、"review my work"、"QA my work" | 实现后评审编排器。启动 5 个并行后台子智能体进行全面评审：目标验证、代码质量、安全检查、实操 QA、上下文挖掘。所有维度均通过才算评审合格。|
| **ai-slop-remover**（AI 冗余清理） | "remove AI slop"、"de-AI"、"humanize"         | 移除文件中的 AI 生成代码冗余特征，同时保留功能完整性。识别并删除冗余注释、多余错误处理、过度工程化模式、通用 AI 话术。|

#### git-master 核心原则

**默认多提交策略**：
```
修改3+文件 → 必须拆分为2+次提交
修改5+文件 → 必须拆分为3+次提交
修改10+文件 → 必须拆分为5+次提交
```

**自动风格检测**：
- 分析最近 30 次提交的语言（韩语/英语）和风格（语义化/普通/简短）
- 自动匹配代码库的提交规范

**使用示例**：
```
/git-master 提交这些变更
/git-master 变基到 main 分支
/git-master 谁编写了这段认证代码？
```

#### frontend-ui-ux 设计流程
- **设计流程**：明确目的 → 确定基调 → 梳理约束 → 打造差异化
- **美学方向**：选择极致风格 - 野兽派、极繁主义、复古未来主义、轻奢风、趣味风
- **排版**：使用独特字体，避免通用字体（Inter、Roboto、Arial）
- **配色**：协调的调色板 + 鲜明强调色，避免紫底白字的 AI 通用配色
- **动效**：高冲击力的分步展示、滚动触发效果、惊喜悬停状态
- **反模式**：通用字体、可预测布局、模板化设计

### 浏览器自动化选项
Oh-My-OpenAgent 提供两种浏览器自动化提供商，可通过 `browser_automation_engine.provider` 配置：

#### 选项 1：Playwright MCP（默认）
```yaml
mcp:
  playwright:
    command: npx
    args: ["@playwright/mcp@latest"]
```

**使用示例**：
```
/playwright 导航到 example.com 并截取屏幕截图
```

#### 选项 2：Agent Browser CLI（Vercel）
```json
{
  "browser_automation_engine": {
    "provider": "agent-browser"
  }
}
```

**安装要求**：
```bash
bun add -g agent-browser
```

**使用示例**：
```
使用 agent-browser 导航到 example.com 并提取主标题
```

**通用能力（两种提供商）**：
- 网页导航与交互
- 截图与 PDF 导出
- 表单填充与元素点击
- 网络请求等待
- 内容爬取

### 自定义技能创建（SKILL.md）
可在项目根目录的 `.opencode/skills/` 或主目录的 `~/.claude/skills/` 中添加自定义技能。

**示例：`.opencode/skills/my-skill/SKILL.md`**
```markdown
---
name: my-skill
description: 我的专属自定义技能
mcp:
  my-mcp:
    command: npx
    args: ["-y", "my-mcp-server"]
---

# 我的技能提示词

此内容将被注入智能体的系统提示词中。
...
```

**技能加载路径**（优先级从高到低）：
- `.opencode/skills/*/SKILL.md`（项目级，OpenCode 原生）
- `~/.config/opencode/skills/*/SKILL.md`（用户级，OpenCode 原生）
- `.claude/skills/*/SKILL.md`（项目级，Claude Code 兼容）
- `.agents/skills/*/SKILL.md`（项目级，Agents 规范）
- `~/.agents/skills/*/SKILL.md`（用户级，Agents 规范）

同名称的技能，高优先级路径会覆盖低优先级路径。

技能展示优先级遵循：`项目级 > 用户级 > opencode 内置 > 插件内置`。

可通过配置 `disabled_skills: ["playwright"]` 禁用内置技能。

### 分类 + 技能组合策略
通过组合分类与技能，可创建功能强大的专业智能体：

#### 设计师（UI 实现）
- **分类**：`visual-engineering`（视觉工程）
- **加载技能**：`["frontend-ui-ux", "playwright"]`
- **效果**：实现高美学标准的 UI，并直接在浏览器中验证渲染效果

#### 架构师（设计评审）
- **分类**：`ultrabrain`（超脑）
- **加载技能**：`[]`（纯推理）
- **效果**：利用 GPT-5.5 xhigh 推理能力进行深度系统架构分析

#### 维护者（快速修复）
- **分类**：`quick`（快速任务）
- **加载技能**：`["git-master"]`
- **效果**：使用高性价比模型快速修复代码并生成规范提交

### task 提示词指南
委派任务时，**清晰且具体**的提示词至关重要，需包含以下 7 要素：
1. **任务（TASK）**：需要完成什么？（单一目标）
2. **预期成果（EXPECTED OUTCOME）**：交付物是什么？
3. **必备技能（REQUIRED SKILLS）**：需通过 `load_skills` 加载哪些技能？
4. **必备工具（REQUIRED TOOLS）**：必须使用哪些工具？（白名单）
5. **必须执行（MUST DO）**：必须完成的约束条件
6. **禁止操作（MUST NOT DO）**：绝对不能执行的操作
7. **上下文（CONTEXT）**：文件路径、现有模式、参考资料

**反面示例**：
> "修复这个问题"

**正面示例**：
> **任务（TASK）**：修复 `LoginButton.tsx` 中移动端布局错乱问题
> **上下文（CONTEXT）**：文件路径 `src/components/LoginButton.tsx`，使用 Tailwind CSS 开发
> **必须执行（MUST DO）**：在 `md:` 断点处修改 flex-direction 属性
> **禁止操作（MUST NOT DO）**：不得修改现有桌面端布局
> **预期成果（EXPECTED）**：按钮在移动端垂直对齐

## 命令系统（Commands）
命令是通过斜杠触发的预定义工作流模板。

### 内置命令

| 命令名称             | 说明                                                                 |
| -------------------- | -------------------------------------------------------------------- |
| `/init-deep`         | 初始化分层结构的 AGENTS.md 知识库                                    |
| `/ralph-loop`        | 启动自引用开发循环，直至任务完成                                     |
| `/ulw-loop`          | 启动超级工作循环 - 以 ultrawork 模式持续运行                        |
| `/cancel-ralph`      | 取消正在运行的 Ralph 循环                                            |
| `/refactor`          | 智能重构，集成 LSP、AST-grep、架构分析、TDD 验证                     |
| `/start-work`        | 从普罗米修斯生成的计划启动西西弗斯工作会话                           |
| `/stop-continuation` | 停止当前会话的所有持续机制（ralph 循环、待办续跑、持续执行）|
| `/handoff`           | 生成详细上下文摘要，便于在新会话中继续工作                           |

### /init-deep
**用途**：在项目中生成分层结构的 AGENTS.md 上下文文件

**使用方式**：
```
/init-deep [--create-new] [--max-depth=N]
```

创建目录专属的上下文文件，智能体会自动读取：
```
project/
├── AGENTS.md              # 项目级上下文
├── src/
│   ├── AGENTS.md          # src 目录专属上下文
│   └── components/
│       └── AGENTS.md      # 组件目录专属上下文
```

### /ralph-loop
**用途**：自引用开发循环，持续运行直至任务完成

**命名来源**：Anthropic 的 Ralph Wiggum 插件

**使用方式**：
```
/ralph-loop "构建带认证功能的 REST API"
/ralph-loop "重构支付模块" --max-iterations=50
```

**行为特征**：
- 智能体持续向目标推进工作
- 检测 `<promise>DONE</promise>` 标记判断任务完成状态
- 若智能体未完成任务就停止，会自动续跑
- 终止条件：检测到完成标记、达到最大迭代次数（默认 100）、执行 `/cancel-ralph`

**配置项**：`{ "ralph_loop": { "enabled": true, "default_max_iterations": 100 } }`

### /ulw-loop
**用途**：与 ralph-loop 功能相同，但启用超级工作模式

所有操作均以最高强度运行 - 并行智能体、后台任务、深度探索。

### /refactor
**用途**：集成全工具链的智能重构

**使用方式**：
```
/refactor <目标> [--scope=<file|module|project>] [--strategy=<safe|aggressive>]
```

**核心特性**：
- 基于 LSP 的重命名与导航
- AST-grep 模式匹配
- 重构前架构分析
- 重构后 TDD 验证
- 代码地图生成

### /start-work
**用途**：从普罗米修斯生成的计划启动执行流程

**使用方式**：
```
/start-work [计划名称]
```

通过阿特拉斯智能体系统化执行已规划的任务。

### /stop-continuation
**用途**：停止当前会话的所有持续机制

终止 ralph 循环、待办续跑、持续执行状态。适用于需要让智能体停止当前多步骤工作流的场景。

### /handoff
**用途**：生成详细上下文摘要，便于在新会话中继续工作

生成结构化的工作交接文档，包含当前状态、已完成工作、待办事项、相关文件路径——支持在全新会话中无缝接续工作。

### 自定义命令
自定义命令可从以下路径加载：
- `.opencode/command/*.md`（项目级，OpenCode 原生）
- `~/.config/opencode/command/*.md`（用户级，OpenCode 原生）
- `.claude/commands/*.md`（项目级，Claude Code 兼容）
- `~/.config/opencode/commands/*.md`（用户级，Claude Code 兼容）

## 工具系统（Tools）
工具注册受配置开关控制。`src/tools/` 目录包含 16 个工具目录，根据配置不同，可暴露 **最少 20 个至最多 39 个工具**。

### 代码检索工具

| 工具名称 | 说明                                   |
| -------- | -------------------------------------- |
| **grep** | 基于正则表达式的内容检索，支持文件过滤 |
| **glob** | 快速文件模式匹配，按名称模式查找文件   |

### 编辑工具

| 工具名称 | 说明                                                                                                                                 |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **edit** | 基于哈希锚点的编辑工具。使用 `LINE#ID` 格式实现精准、安全的修改。应用变更前验证内容哈希，拒绝过时的哈希编辑操作。|

哈希行 ID 使用字符集：`ZPMQVRWSNKTXJBYH`

### LSP 工具（智能体专用 IDE 功能）

| 工具名称              | 说明                                   |
| --------------------- | -------------------------------------- |
| **lsp_diagnostics**   | 构建前获取错误/警告信息                |
| **lsp_prepare_rename**| 验证重命名操作可行性                   |
| **lsp_rename**        | 跨工作区重命名符号                     |
| **lsp_goto_definition**| 跳转到符号定义位置                     |
| **lsp_find_references**| 查找符号在工作区的所有引用             |
| **lsp_symbols**       | 获取文件大纲或工作区符号检索结果       |

### AST-Grep 工具

| 工具名称              | 说明                                   |
| --------------------- | -------------------------------------- |
| **ast_grep_search**   | 支持 25 种语言的 AST 感知代码模式检索  |
| **ast_grep_replace**  | 支持 25 种语言的 AST 感知代码替换      |

### 委派工具

| 工具名称              | 说明                                                                                                                                                                                                 |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **call_omo_agent**    | 生成探索者/图书管理员智能体实例，支持 `run_in_background` 参数。|
| **task**              | 基于分类的任务委派。支持内置分类（如 `visual-engineering`、`ultrabrain`、`deep`、`artistry`、`quick`、`unspecified-low`、`unspecified-high`、`writing`），也可通过 `subagent_type` 直接指定目标智能体。 |
| **background_output** | 获取后台任务结果                                                                                                                                                                                     |
| **background_cancel** | 取消正在运行的后台任务                                                                                                                                                                               |

### 视觉分析工具

| 工具名称   | 说明                                                                                                 |
| ---------- | ---------------------------------------------------------------------------------------------------- |
| **look_at** | 通过多模态观察者智能体分析媒体文件（PDF、图片、图表）。从文档中提取特定信息或摘要，描述视觉内容。|

### 技能工具

| 工具名称     | 说明                                                                 |
| ------------ | -------------------------------------------------------------------- |
| **skill**    | 按名称加载并执行技能或斜杠命令，返回带上下文的详细执行指令           |
| **skill_mcp**| 调用技能内置 MCP 的服务器操作                                        |

### 会话工具

| 工具名称          | 说明                                   |
| ----------------- | -------------------------------------- |
| **session_list**  | 列出所有 OpenCode 会话                 |
| **session_read**  | 读取会话中的消息与历史记录             |
| **session_search**| 跨会话消息全文检索                     |
| **session_info**  | 获取会话元数据与统计信息               |

### 任务管理工具
需在配置中启用 `experimental.task_system: true`。

| 工具名称        | 说明                                   |
| --------------- | -------------------------------------- |
| **task_create** | 创建带自动生成 ID 的新任务             |
| **task_get**    | 通过 ID 检索任务                       |
| **task_list**   | 列出所有活跃任务                       |
| **task_update** | 更新现有任务                           |

#### 任务系统详情
**与 Claude Code 对齐说明**：此实现遵循 Claude Code 内部 Task 工具签名（`TaskCreate`、`TaskUpdate`、`TaskList`、`TaskGet`）及字段命名规范（`subject`、`blockedBy`、`blocks` 等）。但 Anthropic 尚未发布这些工具的官方文档，本实现是 Oh My OpenAgent 基于观察到的 Claude Code 行为及内部规范独立开发的版本。