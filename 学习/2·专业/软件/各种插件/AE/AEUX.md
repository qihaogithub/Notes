# AEUX

figma插件安装：[https://www.bilibili.com/video/av711505011/?p=2\&spm\_id\_from=pageDriver](https://www.bilibili.com/video/av711505011/?p=2\&spm_id_from=pageDriver "https://www.bilibili.com/video/av711505011/?p=2\&spm_id_from=pageDriver")

官网：[https://aeux.io/guide/download.html](https://aeux.io/guide/download.html "https://aeux.io/guide/download.html")

下载链接（非最新）：[AEUX_0.8.2.zip - 123云盘](https://www.123pan.com/s/rjnUVv-KW8kd)



发现了一款非常好用的插件，它的前身是Sketch2AE，花了一点时间研究了它的使用方法，好东西当然要大家一起分享！

目前没找到汉化版，不过功能也不是特别复杂，分享出来是希望能提高大家平时在设计中的效率，如果有说的不对的地方还请帮我指正一下，谢谢\~\~

先简单看一下基本功能

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01220d5bdc622ca80121ab5db47be2_wL1gvLgRCl.gif)

**1、基本功能**

**一、一键复制所有图层到AE**

1.装好插件后，打开sketch，选择 插件>AEUX，打开插件面板，再启动AE，在 窗口>扩展里面找到AEUX，打开。

2.选中要导入到AE的画板，点击“Selection to Ae”，如果界面中含有位图，会弹出一个窗口，选择或者新建一个文件夹，以保存位图。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/011a475bdc5c76a8012092522cdfcb_tf9rqlfhkB.png)

3.切换到AE，会发现AE中的插件面板上已经出现了在sketch里面的画板并显示图层数量，导入时分两种情况：

（1）如果此时没有创建合成，选择Add layers to comp“NEW”，会自动生成一个与画板大小相同的合成，并导入图层。

（2）如果已经创建了合成，选择Add layers to comp“CURRENT”，会直接导入图层到当前合成里。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01098f5bdc5d3fa80121ab5dd842a1_PtXD-H-rd8.png)

下方options中的功能会在下面与其他功能一起讲到。

**二、生成Json文件导入AE**

点击sketch插件中的Export AEUX.json按钮，导出Json文件。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01daf55bdc5c25a80121ab5def1319_c4_j4VQlrq.png)

2.在AE插件面板中点击顶部导航栏的第二个按钮，选择Json文件导入。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/015d405bdc5d9ea80121ab5d85be3f_g8ABDR7Tod.png)

**2、进阶功能**

在使用AE做动效之前，要养成良好的图层整理和命名习惯，提前构思好整个动效的过程，可以更好的提高我们的设计效率,减少设计过程中可能出现的问题。

因此，我个人认为这个良好习惯还是有必要养成的，插件功能只能给你的操作带来方便，想法和逻辑还是要靠自己。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/017b375bdc62aca80121ab5d767ee2_qTakENSFlg.png)

**一、Sketch插件中的进阶功能**

1.Detach symbols 分离组件功能

我们在做产品的时候有时候会为产品建立一个sketch中的library，里面包含许多的组件，在导入到AE中的时候可能会出现变形，位移等现象。这时候可以用到这个功能，选择画板，点击按钮，可以自动分离组件。不过在我的实验过程中发现这个功能在分离组件的时候也会出现一些类似变形的bug，所以我建议可以手动分离组件，将图层打组。

2.Flatten shapes 扁平化形状（蹩脚英文）

AE中不支持复杂的布尔运算，当sketch画板中有复杂的布尔运算图形，并没有将图形合并时，选中画板，点击按钮，可以自动合并复杂的布尔运算图形。

3.Images to symbols 将图片转换成组件

在sketch画板中，超出画板的图层会自动隐藏，还有蒙版功能，都可能导致导入AE之后出现位移，蒙版错位等情况。选中图片，点击按钮，可以将图片转换成sketch中的组件。

