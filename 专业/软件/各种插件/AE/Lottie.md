# Lottie

[https://github.com/bigxixi/bodymovin\_cn](https://github.com/bigxixi/bodymovin_cn "https://github.com/bigxixi/bodymovin_cn")

汉化插件下载&#x20;

[https://lottiefiles.com/preview](https://lottiefiles.com/preview "https://lottiefiles.com/preview")

json文件预览

<https://www.uisdc.com/lottie-dynamic-design-guide>

# 基础篇

动效设计，是 UI 设计当中不可或缺的一环。大家对动效的认知也从最初认为动效只是为了美观酷炫，到逐渐理解了动效对于提升用户体验和产品需求的重要作用。而导致这种认知的转变，相当一部分原因是因为硬件性能的发展和动效输出方式的优化。

因为动效实现的过程就是设计师和开发之间互相博弈的过程。设计师可能通过 AE 或者其他工具做出炫酷的效果，和开发对接就懵了。要么无法实现，要么极其复杂。毕竟开发工程师要通过代码把动效实现出来，设计师得用开发所能理解的语言来描述。就如同你能完美地解出一道数学题一样，让你把解题思路教给别人，你可能就没那么顺畅了。一方面取决于你的表述能力，而更重要的是对方的理解能力。过去所广泛采用的通过动效标注输出给开发的方式，都存在还原度的问题。很多时候还原度达到 80% 可能都算比较好的了。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/fe2fb389963753fdd445b7855ea38a4b_bkRvUBVGEL.jpeg)

而今天要说到的 Lottie 不仅可以 100% 还原动效，而且无需动效标注。直接通过 AE 输出动效文件给开发。开发人员直接调用，然后完美还原。

## Lottie是什么？

Lottie 是 Airbnb 开源的一个动画渲染库，同时支持 Android、iOS、React Native 平台。Lottie 支持渲染播放 AE 动画。通过 AE 插件 bodymovie 导出 json 文件作为动画数据，其工作流程如下：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/87691f0567fdca42762fe796d41d6a5f_0U3-qF33EY.jpeg)

是不是听起来很心动？其实 Lottie 已经火了一两年了，很多人应该也看了一些介绍。希望工作项目中经常涉及到动效设计，但是还在用老方法的同学。可以尝试使用 Lottie 帮助动效落地，提升团队工作效率和个人影响力。

## Lottie有什么用？

Lottie 可以应用在 UI 设计的很多场景中。以下举出几个常用例子。

1、动态启动页

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/29a932d8901dfc9eaf6a870c1ccd41d3_-tDte35TCO.gif)

2\. 动态图标/按钮

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/e2d8dc92a15f8517d831f96a54467ec2_jJX-fQGsEL.gif)

3\. 空页面

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/9099fbb00306fc6c5d2cef1f1a7d1684_nu6TTFH835.gif)

4\. 加载/下拉刷新

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/08bc0a21b6ac5c5affab7a27e80de794_jqQqPF7oak.gif)

5\. Banner/弹框

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/a255aa4f7df9431147534858d07ba223_-7beTutsvW.gif)

6\. 表情/礼物/动态贴纸

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/b31d4692a7f100e8e5cb745e70a43535_xj8MDjYMSk.gif)

以上仅列举了部分常用案例，其实 Lottie 的应用场景远不止这些。在 APP 的多个模块中都可以运用，那么我们要如何将 Lottie 运用在自己的工作项目中呢？那就要了解 Lottie 的原理了。

## Lottie的原理是什么？

前面已经提过 Lottie 是 Airbnb 开源的一个动画渲染库。我们可以理解为它是一个多功能的视频播放器，开发人员需要将这个播放器部署到相应的环境中。然后设计人员提供视频（动效文件）给开发人员，让开发人员按照要求播放视频文件，即可完成动效的应用。

Lottie 动画的播放控制，除了常规的控制，还支持进度播放、帧播放。以一个动态按钮的切换为例，方便大家理解。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/355b765314db6cf02d1a2ec1088b15cf_OBXnJtLa-b.gif)

