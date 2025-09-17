[基于AutoDL云端搭建SD的教程](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d)
[Stable Diffusion超简单的国内云部署\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1MX4y1k7yT/?spm_id_from=333.788)
[镜像作者的教程](https://www.bilibili.com/video/BV1ev4y1t7Rd/?spm_id_from=888.80997.embed_other.whitelist&vd_source=81223299ca5d449a34daaab3e1102d1d)
# 注册 AutoDL
[AutoD官网](https://www.autodl.com/home)
# 选择显卡
[00:55](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=55.431072)
推荐显卡:
综合考虑，最推荐 3080，3080 TI，3090，A 5000。
性价比三巨头为三个 80：3080，2080 TI，3080 TI。
性价比第二档为 3090，A 5000。他们速度和显存有优势，而且数量大好抢。
小图没必要用太强的卡。

显存：图幅、插件、模型
算力：出图效率

[02:50](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=170.882582)
租显卡时选择 novel ai 3.1 整合包 
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415115438.png)


[03:22](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=202.781854)
准备百度网盘，建议把模型都放到百度网盘
打开[百度网盘开放平台](https://eyun.baidu.com/union)
点击右上角申请加入
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415110729.png)
 
[03:49](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=229.006598)
创建应用，填写如下信息
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415111447.png)

[04:16](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=256.360293)
创建后获得一下信息
```
AppID：32420279
Appkey：8kGec2CgSxTqPD9Alnja6cecpzAbFb5h
Secretkey：9UGgxXKD5rYliVjooiw79QQF70bFj8GW
Signkey：R=czxKPk%h~-#Mv6WNMqZxiLBCGh!Mip
```

[04:23](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=263.99151)
分别打开 JupyterLab 和 AutoPanel
[04:30](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=270.684249)
在第一段代码处，点击运行
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415115924.png)

[04:47](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=287.350295)
重新加载网页
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415115955.png)

[04:55](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=295.176257)
加载完成后，在右上角，把 Python3 换成 xl-env
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415120122.png)

[05:03](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=303.074568)
然后选择第二段代码，点击运行
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415120158.png)


[05:08](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=308.112173)
运行后，点击安装下载器
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415120230.png)

[05:20](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=320.210577)
安装完成后，点击移动到数据盘
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415120310.png)

[05:25](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=325.619133)
然后点击自动学术加速
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415120400.png)

[05:28](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=328.855935)
点击更新启动器
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415120436.png)
然后刷新网页
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415120514.png)

[05:39](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=339.291955)
此时只剩下一段代码，点击代码运行即可
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415120626.png)

[05:45](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=345.717399)
随便留一个密码
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415120736.png)

[05:49](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=349.856259)
然后下滑网页，除了安全模式以外，其他的建议全部勾选，然后点击运行 webUI
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415120840.png)
出现以下界面表示运行完成
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415121024.png)

[06:09](https://www.bilibili.com/video/BV1Qh411M7Xu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d#t=369.384819)
在容器示例列表中点击自定义服务
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415121104.png)
输入密码登录
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415121135.png)
之后我们就进入 webUI 界面啦
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230415121216.png)


# 其他
安装完成后的根目录文件
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230428161051.png)
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230428161120.png)
