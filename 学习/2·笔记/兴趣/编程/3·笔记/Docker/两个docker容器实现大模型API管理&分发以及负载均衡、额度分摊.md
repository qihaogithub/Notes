---
title: "管管你的羊毛API吧！两个docker容器实现大模型API管理&分发以及负载均衡、额度分摊|076 -         米拉一频道"
source: "https://www.milaone.com/archives/156.html"
author:
published:
created: 2025-01-15
description: "One-hubdocker run -d -p 3300:3000 \  --name one-hub \  --restart always \  -e TZ=Asia/Shanghai \ ..."
tags:
  - "clippings"
---
![076thum2.png](https://www.milaone.com/usr/uploads/2024/12/3016530476.png "076thum2.png")

### One-api
一键部署
```
docker run --name one-api -d --restart always -p 3005:3000 -e TZ=Asia/Shanghai -v 
/home/ubuntu/data/one-api:/data ghcr.io/songquanpeng/one-api
```

管理员：root  
密码：123456

### One-hub   
```
docker run -d -p 3006:3000 \
  --name one-hub \
  --restart always \
  -e TZ=Asia/Shanghai \
  -e USER_TOKEN_SECRET="user_token_secret" \
  -e SESSION_SECRET="session_secret" \
  -v /home/ubuntu/data/one-hub:/data \
  ghcr.io/martialbe/one-api
```
管理员：root  
密码：123456

### Open-WebUI

```powershell
docker run -d -p 3311:8080 \
    -v /home/ubuntu/data/openwebui/data:/app/backend/data \
    --name open-webui \
    --restart always \
    ghcr.io/open-webui/open-webui:main
```

首次登陆需要注册管理员账户

### github 模型市场地址

[https://github.com/marketplace/models/catalog](https://github.com/marketplace/models/catalog)

### 谷歌 Gemini API

[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)