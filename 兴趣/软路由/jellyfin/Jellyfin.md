## Jellyfin设置

第一次打开「Jellyfin」，会要求创建一个帐户，创建完毕后，添加媒体库。这里的账号创建完毕后，如果想给朋友或者家人新建帐户，可以稍后在「控制台」的「用户」选项卡中添加，并设置权限。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155417.png)
### 媒体库添加

媒体库按照不同的分类，添加不同的内容类型。这里很多朋友在「文件夹」的选择中，会发现无法添加文件夹路径。其原因是你没有在NAS中对Jellyfin开放文件夹的访问权限。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155426.png)
可以在File Station中，按下图所示步骤，为Jellyfin添加文件访问权限，最后点击保存。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155503.png)

文件夹路径添加完毕后，剩余的设置可参考下图。其中「元数据下载器」等表示你的资源相关的信息优先从什么地方自动抓取，后文会讲到。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155537.png)
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155548.png)

元数据下载器即「刮削器」，用于从网络抓取信息

### 「刮削器」设置

「刮削器」一般指从网络上自动获取影片相关信息的软件，我们可以使用插件达成这一目的。如果你专注于电影或影视，有「TMDb」插件就够。如果你想抓取动漫相关的信息，可以考虑使用「Bangumi」插件。如果你想要看漫画或者书籍，可以用「Bookshelf」插件。如果你想与Infuse同步进度，可以使用「InfuseSync」插件。如果你想在安卓TV端同步进度，可以使用TV端的播放器「Kodi」播放，添加「Kodi Sync Queue」插件，加快同步速度。

#### 常规插件安装方式

在「控制台」的「插件」选项卡中，上方找到「目录」，点击后等待几分钟。由于国内网络限制，进入「目录」的时间会比较久，请耐心等待，一定能进得去的，不行就刷新下。在「目录」中找到「TMDb」、「Bookshelf」、「InfuseSync」和「Kodi Sync Queue」插件安装，安装完毕后，需重启方可生效。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155625.png)
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155630.png)

常规插件安装

#### 存储库插件安装方式

如果你有额外的「刮削器」需求，可以在「存储库」中添加插件来源，比如动漫插件「Bangumi」,其来源`https://jellyfin-plugin-bangumi.pages.dev/repository.json`。添加完来源后，依旧是回到「目录」中寻找插件，点击安装，重启Jellyfin。此处重启过后，可以在最下方看到插件设置。

官方提供的存储库可以在[这里](https://sspai.com/link?target=https%3A%2F%2Fjellyfin.org%2Fdocs%2Fgeneral%2Fserver%2Fplugins%2Findex.html%23repositories)找到。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155659.png)
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155703.png)

存储库插件安装

#### 「TMDb」使用说明

TMDB的全称是The Movie Database，几乎所有的电影和电视剧都可以在这里找到信息来源。下载好的资源最好改成跟TMDB中一样的名字，方便刮削信息。国内是可以登陆TMDB网站的，但刮削器的「TMDb」插件往往刮削很慢，甚至刮不出来。其原因在于，举个例子，正常情况下，`themoviedb.org`这个域名会对应一个IP，比如120.120.120.120，由于国内特殊情况，刮削器的插件中，`themoviedb.org`域名对应的IP被修改成了198.198.198.198，因此无法查找到对应的资源信息。

可以通过修改群晖NAS的hosts文件，把正确的IP给矫正过来。这里我们以MAC为例，使用SSH进行修改。

首先我们需要打开SSH选项，同时指定端口，端口不要与常用端口冲突。并在网络选项卡中找到NAS的IP地址（有绑定域名的，用域名也可以）。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155715.png)
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155734.png)

打开SSH功能，并找到IP

打开MAC的「终端」输入：`ssh 用户帐号@IP地址  -p  端口`。

举例：`ssh cth@198.0.0.143 -p 567`。然后输入密码即可连接到服务器。

输入：`vi /etc/hosts`，可以看到hosts列表。将光标移到下方空白处，键盘切换到英文，同时按下shift和大写的I，进入到编辑模式。将查询到的正确的IP地址写在前面，空格后跟 `api.themoviedb.org` 这个域名。添加完成后，按下「esc」，再键入 `:wq`，保存退出。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124155747.png)

正确的IP可以在「[站长工具](https://sspai.com/link?target=https%3A%2F%2Ftool.chinaz.com%2F)」查询，在「Ping检测」选项卡中，输入`api.themoviedb.org`，下拉可以得到不超时的IP地址，选一个离住址近，响应时间少的，填进去就行。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241124160438.png)

站长工具查询TMDb正确的IP地址

恭喜你！回到媒体库，刷新一下就可以得到全部的影片信息了。

## Jellyfin各平台客户端

苹果和安卓手机直接从应用商店搜索即可获得，这里也给出[其他平台的安装包](https://sspai.com/link?target=https%3A%2F%2Fjellyfin.org%2Fdownloads)。

局域网应用登陆的时候，填写`IP地址:8096`及用户名密码即可登录，如果可以在外网访问，就填`http://域名:8096`。

Jellyfin自家开源的应用无法看杜比视界的影片，可以改为用最新版Kodi播放器+Jellyfin插件进行播放，安装教程在[这里](https://sspai.com/link?target=https%3A%2F%2Fjellyfin.org%2Fdocs%2Fgeneral%2Fclients%2Fkodi%2F)。Kodi的下载地址在[这里](https://sspai.com/link?target=https%3A%2F%2Fkodi.tv%2Fdownload%2F)，可以根据自己需要的平台进行安装。

