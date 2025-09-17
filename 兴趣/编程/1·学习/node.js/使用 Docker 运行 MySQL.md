_1\. 必看必看！！！！！_
---------------

针对近期同学们对 Docker 使用，出现的各种问题，整理如下：

### 1.1. 我无法访问 Docker 官网

请在长乐未央站点下载（有可能更新不及时），地址：[https://clwy.cn/tools/docker](https://clwy.cn/tools/docker)

### 1.2. Windows 11 启动错误

近日有同学反映在 Windows 11 23 H 2 (build 22631) 上安装最新版本 Docker，无法正常启动，提示

```
Windows container are not support by your windows version ... 
```

经查阅 `GItHub` 的 [Issues](https://github.com/docker/for-win/issues/13971#issuecomment-2003849974)，发现使用 `4.27.2` 版本能解决。请大家将之前安装的 `Docker` 卸载后，下载 `4.27.2` 版本重新安装。

下载地址：[https://pan.baidu.com/s/1vsQISm6CQITLPo4kx\_DIdw?pwd=clwy](https://pan.baidu.com/s/1vsQISm6CQITLPo4kx_DIdw?pwd=clwy)

### 1.3. Docker 镜像下载不动

根据新闻报道，近期国内 `Docker` 镜像几乎都出问题了。阿里云近期也发通知给我了，说只能在阿里云服务器上访问其镜像，也就说本地配置阿里云镜像已经不可用了。

最近找到的可用镜像是：`https://docker.rainbond.cc`，请调整配置为：

```
"registry-mirrors":  [  "https://docker.rainbond.cc"  ] 
```

### 1.4. Docker 配置代理

如果发现此镜像也失效了，请删除镜像配置后，在 `Docker` 中配置 `VPN` 代理后使用。

[![](https://assets.clwy.cn/uploads/v1e9amnx8lf8prgbw9ohhcmsn8iu!large)
]( https://assets.clwy.cn/uploads/v1e9amnx8lf8prgbw9ohhcmsn8iu!large )

*   **V 2 rayU**：`http://127.0.0.1:1087`
*   **Clash**：`http://127.0.0.1:7890`
*   其他客户端，请自行处理

修改完成后，再次拉取镜像即可。

### 1.5. 使用 Laragon 集成环境

还有的同学，电脑实在安装不了 `Docker`，或者不会配置 `VPN`。那也可以使用 `Laragon` 集成环境，

下载地址（附安装使用教程）：链接：[https://clwy.cn/tools/laragon](https://clwy.cn/tools/laragon)

[![](https://assets.clwy.cn/uploads/rw4jq0dki0l989yfh5d6e3l19d8h!large)
]( https://assets.clwy.cn/uploads/rw4jq0dki0l989yfh5d6e3l19d8h!large )

当学到第 10 回，会使用 `express` 连接 `MySQL` 数据库。但由于 `Laragon` 的 `MySQL` 默认没有密码，所以等学到后，请调整项目中的数据库配置文件 `config/config.json`，将密码 `password` 设置为：`null`。目前暂时还没有学到，可以先不用管它。

```
"development": {
  "username": "root",
  "password": null,
  "database": "clwy_api_development",
  "host": "127.0.0.1",
  "dialect": "mysql",
  "timezone": "+08:00",
  "logQueryParameters": true
}, 
```

**注意：`null`，不要打引号！！！**

_2\. 课程介绍_
----------

Hello，这里是东哥。这节课，我们要学习的是，「长乐未央全栈系列：Node. Js 项目实践」课程的第 5 回：使用 Docker 运行 MySQL，在这节课里，我们将探讨：

*   MySQL 是什么？
*   用哪种方式安装 MySQL 更好？
*   安装配置 Docker，并通过 Docker 运行 MySQL
*   MySQL 的客户端软件

_3\. MySQL 介绍_
--------------

学习 `Node.js` 开发后端，非常重要的就是需要数据库。数据库就是存储各种数据的，例如你在网上商城上买个件衣服，那你的订单记录就是存在数据库当中的。企业中常见的数据库有很多，例如 MySQL、Postgres、Oracle 和 SQL Server 等等。

当今最流行的，无疑就是 `MySQL` 了，根据[官网](https://www.mysql.com/)介绍，有这么多知名的项目，它们使用的都是 `MySQL`，这里面一定也有大家熟悉的项目。

[![](https://assets.clwy.cn/uploads/ny7aecyetuww7jpg5ida5blqzdas!large)
]( https://assets.clwy.cn/uploads/ny7aecyetuww7jpg5ida5blqzdas!large )

接下来，我们就要来安装 `MySQL` 了。

_4\. 用什么方式安装 MySQL_
-------------------

`MySQL` 的安装方法有很多种，可以在官网下载了直接安装，也有很多集成开发环境里都自带了 MySQL。

当然，最基础方法，就是在官网下载安装程序，[https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)，然后一步步的安装了。但我这里不推荐大家使用这种方法来安装，因为这样安装，会有一大堆相关的选项、配置，服务的设置，让人非常的迷惑。

另外使用一些集成环境，相对来说要比直接安装要简单很多。但是我也不推荐，因为这样做，在 Windows 与 macOS 下，整个安装和使用的流程都非常的不同，而且将来部署到服务器后，也会有一些默认配置不同。例如以下这个：

```
low_case_table_names=0 
```

它是让 `MySQL` 区分数据表名是否大小写的配置。默认在 Windows、macOS 和 Linux 下全都不同。而且当你的数据库初始化之后，也就说成功的启动过一次后，就不能修改了。。。

_5\. 使用 Docker_
---------------

所以我们这里选择使用 `Docker` 来运行 `MySQL`。这样在 Windows 与 macOS 上，甚至在 Linux 服务器上，它们的运行环境都是一致的。

还是请大家进入 `Docker` 官网后，[https://www.docker.com/get-started/](https://www.docker.com/get-started/)，直接下载安装。

安装后，mac 上运行一路顺畅，但有的 Windows 上可能会碰到些问题，尤其是当你使用的是家庭版的 Windows，非常有可能启动时，提示 `Starting the Docker Engine...`，然后一直卡住不动。

如果碰到这种情况，也不用着急。进入 `控制面板`，找到 `启动或关闭 Windows 功能`，确认 `Hyper-v` 与 `适用于 Linux 的 Windows 子系统` 勾选上了。

[![](https://assets.clwy.cn/uploads/g93rxbhomoymdoxz669lbhknx53h!large)
]( https://assets.clwy.cn/uploads/g93rxbhomoymdoxz669lbhknx53h!large )

家庭版的 Windows 非常有可能找不到 `Hyper-v` 选项，那也没关系，可以新建一个文本文档，复制以下内容进去

```
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt
for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
del hyper-v.txt
Dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /LimitAccess /ALL 
```

然后保存为 `Hyper.cmd`，接着在这个文件上，点鼠标右键，选 `以管理员身份运行`。

等跑完后，会提示你按 `Y` 重启电脑。重启完成后，启动 Docker，大概率就可以成功启动了。

如果还是不能启动，还有可能是 `Linux 子系统` 版本太老了。可以打开 `PowerShell`，运行命令更新

```
wsl --update 
```

[![](https://assets.clwy.cn/uploads/tkzk6ibnygojl5dsj1kj3l47mpde!large)
]( https://assets.clwy.cn/uploads/tkzk6ibnygojl5dsj1kj3l47mpde!large )

完成后，还是要重启一下电脑，再次启动 `Docker`，应该就没啥问题了。

_6\. 配置中国镜像_
------------

`Docker` 运行起来后，也需要配置一下中国镜像，这样它下载速度会快很多。我们找到设置里面的 `Docker Engine`，增加上

```
"registry-mirrors":  [  "https://docker.rainbond.cc"  ] 
```

[![](https://assets.clwy.cn/uploads/dmzzto9ffme4t830nmtnp5xmjx67!large)
]( https://assets.clwy.cn/uploads/dmzzto9ffme4t830nmtnp5xmjx67!large )

改的时候注意一下，上一行的最后面，要加上一个 `,` 号，不然格式就错了。接着保存，它会自动重新启动。然后就把它在丢一边，不用管它，只要别退出它就好了。

_7\. 使用 docker compose_
-----------------------

接着进入项目根目录中，新建一个文件，叫做 `docker-compose.yml`。千万要注意，一定要在项目根目录中，放在其他地方会找不到的。然后将下面的配置复制进去，这就是 `MySQL` 的一个简单配置了。

```
services:
  mysql:
    image: mysql:8.3.0
    command:
      --default-authentication-plugin=mysql_native_password
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_general_ci
    environment:
      - MYSQL_ROOT_PASSWORD=clwy1234
      - MYSQL_LOWER_CASE_TABLE_NAMES=0
    ports:
      - "3306:3306"
    volumes:
      - ./data/mysql:/var/lib/mysql 
```

然后我们开启另一个命令行窗口，一定要确保命令行所在路径，是在当前项目里的。如果不在当前项目里，就自己先通过 `cd` 命令进入项目，然后再运行

```
docker-compose up -d 
```

这样，`MySQL` 就会自动下载好，并启动起来了。

[![](https://assets.clwy.cn/uploads/zj2n9gcl5vtxhbkwzrcnwuukfp4d!large)
]( https://assets.clwy.cn/uploads/zj2n9gcl5vtxhbkwzrcnwuukfp4d!large )

再看看 `docker 面板` 里，也会出现我们的项目了。将来大家想停止，或者再次启动 `MySQL`，也可以使用这里的按钮。

[![](https://assets.clwy.cn/uploads/ayj79mhqe6gt419apestxssof8u2!large)
]( https://assets.clwy.cn/uploads/ayj79mhqe6gt419apestxssof8u2!large )

关于配置里的内容，还有 `Docker` 本身，还有很多复杂的东西内容。这不是一下能说明白的，我们先不用管那么多，先只需要知道怎么启动 `MySQL` 就好了。如果有兴趣，现在就想进一步的了解 `Docker`，也可以先看看我很早之前写的一个教程：[https://clwy.cn/documents/docker/](https://clwy.cn/documents/docker/)

_8\. MySQL 客户端_
---------------

刚才安装好并运行的，还只是 `MySQL` 服务端。我们要想方便的管理操作数据库，那还需要对应的客户端。

Windows 与 macOS 使用的客户端又有所不同。我们先来看苹果电脑的，大家直接打开应用商店，搜索 `Sequel Ace` 后，直接安装。这是一个免费 App，非常的棒！

[![](https://assets.clwy.cn/uploads/zxr0lrhhlk0z7s3uu8tu8rzg4huh!large)
]( https://assets.clwy.cn/uploads/zxr0lrhhlk0z7s3uu8tu8rzg4huh!large )

打开安装完成的软件，新建一个数据库连接，

```
Name: 本机
Host: 127.0.0.1
Username: root
Password: clwy1234 
```

接着，点击 `Test connection`，确认能成功连接。然后点击 `Add to Favorites`，也就是加入 `喜欢`。

[![](https://assets.clwy.cn/uploads/9wzdvqoloy0mhdv8apan8ak2yjyl!large)
]( https://assets.clwy.cn/uploads/9wzdvqoloy0mhdv8apan8ak2yjyl!large )

这样左侧就会出现 `本机` 这个选择，我们直接双击进去，就能连上数据库了

[![](https://assets.clwy.cn/uploads/wvw4zna6dywe7gpbctfu83wy3tre!large)
]( https://assets.clwy.cn/uploads/wvw4zna6dywe7gpbctfu83wy3tre!large )

现在连好后，先丢到一边，当我们学到数据库的时候，再详细说明它该如何使用。

_9\. Windows 上的 Navicat_
------------------------

Windows 的同学们，我实在没有特别好的客户端推荐给大家。就我个人认为，Windows 上最好用的是 `Navicat`，它有收费的完整版，也有免费的精简版本，大家可以在官网下载免费版本，[https://www.navicat.com.cn/products/navicat-premium-lite](https://www.navicat.com.cn/products/navicat-premium-lite)。

因为我平常开发用的都是 mac，手头上没有合适的设备来和大家演示怎么使用 `Navicat`。所以我只好在讲义里放一些图片，大家就按照图片来一步步操作了。整体的使用流程和苹果上的类似，都是大同小异的。

[![](https://assets.clwy.cn/uploads/jltf0r4fuydrqsx0qzbqm4rx22qt!large)
]( https://assets.clwy.cn/uploads/jltf0r4fuydrqsx0qzbqm4rx22qt!large )

[![](https://assets.clwy.cn/uploads/5z7boofn49q43qak3kqz1g4fbfhr!large)
]( https://assets.clwy.cn/uploads/5z7boofn49q43qak3kqz1g4fbfhr!large )

[![](https://assets.clwy.cn/uploads/s71hpddkmftk5w7cww1jpddrqtuu!large)
]( https://assets.clwy.cn/uploads/s71hpddkmftk5w7cww1jpddrqtuu!large )

[![](https://assets.clwy.cn/uploads/fqis3k2pkna3bql4rk79kekmkfxl!large)
]( https://assets.clwy.cn/uploads/fqis3k2pkna3bql4rk79kekmkfxl!large )

如果碰到问题实在搞不定，也欢迎在课程辅导群里@我，我来一对一远程辅导你搞定它。

_10\. 总结一下_
-----------

*   `MySQL` 安装方法有很多，推荐使用 `Docker` 来运行，这样本地的开发环境与服务器环境一致。
*   有了服务端，还要有用来管理 `MySQL` 的客户端。推荐 `Sequel Ace` 和 `Navicat`。