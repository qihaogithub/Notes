---
创建日期: 2026-01-26T16:05:59+08:00
修改日期: 2026-01-30T09:56:36+08:00
---
Agents 是专用的 AI 助手，可以针对特定任务和工作流程进行配置。它们允许你创建具有自定义提示词、模型和工具访问权限的专注工具。

**提示**

使用 plan agent 分析代码并审查建议，而无需进行任何代码更改。

你可以在会话期间切换 agents，或通过 `@` 提及来调用它们。

---

## [类型](#types)

OpenCode 中有两种类型的 agents：主要 agents 和子 agents。

---

### [主要 agents](#primary-agents)

主要 agents 是你直接交互的主要助手。你可以使用 **Tab** 键或你配置的 `switch_agent` 快捷键在它们之间切换。这些 agents 处理你的主要对话。工具访问通过权限配置——例如，Build 启用了所有工具，而 Plan 受到限制。

**提示**

你可以在会话期间使用 **Tab** 键在主要 agents 之间切换。

OpenCode 内置了两个主要 agents，**Build** 和 **Plan**。我们将在下面查看这些。

---

### [子 agents](#subagents)

子 agents 是主要 agents 可以调用的专用助手。你也可以在消息中通过 **@ 提及**它们来手动调用。

OpenCode 内置了两个子 agents，**General** 和 **Explore**。我们将在下面查看这些。

---

## [内置](#built-in)

OpenCode 内置了两个主要 agents 和两个子 agents。

---

### [Build](#build)

**模式**：`primary`

Build 是启用了所有工具的**默认**主要 agent。这是需要完全访问文件操作和系统命令的开发工作的标准 agent。

---

### [Plan](#plan)

**模式**：`primary`

一个用于规划和分析的受限 agent。我们使用权限系统为你提供更多控制并防止意外更改。默认情况下，以下所有内容都设置为 `ask`：

- `file edits`：所有写入、补丁和编辑
- `bash`：所有 bash 命令

当你希望 LLM 分析代码、建议更改或创建计划而不对代码库进行任何实际修改时，此 agent 非常有用。

---

### [General](#general)

**模式**：`subagent`

一个用于研究复杂问题和执行多步骤任务的通用 agent。拥有完全的工具访问权限（除了 todo），因此可以在需要时进行文件更改。使用它来并行运行多个工作单元。

---

### [Explore](#explore)

**模式**：`subagent`

一个用于探索代码库的快速只读 agent。无法修改文件。当你需要按模式快速查找文件、在代码中搜索关键词或回答有关代码库的问题时使用它。

---

## [使用](#usage)

对于主要 agents，在会话期间使用 **Tab** 键在它们之间循环。你也可以使用你配置的 `switch_agent` 快捷键。

子 agents 可以通过以下方式调用：
   - **自动**：主要 agents 根据描述为特定任务调用它们。
   - **手动**：在消息中 **@ 提及**子 agent。例如：
```
@general 帮我搜索这个函数
```

**会话之间的导航**：当子 agents 创建自己的子会话时，你可以使用以下方法在父会话和所有子会话之间导航：
**<Leader>+Right**（或你配置的 `session_child_cycle` 快捷键）向前循环 父 → 子1 → 子2 → … → 父
**<Leader>+Left**（或你配置的 `session_child_cycle_reverse` 快捷键）向后循环 父 ← 子1 ← 子2 ← … → 父

这允许你在主要对话和专用子 agent 工作之间无缝切换。

##  [配置](#configure)

你可以通过配置自定义内置 agents 或创建自己的 agents。Agents 可以通过两种方式配置：


### [JSON](#json)

在你的 `opencode.json` 配置文件中配置 agents：

