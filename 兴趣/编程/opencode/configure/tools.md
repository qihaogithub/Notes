# 工具管理 (Tools)

管理 LLM 可以使用的工具。
工具允许 LLM 在你的代码库中执行操作。OpenCode 附带了一组内置工具，你也可以通过 [自定义工具](https://opencode.ai/docs/custom-tools) 或 [MCP 服务器](https://opencode.ai/docs/mcp-servers) 进行扩展。

默认情况下，所有工具都是启用的。你可以通过 [权限设置](https://opencode.ai/docs/permissions) 控制工具行为。

## [配置 (Configure)](https://opencode.ai/docs/tools/#configure)
使用 `permission` 字段控制工具。你可以设置为 `allow` (允许)、`deny` (拒绝) 或 `ask` (询问)。

```json
{
  "permission": {
    "edit": "deny",
    "bash": "ask",
    "webfetch": "allow"
  }
}
```

也可以使用通配符，例如 `"mymcp_*": "ask"` 将对特定 MCP 服务器的所有工具要求审批。

## [内置工具 (Built-in)](https://opencode.ai/docs/tools/#built-in)

### [bash](https://opencode.ai/docs/tools/#bash)
在项目环境中执行 shell 命令 (如 `npm install`, `git status`)。

### [edit / write / patch](https://opencode.ai/docs/tools/#edit)
- **edit**: 通过精确的字符串替换修改现有文件。
- **write**: 创建新文件或覆盖现有文件。
- **patch**: 对文件应用补丁。
*注：这些工具统称为文件修改工具，受 `edit` 权限控制。*

### [read](https://opencode.ai/docs/tools/#read)
读取文件内容，支持大文件的行范围读取。

### [grep](https://opencode.ai/docs/tools/#grep)
使用正则表达式在代码库中进行快速内容搜索。

### [glob](https://opencode.ai/docs/tools/#glob)
通过模式匹配 (如 `src/**/*.ts`) 查找文件。

### [list](https://opencode.ai/docs/tools/#list)
列出指定路径下的文件和目录。

### [lsp (实验性)](https://opencode.ai/docs/tools/#lsp-experimental)
与配置的 LSP 服务器交互，提供转到定义、查找引用、悬停信息等智能功能。
需设置 `OPENCODE_EXPERIMENTAL_LSP_TOOL=true` 启用。

### [skill](https://opencode.ai/docs/tools/#skill)
加载 [技能](https://opencode.ai/docs/skills) (SKILL.md 文件) 内容。

### [todowrite / todoread](https://opencode.ai/docs/tools/#todowrite)
管理和读取任务列表，用于组织多步任务。

### [webfetch](https://opencode.ai/docs/tools/#webfetch)
抓取网页内容，用于查阅在线文档。

### [question](https://opencode.ai/docs/tools/#question)
在执行过程中向用户提问，以获取偏好、要求或决策。

## [其他](https://opencode.ai/docs/tools/#internals)
- **自定义工具**: 可以在配置中定义自己的函数。
- **忽略模式**: 工具默认遵循 `.gitignore`。如需搜索被忽略的文件，请在根目录创建 `.ignore` 文件并显式允许。