△ 用 Swift 制作一个漂亮的汉堡按钮过渡动画

上图所示为一个菜单/关闭按钮的动态切换。

假设该按钮动效一共10帧，整个按钮切换分为两部分，第一部分：从菜单切换到关闭（1-10帧）；第二部分：从关闭切换到菜单（10-1）。我们可以让开发通过以下控制方式，完成我们想要的效果。

按钮动效默认显示第1帧（菜单状态），点击按钮以后开始播放动效，动效播放到第10帧的时候停止，并停在第10帧（关闭状态）。

当按钮为关闭状态（第10帧）时，点击按钮以后动效从第10帧倒放到第1帧（关闭状态），并停在第1帧（菜单状态）。

通过以上方式就完成了对一个动效按钮的控制。而日常工作中我们可以灵活地运用多种控制方式。

首先动效的触发，可以是一次交互事件，比如点击、滑动；也可以是监听到了广播，比如网络异常等。

而触发以后的动效控制也多种多样，可以从开始播放到结束，也可以进行倒放；可以循环播放某一段动效；也可以从某一帧播放到另一帧，或者某一个时间点播放到另一个时间点；更多的控制方式需要大家在工作中慢慢挖掘。

## Lottie支持的AE属性

Lottie虽然能够满足多种场景需要，但是并非支持所有的 AE 效果。设计制作时，需要考虑该效果是否支持。否则，会导致出错或者所用效果无法生效。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/143ae6aac2f5e9d8d63d75f888032d85_VENnm7Jk7H.jpeg)

上图为 Lottie 支持的主要 AE 属性，此处有删减掉部分不常用的属性。可以打开以下链接查看完整版http\://airbnb.io/lottie/#/supported-features

需要注意的是文档中虽然说支持渐变，但是会出错，所以大家在使用矢量图形时，请勿使用渐变效果。关于渐变效果的修复后续文章会提到，官网以后也会修复相关问题，但是没有确切时间。

通过上图我们可以了解到，Lottie 支持的 AE 属性基本包含以下几类：

*   基础的形状比如圆形、矩形、星形等，也可以支持钢笔工具绘制的矢量形状和从 AI 中导入的矢量图形。

*   支持位移、大小缩放、透明度、旋转、修剪路径、蒙版、遮罩这些基础动画属性。

*   支持图层间建立父子级关系（只支持图层与图层之间建立，当图层的属性之间建立父子关系会失效，比如 A 图层可以和 B 图层建立父子关系，但是 A 图层的位移属性和 B 图层的位移属性单独建立父子关系则不生效）。

*   支持速度贝塞尔插值，可以搭配 Flow 插件生成各种缓动效果。

*   支持导入图片。

*   支持时间拉伸和时间重映射来通知时间和速度。

## AE插件安装与使用

前面已经提到 Lottie 是通过 AE 插件 bodymovie 导出 json 文件作为动画数据。接下来就为大家讲解插件的安装与使用方法。

1\. 下载bodymovie插件