**opencode.json**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "mode": "primary",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "{file:./prompts/build. Txt}",
      "tools": {
        "write": true,
        "edit": true,
        "bash": true
      }
    },
    "plan": {
      "mode": "primary",
      "model": "anthropic/claude-haiku-4-20250514",
      "tools": {
        "write": false,
        "edit": false,
        "bash": false
      }
    },
    "code-reviewer": {
      "description": "Reviews code for best practices and potential issues",
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "You are a code reviewer. Focus on security, performance, and maintainability.",
      "tools": {
        "write": false,
        "edit": false
      }
    }
  }
}
```

---

### [Markdown](#markdown)

你也可以使用 markdown 文件定义 agents。将它们放置在：

- 全局：`~/.config/opencode/agents/`
- 每个项目：`.opencode/agents/`

**~/.config/opencode/agents/review.md**

```markdown
---
description: Reviews code for quality and best practices
mode: subagent
model: anthropic/claude-sonnet-4-20250514
temperature: 0.1
tools:
  write: false
  edit: false
  bash: false
---

You are in code review mode. Focus on:
- Code quality and best practices
- Potential bugs and edge cases
- Performance implications
- Security considerations

Provide constructive feedback without making direct changes.
```

markdown 文件名成为 agent 名称。例如，`review.md` 创建一个 `review` agent。

---

## [选项](#options)

让我们详细查看这些配置选项。

---

### [Description](#description)

使用 `description` 选项提供关于 agent 功能以及何时使用它的简要描述。

**opencode.json**

```json
{
  "agent": {
    "review": {
      "description": "Reviews code for best practices and potential issues"
    }
  }
}
```

这是一个**必需的**配置选项。

---

### [Temperature](#temperature)

使用 `temperature` 配置控制 LLM 响应的随机性和创造性。

较低的值使响应更加专注和确定，而较高的值增加创造力和变异性。

**opencode.json**

```json
{
  "agent": {
    "plan": {
      "temperature": 0.1
    },
    "creative": {
      "temperature": 0.8
    }
  }
}
```

温度值通常在 0.0 到 1.0 之间：

- **0.0-0.2**：非常专注和确定的响应，适合代码分析和规划
- **0.3-0.5**：具有一些创造性的平衡响应，适合一般开发任务
- **0.6-1.0**：更有创造力和多样化的响应，适合头脑风暴和探索

**opencode.json**

```json
{
  "agent": {
    "analyze": {
      "temperature": 0.1,
      "prompt": "{file:./prompts/analysis.txt}"
    },
    "build": {
      "temperature": 0.3
    },
    "brainstorm": {
      "temperature": 0.7,
      "prompt": "{file:./prompts/creative.txt}"
    }
  }
}
```

如果未指定温度，OpenCode 使用模型特定的默认值；通常大多数模型为 0，Qwen 模型为 0.55。

---

### [Max steps](#max-steps)

控制 agent 在被强制仅以文本响应之前可以执行的最大 agent 迭代次数。这允许希望控制成本的用户限制 agent 操作。

如果未设置此选项，agent 将继续迭代，直到模型选择停止或用户中断会话。

**opencode.json**

```json
{
  "agent": {
    "quick-thinker": {
      "description": "Fast reasoning with limited iterations",
      "prompt": "You are a quick thinker. Solve problems with minimal steps.",
      "maxSteps": 5
    }
  }
}
```

达到限制时，agent 将收到一个特殊的系统提示，指示它总结其工作并推荐剩余任务。

---

### [Disable](#disable)

设置为 `true` 以禁用 agent。

**opencode.json**

```json
{
  "agent": {
    "review": {
      "disable": true
    }
  }
}
```

---

### [Prompt](#prompt)

使用 `prompt` 配置为此 agent 指定自定义系统提示文件。提示文件应包含特定于 agent 目的的说明。

**opencode.json**

```json
{
  "agent": {
    "review": {
      "prompt": "{file:./prompts/code-review.txt}"
    }
  }
}
```

此路径相对于配置文件所在的位置。因此，这对于全局 OpenCode 配置和项目特定配置都有效。

---

### [Model](#model)

使用 `model` 配置覆盖此 agent 的模型。对于使用针对不同任务优化的不同模型很有用。例如，用于规划的更快模型，用于实现的更强大模型。

**提示**

如果你不指定模型，主要 agents 使用[全局配置的模型](/docs/config#models)，而子 agents 将使用调用子 agents 的主要 agent 的模型。

**opencode.json**

```json
{
  "agent": {
    "plan": {
      "model": "anthropic/claude-haiku-4-20250514"
    }
  }
}
```

你的 OpenCode 配置中的模型 ID 使用格式 `provider/model-id`。例如，如果你使用 [OpenCode Zen](/docs/zen)，你将使用 `opencode/gpt-5.1-codex` 来表示 GPT 5.1 Codex。

---

### [Tools](#tools)

使用 `tools` 配置控制此 agent 中可用的工具。你可以通过将它们设置为 `true` 或 `false` 来启用或禁用特定工具。

**opencode.json**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "tools": {
    "write": true,
    "bash": true
  },
  "agent": {
    "plan": {
      "tools": {
        "write": false,
        "bash": false
      }
    }
  }
}
```

