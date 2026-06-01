```
# ============================================
# Pi Agent LLM API 配置
# ============================================
#
# 推荐方式：在管理后台「AI 后端供应商」页面在线配置（无需重启）
# 本文件中的 PI_AGENT_PROVIDER / PI_AGENT_PROVIDERS / PI_AGENT_API_KEY / PI_AGENT_BASE_URL / PI_AGENT_MODEL
# 作为未配置管理后台时的 fallback,或用于 Docker 部署

# ── 方式一：单供应商配置（简单模式）──

# 供应商 ID（决定模型 ID 前缀，如 "jojo" → 模型显示为 "jojo/deepseek-v4-flash"）
# 留空时使用管理后台推送的配置
PI_AGENT_PROVIDER=jojo

# API Key（fallback；管理后台可覆盖）
PI_AGENT_API_KEY=sk-WVZggReZJwlES2Bo0FCkZvAw5D3inMpXlfOzGBZixSgYvEw5

# API 基础地址（OpenAI 兼容格式）
PI_AGENT_BASE_URL=https://token.xjjj.co/v1

# 模型名称（fallback）
PI_AGENT_MODEL=deepseek-v4-flash

# ── 方式二：多供应商配置（JSON 格式，优先级高于方式一）──
# 取消注释以下变量即可启用，同时注释掉方式一的 PI_AGENT_PROVIDER / PI_AGENT_API_KEY / PI_AGENT_BASE_URL / PI_AGENT_MODEL
# 推荐使用管理后台「AI 后端供应商」页面进行配置,无需重启服务
#
# PI_AGENT_PROVIDERS='[{"id":"jojo","name":"xjjj 中转","baseURL":"https://token.xjjj.co/v1","apiKey":"sk-...","models":["deepseek-v4-flash","gpt-4"]}]'

# ============================================
# 服务地址配置
# ============================================

# 外部访问地址(局域网部署时修改为实际 IP)
NEXT_PUBLIC_AGENT_SERVICE_URL=http://localhost:3201
NEXT_PUBLIC_WEB_URL=http://localhost:3200
NEXT_PUBLIC_DATA_BASE=http://localhost:3200

# CORS 允许的来源
CORS_ORIGINS=http://localhost:3200,http://localhost:3300,http://127.0.0.1:3200,http://127.0.0.1:3300

# JWT 密钥
JWT_SECRET=change-this-to-a-random-string

# ============================================
# 管理后台配置
# ============================================

# 管理后台访问密钥 (生产环境必须修改为强随机字符串)
ADMIN_SECRET=admin-change-this-to-random-string

# ============================================
# Pi Agent 配置（agent-service 端，已迁移到统一供应商配置）
# ============================================

# 注：以下 PI_AGENT_* 变量已移至上方「Pi Agent LLM API 配置」段统一管理
# 旧版 OPENCODE_* 变量已全部移除（迁移至 Pi Agent 单后端架构）

# ============================================
# 内部 API 鉴权
# ============================================

# author-site → agent-service 内部调用的共享密钥
# 两端必须使用相同值,否则管理后台「AI 后端供应商」推送会失败
# 建议生产环境使用 32 字节以上随机字符串
INTERNAL_API_TOKEN=change-this-internal-shared-token-32bytes-min

# Pi Agent 超时时间（毫秒）
PI_AGENT_TIMEOUT=120000

```