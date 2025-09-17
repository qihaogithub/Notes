# Android和iOS差异点

# Android和iOS有哪些设计差异点？来看高手总结的7个不同！

#### [\*\*  我要投稿 \*\*](https://wj.qq.com/s2/7185461/75b6 "  我要投稿 ")\*\*  编辑： **[**土拨鼠**](https://www.uisdc.com/author/sstt "土拨鼠")[**作者：Echo的设计笔记**](https://mp.weixin.qq.com/s?__biz=MzI0Nzg2MjI0NQ==\&mid=2247485856\&idx=1\&sn=9bf798f399881cd2ddd9d9fe02a74165\&chksm=e9a8cf2adedf463ce9f133aa99ff3fb8cd8b3e9d425f5ce2cc47a586d1bb7a8e68d1674842f3\&mpshare=1\&srcid=0915z0nZp8pJMSNWApicnHrg\&sharer_sharetime=1600133986887\&sharer_shareid=c6df72080208f72ae41e0fc3360cfa07\&scene=2\&subscene=1\&clicktime=1600135447\&enterid=1600135447\&ascene=2\&devicetype=android-29\&version=27001239\&nettype=WIFI\&abtest_cookie=AAACAA%3D%3D\&lang=zh_CN\&exportkey=A8RuG%2F6qFEljIZi3CTvBgio%3D\&pass_ticket=UWttYgA54zI0TGLgujy4aDZmHE47hMKAzkUayXF%2BW7I%3D\&wx_header=1%E3%80%91 "作者：Echo的设计笔记")**2天前  点赞 13**[**评论区**](https://www.uisdc.com/android-ios-design#post_comment "评论区")**  阅读本文需 7 分钟 \*\*

由于设计师、产品经理使用的移动设备大部分是iPhone，所以在做设计时，容易忽略Android和iOS的差异，按照iOS的规范进行设计，两端只做一套。

只做一套的会存在两个问题：

*   安卓用户的使用习惯不太适应iOS的设计，导致使用时遇到阻碍，任务流程失败率变高。

*   如果设计师或者产品经理有的异常场景状态没有想到，导致安卓开发没有组件调用，为了省事就直接调用安卓自带组件，导致整个产品在视觉风格上面既有产品风格的组件又有安卓系统的组件 ，统一性差。

所以设计师在设计过程中，针对两端的差异性，可以单独将具有差异性的Android部分做出来，保持两端的差异性。

#### **视觉风格和理念**

iOS通过使用留白、简化UI、使用无边框按钮等方式使得呈现的功能更加清晰。减少使用边框、渐变和阴影，使界面尽可能轻量化，从而突显内容。以功能驱动设计，突出重点内容并传达交互性。

留白可以使重要的内容和功能更加醒目、更易理解。使一个应用看起来更加聚焦和高效，如下图1所示。

让颜色简化UI，使用一个主题色。比如备忘录中用了黄色，高亮了重要区块的信息并巧妙地用样式暗示可交互性，如下图2所示。

使用无边框的按钮，通过[文案](https://www.uisdc.com/topic/%e6%96%87%e6%a1%88 "文案")、颜色以及操作指引标题来表明该无边框按钮的可交互性。如下图3所示。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-1_TsIp2VREuC.jpg)

Material 通过构建系统化的动效和空间合理化利用，并将两个理念合二为一，构成了实体隐喻。

在基本元素的处理上，借鉴了传统的印刷设计：排版、网格、空间、比例、配色、图像等，使用这些基础的平面设计规范。

在这些设计基础上，构建出视觉层级、视觉意义以及视觉聚焦。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-2_zBI41QepSk.jpg)

#### **支付规则**

当[App](https://www.uisdc.com/tag/app "App")含有虚拟商品，那么用户购买方式也不一样。

对于iOS用户来说，支付渠道必须走苹果支付平台，并抽取30%作为服务费。而android版不用走平台，使用支付宝、微信支付等第三方支付平台即可。

如下图所示，网易云音乐android版，支付时可以选择支付宝、微信、京东等支付方式。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-3_fqZ6zmVjL1.jpg)

而iOS端则只能走苹果官方平台（App Store）。对于公司来说，抽成30%意味着收入下降，但是这种走平台支付也有一个好处，可以连续订阅，自动续期扣钱。

#### **推送规则**

iOS系统的消息推送必须依靠苹果的APNS（Apple Push Notification Service）服务器来完成，信息与app之间的交互是通过苹果的服务器完成的。

Android的消息推送相比之下更加开源，在不选择使用GCM的情况下，app的消息推送就需要在自己或者是第三方服务器与设备之间建立一条长连接，通过长连接进行推送。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-4_GlRetcKT2R.jpg)

这意味着iOS端，即使app的后台杀死，依旧可以接收到推送。而android端则需要保持后台在线才能收到推送消息。

#### **文件选取规则**

