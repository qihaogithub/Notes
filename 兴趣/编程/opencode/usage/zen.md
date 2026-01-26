# OpenCode Zen

由 OpenCode 提供的精选模型列表。
OpenCode Zen 是由 OpenCode 团队测试并验证的一系列适用于编程助手的模型。

**注意**：OpenCode Zen 目前处于 Beta 阶段。它是完全可选的，你也可以在 OpenCode 中使用其他任何提供商。

## [背景](https://opencode.ai/docs/zen/#background)
市场上有很多模型，但只有少数几个非常适合作为编程助手。不同的提供商配置不同，导致性能和质量差异很大。
OpenCode Zen 作为一个 AI 网关，为你提供经过基准测试、表现最优的模型组合。

## [工作原理](https://opencode.ai/docs/zen/#how-it-works)
1. 登录 [OpenCode Zen](https://opencode.ai/auth)，添加账单详情，并复制 API 密钥。
2. 在 TUI 中运行 `/connect`，选择 **OpenCode Zen**，并粘贴密钥。
3. 运行 `/models` 查看推荐模型列表。

OpenCode Zen 采用按请求付费模式。

## [端点 (Endpoints)](https://opencode.ai/docs/zen/#endpoints)
你可以通过 API 端点访问模型。配置文件中的模型 ID 格式为 `opencode/<model-id>` (例如 `opencode/gpt-5.2-codex`)。

## [定价](https://opencode.ai/docs/zen/#pricing)
支持按需付费模式。信用卡交易手续费 (4.4% + $0.30) 按成本转嫁。
- **免费模型**：部分模型 (如 Grok Code Fast 1, Big Pickle) 在限时内免费，用于收集反馈。
- **自动充值 (Auto-reload)**：余额低于 $5 时，可自动充值 (默认 $20，可自定义)。
- **月度限制**：可以为工作区或个人成员设置月度使用限额。

## [隐私](https://opencode.ai/docs/zen/#privacy)
模型托管在美国。大多数提供商遵循零保留政策，不会将你的数据用于训练 (免费试用期间的部分模型除外)。

## [团队支持 (For Teams)](https://opencode.ai/docs/zen/#for-teams)
- **角色管理**：管理员可以邀请成员，分配管理员(Admin)或成员(Member)角色。
- **模型访问控制**：管理员可以为工作区启用或禁用特定模型。
- **自带密钥 (BYOK)**：你可以使用自己的 OpenAI 或 Anthropic API 密钥，通过 Zen 的界面进行管理和访问。

## [愿景 (Goals)](https://opencode.ai/docs/zen/#goals)
创建 OpenCode Zen 旨在：
1. 为编程助手寻找最佳模型/提供商组合。
2. 确保最高的质量标准，不为降低成本而牺牲性能。
3. 将任何价格下降转嫁给用户，仅收取必要的手续费。
4. 保持开放，不强行绑定，支持任何其他编程助手。