官方英文插件地址：[https://aescripts.com/bodymovin/（文末提供中文汉化版下载地址和详细安装教程）](https://aescripts.com/bodymovin/%EF%BC%88%E6%96%87%E6%9C%AB%E6%8F%90%E4%BE%9B%E4%B8%AD%E6%96%87%E6%B1%89%E5%8C%96%E7%89%88%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80%E5%92%8C%E8%AF%A6%E7%BB%86%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B%EF%BC%89 "https://aescripts.com/bodymovin/（文末提供中文汉化版下载地址和详细安装教程）")

2\. 自动安装方法

下载zxp格式安装器，下载地址：[https://aescripts.com/learn/zxp-installer/，安装成功后，双击步骤](https://aescripts.com/learn/zxp-installer/%EF%BC%8C%E5%AE%89%E8%A3%85%E6%88%90%E5%8A%9F%E5%90%8E%EF%BC%8C%E5%8F%8C%E5%87%BB%E6%AD%A5%E9%AA%A4 "https://aescripts.com/learn/zxp-installer/，安装成功后，双击步骤") 1 中下载的插件即可完成安装。&#x20;

3\. 手动安装方法

如果自动安装失败，可尝试手动安装。首先修改 ZXP 文件后缀名为 ZIP，然后解压缩文件，得到文件夹，将文件夹复制到以下目录。

WINDOWS：

C:\Program Files (x86)\Common Files\Adobe\CEP\extensions or

C:\AppData\Roaming\Adobe\CEP\extensions

MAC：

/Library/Application\ Support/Adobe/CEP/extensions/bodymovin

您可以打开终端并键入：

*   \$ cp -R YOURUNZIPEDFOLDERPATH/extension /Library/Application\ Support/Adobe/CEP/extensions/bodymovin

然后键入：

*   \$ ls /Library/Application\ Support/Adobe/CEP/extensions/bodymovin

以确保它被正确复制类型。

4\. 安装后

**Windows：** 转到编辑>首选项>常规>并选中「允许脚本写入文件和访问网络」。

**Mac：** 转到Adobe After Effects>首选项>常规>并选中「允许脚本写入文件和访问网络」。

安装完成后即可在窗口>扩展>bodymovin（Window> Extensions> bodymovin）中找到 bodymovin 插件。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/95e50837c6ed9a7503179a644d6a6c5c_uvA0uEXA5M.jpeg)

插件主界面如图所示。在主界面可以选择需要导出的合成、导出设置、导出文件夹，并且可以预览动效。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/9771ec4053cef4698cfbc9c25e46cf53_Xm8aGP8RbV.jpeg)

每次导出时都需要进行设置。标红区域为必选选项。字体图形化可以将字体转化为路径，不勾选会因为应用的平台没有相应字体导致文字加载出错；勾选演示模式后会生成 html 文件，打开该文件即可预览动效。

当含有图片资源时可以根据需要选择勾选对应的选项。

保存好设置后，点击渲染即可生成动效文件给开发。当只有矢量图层时，开发只需要使用 json 文件即可。当含有图片文件时需要将 json 文件和图片文件夹一并给到开发人员使用。需要注意的是不能随意修改文件夹名称和内部文件名。如果需要修改图片名称，应该同步修改 json 内部代码。相关修改方法，后续文章将会详解。

动效预览

为了测试 json 文件是否能在对应平台显示正常，Lottie 提供了预览平台。将导出的 json 文件上传到网站即可预览效果，也可以下载相应 APP 扫码或者导入 json 文件预览。

官方社区，可以预览动效和查看其他设计师公开的动效案例（自己上传的预览动效不会被公开）：[https://lottiefiles.com/](https://lottiefiles.com/ "https://lottiefiles.com/")

iOS 在 app store 搜索 Lottie 即可下载预览软件，安卓需要在 google play 下载安装。考虑到部分朋友无法使用 google play， 文末提供下载。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/dbf1242b9f720c6ac84ed11ffeaaffdc_GpN3mjVNgC.gif)

## 推动落地

相信大家看完都有跃跃欲试的想法。但是要实际应用在工作项目中就需要各位设计师去推动了。其中可能会面临一些阻力，比如开发人员的能力水平以及个人的沟通方式等等问题。但是对于正确的事，只要我们坚持去做就会有结果的。首先对于 gif 动画而言，Lottie 更加轻量，且性能更好，并且不易失真；对于开发人员自己写动效来说，一方面 Lottie 减少了大量动效标注的时间，并且可以 100% 还原动效，对于开发人员来说无需再手动写动效了。一次部署，终身轻松。相信相关人员了解以后都会去支持的。

为了方便开发人员使用，下面列出几个使用网站，如果开发人员不知道如何部署和控制动效，直接把链接扔给他们就行了。

