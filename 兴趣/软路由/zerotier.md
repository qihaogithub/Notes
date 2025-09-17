
一. 关于 zerotier  

---------------

zerotier 这个软件就不多说了，主页可以去度娘，如何注册，如何添加**非群晖客户端**，大妈上的教程很多，也是正确的，不多说了。唯一的问题是登陆有时很慢，很慢，蜗牛那种。但是搭建完成以后，网速可以达到你[宽带](https://www.smzdm.com/ju/sz087y3/)的上传极限，如果是电信，远程转码看个 1080 P 的电影是毫无压力的。

[![](https://am.zdmimg.com/202212/07/638ff80568f2f8309.jpg_e1080.jpg)
]( https://post.smzdm.com/p/a60lgv60/pic_2/ )

二. 安装过程
------

感谢矿神，本教程只是对矿神教程的细化，并讲一下自己踩过的坑。矿神的教程在这里，看链接。下面讲一下安装过程。

[![](https://qnam.smzdm.com/202212/07/638ff89fab5a16666.jpg_e1080.jpg)
]( https://post.smzdm.com/p/a60lgv60/pic_3/ )

### 第一步，打开群晖终端机，开启 SSH 功能。

[![](https://qnam.smzdm.com/202212/07/638ff98046fb37779.jpg_e1080.jpg)
]( https://post.smzdm.com/p/a60lgv60/pic_4/ )

第二步，设置套件来源。
-----------

本套件是矿神开发的，所以我不是矿神的套件来源必须添加上，其他的可以不需要。

[![](https://am.zdmimg.com/202212/07/638ff9d34b6d37642.jpg_e1080.jpg)
]( https://post.smzdm.com/p/a60lgv60/pic_5/ )

第三步，安装 Zerotier 套件。

在套件中心直接搜索 Zerotier，安装即可。安装后，记得启动，启动后会发现，无法启动成功，显示已手动停止。此时，停用该套件或重启一下 [NAS](https://www.smzdm.com/ju/sp3qr1k/)，然后进行下一步。

第四步，启动 SSH，授予 Zerotier 权限。

此步可以直接看矿神的教程。如果小白，可以看我的操作。

启动 ssh 客户端，有多种，我就直接用 win 11 自带的了。按 WIN+R 键，输入 cmd, 进入如下界面。

[![](https://am.zdmimg.com/202212/07/638ffc7eae3717505.jpg_e1080.jpg)
]( https://post.smzdm.com/p/a60lgv60/pic_6/ )

输入 ssh 用户名@nas ip。

[![](https://qnam.smzdm.com/202212/07/638ffe962a1d94109.jpg_e1080.jpg)
]( https://post.smzdm.com/p/a60lgv60/pic_7/ )

在 1 处输入你的登陆密码，在 2 处输入 sudo -i

[![](https://qnam.smzdm.com/202212/07/639001518a0be3872.jpg_e1080.jpg)
]( https://post.smzdm.com/p/a60lgv60/pic_8/ )

在 3 处，让你填密码，仍然是登陆密码。然后你发现取得了 root 权限。

在 4 处输入 sed -i 's/package/root/g' /var/packages/zerotier/conf/privilege

按照矿神的说法，这是修复 ssh。  

在 5 处输入 sudo -i（也可直接跳到第 6 处）。

在 6 处输入 cd /var/packages/zerotier/target/bin

然后来到第 7 处，输入 ./zerotier-one -q join XXXX

注意/前有个点，XXXX 是你注册的 zerotier 的 Network ID，一共 16 位。

显示第 8 步“200 join OK”即表示连接成功，进入你的 zerotier，勾选上即可，然后可以自己修改一个容易记的 IP，远程登陆即可。

总结  

-----

1. 优点：就我的使用而言，zerotier 的连接速度还是非常给力的，远程转码看电影，没有压力。从 NAS 上下载文件，可以达到 3 M/S。连接稳定，不需要取得 ROOT 授权，不需要使用 docker，docker 对我来说，是异族文字。

2. 缺点。不友好，再也回不去那种即搜即安装即使用的过去了。  

3. 为方便本小白和其他小白而记录的东西，大神们别取笑。

