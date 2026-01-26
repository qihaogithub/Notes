# 模型设置 (Models)

配置 LLM 提供商和模型。
OpenCode 支持超过 75 家提供商，并支持运行本地模型。

## [选择模型](https://opencode.ai/docs/models/#select-a-model)
在 TUI 中输入 `/models` 可以查看并选择已配置的可用模型。
推荐使用的模型包括：
- Claude 3.5 Sonnet / Opus
- GPT-4o / GPT-4 Turbo
- Gemini 1.5 Pro / Flash
- Minimax M2.1

## [设置默认模型](https://opencode.ai/docs/models/#set-a-default)
在 `opencode.json` 中配置 `model` 键：
```json
{
  "model": "anthropic/claude-3-5-sonnet"
}
```
ID 格式为 `provider_id/model_id`。

## [配置模型参数](https://opencode.ai/docs/models/#configure-models)
你可以为特定模型配置全局选项，例如推理强度 (reasoning effort) 或思考预算 (thinking budget)：

```json
{
  "provider": {
    "anthropic": {
      "models": {
        "claude-3-5-sonnet": {
          "options": {
            "thinking": {
              "type": "enabled",
              "budgetTokens": 16000
            }
          }
        }
      }
    }
  }
}
```

## [模型变体 (Variants)](https://opencode.ai/docs/models/#variants)
许多模型支持多种配置变体。
- **Anthropic**: `high` (默认高思考预算)、`max` (最大预算)。
- **OpenAI**: `none`、`minimal`、`low`、`medium`、`high`、`xhigh` (推理级别)。
- **Google**: `low`、`high` (Token 预算)。

你可以使用快捷键 `variant_cycle` 在变体之间快速切换。

## [加载优先级](https://opencode.ai/docs/models/#loading-models)
启动时，模型加载顺序如下：
1. `--model` 或 `-m` 命令行标志。
2. 配置文件中的 `model` 字段。
3. 上次使用的模型。
4. 内部默认列表中的第一个模型。