*   Lottie官方介绍和开发文档：[http://airbnb.io/lottie/#/README](http://airbnb.io/lottie/#/README "http://airbnb.io/lottie/#/README")

*   York\_魚的lottie介绍和动效控制方法详解：[https://www.jianshu.com/p/01f6bb509d54](https://www.jianshu.com/p/01f6bb509d54 "https://www.jianshu.com/p/01f6bb509d54")

## 下载链接

文件下载链接：[https://share.weiyun.com/5DpXrKm](https://share.weiyun.com/5DpXrKm "https://share.weiyun.com/5DpXrKm") 密码：iuaruk&#x20;

备用下载链接：[https://share.weiyun.com/5m2Dinf](https://share.weiyun.com/5m2Dinf "https://share.weiyun.com/5m2Dinf")

关于 Lottie 的介绍就到这里，后续将会持续更新 Lottie 动效设计过程中涉及的各种问题和方法技巧。

# 导入篇

本次将以一个实际动效案例的导入流程为例，帮助大家了解高效导入设计文件的方法。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/7330ae1828ea160aa2385085cdb56dda_--rHAE1-Kk.gif)

以上为本次演示的动效案例。导入文件之前我们首先要分析操作对象的特点，有哪些部分是要做动效的，哪些部分是静止的。需要运动的图层或组要单独分开，保持静止的图层可以合并。如果涉及对称结构，可以在 AE 中只做一边，预合成以后使用翻转即可。

从PS导入AE

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/137182974f36c1524125d5a07530c3df_FwezX_4FTQ.jpeg)

将动效文件整理好就可以导入 AE 了，当我们将 psd 文件拖入 AE 中会有三个提示选项：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/892a6cff0d31c4e976e413ee119313ba_IaT_TuTd0r.jpeg)

1\. 素材

当我们已经导入了 psd 文件，需要从原 psd 补充素材的时候可以选择此选项，但是每次只能选择一个图层或者将所有图层合并为一个图层导入。优点是能让图层保持在 ps 中的位置，缺点是当有多个图层需要添加时需要多次导入。

2\. 合成

选择此选项，所有图层都会按照画板大小导入，所以会导致很多图层有透明区域。优点是对于可以复用的元素（如小鸡仔的翅膀）可以采用翻转的方式快速复制，无需移动即可变化到对称位置。缺点是会增大文件尺寸。使用 Lottie 输出动效时不建议此方式，会增加资源。

3\. 合成-保持图层大小

选择此项，优点是图层会裁切掉所有的透明区域，能够保证文件尺寸最小。缺点是翻转以后需要通过位移才能让图层和对称元素保持相同位置。可以通过先建立预合成，再一键翻转的方式，避免移动操作。使用 Lottie 制作动效时，推荐采用此方式。

从AI导入AE

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/b32f62d511f7a937e97d83f12edc4959_3Md3xEm-Zd.jpeg)

从 AI 中导入 AE 相对要麻烦一些。首先我们需要将 AI 文件导入 AE 中，选中 AI 图层，然后「右键-创建-从矢量图层创建形状」。AI 文件就转换为可以在 AE 中编辑的矢量图形，但是如果我们直接将 AI 文件直接拖入 AE 中，这样会导致所有形状都在一个图层里，如下图所示。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/05f5fdc2bfec5b2ad9e29e7f28924927_9qMuuPxqlf.jpeg)

在AI中拆分图层

所以我们需要在导入 AE 之前，先将 AI 文件拆分成多个图层。

首先还是和 PS 一样将各部分按照需要进行拆分，先不用命名。然后选中最上方图层，选择「选项卡菜单-释放到图层（顺序）」，再选中除最上方图层外的所有图层，按住鼠标并下拉。这样所有的图层就拆分开了。最后再删除掉最上方空图层即可。

完成以上步骤再对拆分开的图层进行命名。之所以没有让大家一开始就命名，是因为操作的过程中发现，释放图层以后命名好的图层名就改变了。

使用插件在AE中拆分图层

刚才提到的，导入的 AI 文件不分层，其实可以通过 Explode Shape Layers 插件解决。只需在 AE 中安装即可解决我们导入 AI 文件过程中的问题。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/bef3ab18d0e90f9cd2637742c3652c4e_WULARw6x64.jpeg)

