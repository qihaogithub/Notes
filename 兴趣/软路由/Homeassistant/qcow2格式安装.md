HOME ASSISTANT OS 适应大陆地区网络环境 [固件下](https://sumju.net/?p=8022)载（HASSOS 12.1 稳定版本）

[视频教程](https://www.bilibili.com/video/BV1DY411J7SU/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d)

好镜像，文件名为：haos_ova-12.1.qcow2.xz
需要先解压，解压后文件名：haos_ova-12.1.qcow2
接下来打开终端，输入
cd Downloads 进入电脑Downloads 目录
| grep haos  查找文件
scp haos_ova-12.1.qcow2 root@192.168.31.250 :/root  将haos_ova-12.1.qcow2 文件传到pve

![202403312208517.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403312208517.png)

在pve 控制台输入命令ls -1h，查看刚才上传的文件
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403312213555.png)
然后新建虚拟机
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403312216324.png)
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403312216011.png)
删除磁盘
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403312217957.png)
其他都默认


终端输入命令，将镜像导入给虚拟机
qm importdisk 103 haos_ova-12.1.qcow2 local-lvm

qm importdisk 109 haos_ova-7.5.qcow2 local-lvm

103 是虚拟机编号，haos_ova-12.1.qcow2 是上传的镜像名称
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403312221501.png)

回到 103 虚拟机，把刚导入的硬盘添加上
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403312225615.png)
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403312226478.png)
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202403312226437.png)
添加 USB 设备（zigbee 2 mqtt 网关）
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202404010741330.png)


接下来点击启动虚拟机
