# GitLab 集成

在 GitLab Issue 和 Merge Request (MR) 中使用 OpenCode。
OpenCode 通过 GitLab CI/CD 流水线或 GitLab Duo 与你的 GitLab 工作流集成。在这些情况下，OpenCode 都运行在你的 GitLab Runner 上。

## [GitLab CI](https://opencode.ai/docs/gitlab/#gitlab-ci)
OpenCode 可以在常规的 GitLab 流水线中工作。你可以将其作为 [CI 组件](https://docs.gitlab.com/ee/ci/components/) 引入。

### 主要功能
- **自定义配置**：可以为每个任务配置不同的 OpenCode 行为。
- **极简安装**：CI 组件会在后台自动处理 OpenCode 的安装。
- **灵活性**：支持多种输入参数以自定义行为。

### 设置步骤
1. 在 **Settings > CI/CD > Variables** 中，将 OpenCode 的认证 JSON 存为 **File** 类型的环境变量 (建议勾选 Masked)。
2. 在 `.gitlab-ci.yml` 中引用组件：
   ```yaml
   include:
     - component: $CI_SERVER_FQDN/nagyv/gitlab-opencode/opencode@2
       inputs:
         config_dir: ${CI_PROJECT_DIR}/opencode-config
         auth_json: $OPENCODE_AUTH_JSON
         message: "你的提示词"
   ```

## [GitLab Duo 支持](https://opencode.ai/docs/gitlab/#gitlab-duo)
在评论中提及 `@opencode`，OpenCode 将在 GitLab CI 流水线中执行任务。

### 主要功能
- **Issue 诊断**：要求 OpenCode 解释 Issue 内容。
- **修复与实现**：自动创建新分支并提交 MR。
- **安全**：在你的组织内部 Runner 中运行。

### 设置步骤
设置涉及配置 GitLab 环境、CI/CD 变量以及服务账号。你需要在项目的流水线配置中安装 `opencode-ai` CLI 和 `glab` CLI，并配置认证信息。

## [示例用法](https://opencode.ai/docs/gitlab/#examples)
- **解释 Issue**: `@opencode explain this issue`
- **修复 Issue**: `@opencode fix this`
- **审查 MR**: `@opencode review this merge request`