1\. 形状一键拆分

通过该插件可以一键将 AI 图层转换为矢量形状，相对于「右键-创建-从矢量图层创建形状」要更加简单高效。转化为矢量形状后，点击第一个按钮，即可将图层拆分为单个形状。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/3d96b67a55ce901d1551c4693516db20_yF1w4-Fy6h.gif)

2\. 形状一键组合

使用一键拆分功能会将图层拆分成一个一个图形，但是很多时候我们不需要拆分的那么细。比如案例中的小鸡仔，有的部分是不动的，我们希望把它合并成一个图层。这个时候点击第二个按钮即可一键组合形状。

3\. 删除空图层

有时候拆分 AI 图层后会出现空图层，此时选择第四个按钮即可选中这些图层，便于删除。

4\. 批量选择修改填充/描边属性

使用最后两个功能可以快速选中形状层并快速修改属性，不常用。

AE与AI无缝衔接

以上说的方法都是单纯的在 AI 或者 AE 中处理素材的方法，但是我们实际工作中，经常会需要增加或者调整素材。最后介绍一款大杀器，可以无缝衔接 AI 与 AE ，不仅可以将 AI 中的元素一键导入到 AE 中，还可以将 AE 中的文件导入 AI。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/059adbcc7216a7a9bf9c1f0c733f1862_JygI2ql-2d.jpeg)

Overlord 具有全面而强大的，能够满足我们导入文件的各种需要：

*   导出所选内容：AI导出到AE，或者AE导出到AI；

*   导入所选内容：AI/AE选中内容后，在AE/AI中选择导入，即可导入所选内容；

*   导出选项：分层导入所选元素、记录形状数据、保持中心点在形状中心，默认是在合成的中心、导出内容到画布中心，默认是保持原位置；

*   快速切换 AE/AI 窗口；

*   在 AI 中新建一个与 AE 合成相同尺寸的画布；

*   导入色板到 AE 中（需配合 Ray Dynamic color2 插件）；

*   将参考线导入 AE。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/52d70141540c0e1d318a7ce7d97b0901_ZQ9A7EzgcA.gif)

日常使用过程中我们只需在导出选项中，选择分层导入所选元素，即可快速将所选内容快速原位复制到 AE 合成中（需要 AI 画布与 AE 合成大小相同）。

当我们需要将几个部分导出为一个图层时，只需关闭分层导出，再将几个元素选中以后，点击导出即可。

综合对比以上几种方式，Overlord 对我们日常导入和编辑素材来说更加方便快捷，当然不同的方式也有不同的应用场景。大家按需使用。

Sketch和Figma导入AE

