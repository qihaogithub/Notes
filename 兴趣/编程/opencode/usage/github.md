# GitHub 集成

在 GitHub Issue 和 Pull Request 中使用 OpenCode。
OpenCode 与你的 GitHub 工作流集成。在评论中提及 `/opencode` 或 `/oc`，OpenCode 将在 GitHub Actions Runner 中执行任务。

## [主要功能](https://opencode.ai/docs/github/#features)
- **Issue 诊断**：要求 OpenCode 查看 Issue 并为你解释。
- **修复与实现**：要求 OpenCode 修复 Bug 或实现功能。它会在新分支上工作并提交包含更改的 PR。
- **安全**：OpenCode 在你自己的 GitHub Runner 中运行。

## [安装](https://opencode.ai/docs/github/#installation)
在项目仓库中运行：
```bash
opencode github install
```
这会引导你通过 GitHub App 安装、创建工作流文件并设置 Secrets。

### [手动设置](https://opencode.ai/docs/github/#manual-setup)
1. 安装 [GitHub App](https://github.com/apps/opencode-agent)。
2. 添加工作流文件 `.github/workflows/opencode.yml`。
3. 在仓库设置中添加 API 密钥 (如 `ANTHROPIC_API_KEY`) 到 Actions Secrets。

## [配置项](https://opencode.ai/docs/github/#configuration)
- `model`: (必填) 指定模型，格式为 `provider/model`。
- `agent`: 指定主要代理，默认为 "build"。
- `share`: 是否分享会话，公开仓库默认为 `true`。
- `prompt`: 自定义提示词以覆盖默认行为。
- `token`: (可选) GitHub 访问令牌。默认使用 GitHub App 的令牌。

## [支持的事件](https://opencode.ai/docs/github/#supported-events)
OpenCode 可由以下事件触发：
- `issue_comment`: 提及 `/opencode` 或 `/oc` 时触发。
- `pull_request_review_comment`: 对代码行的评论中提及 `/oc` 时触发。
- `issues`: 开启 Issue 时自动诊断。
- `pull_request`: 开启或更新 PR 时自动审查。
- `schedule`: 定时运行自动化任务。
- `workflow_dispatch`: 手动运行。

## [示例用法](https://opencode.ai/docs/github/#examples)
- **解释 Issue**: `/opencode explain this issue`
- **修复 Issue**: `/opencode fix this`
- **审查并更改 PR**: `Delete the attachment from S3 when the note is removed /oc`
- **针对特定代码行建议**: 在 PR 的 "Files" 标签页评论：`/oc add error handling here`
