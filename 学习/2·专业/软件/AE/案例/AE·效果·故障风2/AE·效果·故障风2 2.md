# AE·效果·故障风2

[故障效果.aep](故障效果_MsoTWyqJt3.aep)

# 1、颜色分离

新建一个合成，1280\*720px，持续时间5秒，黑色画布

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/3d133e88477a8e6840a147c35054a360_OHX8Wdstcq.png)

添加文字图层“故障风效果”

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6ea688207f0063250887954eb72fe3d8_9AaA4MCsvp.png)

将文字图层预合成，复制2次（快捷键：ctrl+d），分别命名为红，绿，蓝

在效果栏搜索色阶（单独控件），添加到红，绿，蓝图层中

点击红色图层，我们将在效果控件里将绿色-绿色输出白色改为0；蓝色-蓝色输出白色改为0

点击绿色图层，我们将在效果控件里将红色-红色输出白色改为0；蓝色-蓝色输出白色改为0

点击蓝色图层，我们将在效果控件里将红色-红色输出白色改为0；绿色-绿色输出白色改为0

我们将绿色图层和蓝色图层模式改为屏幕

在点击红色图层，按P打开位置图层，按alt打开表达式，输入wiggle(15,20)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/3fd8b3cd1a3b9849e5c8a6574c0c7d91_MVFwvBT81x.png)

新建一个调整图层，命名为故障风，右键添加效果-表达式控制-滑块控制，在效果控件旁边我们将效果锁住

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d4bde486c7b57a05982ef0fbb93044ab_jbcMOxVFDF.png)

在选择wiggle（15,20）里面的20，拖动关联器关联滑块

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/5aa8ac9990aab17b5fb172e82a919caf_g2bEdmGidk.png)

给滑块控制打关键帧就可以控制颜色分离效果

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6015df85725544e9b0c360d7c9185ea6_2ZhFlO-5L2.png)

# 2、抖动效果

建立纯色层，添加分形杂色

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/a42d01c2f184c2704c0952efcf12c6a7_AV6vu30T4N.png)

将纯色层预合成，命名为分形杂色，隐藏图层

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/988a7d08f44972a83a6c9eec5217ae68_vFtucZXGIf.png)

新建调整图层，命名为置换图，添加置换图效果，参数如图

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/a2bd4360c5f4e3760e30a76956419539_V4WpqqEU-m.png)