**注意**

agent 特定的配置会覆盖全局配置。

你也可以使用通配符一次控制多个工具。例如，要禁用来自 MCP 服务器的所有工具：

**opencode.json**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "readonly": {
      "tools": {
        "mymcp_*": false,
        "write": false,
        "edit": false
      }
    }
  }
}
```

[了解更多关于工具的信息](/docs/tools)。

---

### [Permissions](#permissions)

你可以配置权限来管理 agent 可以采取的操作。目前，`edit`、`bash` 和 `webfetch` 工具的权限可以配置为：

- `"ask"` — 在运行工具之前提示批准
- `"allow"` — 允许所有操作而无需批准
- `"deny"` — 禁用工具

**opencode.json**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "deny"
  }
}
```

你可以为每个 agent 覆盖这些权限。

**opencode.json**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "deny"
  },
  "agent": {
    "build": {
      "permission": {
        "edit": "ask"
      }
    }
  }
}
```

你也可以在 Markdown agents 中设置权限。

**~/.config/opencode/agents/review.md**

```markdown
---
description: Code review without edits
mode: subagent
permission:
  edit: deny
  bash:
    "*": ask
    "git diff": allow
    "git log*": allow
    "grep *": allow
  webfetch: deny
---

Only analyze code and suggest changes.
```

你可以为特定的 bash 命令设置权限。

**opencode.json**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "permission": {
        "bash": {
          "git push": "ask",
          "grep *": "allow"
        }
      }
    }
  }
}
```

这可以采用 glob 模式。

**opencode.json**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "permission": {
        "bash": {
          "git *": "ask"
        }
      }
    }
  }
}
```

你也可以使用 `*` 通配符来管理所有命令的权限。由于最后匹配的规则优先，请将 `*` 通配符放在前面，特定规则放在后面。

**opencode.json**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "permission": {
        "bash": {
          "*": "ask",
          "git status *": "allow"
        }
      }
    }
  }
}
```

[了解更多关于权限的信息](/docs/permissions)。

---

### [Mode](#mode)

使用 `mode` 配置控制 agent 的模式。`mode` 选项用于确定如何使用 agent。

**opencode.json**

```json
{
  "agent": {
    "review": {
      "mode": "subagent"
    }
  }
}
```

`mode` 选项可以设置为 `primary`、`subagent` 或 `all`。如果未指定 `mode`，则默认为 `all`。

---

### [Hidden](#hidden)

使用 `hidden: true` 从 `@` 自动完成菜单中隐藏子 agent。对于应该仅通过 Task 工具由其他 agents 以编程方式调用的内部子 agents 很有用。

**opencode.json**

```json
{
  "agent": {
    "internal-helper": {
      "mode": "subagent",
      "hidden": true
    }
  }
}
```

