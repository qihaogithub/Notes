

前言
--

本期教程将讲解一下如何在pve下安装黑[群晖](https://pinpai.smzdm.com/2315/)系统,其他后缀为img格式的比如openwrt镜像也可以通过此方式安装。

镜像下载上传
------

1、下载最新的rr黑群晖引导镜像，解压之后后缀为img格式。

链接：[https://pan.baidu.com/s/11MFVGDO9llVdwejIeYWscg](https://pan.baidu.com/s/11MFVGDO9llVdwejIeYWscg)?pwd=7rdm 提取码：7rdm

[![](https://qnam.smzdm.com/202403/19/65f8f37ccd0fd7261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_2/)

2、登录pve，将rr黑群晖引导镜像上传到pve中。

[![](https://am.zdmimg.com/202403/19/65f8f37c245157261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_3/)

3、镜像上传完成之后，在target file后面会出现引导镜像的保存路径，复制保存此路径信息后续过程中会用到。

> /var/lib/vz/template/iso/rr.img

[![](https://am.zdmimg.com/202403/19/65f8f37c9a36a7261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_4/)

引导部署过程
------

1、登录pve，点击右上角创建虚拟机，名称自定义。

[![](https://am.zdmimg.com/202403/19/65f8f37cd94a67261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_5/)

2、操作系统选择不适用任何介质，其他保持默认。

[![](https://qnam.smzdm.com/202403/19/65f8f37c099077261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_6/)

3、系统页面保持默认即可。

[![](https://qnam.smzdm.com/202403/19/65f8f37cb57107261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_7/)

4、磁盘默认会创建一个32G的硬盘保持默认即可。

[![](https://qnam.smzdm.com/202403/19/65f8f37c587197261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_8/)

5、CPU核心根据机器配置给，类别选择性能最大化的host。

[![](https://qnam.smzdm.com/202403/19/65f8f37c5e93a7261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_9/)

6、内存按照机器配置给，因为是演示机我给 2G足够用了。

[![](https://am.zdmimg.com/202403/19/65f8f37cab0c37261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_10/)

7、网络这里注意一下，选兼容性最好的e1000。

[![](https://qnam.smzdm.com/202403/19/65f8f37c13bb67261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_11/)

8、检查配置没有问题后点击完成。

[![](https://am.zdmimg.com/202403/19/65f8f37c241137261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_12/)

9、虚拟机创建成功，点击虚拟机→硬盘→分离。

[![](https://am.zdmimg.com/202403/19/65f8f37ccc4d77261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_13/)

10、分离成功后移除此硬盘。

[![](https://am.zdmimg.com/202403/19/65f8f37c3e1657261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_14/)

11、接下来在shell中使用命令将黑群晖的引导文件rr导入到创建好的DSM虚拟机（请根据图标实例修改相关命令）。

> qm importdisk 115 /var/lib/vz/template/iso/rr.img local


```
qm importdisk 101 /var/lib/vz/template/iso/DS918_7.21-69057.img  local
```

[![](https://am.zdmimg.com/202403/19/65f8f37c18c047261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_15/)

12、点击节点（pve）→shell，将上面命令辅助粘贴到命令窗口，然后按回车按键执行。

[![](https://qnam.smzdm.com/202403/19/65f8f37c9b4077261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_16/)

13、当出现Successfully关键字的时候表示镜像导入成功。

[![](https://qnam.smzdm.com/202403/19/65f8f37ccc3937261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_17/)

13、再次回到虚拟机中可以看到引导导入成功，双击磁盘，将总线/设备修改为 “**SATA**”

[![](https://am.zdmimg.com/202403/19/65f8f37c9e23e7261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_18/)

14、引导设置成功，可以看到镜像大小为1G。

[![](https://qnam.smzdm.com/202403/19/65f8f37c40d707261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_19/)

15、引导盘设置成功后我们还需要设置系统安装盘也就数据盘，有两种方式，一个是将硬盘直通给黑群晖，另外一个增加虚拟磁盘，本次演示将使用虚拟磁盘方式，如下图我增加了一个100G的SATA硬盘。

[![](https://am.zdmimg.com/202403/19/65f8f37cae1287261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_20/)

16、接下来我们需要设置一下黑群晖的启动项，将rr引导设置为第一、增加的数据盘设置为第二、网卡设置为第三，然后点击Reset。

[![](https://am.zdmimg.com/202403/19/65f8f37c391867261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_21/)

17、完成以上设置后，我们点击启动按钮，完成黑群晖系统的安装。

[![](https://am.zdmimg.com/202403/19/65f8f37cfd5f37261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_22/)

DSM系统安装
-------

1、点击启动后成功进入rr引导配置向导页面。

[![](https://qnam.smzdm.com/202403/19/65f8f37cde91e7261.png_e1080.jpg)
](https://post.smzdm.com/p/al82z7ee/pic_23/)

2、接下来的步骤请查看此篇教程。

文章

![](https://a.zdmimg.com/202311/24/65606b9cdc9ff2682.jpg_a200.jpg)

