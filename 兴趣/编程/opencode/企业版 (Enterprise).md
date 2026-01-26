---
创建日期: 2026-01-26T16:05:59+08:00
修改日期: 2026-01-26T16:11:28+08:00
---
在你的组织中安全地使用 OpenCode。
OpenCode 企业版适用于希望确保其代码和数据永远不会离开其基础设施的组织。它通过使用集成 SSO 和内部 AI 网关的集中式配置来实现这一点。

**注意**：OpenCode 不会存储你的任何代码或上下文数据。

## [试用 (Trial)](https://opencode.ai/docs/enterprise/#trial)
OpenCode 是开源的且不存储代码，你的开发人员可以直接[开始](https://opencode.ai/docs/)进行内部试用。

### [数据处理 (Data handling)](https://opencode.ai/docs/enterprise/#data-handling)
OpenCode 不存储你的代码或上下文数据。所有处理都在本地发生，或通过直接的 API 调用发送到你的 AI 提供商。
这意味着只要你使用的是信任的提供商或内部 AI 网关，你就可以安全地使用 OpenCode。

唯一的例外是可选的 `/share` 功能。

#### [分享对话 (Sharing conversations)](https://opencode.ai/docs/enterprise/#sharing-conversations)
如果用户启用了 `/share` 功能，对话及其关联数据将被发送到我们的分享页面服务。
对于企业试用，我们建议禁用此功能：

```json
{
  "share": "disabled"
}
```

### [代码所有权 (Code ownership)](https://opencode.ai/docs/enterprise/#code-ownership)
你拥有 OpenCode 生成的所有代码，没有任何许可限制或所有权声明。

## [定价 (Pricing)](https://opencode.ai/docs/enterprise/#pricing)
企业版采用按席位计费的模式。如果你拥有自己的 LLM 网关，我们不会对使用的 Token 收费。

## [部署 (Deployment)](https://opencode.ai/docs/enterprise/#deployment)

### [集中式配置 (Central Config)](https://opencode.ai/docs/enterprise/#central-config)
我们可以为整个组织设置单一的集中式配置，集成 SSO 并确保用户只能访问内部 AI 网关。

### [SSO 集成](https://opencode.ai/docs/enterprise/#sso-integration)
通过集中式配置，OpenCode 可以集成组织的 SSO 身份验证。

### [内部 AI 网关](https://opencode.ai/docs/enterprise/#internal-ai-gateway)
OpenCode 可以配置为仅使用内部 AI 网关，并禁用所有其他 AI 提供商。

### [私有 npm 仓库](https://opencode.ai/docs/enterprise/#faq)
OpenCode 支持私有 npm 仓库。如果你的组织使用私有仓库 (如 JFrog Artifactory)，请确保开发人员在运行 OpenCode 之前已通过 `npm login` 进行身份验证。
OpenCode 会自动读取 `~/.npmrc` 文件中的认证信息。