这只影响用户在自动完成菜单中的可见性。如果权限允许，隐藏的 agents 仍然可以由模型通过 Task 工具调用。

**注意**

仅适用于 `mode: subagent` agents。

---

### [Task permissions](#task-permissions)

使用 `permission.task` 控制 agent 可以通过 Task 工具调用哪些子 agents。使用 glob 模式进行灵活匹配。

**opencode.json**

```json
{
  "agent": {
    "orchestrator": {
      "mode": "primary",
      "permission": {
        "task": {
          "*": "deny",
          "orchestrator-*": "allow",
          "code-reviewer": "ask"
        }
      }
    }
  }
}
```

设置为 `deny` 时，子 agent 将从 Task 工具描述中完全删除，因此模型不会尝试调用它。

**提示**

规则按顺序评估，**最后匹配的规则获胜**。在上面的示例中，`orchestrator-planner` 匹配 `*`（deny）和 `orchestrator-*`（allow），但由于 `orchestrator-*` 在 `*` 之后，结果是 `allow`。

**提示**

用户始终可以通过 `@` 自动完成菜单直接调用任何子 agent，即使 agent 的任务权限会拒绝它。

---

### [Additional](#additional)

你在 agent 配置中指定的任何其他选项都将**直接传递**给提供商作为模型选项。这允许你使用提供商特定的功能和参数。

例如，使用 OpenAI 的推理模型，你可以控制推理工作量：

**opencode.json**

```json
{
  "agent": {
    "deep-thinker": {
      "description": "Agent that uses high reasoning effort for complex problems",
      "model": "openai/gpt-5",
      "reasoningEffort": "high",
      "textVerbosity": "low"
    }
  }
}
```

这些附加选项是模型和提供商特定的。查看你的提供商文档以了解可用参数。

**提示**

运行 `opencode models` 查看可用模型列表。

---

## [创建 agents](#create-agents)

你可以使用以下命令创建新的 agents：

**终端窗口**

```
opencode agent create
```

此交互式命令将：

1. 询问在哪里保存 agent；全局或项目特定。
2. 描述 agent 应该做什么。
3. 生成适当的系统提示和标识符。
4. 让你选择 agent 可以访问哪些工具。
5. 最后，创建一个带有 agent 配置的 markdown 文件。

---

## [用例](#use-cases)

以下是一些不同 agents 的常见用例。

- **Build agent**：启用所有工具的完整开发工作
- **Plan agent**：分析和规划而不进行更改
- **Review agent**：具有只读访问权限加上文档工具的代码审查
- **Debug agent**：专注于调查，启用 bash 和读取工具
- **Docs agent**：文档编写，具有文件操作但没有系统命令

---

## [示例](#examples)

以下是一些你可能觉得有用的示例 agents。

**提示**

你有想要分享的 agent 吗？[提交 PR](https://github.com/anomalyco/opencode)。

---

### [文档 agent](#documentation-agent)

**~/.config/opencode/agents/docs-writer.md**

```markdown
---
description: Writes and maintains project documentation
mode: subagent
tools:
  bash: false
---

You are a technical writer. Create clear, comprehensive documentation.
Focus on:
- Clear explanations
- Proper structure
- Code examples
- User-friendly language
```

---

### [安全审计员](#security-auditor)

**~/.config/opencode/agents/security-auditor.md**

```markdown
---
description: Performs security audits and identifies vulnerabilities
mode: subagent
tools:
  write: false
  edit: false
---

You are a security expert. Focus on identifying potential security issues.
Look for:
- Input validation vulnerabilities
- Authentication and authorization flaws
- Data exposure risks
- Dependency vulnerabilities
- Configuration security issues
```

---

[编辑此页面](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/agents.mdx) [发现错误？打开问题](https://github.com/anomalyco/opencode/issues/new) [加入我们的 Discord 社区](https://opencode.ai/discord)

© [Anomaly](https://anoma.ly)

2026年1月29日