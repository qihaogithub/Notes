---
创建日期: 2026-04-17T18:13:35+08:00
修改日期: 2026-04-17T18:13:53+08:00
---

## 问题背景
执行 `git clone/push` 时，报错：
`fatal: unable to access 'https://github.com/xxx/xxx.git/': LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to github.com:443`

排查发现 `ping github.com` 解析到了虚假 IP：`198.18.1.26`，根源是 **Clash 的 DNS 虚假 IP 模式与 Git 不兼容**。

---

## 🔍 核心原因
1.  **Clash 虚假 IP 模式的机制**：为了绕过 DNS 污染，给域名分配 `198.18.0.0/16` 段的虚假 IP，连接时再转发到真实节点。
2.  **Git 兼容性问题**：Git 会直接用虚假 IP 发起 SSL 连接，导致证书域名校验失败，触发 `SSL_ERROR_SYSCALL`。
3.  **规则配置错误**：`真实IP回应` 列表里的通配符写法错误，且被优先级更高的 `*` 规则覆盖，导致 GitHub 域名仍走虚假 IP。

---

## ✅ 最终解决步骤
### 1. 修正 Clash DNS 配置
1.  打开 Clash → 设置 → DNS 设置
2.  找到「真实 IP 回应」列表：
    - 删除列表最顶部的 `*` 规则（它会强制所有域名走虚假 IP）
    - 按以下顺序添加开发常用域名（Clash 从上到下匹配，越靠上优先级越高）：
      ```
      github.com
      +.github.com
      gitlab.com
      +.gitlab.com
      npmjs.com
      +.npmjs.com
      docker.com
      +.docker.com
      ```
    - 原有的 `+.lan`、`+.local` 等本地规则可以保留在列表下方。
3.  「域名映射模式」保持 `虚假 IP` 即可（不影响浏览器使用，仅让开发域名走真实 IP）。

### 2. 验证配置是否生效
终端执行：
```bash
ping github.com
```
- 正常：解析到 GitHub 真实公网 IP（如 `140.82.113.4`）
- 异常：仍解析到 `198.18.x.x`，重启 Clash 再试。

### 3. 修复 Git 配置（可选，防止后续异常）
```bash
# 清空残留代理配置
git config --global --unset http.proxy
git config --global --unset https.proxy

# macOS 切换 SSL 后端，解决 LibreSSL 兼容性问题
git config --global http.sslBackend "openssl"

# 强制使用 HTTP/1.1，规避 HTTP/2 握手问题
git config --global http.version HTTP/1.1
```

---

## 💡 避坑总结
1.  **通配符规则写法**：Clash 中匹配子域名用 `+.xxx.com`，`*.xxx.com` 不生效。
2.  **规则优先级**：列表越靠上的规则优先级越高，通用规则（如 `*`）会覆盖下方的具体域名规则。
3.  **虚假 IP 模式**：对终端工具（Git、curl、npm）兼容性差，开发场景建议给常用域名配置「真实 IP 回应」。
4.  **快速兜底方案**：如果配置复杂，可临时把「域名映射模式」改成 `真实 IP`，所有域名直接解析真实 IP，避免终端兼容性问题。

---

## 附：开发场景推荐 Clash DNS 配置
| 配置项 | 推荐值 | 说明 |
| :--- | :--- | :--- |
| 启用 DNS | ✅ 开启 | 保持 DNS 代理能力 |
| 域名映射模式 | 虚假 IP | 兼顾浏览器防污染能力 |
| 回应范围 | `198.18.0.1/16` | 默认即可 |
| 真实 IP 回应 | 按顺序添加：`github.com`、`+.github.com`、`gitlab.com`、`+.gitlab.com`、`npmjs.com`、`+.npmjs.com`、`+.lan`、`+.local`、`time.*.com`、`ntp.*.com` | 开发域名优先真实 IP，本地和 NTP 规则保留 |
| IPv6 | ❌ 关闭 | 避免 IPv6 解析异常 |

需要我帮你整理一份可以直接复制的「开发友好型 Clash DNS 配置模板」吗？