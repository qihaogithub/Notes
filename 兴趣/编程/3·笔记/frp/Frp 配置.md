## Frps 配置

```toml
[common]
bind_addr = "0.0.0.0"
bind_port = 7000
vhost_http_port = 40800
vhost_https_port = 40443

auth.method = "token"
auth.token = "60d8a83c544e6168db"

web_server.addr = "0.0.0.0"
web_server.port = 7500
web_server.user = "qihao"
web_server.password = "qh9189"

# tls
# transport.tls.force = true
# transport.tls.cert_file = "/etc/frp/ssl/server.crt"
# transport.tls.key_file = "/etc/frp/ssl/server.key"
# transport.tls.trusted_ca_file = "/etc/frp/ssl/ca.crt"
```

## Frpc 配置

```toml
# frpc 配置
[common]
server_addr = "152.32.226.106"  
server_port = 7000               
auth.method = "token"
auth.token = "60d8a83c544e6168db"

# 客户端管理服务
admin_addr = "10.130.33.131"
admin_port = 7400
admin_user = "admin"
admin_pwd = "admin"

# 如果服务器启用 TLS，取消注释以下行
# transport.tls.enable = true

[ChatGPT-Mirror]
type = "tcp"
local_ip = "127.0.0.1"
local_port = 50002
remote_port = 50002

[baota]
type = "tcp"
local_ip = "127.0.0.1"
local_port = 11387
remote_port = 11387
```