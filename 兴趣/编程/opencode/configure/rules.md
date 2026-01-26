# 规则设置 (Rules)

为 OpenCode 设置自定义指令。

## [初始化 (Initialize)](https://opencode.ai/docs/rules/#initialize)
运行 `/init` 命令会自动扫描项目并生成 `AGENTS.md` 文件。
建议将 `AGENTS.md` 提交到 Git，以便团队共享项目的编码规范和结构信息。

## [规则文件类型 (Types)](https://opencode.ai/docs/rules/#types)
- **项目规则**：存放在项目根目录的 `AGENTS.md`。仅适用于当前项目。
- **全局规则**：存放在 `~/.config/opencode/AGENTS.md`。适用于所有会话，适合存放个人偏好。
- **Claude Code 兼容性**：支持读取 `CLAUDE.md` 或 `~/.claude/CLAUDE.md` 作为回退方案。

## [优先级 (Precedence)](https://opencode.ai/docs/rules/#precedence)
加载顺序 (越靠前优先级越高)：
1. 向上查找得到的本地文件 (`AGENTS.md` > `CLAUDE.md` > `CONTEXT.md`)。
2. 全局文件 `~/.config/opencode/AGENTS.md`。
3. Claude Code 的全局文件。

## [自定义指令 (Custom Instructions)](https://opencode.ai/docs/rules/#custom-instructions)
除了 `AGENTS.md`，你还可以在 `opencode.json` 中通过 `instructions` 字段指定其他指令文件或远程 URL：

```json
{
  "instructions": [
    "CONTRIBUTING.md",
    "docs/guidelines.md",
    "https://example.com/shared-rules.md"
  ]
}
```

## [引用外部文件](https://opencode.ai/docs/rules/#referencing-external-files)
虽然 OpenCode 不会自动解析 `AGENTS.md` 中的文件引用，但你可以通过以下方式实现：
1. **使用 opencode.json**：通过 `instructions` 字段包含外部文件 (推荐)。
2. **手动指令**：在 `AGENTS.md` 中告诉 OpenCode 在需要时使用 `Read` 工具读取指定文件。
   例如：`对于 TypeScript 代码风格，请参考 @docs/typescript-guidelines.md`。
