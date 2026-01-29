---
创建日期: 2026-01-29T17:00:37+08:00
修改日期: 2026-01-29T17:30:35+08:00
---
# Antigravity + Gemini CLI OAuth Plugin for Opencode


使 OpenCode 能够通过 OAuth 对 **Antigravity**（Google 的 IDE）进行身份验证，以便您可以使用 Antigravity 的速率限制并使用您的 Google 凭据访问 `gemini-3-pro` 和 `claude-opus-4-5-thinking` 等模型。

## 您将获得

- 通过 Google OAuth 访问 **Claude Opus 4.5、Sonnet 4.5** 和 **Gemini 3 Pro/Flash**
- **多账户支持** — 添加多个 Google 账户，在达到速率限制时自动轮换
- **双重配额系统** — 从一个插件同时访问 Antigravity 和 Gemini CLI 配额
- **思考模型** — 为 Claude 和 Gemini 3 提供可配置预算的扩展思考
- **Google 搜索 grounding** — 为 Gemini 模型启用网络搜索（自动或始终开启）
- **自动恢复** — 自动处理会话错误和工具失败
- **插件兼容** — 与其他 OpenCode 插件（oh-my-opencode、dcp 等）一起使用

---

<details open>
<summary><b>⚠️ 服务条款警告 — 安装前请阅读</b></summary>

> [!CAUTION]
> 使用此插件可能违反 Google 的服务条款。少数用户报告其 Google 账户已被**封禁**或**被暗中封禁**（限制访问但未明确通知）。
>
> **高风险场景：**
> - 🚨 **新的 Google 账户**被封禁的可能性很高
> - 🚨 **拥有 Pro/Ultra 订阅的新账户**经常被标记并封禁
>
> **使用此插件，即表示您确认：**
> - 这是一个非官方工具，未经 Google 认可
> - 您的账户可能会被暂停或永久封禁
> - 您承担使用此插件的所有风险
>
> **建议：** 使用一个不依赖关键服务的现有 Google 账户。避免为此插件专门创建新账户。

</details>

---

## 安装

<details open>
<summary><b>面向普通用户</b></summary>

**选项 A：让 LLM 完成**

将此内容粘贴到任何 LLM 代理（Claude Code、OpenCode、Cursor 等）中：

```
按照 https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/dev/README.md 的说明安装 opencode-antigravity-auth 插件并将 Antigravity 模型定义添加到 ~/.config/opencode/opencode.json
```

**选项 B：手动设置**

1. **添加插件**到 `~/.config/opencode/opencode.json`：

   ```json
   {
     "plugin": ["opencode-antigravity-auth@latest"]
   }
   ```

   > 想要最新功能？使用 `opencode-antigravity-auth@beta` 代替。

2. **登录**您的 Google 账户：

   ```bash
   opencode auth login
   ```