**二、AE插件中的进阶功能**

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01dd935bdc6d77a80121ab5dfc6ee2_BtsbRuInVZ.png)

1.com size multiplier 导入倍数设置

这个不需要多讲了吧，如果用sketch375宽度做图，选择2x导入可以直接得到一个750宽度的合成。

2.Precomp groups 将所有组建立成预合成

勾选此功能之后，在sketch中打组的图层将会自动生成为一个个预合成。如果不勾选此功能，组内的图层都会生成在AE中的同一个合成中，并且每一个图层组中的内容都会连接到一个隐藏的父级图层上，相当于在AE里变相的给图层分了组。

随便画了个东西做一个演示，如下图

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/019d495bdc71eaa801209252326bb6_SA5d2ozkMO.png)

3.Auto build artboards 自动建立新合成

勾选此功能之后，Build artboard 按钮就会消失，之后在sketch中复制完图层后都会自动导入AE。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/010ba95bdc72f3a80121ab5d814ada_EAb-kNgQHd.png)

4.TOGGLE VISIBILITY 隐藏/显示 所有父级图层

前面有提到，如果不勾选自动建立预合成功能，每一个图层组中的内容都会连接到一个隐藏的父级图层上，此功能可以一键隐藏/显示 所有父级图层。下图中带蓝色标记的“名片”图层，为父级图层。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/014f655bdc74e8a80121ab5dc46d51_9tE09qPNRt.png)

5.CONCERT TO PRECOMP 将同一个组内的图层新建一个预合成

选择父级图层后，点击按钮，会自动将所有连接到该父级图层上的子级图层新建一个预合成。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01744c5bdd191ca80121ab5d494872_ZPHBICVDFZ.gif)

6.UN-PRECOMP GROUP 将预合成拆分成图层

选择预合成，点击按钮，会将预合成拆分成图层，与上个功能相反。

7.DELETE GROUP LAYERS 删除所有父级图层

**3、安装插件**

**一、Sketch插件安装**

解压压缩包后，得到一个文件夹和一个dmg文件，先打开文件夹，双击sketch插件文件，直接安装。

**二、AE插件安装**

两种方法，第一种方法失败的话尝试第二种方法

1.安装压缩包内的dmg文件

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/015c485bdd1794a80121ab5dda2037_qLgcTXA4F7.png)

2.打开刚刚安装好的软件，单击界面选择文件夹内的后缀为“zxp”的文件，或者将文件拖拽至软件内，开始安装。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01ee525bdd190da80120925203c4b5_9vVexe3kLK.gif)

3.如果这个安装方法失败了（我就是。。。），尝试另一个安装方法。

将文件夹内的后缀为“zxp”的文件重命名，将后缀改为“zip”，然后解压压缩包，将得到的“AEUX”文件夹复制到以下路径：

“你的硬盘名称”>资源库>Application Support >Adobe>CEP>extensions

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/0166a85bdd1acaa801209252bee615_CyAwoDNgz1.gif)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01f9a25bdd1acca80121ab5db0912d_vCXiA_naaS.gif)

压缩包上传文件大小限制，dmg文件需要大家自行下载，工具名字为zxpinstaller（懒得下载的话可以直接使用第二种安装方法）插件就直接上传到附件里了。

最后说个小问题，最近在一些交流群内发现很多同学遇到了更新 Mac Mojave系统之后系统不显示图片略缩图的问题，调整文件夹选项也没用。如果你也遇到这个问题，可以尝试一下这个方法：

卸载你的Sketch

重启电脑，你会发现问题已经解决了，就是这么玄学。

再安装一个最新版本的Sketch咯\~

如果觉得对你有帮助的话，可以帮我点个赞\~

*263*

&#x20; \- 2位站酷推荐设计师推荐 -
&#x20;&#x20;

声明：站酷（ZCOOL）内网友所发表的所有内容及言论仅代表其本人，并不反映任何站酷（ZCOOL）之意见及观点。

[0.4M](https://www.zcool.com.cn/down?id=ZODA4NTMy\&type=8 "0.4M")
