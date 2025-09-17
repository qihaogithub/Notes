# 安装
Ssh 连接 ubuntu 后，输入命令
```
curl -s https://install.zerotier.com | sudo bash
```
# 使用
在Ubuntu系统中安装ZeroTier后，您可以按照以下步骤来使用它：

1. **启动ZeroTier服务**：
   您可以通过以下命令来启动ZeroTier服务：
   ```bash
   sudo systemctl start zerotier-one.service
   # 或者
   sudo service zerotier-one start
   ```

2. **加入网络**：
   要加入一个ZeroTier网络，您需要知道该网络的Network ID。使用以下命令加入网络：
   ```bash
   sudo zerotier-cli join <Network ID>
   ```
   替换`<Network ID>`为您的实际网络ID。执行该命令后，您应该会看到“200 join OK”的响应，表示您已成功加入网络。

3. **查看网络列表**：
   您可以通过以下命令查看所有可用的ZeroTier网络列表：
   ```bash
   sudo zerotier-cli listnetworks
   ```

4. **查看当前网络状态**：
   要查看当前ZeroTier网络的状态，可以使用以下命令：
   ```bash
   sudo zerotier-cli status
   ```

5. **离开网络**：
   如果您想离开当前的ZeroTier网络，可以使用以下命令：
   ```bash
   sudo zerotier-cli leave <Network ID>
   ```
   同样，替换`<Network ID>`为您的实际网络ID。

6. **设置开机自启动**：
   如果您希望ZeroTier在系统启动时自动启动，可以使用以下命令：
   ```bash
   sudo systemctl enable zerotier-one.service
   ```

7. **图形化管理界面（可选）**：
   如果您想要一个图形化界面来管理ZeroTier，可以安装ZeroTier的GUI版本。具体安装步骤可以参考相关教程和文档[^8^]。

以上步骤可以帮助您在Ubuntu系统中使用ZeroTier进行网络配置和管理。如果您遇到任何问题，可以查看ZeroTier的官方文档或者社区论坛获取更多帮助。