iOS系统每个app之间没有文件夹概念，导致无法找到对应app的文件夹。

如果iOS版app想要发送文件时，则无法选择对应的文件夹里面的文件。但是因为有了iCloud的存在，可以通过iCloud选择文件。

如下图所示，微信如果想发送文件到微信好友时，点击文件，进入iCloud选择文件发送即可。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-5_m3CEYKvBT6.jpg)

而安卓版则可以调取文件夹，选择对应的文件发送。如下图所示，qq给好友发送文件时，直接进入手机的文件夹中找到对应的文件

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-6_1S9FpLXQ7Y.jpg)

#### **手势区别**

android和iOS的手势区别比较大，对于隐藏的操作，安卓长按较多，iOS左右滑动较多。

如下图所示，安卓针对列表更多操作时，采用长按手势，长按出现菜单。

而iOS左右滑动出现隐藏的操作。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-7_qVCnEV8c4c.jpg)

#### **组件风格的差异性**

iOS和android整体上视觉差异很明显。

android组件整体呈现通过投影产生层级区分，如下图所示。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-8_kqRbEPvHHz.jpg)

iOS则通过简洁的视觉层级区分，如下图的组件样式。单纯的分割线区分层级关系。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-9_QxEGdjjHO1.jpg)

#### **组件用法**

**1. 搜索栏**

android常使用搜索图标，用户点击图标进入搜索栏界面。

iOS直接以输入框的形式展示，用户点击激活输入框，从视觉的角度上看，iOS的搜索栏视觉更强化，更容易引导用户搜索。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-10_19E2A-QtPY.jpg)

**2. 警示对话框**

android对话框文案左对齐，按钮文案右对齐。

iOS对话框文案居中对对齐，按钮也都居中对齐。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-11_aHlsSYijKf.jpg)

**3. 卡片**

android针对于提示语，通常放在卡片里面，而iOS放在卡片外面。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-12_yONyPsg4sS.jpg)

**4. toast**

android的tost一般在界面底部，文案左对齐（非居中对齐）。安卓除了toast还有snackbar 。

iOS一般在界面居中位置，为了强化反馈状态，一般会有图标搭配对应的文案。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-13_LGCClMwPlU.jpg)

**5. 导航栏**

Android版的返回icon，通常用左箭头（中间有一杠）。同时导航栏的标题位于左边箭头之后，标题为当前界面的标题。

iOS版的返回箭头（中间没有一杠），返回箭头之后为上一级界面的标题。[导航](https://www.uisdc.com/topic/%e5%af%bc%e8%88%aa "导航")栏中间的标题为当前界面的标题。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-14_zJxwKaMKsY.jpg)

**6. 发送按钮**

Android版微信信息发送的按钮放在了工具栏上，ios版微信的信息发送按钮内嵌在键盘上。

下图为android版发送流程。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-15_AnVmeTjIhW.jpg)

下图为iOS版发送流程：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-16_361vbhfSd8.jpg)

**7. 更多操作**

针对于更多操作时，android长按通常出现菜单，而iOS长按通常出现底部操作列表

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-ad-20200916-17_oBQosByHxO.jpg)

#### **总结**

以上是针对iOS和android端部分设计的差异性总结。

如果需要做两套设计，那么应该如何设计呢？

可以先做一套iOS的，然后针对android端的，组件涉及到不同的地方进行全局替换。

例如长按操作，android使用菜单，iOS使用底部操作列表。对话框、底部操作列表和toast等组件进行全局替换即可。

## [**连高手都容易忽略的9个 iOS 与 Android 间的交互差异**](https://www.uisdc.com/android-and-ios-differences "连高手都容易忽略的9个 iOS 与 Android 间的交互差异")

[现在大多数的 PM /交互/ UI 设计师，在设计产品的时候都是以 iOS 为基准 思考产品上的各种功能逻辑、交互状态，而很容易忽略了某些功能在 Android 里并不能「一稿适应两端」，部分产品差异在安卓上是不一样的。](https://www.uisdc.com/android-and-ios-differences "现在大多数的 PM /交互/ UI 设计师，在设计产品的时候都是以 iOS 为基准 思考产品上的各种功能逻辑、交互状态，而很容易忽略了某些功能在 Android 里并不能「一稿适应两端」，部分产品差异在安卓上是不一样的。")

阅读文章 [*>>*](https://www.uisdc.com/android-and-ios-differences ">>")

欢迎关注作者的微信公众号：「Echo的设计笔记」

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-uxechoqr_c7OZaUgjLt.jpg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/uisdc-dtk-0921_jx4-QfjYvP.jpg)

&#x20;       点赞 *13*

&#x20;       收藏 *58*

[  复制本文链接  ](https://www.uisdc.com/android-ios-design "  复制本文链接  ")
&#x20;     文章为作者独立观点不代表优设网立场，未经允许不得转载。
&#x20;  &#x20;
