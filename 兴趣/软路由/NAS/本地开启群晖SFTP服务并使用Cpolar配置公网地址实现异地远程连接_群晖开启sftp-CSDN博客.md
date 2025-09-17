

### 前言

本文主要介绍如何将在[群晖NAS](https://so.csdn.net/so/search?q=%E7%BE%A4%E6%99%96NAS&spm=1001.2101.3001.7020) 中开启 SFTP 服务，并安装 cpolar 内网穿透工具配置公网地址，轻松打造一套高效、安全的跨网络远程文件传输解决方案，享受无缝的远程工作与生活体验。

在数字化转型的浪潮中，远程办公与数据共享已成为常态。群晖 [SFTP文件传输](https://so.csdn.net/so/search?q=SFTP%E6%96%87%E4%BB%B6%E4%BC%A0%E8%BE%93&spm=1001.2101.3001.7020)服务以其强大的安全性和灵活性，成为了众多用户管理与传输文件的首选。然而，当面对无公网 IP 或复杂网络环境时，如何实现远程访问成为一大挑战。

为此，我们引入了 [Cpolar](https://so.csdn.net/so/search?q=Cpolar&spm=1001.2101.3001.7020) 内网穿透技术，它如同一把钥匙，解锁了远程访问内网 SFTP 服务的可能性。通过简单配置，Cpolar 能将群晖 SFTP 服务安全地映射至公网，让您无论身处何地，都能轻松实现文件的上传、下载与管理。

![](https://i-blog.csdnimg.cn/direct/6cf4c4f39a454c0e8cb2e66a1a4d33ff.jpeg)

### 1\. 开启群晖 SFTP 连接

打开群晖控制面板, 找到文件服务, 点击 FTP, 最下面开启 SFTP 服务即可, 然后点击应用, 这样群晖 SFTP 服务就开启了, 我们看到端口是 22, 下面我们本地测试一下能否正常连接

![](https://i-blog.csdnimg.cn/blog_migrate/452bc63471eada1a65a7bfdbb3cf879c.png)

打开一个连接工具, 这里使用 filezilla 客户端进行连接, 打开后输入群晖局域网 IP, 用户名密码, 还有 22 端口, 点击连接

![](https://i-blog.csdnimg.cn/blog_migrate/04014066fb7dc4e99afe516f08e50050.png)

出现提示信息, 点击确定

![](https://i-blog.csdnimg.cn/blog_migrate/a13ef9d63597592076005d6a62def2b6.png)

可以看到列出目录成功, 表示连接成功了, 本地开启群晖 SFTP 服务和本地测试连接就通过了, 下面我们安装 cpolar 实现远程也可以连接

![](https://i-blog.csdnimg.cn/blog_migrate/280d25c33986d055e8822e669757179b.png)

### 2\. 群晖安装 Cpolar 工具

Cpolar 提供了群晖安装的套件, 点击下面 Cpolar 群晖套件下载地址, 下载相应版本的群晖 Cpolar 套件, 如果找不到对应的型号, 可以选择相近版本型号套件

> https://www.cpolar.com/synology-cpolar-suite ,

![](https://i-blog.csdnimg.cn/blog_migrate/5356538430cbfccffe1b06c391ac5f5f.png)

打开群晖 `套件中心`，点击右上角的 `手动安装` 按钮。

![](https://i-blog.csdnimg.cn/blog_migrate/ecf39c4df63d175be8bb4b28c11f6426.png)

选择我们本地下载好的 cpolar 套件安装包, 然后点击下一步

![](https://i-blog.csdnimg.cn/blog_migrate/eae2b070b66e0de914b8615635d59227.png)

点击 `同意` 按钮, 然后点击下一步

![](https://i-blog.csdnimg.cn/blog_migrate/00139d4f233ac04af58861fd5b03edf1.png)

最后点击完成即可。

![](https://i-blog.csdnimg.cn/blog_migrate/f0a1b0faa6956ef8744e6f92688a5253.png)

安装完成后, 在外部浏览器, 我们通过 `群晖的局域网ip地址` 加 `9200` 端口访问 Cpolar 的 Web 管理界面, 然后输入 Cpolar 邮箱账号与密码进行登录

![](https://i-blog.csdnimg.cn/blog_migrate/5a24442b8c870bbd10cbd811234aa81e.png)

### 3\. 创建 SFTP 公网地址

登录 cpolar web UI 管理界面后, 点击左侧仪表盘的隧道管理——创建隧道：

*   隧道名称：可自定义，注意不要与已有的隧道名称重复
*   协议：tcp
*   本地地址：22 (SFTP 默认端口)
*   域名类型：临时随机 TCP 端口
*   地区：选择 China vip

点击 `创建`

![](https://i-blog.csdnimg.cn/blog_migrate/c7e3cddce7ad44d74bdfdac201190a0c.png)

创建后, 然后打开左侧在线隧道列表, 查看我们创建的 cpolar 公网 TCP 地址, 使用这个地址, 我们可以在其他网络设备上连接群晖 SFTP 文件服务, 下面进行连接测试

![](https://i-blog.csdnimg.cn/blog_migrate/f3b1b71369c8ccefa7bd4d7eea3e09f9.png)

### 4\. 群晖 SFTP 远程连接

还是打开 filezilla, 输入我们在 cpolar 创建的公网 tcp 地址, 注意端口要改为公网地址后面的 5 位数端口号, 然后点击连接

![](https://i-blog.csdnimg.cn/blog_migrate/60b6715c34232ad0f6dc14334ac56390.png)

出现提示, 点击确定

![](https://i-blog.csdnimg.cn/blog_migrate/176e7d7c9c38c3b4985a5961f544a058.png)

可以看到列出目录成功了, 表示连接也成功了, SFTP 对比 FTP 好处就是, 简单, 容易配置, 更安全, 这样一个远程地址就设置好了, 使用该地址, 可以到任意设备连接!

![](https://i-blog.csdnimg.cn/blog_migrate/68ae9127dd2f939a8602bccea678cb68.png)

**小结**

为了更好地演示，我们在前述过程中使用了 Cpolar 生成的隧道，其公网地址是随机生成的。

这种随机地址的优势在于建立速度快，可以立即使用。然而，它的缺点是网址是随机生成，这个地址在 24 小时内会发生随机变化，更适合于临时使用。

我一般会建议使用固定 TCP 域名，原因是我希望将地址发送给同事或客户时，它是一个固定、易记的公网地址，这样更显正式，便于流交协作。

### 5\. 固定 SFTP 公网地址

以上步骤在 cpolar 中使用的是随机临时 tcp 端口地址，所生成的公网地址为随机临时地址，该公网地址 24 小时内会随机变化。我们接下来为其配置固定的公网地址和端口，该地址端口不会变化，设置后将无需每天重复修改地址。

> 配置固定 tcp 端口地址需要将 Cpolar 升级到专业版套餐或以上。

登录 Cpolar 官网 ([https://www.cpolar.com](https://www.cpolar.com/))，点击左侧的预留，找到保留的 tcp 地址，我们来为 SSH 保留一个固定 tcp 地址：

*   地区：选择 China vip
*   描述：即备注，可自定义

点击 `保留`

![](https://i-blog.csdnimg.cn/blog_migrate/e7b1cf29aaeb265729aa0e3789e9d31f.png)

地址保留成功后，系统会生成相应的固定公网地址，将其复制下来

![](https://i-blog.csdnimg.cn/blog_migrate/1a31c6cf49e2db23b5fc4a514073a1bf.png)

再次打开 cpolar web ui 管理界面，点击左侧仪表盘的隧道管理——隧道列表，找到我们上面创建的 TCP 隧道，点击右侧的 `编辑`

![](https://i-blog.csdnimg.cn/blog_migrate/1a0bd6d8dd076b776e5a299a63c82238.png)

修改隧道信息，将保留成功的固定 tcp 地址配置到隧道中

*   端口类型：修改为固定 tcp 端口
*   预留的 TCP 地址：填写官网保留成功的地址，

点击 `更新` (只需要点击一次更新即可)

![](https://i-blog.csdnimg.cn/blog_migrate/d1a26f67895c9689aa70158f1b77631f.png)

隧道更新成功后，点击左侧仪表盘的状态——在线隧道列表，可以看到公网地址已经更新成为了和我们在官网固定的 TCP 地址和端口一致。

![](https://i-blog.csdnimg.cn/blog_migrate/0911e40814d24a4b9d3c0226a9fdad93.png)

### 6\. SFTP 固定地址连接

固定好了地址后, 使用我们固定的 TCP 地址进行连接, 同样打开 filezilla, 输入我们固定的 tcp 地址, 点击快速连接, 列出目录成功, 可以看到同样连接成功, 一个永久不变的固定地址就设置好了, 不用担心地址会变化了!

![](https://i-blog.csdnimg.cn/blog_migrate/389332470e1ccfbffe2dc3f292e397cb.png)