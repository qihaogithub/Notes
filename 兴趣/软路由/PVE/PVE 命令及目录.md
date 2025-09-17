
命令
1。备份虚拟机
1. Qm list
查看虚拟机 VMID
2. Vzdump {{VMID}}
备份虚拟机

2。还原虚拟机
1. Ls /var/lib/vz/dump
查看现有虚拟机备份文件
2. Qmrestore {{还原为某VMID}} /var/lib/vz/dump/ {{.vma文件}}
这里可能会报语法错误，调换位置即可，比如改成：qmrestore {{.vma文件}} {{还原为某VMID}}

3. 删除虚拟机
Qm destroy VMID

目录
1. 虚拟机备份. Vma 文件路径
/var/lib/vz/dump

2. PVE 镜像文件路径
/var/lib/vz/template/iso

3. PVE 配置文件路径
/etc/pve/qemu-server
Pve 服务器中各虚拟机的配置，配置网卡所绑定的 bridge
————————————————

原文链接： https://blog.csdn.net/weixin_43775840/article/details/136443960