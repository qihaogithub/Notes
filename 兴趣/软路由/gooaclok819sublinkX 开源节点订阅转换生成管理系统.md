---
title: "gooaclok819/sublinkX: 开源节点订阅转换生成管理系统"
source: "https://github.com/gooaclok819/sublinkX"
author:
published:
created: 2025-01-17
description:
tags:
  - "clippings"
---
[![](https://github.com/gooaclok819/sublinkX/raw/main/webs/src/assets/logo.png)](https://github.com/gooaclok819/sublinkX/blob/main/webs/src/assets/logo.png)

## \[项目简介\]

项目基于sublink项目二次开发：[https://github.com/jaaksii/sublink](https://github.com/jaaksii/sublink)

前端基于：[https://github.com/youlaitech/vue3-element-admin](https://github.com/youlaitech/vue3-element-admin)

后端采用go+gin+gorm

默认账号admin 密码123456 自行修改

因为重写目前还有很多布局结构以及功能稍少

## \[项目特色\]

自由度和安全性较高，能够记录访问订阅，配置轻松

二进制编译无需Docker容器

目前仅支持客户端：v2ray clash surge

v2ray为base64通用格式

clash支持协议:ss ssr trojan vmess vless hy hy2 tuic

surge支持协议:ss trojan vmess hy2 tuic

## \[项目预览\]

[![1712594176714](https://github.com/gooaclok819/sublinkX/raw/main/webs/src/assets/1.png)](https://github.com/gooaclok819/sublinkX/blob/main/webs/src/assets/1.png) [![1712594176714](https://github.com/gooaclok819/sublinkX/raw/main/webs/src/assets/2.png)](https://github.com/gooaclok819/sublinkX/blob/main/webs/src/assets/2.png)

## \[更新说明\]

新增指定客户端

修复菜单更新功能没更新菜单版本

## \[安装说明\]

### linux方式：

```
curl -s -H "Cache-Control: no-cache" -H "Pragma: no-cache" https://raw.githubusercontent.com/gooaclok819/sublinkX/main/install.sh | sudo bash
```

`sublink` 呼出菜单

然后输入安装脚本即可

### docker方式：

在自己需要的位置创建一个目录比如mkdir sublinkx

然后cd进入这个目录，输入下面指令之后数据就挂载过来

需要备份的就是db和template

```
docker run --name sublinkx -p 8000:8000 \
-v $PWD/db:/app/db \
-v $PWD/template:/app/template \
-v $PWD/logs:/app/logs \
-d jaaksi/sublinkx
```

## Stargazers over time

[![Stargazers over time](https://camo.githubusercontent.com/1a250c40ac87f2220d4375a111646c62d0d063ff7d34f0063685883c8b364b82/68747470733a2f2f7374617263686172742e63632f676f6f61636c6f6b3831392f7375626c696e6b582e7376673f76617269616e743d6164617074697665)](https://starchart.cc/gooaclok819/sublinkX)