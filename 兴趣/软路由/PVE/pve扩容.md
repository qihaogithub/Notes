扩容就是把 local -lvm 中内容移动到 local，然后删除 local -lvm，
## 第一步: 备份并删除虚拟机
选中虚拟机，然后选择备份>立即备份
备份文件出储存在 local，所以删除 local -lvm 并不会丢失备份
备份完成后删除虚拟机，选中虚拟机后，关机后，点击右上角更多找到删除

## 第二步
### 删除local-Ig逻辑卷pve/data
在节点中 shell 中输入以下命令

```
lvremove pve/data
```

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241116204302.png)
### local逻辑卷pve/root扩容

```
lvextend -l +100%FREE -r pve/root
```

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241116204435.png)

### 从管理界面删除local-lvm
在数据中心，存储中移除
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241116204507.png)

### 设置 local
把容器也选中
 ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241116204635.png)
### 恢复虚拟机
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20241116204740.png)


[视频教程](https://www.bilibili.com/video/BV1Pa4y1H7jB/?spm_id_from=333.880.my_history.page.click&vd_source=81223299ca5d449a34daaab3e1102d1d)