目前越来越多的设计师通过 Sketch 和 Figma 来设计文件了。Google 团队开发了一款插件 AEUX，可以让这两个软件和 AE 无缝打通。详情可阅读：[《谷歌设计团队发布了一款动效神器，让 UI 和动效无缝打通！》](https://www.uisdc.com/google-design-aeux "《谷歌设计团队发布了一款动效神器，让 UI 和动效无缝打通！》")

插件安装

1\. 插件下载

下载链接：[https://pan.baidu.com/s/1CL9LO3gA17cSBBqaIZflJQ](https://pan.baidu.com/s/1CL9LO3gA17cSBBqaIZflJQ "https://pan.baidu.com/s/1CL9LO3gA17cSBBqaIZflJQ") 提取码：tmue&#x20;

备用下载链接：[https://share.weiyun.com/5895PQ8](https://share.weiyun.com/5895PQ8 "https://share.weiyun.com/5895PQ8")

2\. Explode Shape Layers安装说明

将「AE脚本」文件夹复制到相应 AE 目录下即可，如下：

..Support Files/Scripts/ScriptUI Panels

该脚本将会出现在 AE 的「Window」菜单下。

2\. Overlord安装说明

将 overload 文件夹分别复制到：

*   C:\Program Files（x86）\Common Files\Adobe\CEP\extensions

*   C:\Users\用户名\AppData\Roaming\Adobe\CEP\extensions

*   C:\Users\用户名\AppData\Roaming\BattleAxe

以上路径最后面文件夹如果没有就自己手动创建。打开 AE，在拓展里打开脚本随便输入注册码。打开 AI，在拓展里打开脚本，开始使用，这个脚本也需要在 AI 打开配合使用。

使用 AE 过程中的文件导入，就讲解到这里。下一篇将带大家了解使用 AE 导出 Lottie 文件时需要注意的问题，欢迎持续关注。

# 导出 Lottie 文件

## 动效导出类型

一般情况下我们导出的动效可以分为三种类型。

1\. 纯矢量图形动效

此类动效常用于图标、加载、启动页等。

2\. 包含位图的基本动效

此类动效为了表现一定的视觉效果，会用到丰富的渐变和图层样式等效果，因为 AE 无法直接输出，所以需要使用位图的形式输出。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/4c00db1c96cacd1a2a6d00076548b00f_g7JcSnTlaP.gif)

3\. 使用特殊效果的动效

前两类虽然输出的文件形式不一样，但是都是使用基本的位移、大小、旋转、透明度的基本动效属性，可以通过代码直接输出。但是如果试用了 AE 中的特殊效果或者第三方插件的话，是无法直接输出这些效果的。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/c4b0d96076c68e3cbdfcced00b06d63b_fvWgaIrOBz.gif)

## 动效导出方法

1\. 纯矢量动效导出

纯矢量动效导出相对简单，只需在导出时勾选字体图形化和演示模式两个选项，导出以后会生成一个 json 和 html 文件。分别供开发人员使用和预览动效。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/73e3c5aa37b43734d41cbece6291984d_36nyTLK856.jpeg)

但是矢量动效导出目前有一个最大的问题就是渐变色导出会变为无彩色。官方说是因为编码和语言的问题，所以中文版 AE 会出错。目前有相关的修复方法，但是相对麻烦。工作中尽量规避使用矢量渐变色。

关于渐变导出出错的修复方法，Windows 和 MacOS 需要进行不同操作。详细请看以下步骤。

2\. windows系统修复渐变问题

将AE程序语言设置为英文

方法一：在以下路径找到 application.xml 文件，用记事本打开 application.xml，按键盘的 CTRL+F 键搜索 zh\_CN 替换为 en\_US，并保存文件，重启 AE 即可

语言配置文件路径：C:\Program Files\Adobe\Adobe After Effects CC 2018\Support Files\AMT

但如果 AE 是从网上下载的中文版本，可能会提示当前账号只支持中文版 AE，修改后的 AE 无法正常打开。此时可以尝试方法二。

方法二：卸载 AE，然后在 creative cloud 中点击右上角菜单进入「首选项-creatice cloud-应用程序语言-设置为英文」，再通过 creative cloud 重新安装 AE。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/12cf3eccc5dcc30e6156f65b4d124312_eTDQ9udqLo.jpeg)

修改非unicode程序的语言为英文

通过「控制面板-时钟和区域-更改日期、时间或数字格式-管理–更改系统区域设置-选择英语（美国）」确定，然后重启电脑。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d37aa89b6cec2d0735068fb1b3bc37c0_ZLNsbI-iDp.jpeg)

步骤 2 的修改可能导致部分程序出错，建议使用完毕后再将程序语言改为中文。

3\. MacOS修复渐变问题

MacOS 相对简单，只需将 AE 修改为英文版即可。

将 AE 程序语言设置为英文。在「在访达-应用程序-选择ae的程序包-点击右键选择现显示包内容」，在 contens 文件夹下找到 resources，选择 resources 的子文件。在 resources 文件夹中找到 zh\_cn 和 zh\_tw，将 zh\_cn 和 zh\_tw 这两个文件夹拖出 resources 文件，就可实现 AE 的英文切换，重新拖回就实现了中文切换。

如果修改语言后，AE 无法打开，请参考上方，windosw 系统下通过 creative cloud 重装英文版 AE 。需要注意的是 bodymovin 也需要使用最新版本，旧版本可能不支持。

