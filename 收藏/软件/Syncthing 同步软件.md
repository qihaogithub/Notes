要在Docker中安装和运行Syncthing，可以按照以下步骤操作：

1. **拉取Syncthing官方镜像**

   ```bash
   docker pull syncthing/syncthing
   ```

2. **创建配置和数据目录**

   ```bash
   mkdir -p ~/syncthing/config ~/syncthing/data
   ```

3. **运行Syncthing容器**

```bash
docker run --name syncthing  -d --restart=always \
        --hostname=syncthing \
        -e PUID=1000 -e PGID=1000 \
        -e TZ=Asia/Shanghai \
        -p 8384:8384 \
        -p 22000:22000/tcp \
        -p 22000:22000/udp \
        -p 21027:21027/udp \
        -v /www/wwwroot/syncthing/config:/config \
        -v /www/wwwroot/syncthing/data:/var/syncthing \ 
        syncthing/syncthing
```

3. **访问Web界面**
   打开浏览器，访问 `http://localhost:8384` 即可管理Syncthing。

4. **配置防火墙（如果需要）**
   确保防火墙开放了以下端口：
   - `8384/tcp`（Web界面）
   - `22000/tcp` 和 `22000/udp`（设备同步）
   - `21027/udp`（发现协议）

**注意事项**：
- 配置和数据目录会持久保存在主机上，确保有足够空间
- 如果需要远程访问Web界面，建议启用HTTPS和认证
- 如需在后台运行，可添加 `-d` 参数到 `docker run` 命令