3. **添加模型** — 复制下方的[完整配置](#models)

4. **使用：**

   ```bash
   opencode run "Hello" --model=google/antigravity-claude-sonnet-4-5-thinking --variant=max
   ```

</details>

<details>
<summary><b>面向 LLM 代理</b></summary>

### 分步说明

1. 编辑位于 `~/.config/opencode/opencode.json` 的 OpenCode 配置文件
   
   > **注意**：此路径在所有平台上都有效。在 Windows 上，`~` 解析为您的用户主目录（例如 `C:\Users\YourName`）。

2. 将插件添加到 `plugin` 数组

3. 从[完整模型配置](#models)部分添加模型定义

4. 将 `provider` 设置为 `"google"` 并选择一个模型

### 验证

```bash
opencode run "Hello" --model=google/antigravity-claude-sonnet-4-5-thinking --variant=max
```

</details>

---

## 模型

### 模型参考

**Antigravity 配额**（Claude + Gemini 3）：

| 模型 | 变体 | 说明 |
|-------|----------|-------|
| `antigravity-gemini-3-pro` | low, high | Gemini 3 Pro 带思考 |
| `antigravity-gemini-3-flash` | minimal, low, medium, high | Gemini 3 Flash 带思考 |
| `antigravity-claude-sonnet-4-5` | — | Claude Sonnet 4.5 |
| `antigravity-claude-sonnet-4-5-thinking` | low, max | Claude Sonnet 带扩展思考 |
| `antigravity-claude-opus-4-5-thinking` | low, max | Claude Opus 带扩展思考 |

**Gemini CLI 配额**（与 Antigravity 分开）：

| 模型 | 说明 |
|-------|-------|
| `gemini-2.5-flash` | Gemini 2.5 Flash |
| `gemini-2.5-pro` | Gemini 2.5 Pro |
| `gemini-3-flash-preview` | Gemini 3 Flash（预览） |
| `gemini-3-pro-preview` | Gemini 3 Pro（预览） |

**使用变体：**
```bash
opencode run "Hello" --model=google/antigravity-claude-sonnet-4-5-thinking --variant=max
```

有关变体配置和思考级别的详细信息，请参阅 [docs/MODEL-VARIANTS.md](docs/MODEL-VARIANTS.md)。

<details>
<summary><b>完整模型配置（可直接复制粘贴）</b></summary>

将其添加到您的 `~/.config/opencode/opencode.json`：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-antigravity-auth@latest"],
  "provider": {
    "google": {
      "models": {
        "antigravity-gemini-3-pro": {
          "name": "Gemini 3 Pro (Antigravity)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingLevel": "low" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-gemini-3-flash": {
          "name": "Gemini 3 Flash (Antigravity)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "minimal": { "thinkingLevel": "minimal" },
            "low": { "thinkingLevel": "low" },
            "medium": { "thinkingLevel": "medium" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-claude-sonnet-4-5": {
          "name": "Claude Sonnet 4.5 (Antigravity)",
          "limit": { "context": 200000, "output": 64000 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "antigravity-claude-sonnet-4-5-thinking": {
          "name": "Claude Sonnet 4.5 Thinking (Antigravity)",
          "limit": { "context": 200000, "output": 64000 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingConfig": { "thinkingBudget": 8192 } },
            "max": { "thinkingConfig": { "thinkingBudget": 32768 } }
          }
        },
        "antigravity-claude-opus-4-5-thinking": {
          "name": "Claude Opus 4.5 Thinking (Antigravity)",
          "limit": { "context": 200000, "output": 64000 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingConfig": { "thinkingBudget": 8192 } },
            "max": { "thinkingConfig": { "thinkingBudget": 32768 } }
          }
        },
        "gemini-2.5-flash": {
          "name": "Gemini 2.5 Flash (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-2.5-pro": {
          "name": "Gemini 2.5 Pro (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3-flash-preview": {
          "name": "Gemini 3 Flash Preview (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3-pro-preview": {
          "name": "Gemini 3 Pro Preview (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        }
      }
    }
  }
}
```

</details>

---

## 多账户设置

添加多个 Google 账户以获得更高的组合配额。当一个账户达到速率限制时，插件会自动在账户之间轮换。

```bash
opencode auth login  # 再次运行以添加更多账户
```

**账户管理选项（通过 `opencode auth login`）：**
- **查看配额** — 查看每个账户的剩余 API 配额
- **管理账户** — 启用/禁用特定账户进行轮换

有关负载平衡、双重配额池和账户存储的详细信息，请参阅 [docs/MULTI-ACCOUNT.md](docs/MULTI-ACCOUNT.md)。

---

## 故障排除

> **快速重置**：大多数问题可以通过删除 `~/.config/opencode/antigravity-accounts.json` 并再次运行 `opencode auth login` 来解决。

### 配置路径（所有平台）

OpenCode 在**所有平台**（包括 Windows）上都使用 `~/.config/opencode/`。

| 文件 | 路径 |
|------|------|
| 主配置 | `~/.config/opencode/opencode.json` |
| 账户 | `~/.config/opencode/antigravity-accounts.json` |
| 插件配置 | `~/.config/opencode/antigravity.json` |
| 调试日志 | `~/.config/opencode/antigravity-logs/` |

> **Windows 用户**：`~` 解析为您的用户主目录（例如 `C:\Users\YourName`）。请勿使用 `%APPDATA%`。

---

### 多账户身份验证问题

如果您遇到多账户的身份验证问题：

1. 删除账户文件：
   ```bash
   rm ~/.config/opencode/antigravity-accounts.json
   ```
2. 重新验证：
   ```bash
   opencode auth login
   ```

---

### 403 权限被拒绝 (`rising-fact-p41fc`)

**错误：**
```
Permission 'cloudaicompanion.companions.generateChat' denied on resource 
'//cloudaicompanion.googleapis.com/projects/rising-fact-p41fc/locations/global'
```

**原因：** 当找不到有效项目时，插件会回退到默认项目 ID。这对 Antigravity 有效，但对 Gemini CLI 模型会失败。

**解决方案：**
1. 前往 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建或选择一个项目
3. 启用 **Gemini for Google Cloud API** (`cloudaicompanion.googleapis.com`)
4. 将 `projectId` 添加到您的账户文件：
   ```json
   {
     "accounts": [
       {
         "email": "your@email.com",
         "refreshToken": "...",
         "projectId": "your-project-id"
       }
     ]
   }
   ```

> **注意**：在多账户设置中，对每个账户都执行此操作。

---

### Gemini 模型未找到

将此添加到您的 `google` 提供商配置中：

```json
{
  "provider": {
    "google": {
      "npm": "@ai-sdk/google",
      "models": { ... }
    }
  }
}
```

---

### Gemini 3 模型 400 错误（"Unknown name 'parameters'"）

**错误：**
```
Invalid JSON payload received. Unknown name "parameters" at 'request.tools[0]'
```

**原因：**
- 工具架构与 Gemini 的严格 protobuf 验证不兼容
- 具有错误架构的 MCP 服务器
- 插件版本回退

**解决方案：**
1. **更新到最新 beta 版本：**
   ```json
   { "plugin": ["opencode-antigravity-auth@beta"] }
   ```

2. **逐个禁用 MCP 服务器**以找到有问题的服务器

3. **添加 npm 覆盖：**
   ```json
   { "provider": { "google": { "npm": "@ai-sdk/google" } } }
   ```

---

### MCP 服务器导致错误

某些 MCP 服务器的架构与 Antigravity 的严格 JSON 格式不兼容。

**常见症状：**
```bash
Invalid function name must start with a letter or underscore
```

有时显示为：
```bash
GenerateContentRequest.tools[0].function_declarations[12].name: Invalid function name must start with a letter or underscore
```

这通常意味着 MCP 工具名称以数字开头（例如，1mcp 密钥如 `1mcp_*`）。将 MCP 密钥重命名为以字母开头（例如 `gw`）或为 Antigravity 模型禁用该 MCP 条目。

**诊断：**
1. 在配置中禁用所有 MCP 服务器
2. 逐个启用，直到错误再次出现
3. 在 [GitHub issue](https://github.com/NoeFabris/opencode-antigravity-auth/issues) 中报告特定的 MCP

---

### "所有账户已达到速率限制"（但配额可用）

**原因：** 混合模式下 `clearExpiredRateLimits()` 中的级联错误（在最近的 beta 版本中已修复）。

**解决方案：**
1. 更新到最新的 beta 版本
2. 如果仍然存在，删除账户文件并重新验证
3. 尝试在 `antigravity.json` 中将 `account_selection_strategy` 切换为 `"sticky"`

---

### 会话恢复

如果您在会话期间遇到错误：
1. 输入 `continue` 触发恢复机制
2. 如果被阻止，使用 `/undo` 恢复到错误前的状态
3. 重试操作

---

### 与 Oh-My-OpenCode 一起使用

**重要：** 禁用内置的 Google 身份验证以防止冲突：

```json
// ~/.config/opencode/oh-my-opencode.json
{
  "google_auth": false,
  "agents": {
    "frontend-ui-ux-engineer": { "model": "google/antigravity-gemini-3-pro" },
    "document-writer": { "model": "google/antigravity-gemini-3-flash" }
  }
}
```

---

### 创建无限 `.tmp` 文件

**原因：** 当账户达到速率限制且插件无限重试时，它会创建许多临时文件。

**解决方法：**
1. 停止 OpenCode
2. 清理：`rm ~/.config/opencode/*.tmp`
3. 添加更多账户或等待速率限制过期

---

### OAuth 回调问题

<details>
<summary><b>Safari OAuth 回调失败（macOS）</b></summary>

**症状：**
- 成功登录 Google 后显示"授权失败"
- Safari 显示"Safari 无法打开页面"

**原因：** Safari 的"仅 HTTPS 模式"阻止 `http://localhost` 回调。

**解决方案：**

1. **使用 Chrome 或 Firefox**（最简单）：
   复制 OAuth URL 并粘贴到不同的浏览器中。

2. **临时禁用仅 HTTPS 模式：**
   - Safari > 设置 (⌘,) > 隐私
   - 取消勾选"启用仅 HTTPS 模式"
   - 运行 `opencode auth login`
   - 身份验证后重新启用

</details>

<details>
<summary><b>端口冲突（地址已被使用）</b></summary>

**macOS / Linux:**
```bash
# 查找使用端口的进程
lsof -i :51121

# 如果是陈旧进程则终止
kill -9 <PID>

# 重试
opencode auth login
```

**Windows (PowerShell):**
```powershell
netstat -ano | findstr :51121
taskkill /PID <PID> /F
opencode auth login
```

</details>

<details>
<summary><b>Docker / WSL2 / 远程开发</b></summary>

OAuth 回调需要浏览器能够到达运行 OpenCode 的机器上的 `localhost`。

**WSL2:**
- 使用 VS Code 的端口转发，或
- 配置 Windows → WSL 端口转发

**SSH / 远程:**
```bash
ssh -L 51121:localhost:51121 user@remote
```

**Docker / 容器:**
- 容器中不支持使用 localhost 重定向的 OAuth
- 等待 30 秒以进行手动 URL 流程，或使用 SSH 端口转发

</details>

---

### 配置键拼写错误：`plugin` 不是 `plugins`

正确的键是 `plugin`（单数）：

```json
{
  "plugin": ["opencode-antigravity-auth@beta"]
}
```

**不是** `"plugins"`（会导致"无法识别的键"错误）。

---

### 在机器之间迁移账户

将 `antigravity-accounts.json` 复制到新机器时：
1. 确保插件已安装：`"plugin": ["opencode-antigravity-auth@beta"]`
2. 复制 `~/.config/opencode/antigravity-accounts.json`
3. 如果出现"API 密钥缺失"错误，刷新令牌可能无效 — 重新验证

## 已知插件交互
有关负载平衡、双重配额池和账户存储的详细信息，请参阅 [docs/MULTI-ACCOUNT.md](docs/MULTI-ACCOUNT.md)。

---

## 插件兼容性

### @tarquinen/opencode-dcp

DCP 创建缺少思考块的合成助手消息。**将此插件列在 DCP 之前：**

```json
{
  "plugin": [
    "opencode-antigravity-auth@latest",
    "@tarquinen/opencode-dcp@latest"
  ]
}
```

### oh-my-opencode

在 `oh-my-opencode.json` 中禁用内置身份验证并覆盖代理模型：

```json
{
  "google_auth": false,
  "agents": {
    "frontend-ui-ux-engineer": { "model": "google/antigravity-gemini-3-pro" },
    "document-writer": { "model": "google/antigravity-gemini-3-flash" },
    "multimodal-looker": { "model": "google/antigravity-gemini-3-flash" }
  }
}
```

> **提示：** 生成并行子代理时，在 `antigravity.json` 中启用 `pid_offset_enabled: true` 以跨账户分配会话。

### 您不需要的插件

- **gemini-auth 插件** — 不需要。此插件处理所有 Google OAuth。

---

## 配置

创建 `~/.config/opencode/antigravity.json` 以进行可选设置：

```json
{
  "$schema": "https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/assets/antigravity.schema.json"
}
```

大多数用户不需要配置任何内容 — 默认设置效果很好。

### 模型行为

| 选项 | 默认值 | 作用 |
|--------|---------|--------------|
| `keep_thinking` | `false` | 在回合间保留 Claude 的思考。**警告：** 启用可能会降低模型稳定性。 |
| `session_recovery` | `true` | 从工具错误中自动恢复 |
| `web_search.default_mode` | `"off"` | Gemini Google 搜索：`"auto"` 或 `"off"` |

### 账户轮换

| 您的设置 | 推荐配置 |
|------------|-------------------|
| **1 个账户** | `"account_selection_strategy": "sticky"` |
| **2-5 个账户** | 默认（`"hybrid"`）效果很好 |
| **5+ 个账户** | `"account_selection_strategy": "round-robin"` |
| **并行代理** | 添加 `"pid_offset_enabled": true` |

### 速率限制调度

控制插件如何处理速率限制：

| 选项 | 默认值 | 作用 |
|--------|---------|--------------|
| `scheduling_mode` | `"cache_first"` | `"cache_first"` = 等待同一账户（保留提示缓存），`"balance"` = 立即切换，`"performance_first"` = 轮询 |
| `max_cache_first_wait_seconds` | `60` | 在 cache_first 模式下切换账户前等待的最长秒数 |
| `failure_ttl_seconds` | `3600` | 在此秒数后重置失败计数（防止旧失败永久惩罚账户） |

**何时使用每种模式：**
- **cache_first**（默认）：最适合长对话。等待同一账户恢复，保留您的提示缓存。
- **balance**：最适合快速任务。达到速率限制时立即切换账户以获得最大可用性。
- **performance_first**：最适合许多短请求。在所有账户之间均匀分配负载。

### 应用行为

| 选项 | 默认值 | 作用 |
|--------|---------|--------------|
| `quiet_mode` | `false` | 隐藏 toast 通知 |
| `debug` | `false` | 启用调试日志 |
| `auto_update` | `true` | 自动更新插件 |

有关所有选项，请参阅 [docs/CONFIGURATION.md](docs/CONFIGURATION.md)。

**环境变量：**
```bash
OPENCODE_ANTIGRAVITY_DEBUG=1 opencode   # 启用调试日志
OPENCODE_ANTIGRAVITY_DEBUG=2 opencode   # 详细日志
```

---

## 故障排除

请参阅完整的[故障排除指南](docs/TROUBLESHOOTING.md)，了解常见问题的解决方案，包括：

- 身份验证问题和令牌刷新
- "模型未找到"错误
- 会话恢复
- Gemini CLI 权限错误
- Safari OAuth 问题
- 插件兼容性
- 迁移指南

---

## 文档

- [配置](docs/CONFIGURATION.md) — 所有配置选项
- [多账户](docs/MULTI-ACCOUNT.md) — 负载平衡、双重配额池、账户存储
- [模型变体](docs/MODEL-VARIANTS.md) — 思考预算和变体系统
- [故障排除](docs/TROUBLESHOOTING.md) — 常见问题和修复
- [架构](docs/ARCHITECTURE.md) — 插件工作原理
- [API 规范](docs/ANTIGRAVITY_API_SPEC.md) — Antigravity API 参考

---

## 支持

如果此插件对您有帮助，请考虑支持其维护：

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/S6S81QBOIR)

---

## 致谢

- [opencode-gemini-auth](https://github.com/jenslys/opencode-gemini-auth) by [@jenslys](https://github.com/jenslys)
- [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)

## 许可证

MIT 许可证。详细信息请参阅 [LICENSE](LICENSE)。

<details>
<summary><b>法律</b></summary>

### 预期用途

- 仅用于个人/内部开发
- 尊重内部配额和数据处理策略
- 不用于生产服务或绕过预期限制

### 警告

使用此插件，即表示您确认：

- **服务条款风险** — 此方法可能违反 AI 模型提供商的服务条款
- **账户风险** — 提供商可能会暂停或封禁账户
- **无保证** — API 可能会在不通知的情况下更改
- **风险承担** — 您承担所有法律、财务和技术风险

### 免责声明

- 与 Google 无关。这是一个独立的开源项目。
- "Antigravity"、"Gemini"、"Google Cloud" 和 "Google" 是 Google LLC 的商标。

</details>