# 网络设置 (Network)

配置代理和自定义证书。
OpenCode 支持标准代理环境变量以及企业网络环境中的自定义证书。

## [代理 (Proxy)](https://opencode.ai/docs/network/#proxy)
OpenCode 遵循标准代理环境变量。

```bash
# HTTPS 代理 (推荐)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP 代理 (如果 HTTPS 不可用)
export HTTP_PROXY=http://proxy.example.com:8080

# 为本地服务器绕过代理 (必须)
export NO_PROXY=localhost,127.0.0.1
```

**警告**：TUI 与本地 HTTP 服务器通信。你 **必须** 为此连接绕过代理，以防止路由回环。

### [认证 (Authenticate)](https://opencode.ai/docs/network/#authenticate)
如果你的代理需要基本身份验证 (Basic Auth)，请在 URL 中包含凭据。

```bash
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

**注意**：避免硬编码密码。建议使用环境变量或安全凭据存储。对于需要 NTLM 或 Kerberos 等高级认证的代理，请考虑使用支持该认证方式的 LLM 网关。

## [自定义证书](https://opencode.ai/docs/network/#custom-certificates)
如果你的企业使用自定义 CA 进行 HTTPS 连接，请配置 OpenCode 信任它们。

```bash
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```

这适用于代理连接和直接的 API 访问。
