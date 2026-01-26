# 模型提供商 (Providers)

在 OpenCode 中使用任何 LLM 提供商。
OpenCode 使用 [AI SDK](https://ai-sdk.dev/) 和 [Models.dev](https://models.dev) 来支持 75 个以上的 LLM 提供商，并支持运行本地模型。

要添加提供商，你需要：
1. 使用 `/connect` 命令添加提供商的 API 密钥。
2. 在 OpenCode 配置中配置提供商。

## [凭据 (Credentials)](https://opencode.ai/docs/providers/#credentials)
当你使用 `/connect` 命令添加 API 密钥时，它们存储在 `~/.local/share/opencode/auth.json`。

## [配置 (Config)](https://opencode.ai/docs/providers/#config)
你可以通过配置文件的 `provider` 部分自定义提供商。

### [Base URL](https://opencode.ai/docs/providers/#base-url)
你可以为任何提供商自定义 `baseURL`，这在处理代理服务或自定义端点时非常有用。

```json
{
  "provider": {
    "anthropic": {
      "options": {
        "baseURL": "https://api.anthropic.com/v1"
      }
    }
  }
}
```

## [OpenCode Zen](https://opencode.ai/docs/providers/#opencode-zen)
OpenCode Zen 是由 OpenCode 团队提供的一组经过测试和验证的模型列表。
1. 在 TUI 中运行 `/connect`，选择 opencode。
2. 在 [opencode.ai/auth](https://opencode.ai/auth) 登录并复制 API 密钥。
3. 运行 `/models` 查看推荐的模型列表。

---

## [提供商目录 (Directory)](https://opencode.ai/docs/providers/#directory)

### [302.AI](https://opencode.ai/docs/providers/#302ai)
1. 在 [302.AI 控制台](https://302.ai/) 生成 API 密钥。
2. 运行 `/connect` 并搜索 302.AI。
3. 运行 `/models` 选择模型。

### [Amazon Bedrock](https://opencode.ai/docs/providers/#amazon-bedrock)
1. 在 Amazon Bedrock 控制台中请求模型访问权限。
2. 配置身份验证 (环境变量、AWS 配置文件或 Bearer Token)。
   - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`
   - 或者使用 `/connect`

### [Moonshot AI (Kimi)](https://opencode.ai/docs/providers/#moonshot-ai)
1. 在 [Moonshot AI 控制台](https://platform.moonshot.ai/console) 创建 API 密钥。
2. 运行 `/connect` 并搜索 Moonshot AI。

### [MiniMax](https://opencode.ai/docs/providers/#minimax)
1. 在 [MiniMax 开放平台](https://platform.minimax.io/) 获取 API 密钥。
2. 运行 `/connect` 并连接。

### [Ollama (本地模型)](https://opencode.ai/docs/providers/#ollama)
你可以通过 Ollama 使用本地运行的模型。
```json
{
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "llama3": { "name": "Llama 3" }
      }
    }
  }
}
```

### [OpenAI](https://opencode.ai/docs/providers/#openai)
1. 运行 `/connect` 并选择 OpenAI。
2. 你可以选择 **ChatGPT Plus/Pro** 方式自动认证，也可以手动输入 **API Key**。

### [OpenRouter](https://opencode.ai/docs/providers/#openrouter)
1. 在 [OpenRouter 仪表板](https://openrouter.ai/settings/keys) 获取密钥。
2. 运行 `/connect` 连接。
3. 你可以在配置中添加自定义模型。