## 含有位图的动效导出

当动效中含有位图时，导出的动效文件就会多出一个 imags 文件夹，用于存放图片资源。导出之前可以在 bodymovin 的设置选项内可以进行相应的设置。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/9180f5c674cfe77e3f50721dba557841_TWS4-U7dlC.jpeg)

*   可以通过设置项来压缩图片资源，也可以导出图片后再用压缩工具压缩。

*   将图片转为 base64 编码并放进 JSON 文件里。这样就不用导出 images 文件夹了。但是图片转为 base64 后体积会增加，并且目前只有最新版的 web 和安卓端支持带 base64 的 JSON 文件的播放，iOS 以后才会加入。

这里额外需要注意的是，images 文件夹的名称和内部图片名称不可随意更改，不然 json 文件就无法调用资源，导致图片资源加载出错。

我们日常导出动效资源的时候默认生成的图片资源命名都是 ima\_0 这种格式的。但是在实际使用中会调用很多个 json 文件，如果每次生成的图片名称都一样会导致加载错乱，所以需要提前规避。一种方法是让开发人员去规避，另一方面就是我们在设计之初就做好命名。

如果导入素材之前就已经命名好了就无需调整了，只需在 bodymovin 的「设置-图片资源设置里勾选保留图片名称」。导出的图片资源即可按照命名导出。

如果需要在 AE 内部修改，务必要在项目中修改素材名称，在合成里修改的只是图层名称，这样是不生效的。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/5cdbc5117b3bdde5f015d1b48ed6ca1a_6l3xxicfB-.jpeg)

## 特殊效果的动效导出

含有特殊效果的动效是无法直接导出的，所以只能用笨办法，将动效渲染为序列帧。然后再导入 AE 按照帧动画的方式输出。

以一个粒子动效为例，首先我们将动效渲染为序列帧，然后隔一帧删除一帧或者多帧，以此来减少图片资源。在保证动效流畅的情况下，尽可能的减少图片资源。以优化存储和性能。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/cd1e80a5cd5923b662526ddbccda6827_h3A0kWNp4C.jpeg)

在合成设置里将帧率变为原来的 1/2，因为删除了一半素材，仍然使用原来的帧率会导致动效速度加快。所以需要减少帧率以保持速度和原本一致。

选中所有图层，将图层的轨道向左移动到最小，然后「右键-关键帧辅助-序列图层」，即可让图层一帧一帧播放。这里需要注意的是，首先选中最上方图层，然后按住 shift 键，再次点击最下方图层。用这样的方式全选图层以后，再序列化图层。动效的播放顺序才是正常的，否则可能会倒放。

关于 Lottie 动效的介绍，以及设计输出中可能会遇到的问题。到这里就告一段落了。相信看完这三篇文章，无论是对初次接触的设计师推动团队使用，还是新手设计师提高设计效率都会有一定帮助。

欢迎关注作者的微信公众号：「懿凡设计」

大家在使用Lottie输出矢量渐变图形的时候，应该有遇到过设计的渐变效果无法正常显示的问题。无论你设计的效果是什么样的，导出以后都变成了黑白渐变。那么这个问题可以修复吗？答案是肯定的。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/18374fe5e8bccb0cca8ed760873e52a3_SudsRzJlec.jpeg)

MAC系统渐变修复

其实在之前的文章中有提到过修复渐变的问题。对于MAC平台而言很简单，只需要修改「渐变填充」为「Gradient」即可，方法是选中渐变填充属性，点击键盘回车键即可重命名。(如果修改后还是无效，建议更新bodymovin插件为最新版)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1edc92d813258bf94d66df4043f0dde8_N4zu4Dy_QX.jpeg)

.json文件中记录的动效代码UI不需要过多关心，但是其中两个信息你是一定要了解的。**它们是你与前端对接沟通和获悉文件信息的一些关键参数。**

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d828ed2bf3bcdf85ae5ff919c3017f0a_EURWsw5Htx.jpeg)
