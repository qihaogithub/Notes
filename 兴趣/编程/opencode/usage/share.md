# Share (分享功能)

分享你的 OpenCode 对话。
OpenCode 的分享功能允许你为对话创建公开链接，以便与团队成员协作或向他人寻求帮助。

**注意**：已分享的对话可供任何拥有链接的人公开访问。

## [工作原理](https://opencode.ai/docs/share/#how-it-works)
当你分享对话时，OpenCode 会：
1. 为该会话创建一个唯一的公开 URL。
2. 将对话历史同步到我们的服务器。
3. 通过分享链接 `opncd.ai/s/<share-id>` 进行访问。

## [分享模式](https://opencode.ai/docs/share/#sharing)
OpenCode 支持三种分享模式：

### [手动模式 (默认)](https://opencode.ai/docs/share/#manual-default)
会话不会自动分享，你可以使用 `/share` 命令手动分享并获取 URL。

### [自动分享 (Auto-share)](https://opencode.ai/docs/share/#auto-share)
在配置文件中将 `share` 设置为 `"auto"`，所有新对话都将自动生成分享链接。

### [禁用分享 (Disabled)](https://opencode.ai/docs/share/#disabled)
将 `share` 设置为 `"disabled"` 彻底禁用分享功能。

## [取消分享 (Un-sharing)](https://opencode.ai/docs/share/#un-sharing)
运行 `/unshare` 命令停止分享。这会移除分享链接并删除相关数据。

## [隐私建议](https://opencode.ai/docs/share/#privacy)
- 仅分享不含敏感信息的对话。
- 分享前审查内容。
- 协作完成后及时取消分享。
- 避免分享包含专利代码或机密数据的对话。
- 对于敏感项目，建议彻底禁用分享。

## [企业版支持](https://opencode.ai/docs/share/#for-enterprises)
在企业部署中，分享功能可以由管理员全局禁用、限制为仅限 SSO 用户访问，或支持在企业内部私有化部署。
了解更多：[企业版文档](https://opencode.ai/docs/enterprise)
