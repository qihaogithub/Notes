# 代理设置 (Agents)

配置和使用专业化代理。
代理是专门针对特定任务和工作流配置的 AI 助手。你可以自定义它们的提示词、模型和工具访问权限。

## [代理类型 (Types)](https://opencode.ai/docs/agents/#types)

### [主要代理 (Primary agents)](https://opencode.ai/docs/agents/#primary-agents)
你直接交互的主要助手。你可以通过 `Tab` 键在它们之间切换。
内置的主要代理有：
- **Build**: 默认代理，拥有所有工具权限，适用于标准的开发工作。
- **Plan**: 受限代理，主要用于规划和分析。默认情况下，文件修改和 Bash 命令均需询问授权。

### [子代理 (Subagents)](https://opencode.ai/docs/agents/#subagents)
主要代理可以调用子代理来完成特定子任务。你也可以在消息中通过 `@` 提及手动调用它们。
内置的子代理有：
- **General**: 通用子代理，用于研究复杂问题和执行多步任务。
- **Explore**: 只读子代理，用于快速探索代码库 (查找文件、搜索关键词)，无法修改文件。

## [用法](https://opencode.ai/docs/agents/#usage)
1. **切换**：按 `Tab` 键循环切换主要代理。
2. **手动调用**：在消息中输入 `@general` 等。
3. **会话导航**：子代理创建子会话时，使用 `Leader + 方向键` 在父子会话间切换。

## [配置 (Configure)](https://opencode.ai/docs/agents/#configure)

### [JSON 配置](https://opencode.ai/docs/agents/#json)
在 `opencode.json` 中配置代理：
```json
{
  "agent": {
    "code-reviewer": {
      "mode": "subagent",
      "model": "anthropic/claude-3-5-sonnet",
      "description": "审查代码质量和最佳实践",
      "tools": { "write": false, "edit": false }
    }
  }
}
```

### [Markdown 配置](https://opencode.ai/docs/agents/#markdown)
你可以在 `.opencode/agents/` 目录下创建 `.md` 文件来定义代理。文件名即为代理名。
文件顶部使用 YAML Frontmatter 定义属性，下方为系统提示词。

## [配置选项 (Options)](https://opencode.ai/docs/agents/#options)
- `description`: (必填) 代理功能的简短描述。
- `model`: 覆盖该代理使用的模型。
- `temperature`: 控制响应的随机性 (0.0 - 1.0)。
- `maxSteps`: 控制代理在强制停止前可以进行的最大迭代次数。
- `tools`: 启用或禁用特定工具 (支持通配符)。
- `prompt`: 指定自定义系统提示词文件。
- `disable`: 设置为 `true` 以禁用该代理。
