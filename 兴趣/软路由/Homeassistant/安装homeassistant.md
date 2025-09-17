# 安装教程收集

【PVE安装HomeAssistant-哔哩哔哩】 [https://b23.tv/mbZ1NiB](https://b23.tv/mbZ1NiB)
【PVE 安装 HomeAssistant-哔哩哔哩】 [https://b23.tv/OxlWSOU](https://b23.tv/OxlWSOU)

# 01 一键安装

一键安装教程： https://bbs.hassbian.com/thread-14941-1-1.html
通过虚拟机备份的方式安装

# 02 手动安装

[[qcow2格式安装]]
下载镜像地址：[https://www.home-assistant.io/installation/linux](https://www.home-assistant.io/installation/linux)

下载kvm虚拟机镜像，下载完成后解压

上传镜像

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image%202.png)

复制并保存路径
/var/lib/vz/template/iso/haos_generic-x86-64-11.5.img

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image%203.png)

新建虚拟机，名称随意，开机自启动打钩

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image%204.png)

不适用任何介质

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image%205.png)

系统设置默认

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image%206.png)

删除磁盘
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20240327155448.png)


CPU随意
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20240327155505.png)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20240327155520.png)


网络默认

在_ Shell中输入代码

```
qm importdisk 编号 文件位置 local（或local-lvm）
#如果没有做分区合并，就是local-lvm
```


我的代码是：

qm importdisk 102 /var/lib/vz/template/iso/haos_generic-x86-64-11.5.img local-lvm
qm importdisk 104 /var/lib/vz/template/iso/haos_generic-x86-64-12.1.img local-lvm
出现如下图则完成

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image%2010.png)

在硬件设置中，会出现一个未使用磁盘，双击把类型改为IDE

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image%2011.png)

将BIOS改为ovmf，无视出现的提示

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image%2012.png)

修改引导顺序

![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image%2013.png)
添加USB 设备（zigbee 2mqtt 网关）
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202404010741330.png)


最后点击启动虚拟机，就会自动安装

安装完后去路由器后台找ip地址，打开后可以看到安装过程
