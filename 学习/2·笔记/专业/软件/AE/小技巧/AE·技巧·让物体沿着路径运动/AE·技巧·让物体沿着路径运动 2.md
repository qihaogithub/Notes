# AE·技巧·让物体沿着路径运动

在AE里如何让物体沿着路径运动？
听语音
===

*   原创

*   |

*   浏览：28873

*   |

*   更新：2019-06-22 15:21

*   |

*   标签：[AE](https://jingyan.baidu.com/tag?tagName=AE "AE")

*   1

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6ca9846186254193b71dc2b7df1bd10ff326ab48_HJYTzQ2R_.jpg)

*   2

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d04eec260d9a310e976c9b9931b842406bfea248_xBqfD3BIE.jpg)

*   3

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/bbf95c406afec3147730e75dcac1b727ad539c48_Y7wy0-Djv.jpg)

*   4

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/07c98f2ca5cadce81fbd724ffcf7980e5e209548_UY14bu-Wf.jpg)

*   5

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/994f412043715fdba0d5cb89468920c5270f8c48_g8Lh0EqVK.jpg)

*   6

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/dccb47de450788019885a7f2b18ca608a40f8248_FyY6v76ip.jpg)

*   7

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/a749bb0f94fc508c3c3bb54b01775ddd894cfd48_6So5Zqi5q.jpg)

[分步阅读](http://jingyan.baidu.com/album/e4511cf38aba0b2b845eaf28.html "分步阅读")

如何让物体精确的沿着路径轨迹运动，

手动K帧也能创造出曲线运动，但控制比较麻烦，而且不精确，

用钢笔绘制运动路径可以精确的让物体沿着路径运动，控制简单。

工具/原料

*   AE

*   蒙版

一、创建物体

1.  1

    新建一个AE合成，选择HDTV 720 25的预设，确定。

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6ca9846186254193b71dc2b7df1bd10ff326ab48_OsfNpbK8i.jpg)

2.  2

    选择工具栏中的形状工具，选择五角星。

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d04eec260d9a310e976c9b9931b842406bfea248_DfUsrrZ60.jpg)

3.  3

    创建一个五角星形状，调整一下大小、颜色。

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/bbf95c406afec3147730e75dcac1b727ad539c48_HNlM2W8Ze.jpg)

4.  4

    选中创建的形状，按**快捷键Ctrl+Alt+Home，**
    将形状的轴心点恢复到中心点位置，
    **注意：这一步很重要，如果不轴心点不归位到中心，****后面粘贴蒙版路径的时候，就会出现路径错位。**

    END

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/07c98f2ca5cadce81fbd724ffcf7980e5e209548_xPS9C7A_Q.jpg)

二、绘制路径

1.  1

    选择——菜单——图层——新建——纯色层。
    弹出对话框——保持默认，确定。

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/994f412043715fdba0d5cb89468920c5270f8c48_0EgEzs2TH.jpg)

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/dccb47de450788019885a7f2b18ca608a40f8248_XUZt6q_9Y.jpg)

2.  2

    选择钢笔工具。

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/a749bb0f94fc508c3c3bb54b01775ddd894cfd48_0lD0VSAp7.jpg)

3.  3

    选中纯色层。

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/5c9c964ce54a2f27491a5ab5e00192dd3240f448_0TgNARs69.jpg)

4.  4

    在视图窗口用钢笔工具任意绘制一个路径，
    这样纯色层上就有了蒙版路径。
    注意：有时钢笔工具变成了黑色箭头是因为你是点选的，
    只要拖动绘制就不会出现了。比如在点击完一个点后，在点击第二个点时，
    点下后立马向某个方向拖动鼠标就不会出现黑色箭头了。

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/3201a8f39187031c2f35dd4f6a86242fa972ec48_HSJb3fpni.jpg)

5.  5

    选择路径上的每个控制点，会出现控制滑竿，
    用选择工具通过调整滑竿来调整路径的弯曲度，使路径更平滑。

    END

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/e0c73a2fa872941f021146697b5e4a237871e648_GmmGg07XT.jpg)

三、生成路径动画

1.  1

    路径画好后，在图层面板关闭纯色层的显示。
    这是为了不遮挡住运动物体。

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/4b626771fe1d96d8dbec13932ccd0c6efaf2e148_e1BDm2Lqx.jpg)

2.  2

    选中纯色层，展开下面的**蒙版**选项，选中蒙版路径。
    按Ctrl+C进行复制。

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/fab31cb375d7997b7001a8ebf9dade49600fd948_Z6Rx_c1z7.jpg)

3.  3

    再选中形状图层，展开下面的**变换**选项，选中**位置，**
    将时间线移动到起始位置，按Ctrl+V进行粘贴。

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/739bc049610f8b567cf15cdb9ce951e10ff8d348_lUTmH-8JC.jpg)

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/2f2909e951e10ef88ea3a78e2324d8e9cdd2cc48_ZlW1S30LZ.jpg)

4.  4

    可以看到：物体自动添加了关键帧和运动路径。
    并且自动跑到了蒙版路径的起始位置。
    按空格键播放，发现物体沿着绘制的路径运动了。

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/a965c6e9ccd2bb668dacf7f39b2a04e23fa2c648_mzNY3bwcj.jpg)

5.  5

    为了使物体运动的方向也始终和路径一致，
    **选中物体，再选择选择——菜单栏——图层——变换——自动方向，****弹出对话框，选择——沿路径定向——确定。**
    这样物体不仅沿着路径运动，而且会自动转变方向，与路径方向保持一致。

    END

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/84010e2a04e23ea2dbb7d2c92b10bc33ed38c348_3uMsW30nH.jpg)

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/a151a233ec3834bbfe1ad0ec8714c27bd3823d49_KK8US9Y25.jpg)

步骤回顾：

1.  1

    1、创建物体，可以使形状，也可是导入的PNG素材。
    2、绘制蒙版路径，
    3、生成物体的路径动画。
    END

注意事项

*   注意将物体的轴心点归位到中心。

*   钢笔出现黑色箭头时，注意拖动绘制曲线。

*   为物体开启沿路径定向。

经验内容仅供参考，如果您需解决具体问题(尤其法律、医学等领域)，建议您详细咨询相关领域专业人士。

作者声明：本篇经验系本人依照真实经历原创，未经许可，谢绝转载。
