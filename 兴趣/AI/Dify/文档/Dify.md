## 安装
https://docs.dify.ai/zh-hans/getting-started/install-self-hosted/docker-compose

## 更新
首先电脑打开 docker desktop，然后
进入 dify 源代码的 docker 目录，按顺序执行以下命令：
```
cd dify/docker
docker compose down
git pull origin main
docker compose pull
docker compose up -d
```
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20250113230101.png)
