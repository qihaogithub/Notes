# AE·效果·动效周期表·文章

[http://foxcodex.html.xdomain.jp/index.html](http://foxcodex.html.xdomain.jp/index.html "http://foxcodex.html.xdomain.jp/index.html")

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/67e0ff21fa44e7ff2a03530a5eb3b639_dos7GsdYeC.jpeg)

## [NO.01 偏移旋转系：轨道](https://uiiiuiii.com/aftereffects/12127765.html "NO.01 偏移旋转系：轨道")

**(在轨道上旋转对象的运动)**

**原理:** 移动锚点属性使物体与锚点产生距离，为旋转属性添加关键帧或表达式。

**步骤:** 新建合成，绘制一个圆形，取消填充，保留描边，可将图层命名为圆轨道，其次绘制一个小圆形，保留填充，取消描边，将小圆与圆轨道呈同心圆的状态，中心点一致，然后修改小圆的锚点，使小圆圆心在圆轨道上边缘点的中心上（为保证中心点一致，此处不要移动位置而是修改锚点，因为旋转是以中心点的位置进行的），接下来设置关键帧，在0S时将旋转属性添加关键帧，在2S时，将旋转属性设为360度也就是刚好小圆绕圆轨道一圈（可以通过调整时间的长短来控制小圆的旋转速度）。也可以采用表达式的方法来制作轨道旋转，在上述方法的基础上删除关键帧，按住ALT键同时在小圆的旋转属性前面的码表上单击鼠标左键，为此添加表达式，将表达式改为time\*180(意思为每秒钟旋转180度)这样2秒会旋转360度为一圈，即可呈现出轨道旋转的效果。

拓展应用:可将小圆复制多个，修改不同小圆中表达式的度数值，来实现雷达的效果，也可能将小圆替换成星球，月亮太阳等图形。&#x20;

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/a70d86d7d2268913bdca2a2df228fc8b_w50OsKx9uv.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/2a334b94eabbe424e63535bee7c51bc5_oyKJCQPRaA.gif)

## [NO.02 偏移旋转系：偏移量](https://uiiiuiii.com/aftereffects/12128242.html "NO.02 偏移旋转系：偏移量")

**(运动沿着形状的路径旋转)**

**原理:** 调节描边的虚线属性以及修改偏移的数值

**步骤:** 新建合成，双击多边形工具绘制出五边形，在属性-点中改为6，将图形变为六边形，打开描边属性，修改描边粗细，线段端点可改为方头端点，线段连接可改为圆角连接,打开虚线，点击加号，将虚线数值改为100（可根据想达到的效果字行调整数值），然后给偏移属性添加表达式为time\*360(意思为每秒钟旋转360度),即可呈现出运动沿着形状的路径旋转的形态。

**拓展应用:** 可设置内框，外框，内部图形，调整它们的虚线间隙或者将六边形换成其他图形等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/e999b106c1be9526da0fdc490332bf91_fbEkNErlGI.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/8b5b1b16ab0dfbbc23996e4fded7ea6d_nHTyKFs6UL.gif)

# **3.勾画**

**(沿着路径跑光的效果)**

**原理:** 为纯色层添加蒙版，为蒙版路径添加勾画效果。

**步骤:** 新建合成，新建一个白色纯色层，选中纯色层绘制正矩形即为纯色层添加蒙版，在效果和预设中找到勾画，将勾画拖拽到纯色层中，在FX勾画中将描边选择蒙版和路径，路径里选择我们画好的矩形即蒙版1，片段属性改为4（需要X条线就改为X），混合模式选择透明，颜色，宽度以及硬度可根据需要自行调节，然后为旋转设置关键帧，在0S时将旋转属性添加关键帧，在2S时，将旋转属性设为360度也就是一圈。

**拓展应用:** 可用钢笔绘制蒙版，做出心电图波动的状态，或多个形状组合成旋转的轮胎等等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/81928fcf0b657ae6ad0907886d7b908e_iunyc0siRJ.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/0309ac40faccaf489038010bcbe64459_dbPjAaEjlj.gif)

# **4.循环**

**原理:** 偏移效果的调节。

**步骤:** 新建合成，新建六边形，在效果和预设中找到扭曲下的偏移，将偏移拖拽到六边形上，然后为FX偏移中的“将中心转换为”这个属性加关键帧，在0S时添加关键帧，在1S15f时，把将中心转换为属性的X值改为1204（可根据合成大小以及六边形大小自行调节，让六边形重合的数值即可）,将工作区切到1S20f,给六边形一个稳定的时间，此时预览，六边形会呈现匀速运动，可打开图标编辑器，改变匀速运动为先加速运动后缓慢停下的运动轨迹，然后所有关键帧设置缓动（选择关键帧按F9键或选择关键帧，然后菜单栏找到动画-关键帧辅助-缓动）。

**拓展应用:** 可做UI界面滑动效果，长条过渡，循环效果等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/2a2b7ee436c0f491b67b189a9a3418ff_dsiTkgo6bT.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6571ebd2ff5ffd54a7ace490bcb5e276_VHrJh_8x1Y.gif)

# **5.砖瓦匠(平铺)**

**原理:** 为纯色层添加蒙版，为蒙版路径添加CC Tiler 。

**步骤:** 新建合成，新建白色纯色层，为纯色层建立一个矩形蒙版，然后在效果和预设中找到扭曲下的CC Tiler,将CC Tiler拖拽到纯色层上，可以看到有三个属性，scale为缩放，Center中心点，Blend w\.Original为与原始图像的混合程度，在0S时为scale添加关键帧，然后在3S时把scale数值调到10%，这样就可以实现由一到多的平铺的效果，然后在3S时为Blend w\.Original添加关键帧数值为100%。将时间标尺向前移动10f,将Blend w\.Original的数值改为0，这样整体就有了循环衔接的感觉，最后为关键帧加上缓动。

**拓展应用:** 可替换其他形状，或一些图片来尝试做出更多有趣的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/f3062e8b2561f6ad06b228b5c7227cfc_LW-ptYgk_4.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d9a40178d0253bec4843fd36776561ad_GHwvN1Uw9i.gif)

# **6.极坐标**

**原理:** 为图形添加极坐标效果。

**步骤**:新建合成，新建一个矩形，然后想矩形横坐标的位置调为0，然后复制出5个矩形，将最后一个矩形的横坐标调到803（根据合成大小来设置即可）选择6个矩形，单击水平均匀分布后添加预合成，然后在效果和预设中找到扭曲下的极坐标，将极坐标拖拽到预合成上，把转换类型改为矩形到极限，然后为差值添加关键帧，0S时为0%，1S时为100%，2S时为0%，为保证整体过度自然，可在中间在相同关键帧让此状态产生停顿，最后整关键帧添加缓动，参数如下图所示，仅供参考可自行调节。&#x20;

**拓展应用:** 可用网格或矩形拉长或只保留描边等图形来制作，也可多个图层结合成多个预合成制作出更多的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/960481990e2dec3ab350d2e17e31271d_ZDszoUoLTn.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d539076f9925bbeba828402d7e17e797_30C8uc6MIK.gif)

# **7.线宽（改变图形和路径的线宽）**

**原理:** 为图形添加描边宽度的效果。

**步骤:** 新建合成，绘制一个圆形,取消填充,描边改为20,然后找到内容-椭圆-描边-描边宽度,为描边宽度添加关键帧,在0S时数值为20,在1S时数值为0,然后在2S时复制第一帧关键帧，最后选择全部关键帧添加缓动。

**拓展应用:** 可以添加缩放，做成小爆炸的效果或者添加多个圆形做成水波纹的效果等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/f648a1405c9b7bea3633f86d648c0eb8_NWnnW4LwGA.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/b42752ce54607c8480cee9c1db344749_OuqxUPEam4.gif)

# **8.图形变形**

**原理:** 调整多边形内外半径。

**步骤:** 新建合成，绘制一个星形，在内容-多边形-多边星形路径中，把点改为3，然后内径和外径均改为100，此时图形由星形变成了一个六边形，然后在0S时为内径和外径添加关键帧，在20f时把内径改为50，在1S15f时把内径改为100同时为外径添加关键帧，在2S10f时把外径改为50，在3S时把外径改回去初的100。此时整体过度会比较快，我们可在每次变化中间让图形停顿5帧，然后为整体关键帧添加缓动，如下图所示。

**拓展应用:** 可以和其他效果结合使用，形成更多有趣的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/59e28a44a0be0195611b3d4408350eb4_xUNNsaBwc2.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/614713611ea12ccf9c5fb68158127ee2_lbJWq5mq6w.gif)

# **9.连续图形变形**

**原理:** 在图形变形的基础上进行多图形的变换。

**步骤:** 可在第8个效果的基础上来制作，将第8个效果的描边改为填充，然后复制出4个图形，全部选择按U键，显示出带有关键帧的内径和外径，将第一个图形的不透明度改为100，其他图形的不透明度改为30，先将除了前两个关键帧之外的关键帧向后移动，先调整前两个关键帧，调整图形出现的时间，每个图形相隔5f（从形状5到形状1）,然后将第二组变化的关键帧移动到第一组变化结束之后（相同关键帧可以删除，如想中间有停顿也可保留并移动相应位置），每个图形相隔5f（从形状1到形状5）以此类推，如果变化更多的形态皆如此（1-5,5-1,1-5等等）

**拓展应用:** 可以变换其他的图形来进行处理也可结合其他效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/f3fbe95f2c5c3b6e260fe3180dfb9d7c_uelPl7oZRf.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/ba322c514f13e9b4a770cbd112837c27_-lcY2Rud17.gif)

# **10.阴影**

**原理:** 为预合成添加CC Scale Wipe效果，结合遮罩。

**步骤:** 新建合成，把之前的第8个效果拖拽过来或者重新练习制作出第8个效果，将形状图层添加预合成（因为六边形的边界有局限性，，创建合成后边界就变成了合成的边界）然后在效果和预设中找到过渡-CC Scale Wipe，将CC Scale Wipe拖拽到预合成上，Stretch表示拉伸（最长到达边界为100，负数是向反方向进行拉伸）Center表示中心，Direction表示方向，接下来把Stretch数值设置为100，Direction数值改为120°，然后将预合成进行复制取消效果，因为作者图中是镂空的所以，我们再次复制刚刚复制好的取消效果后的预合成，将后面两个合成再次建立预合成并且为他们建立轨道蒙版，选择Alpha反转遮罩，然后将形状图形的缩放改为80（此时预览动画，会发现在变换过程中描边会有所变化），所以我们为缩放添加关键帧，0S为80%，15f为70%，20f为70%，以此类推。

**拓展应用:** 可以将阴影的颜色进行更改或为中心点添加关键帧做出更多有趣的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/44926e77224e0a3be99787e186f3f52d_5VKCFftcC9.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1f80c6da0e99a909088ebe009a1a2952_RKaKJGfwR6.gif)

# **11.重塑(改变形状)**

**原理:** 为纯色层添加多个蒙版结合改变形状的效果。

**步骤:** 首先用AI软件绘制出四个图形分别是：正矩形，四角星形，圆形和七角星形，然后打开AE新建合成，新建纯色层，然后到AI里选择第一个正矩形复制，到AE中选择纯色层然后粘贴（后面三个图形也是同样逐一粘贴过来，注意要选中纯色层在粘贴），这样在纯色层上将产生四个蒙版，将蒙版1的混合模式改为相加，蒙版2.3.4的混合模式改为无，然后在效果和预设中找到扭曲-改变形状，将改变形状拖拽到纯色层上，源蒙版（优先想显示的蒙版）选择蒙版1，目标蒙版（改成哪个蒙版）选择蒙版2，弹性选择超级流体（里面选项是由生硬的变化到柔软的变化逐一递减的选项），在0S时为百分比添加关键帧数值为0%，然后选择FX改变形状进行复制，一共复制出四个，分别调整源蒙版和目标蒙版（如下图），因为百分比0到百分比100，,饿过程就是源蒙版到目标蒙版的过度，我们逐一调节关键帧（具体变化时间和停顿间隔可以自行调节），最后为所有关键帧添加缓动。

**拓展应用**:可以绘制其他图形作为蒙版或结合其他效果。&#x20;

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/0ff96298a7d0b6588459a85f69e5bed5_5C0Q2lvwZd.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/ba2abb0bacfdf831363e8bccf387ba97_Dxs34Gprll.gif)

# **12.缓动**

**原理:** 添加缓动和调整运动曲线。

**步骤:** 新建合成，绘制一个圆形，然后为位置属性加关键帧，由于真实事物是不存在匀速运动的，所以我们可以为关键帧添加缓动效果，并且调节图表编辑器，使圆形由快向慢的向前运动直到停下。然后用钢笔绘制一条与运动相符的线段，可为圆形上下加入一条虚线对比更明显，让虚线成为小圆的子集，跟随小圆运动而运动。

**拓展应用:** 可以结合矩形与其他图形做成转场的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/b48a8ad1fe2b14c76614008868aca075_cHeYauBXyI.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/325b26aa6b9967f40efc6bec77049bfc_gRN9bwi-0O.gif)

# **13.节奏**

**原理:** 缓动，曲线速度让效果更有节奏感。

**步骤:** 新建合成，绘制一个多边形（去掉填充保留描边），将点改为4，然后为外圆度添加关键帧，0S时为0°，在15f时为-612°，在1s5f时为-612°，在1s20f时为0°，然后为所有关键帧添加缓动，然后调整图标编辑器，形成先快后慢的运动轨迹，然后在15f时为形状添加关键帧，1s5f时旋转90°，在1s20f时为90°，在2s10f时为180°，并为所有旋转关键帧添加缓动，调整图标编辑器的速度。

**拓展应用:** 可以添加旋转，缩放，让更多图形融入形成带有更强的节奏感的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/fefe02dc4def50672a786a91abf5b3ef_bTNNchgTck.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d6e44bc9af3276cb13d5ad13e8dfe6f6_zl9JmkcJ2s.gif)

# **14.阶梯变化**

**原理:** 理解这个表达式:Math.floor(time*x)* y即x表示每秒旋转的次数，y表示旋转的幅度。

**步骤:** 新建合成，绘制椭圆，取消填充保留描边，作为钟表的外框，然后绘制一个矩形，然后点击添加一个中继器，副本改为36，让位置为0，然后调整旋转角度为10°（360/36），作为表的刻度，绘制一个圆形作为重心，绘制矩形作为指针，然后为指针的选择属性添加表达式Math.floor(time*5)* 10可以这样理解{(Math.floor(time*x)* y]  即x表示每秒旋转的次数，y表示旋转的幅度}，然后钟表就会按阶梯变化进行运动。

**拓展应用:** 可以绘制吃齿轮旋转的效果，添加不同表达式可使不同齿轮旋转效果不同。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/fb518ea4a7569206f0b48689114e2e34_df7mfnlIxM.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6ccf43a78fd8c43e2646849fc31ca091_HEONrY9BJ8.gif)

# **15.时间置换**

**原理:** 无线电波和时间置换效果。

**步骤:** 新建合成，新建纯色层，效果和预设中找到生成-无线电波，添加到纯色层上，然后把无线电波里的多边形的边调为6，波动的方向调为30°，开始宽度和末端宽度调为10，颜色可以改为白色，新建纯色层添加图层样式为渐变叠加，将样式改为角度，然后新建合成选择将所有属性移动到新合成，新建调整图层，给调整图层添加时间置换效果，将时间置换图层改为渐变，最大位移时间改为0.5S，时间分辨率改为4（将画面分为4部分），然后在2S时为六边形里的频率加关键帧，数值为0，然后在前一帧时关键帧数值改为1。

**拓展应用:** 调整频率，位移时间等等，尝试发现一些新效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/0ca9150bfb050d95d32836c75617d785_MkibDGHHEM.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/649675f53c8bd77684ea40af91603d6c_F2YxMF9Qk_.gif)

# **16.尖端形状**

**原理:** 修剪路径以及表达式。

**步骤:** 新建合成，绘制一个六边形（要勾选贝塞尔曲线路径），然后为六边形添加修剪路径，在效果和预设中找到滑块添加到六边形上，在修剪路径中的结束属性添加表达式，并将表达式关联器拖拽到滑块上，在0S时为滑块添加关键帧数值为0，在2S时滑块数值为100，然后绘制一个圆形，找到六边形的路径进行复制，到小圆的位置上（要在0S时）进行粘贴（如出现偏差手动调节因为路径是按你第一次绘制的路径产生的如中途有移动都会产生一定的偏差），为小圆的位置属性添加表达式，找到添加Property-valueAtTime(t),用鼠标选中t,然后将表达式关联器拖拽到滑块上，因为滑块动了100步，小圆运动时间是2秒所以表达式后面需要除以100乘以2，然后圆形每次画过的端点都加一个关键帧并为关键帧添加缓动，然后调整运动图表，让整体的运动更加自然，然后在6S时加滑块的数值改为0，加缓动并调节速度。

**拓展应用:** 可以利用滑块做出多样式的转场效果等等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/7fc3fb8aa06ca31acb4054f517a6c738_p0BgggZ8CU.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/206bffe9f36d874f7984f990823b90e2__3A235NcP3.gif)

# **17.音频波动**

**原理:** 结合音乐素材，让波形随音乐节奏而动。

**步骤:** 新建合成，新建纯色层，在效果与预设中找到音频频谱拖拽到纯色层中，然后把音频素材导入进来，然后把音频频谱中的源改为我们导入进来的音频素材，起始频率和结束频率可以改变图形的样式，频段可以增加或者减少声波线条的数量，最大高度可以限制波形的高度，厚度可以更改描边的粗细，柔和度类似于羽化的感觉，显示选项改为模拟谱线，选择纯色层绘制椭圆为纯色层添加蒙版，将蒙版模式改为无，将音频频谱路径改为蒙版1，然后复制纯色层放大蒙版路径，然后改变参数，继续重复上一部操作，根据不同音乐节奏的不同出现的效果也是不同的。

**拓展应用:** 可以做不带蒙版的效果或复制多个波形改变参数调节出更多的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/ee057246582b3f5af9d872bf2829a6f5_JgogLq7AE9.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/5e16034f9945db617d1261669d937ec8_bABjwwvwG6.gif)

# **18.波（制作辐射波的动作）**

**原理:** 无线电波效果。

**步骤:** 新建合成，新建纯色层，然后在效果与预设中找到无线电波并为纯色层添加，将多边形的边改为6，方向旋转90°即可。其他参数可以根据自己的喜好来进行调节数值。

**拓展应用:** 可以做不带蒙版的效果或复制多个波形改变参数调节出更多的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/2ec97b9f34462635d05b9deae7442223_In6gxdmprE.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/14055e8caf1576ee095da135bb5c9ec2_fNaS-VRDuy.gif)

# **19.链接**

**原理:** 图形结合光束效果与表达式。

**步骤:** 新建合成，绘制一个圆形，复制三个，改变大小和位置，然后新建纯色层，在效果和预设里找到光束并拖拽到纯色层上，柔和度改为0，颜色改为白色，调整长度以及厚度，然后选择两个圆形调出位置属性，之后为光束的起始点和结束点添加表达式，关联到两个圆形的位置上,（如果此时光束并没有把两个圆连接上可调整光束的长度），然后复制纯色层，选择其他的两个点重复上述操作，知道点皆两两相连，（共6根），然后为所有的圆的位置加关键帧每隔15f调节一下圆的位置，然后为所有关键帧添加缓动并调节运动速度。

**拓展应用:** 可以结合移动缩放等效果做出其他有趣的动态。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/160da1fbbc0b9b1a1c184aa451309ee0_qqpnlbHbWl.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/b7c092f1fd5ba7c359eaef0f05de09ae_yFxK_Ufl-5.gif)

# **20.粒子**

**原理:** 粒子效果与插件Particler。

**步骤:** 新建合成，新建纯色层，在效果和预设中找到CC Particle World并拖拽到纯色层上，为出生率，旋转，粒子寿命，出生以及死亡尺寸添加关键帧，即可得到很多有趣的效果，下面是给大家翻译好的名称，此效果最好使用插件Particler来制作，两者的效果有相似之处。

**拓展应用:** CC Particle World的翻译如下图所示（大家可手动调节不同的属性来熟悉操作）。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/81c94e0a45b6ca435dd707784bbb216d_UaNwsvqlhE.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d53e4d41be81ac8f4d9a333fc597d0cf_KtZqgYCay3.gif)

# **21.网格**

**原理:** 网格效果的应用。

**步骤:** 新建合成，新建纯色层，在效果和预设中找到网格并拖拽到纯色层上，大小依据改为宽度滑块，然后宽度为50在0s时加关键帧，在1S时宽度改为150，在10f后再次添加关键帧，让网格宽度保持不动，然后1S后复制第一帧关键帧粘贴到此处，最后为整体关键帧添加缓动。

**拓展应用:** 可以结合效果和预设中的其他效果来实现更多动态，比如旋转，极坐标等等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/91cd9e361dfb9e69f622265c79aa4518_5vYrYpSybq.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/678c7c9987a24e89f16afdf04954530f_A-rsXEnB_F.gif)

# \*\*22.遮罩擦除  \*\*

**原理:** 反转遮罩。

**步骤:** 新建合成，绘制一个圆形，为缩放属性添加关键帧，让圆形由0经过20f到100%(如绘制的圆过大不到100%到自定义数值也可以)，然后复制此图形，讲整体加关键帧向后移动20f,在形状图层1上遮罩设为alpha反转遮罩形状图层2，即可达到效果。

**拓展应用:** 可以结合变换的效果制作或使用其他蒙版遮罩。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/a488006506d9188651b3e05bc256c7b1_yVgLWvsw4y.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/2876f164bb819421df94596b0b99b93d_VzwpQJHh6a.gif)

# **23.粉碎**

**原理:** 破碎效果。

**步骤:** 新建合成，新建纯色层，在效果和预设中找到碎片并拖拽到纯色层上，形状图案选择玻璃（也可以自定义绘制）调节方向，速度以及凹凸深度即可出现效果。

**拓展应用:** 可调节灯光材质出现更加立体的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/9bccb7f7b59ebe776bc0ac602b2e1227_dGETizJnZU.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/415bf764dffec648b92dd30c4caa7148_ettLqiObYn.gif)

# **24.卡片舞**

**原理:** 卡片动画的偏移。

**步骤**:新建合成，创建矩形，然后在效果和预设中找到卡片动画并添加到矩形上,因为行和列的数值是根据合成大小来确定的，矩形是比合成小的，所有行列要由肉眼去看而不是针对数值去调节,将灯光的强度深度环境光均调节到最大，为Z轴偏移和y轴偏移添加关键帧，复制矩形，删除所有关键帧，在下边图层的最后一帧关键帧对应位置，为复制好的图层的X轴偏移添加关键帧，可以在中间第二次变换是添加5f的停顿，并为所有关键帧添加缓动效果。&#x20;

**拓展应用:** 可以结合破碎效果与时间反向，使图形或文字由破碎到复原等等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/4612fdbb74ba4b742ff5f0749daaf037_lmwQ6Fz99t.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/c836317b84e9d5c8f31d6eca6dbd93b9_2aT9iOIw_U.gif)

# **25.旋转褪色**

**原理:** 旋转与不透明度结合。

**步骤:** 新建合成，绘制一个矩形并为旋转和不透明度添加关键帧，然后复制矩形，将旋转角度改为90°，透明度为0，在20f的位置将上矩形旋转角度改为180°，下部矩形旋转改为90°，不透明度进行调换，最后为整体关键帧添加缓动并调节运动速度。

**拓展应用:** 可用文字或其他图案形状来替换矩形，可增加多个属性结合当前效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6b0e88ce0d51480ddec9dbe25826fd5a_2qTE6rpkhO.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/4346dcfbcd4db349b24dae310e81d331_hNIserj5O6.gif)

# \*\*26.滑动切换（幻灯片）  \*\*

**原理:** 通过路径使形状变形，并通过序列图层进行调整。

**步骤:** 新建合成，绘制矩形（勾选贝塞尔曲线路径），选择上部两个瞄点，向右侧倾斜，然后复制矩形，像矩形2向左侧移动使矩形右侧边贴合原矩形左侧边，在1S时为两个矩形的位置和不透明度添加关键帧，然后在0S时将形状图层2的位置向右上方调节（形状图层1的位置向左下方）,然后将不透明度调整为0，因为最终效果是先在中间，然后走开，在回来，所以要讲整体关键帧向后移动，复制最后一帧的关键帧粘贴到最前方并为整体关键帧添加缓动修改运动速度。选择设置好关键帧的两个图层进行复制并将图层顺序移动到上方，选择复制好的图层的所有关键帧向右移动（重复操作多次，左侧也是相同方法），调整图层的顺序（右侧-左侧），然后从下至上选择全部图层，然后选择动画-关键帧辅助-序列图层（时间选择8S其他数值也可以），然后将时间调到0秒并补全关键帧，把全部图形添加预合成，然后绘制一个正矩形作为遮罩。最后讲时间调节到合适位置也可以放大缩小预合成。

**拓展应用:** 可以将正矩形遮罩改为文字或者其他的图形均可。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/255be96cdfc0addf45750a339e45b27e_UPl29dBtyh.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/9ec2b034064aa8c14dc07409631ec19d_Jkj0fPmSK0.gif)

# **27.查找边缘**

**原理:** 效果和预设中的马赛克与查找边缘结合。

**步骤:** 新建合成，新建六边形，在效果和预设中找到风格化-马赛克并添加在六边形上,增加水平和垂直的数量,然后在效果和预设中找到查找边缘并拖拽到六边形上，为与原始图像混合添加关键帧。最后为所有关键帧添加缓动。

**拓展应用:** 可以结合其他效果联合使用，强化边缘。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/aa6ee686d974a3f5790df6540b3c18cd_nsgi-JlG7v.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/43dbb7dd379526fda76931cd57d47137_YpI-8gfxtg.gif)

# **28.涂写**

**原理:** 效果和预设中的涂写。

**步骤:** 新建合成，绘制一个正矩形并为矩形添加蒙版，然后在效果与预设中找到生成-涂写并为正矩形添加，调节涂写里的参数到合适数值，为起始和结束属性添加关键帧（如下图），然后为所有关键帧添加缓动，然后将摆动类型改为静态。

**拓展应用:** 可以将六边形改为其他形状或者文字都可以使用涂写的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/4c6ac5e07756d8fd89c8c8661d6716ba_6QQ_j3Nnyi.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/af5d4343ee355f3a6e35f4c1712c71e9_kyTfTmj3x9.gif)

# **29.百叶窗**

**原理:** 效果和预设中的百叶窗。

**步骤:** 新建合成，绘制一个矩形，在效果和预设中找到过渡-百叶窗并为矩形添加此效果，为过渡完成添加关键帧，然后复制矩形移动关键帧，调节角度和位置删除不需要的部分，并为所有关键帧添加缓动并调节运动曲线。

**拓展应用:** 也可在文字里设置百叶窗的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/bdded8f71e4f51c3cc059ca21f276506_UU5p_NJyLI.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/690ef8767adea1a02a6262024d588171_0C1utjwx5G.gif)

# **30.线性扫描**

**原理:** 效果和预设中的CC Line Sweep。

**步骤:** 新建合成，绘制一个矩形，在效果和预设中找到过渡-CC Line Sweep并为矩形添加此效果，在矩形上为结束属性添加关键帧，然后复制矩形（方法和百叶窗的制作相似），我们可以调节关键帧的位置，让中间有一个停留，最后为所有关键帧添加缓动。

**拓展应用:** 也可以结合马赛克来为图形或文字添加此效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/ffdc1dda4daf6308eb47b6164c1af11a_4w1gdR3qBQ.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/ceaa90eae380fc306da6175d846a3483_VyjDw1o_sb.gif)

# **31.文本特效**

**原理:** 效果和预设中的解码淡入效果。

**步骤:** 新建合成，新建文本输入文字，在效果和预设中找到解码淡入并为文字添加此效果，调节关键帧的位置。然后可在文字下部绘制一条横线。

**拓展应用:** 可添加滑块，百叶窗等其他效果为文字做出更多有趣的动效。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/74f98fb126f02fb871af1d8c5d1ec426_0j6hDt3vfu.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/9e6437e7111807af9e03a78dc3e62ada_6V2PLYnBkX.gif)

# **32.随机**

**原理:** 采用随机表达式。

**步骤:** 新建合成，新建纯色层，绘制一个圆形，并为圆形的位置属性添加表达式\[t1+w,t2+h];t1=random(200);t2=random(200);h=thisComp.height/50;w=thisComp.width/50;\[t1,t2],（解释在下图）最后可以添加预合成，调整预合成的位置。

**拓展应用:** 也可以为数字添加表达式。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/134c5ab3bd3b040b8c78c4b29a6ab6a8_BNw5hsao-Y.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/ee35fc9f89b0db1119bf2d19737000d6_0eLorHyGda.gif)

# **33.sin正弦**

**原理:** 正弦表达式。

**步骤:** 新建合成，新建纯色层，在效果和预设中找到写入并为纯色层添加此效果，为画笔位置添加表达式（下图会进行解释），绘制一个圆形并为位置属性添加表达式(如下方)，然后绘制一调虚线，将虚线的位置关联到圆形上。也可以将整体设置预合成添加蒙版等等。

**拓展应用:** 如果想让圆随着正弦波动可以设置父子关联。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/68e892812efa39ed23b9de875b66736d_hIjmwhqJln.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/0b639ec2aa7602480742a12b12d15257_xNtkYxHOtg.gif)

# **34.弯曲**

**原理:** CC Bender效果。

**步骤:** 新建合成，绘制一个矩形复制四个，为五个矩形拉开距离进行对齐，在效果和预设中找到CC Bender并为矩形添加此效果，调整顶点和底点的位置，然后为弯曲的数值和类型添加关键帧（如下图），最后为整体添加缓动。

**拓展应用:** 可制作转场动画。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/b7b3f3e1ef699722453894456379a515_3gXy8yxTAK.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/2fab943f01968a128b325cebe3a16b7c__e-ioEWCP0.gif)

# **35.波形变形**

**原理:** 波形变形效果。

**步骤:** 新建合成，绘制一个圆形，在效果和预设中找到波形变形并为圆形添加此效果，为波形的类型和高度添加关键帧（如下图所示），

**拓展应用:** 可以结合摆动或其他效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/4e94802c719707839e7dd16f85437060_08zfB1aP-p.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/8c39b9c95d70961105c4bac7e6aef52f_qqd_zKg51n.gif)

# **36.旋转扭曲**

**原理:** 旋转扭曲效果。

**步骤:** 新建合成，绘制一个矩形并为矩形添加旋转扭曲效果，为角度属性添加关键帧，为图形自身旋转属性添加关键帧（如下图所示），最后为所有关键帧添加缓动。

**拓展应用:** 可结合文字或其他图形来做此效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/ef99ea86632294468c0b7b3107c46659__LpIKK9Wdp.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/24b1bab0b3320f753f65604f0a338ddb_d8hU77gevY.gif)

# **37.扩散（散布）**

**原理:** 效果和预设中的散布效果。

**步骤:** 新建合成，绘制一个圆形，在效果和预设中找到风格化-散布并拖拽到圆形图层上，为散布数量添加关键帧（如图），最后为所有关键帧添加缓动。

**拓展应用:** 可为路径或文字添加此效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/587b7ae75c7a46b0b29ed2663140b18f_OTkzmIHJ56.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/0b0486d94f2bff37811dd0b52759643d_sKPc8adJor.gif)

# **38.中间值**

**原理:** 效果和预设中的中间值。

**步骤:** 新建合成，绘制一个六边形，在内容里添加中继器，副本改为4，位置改为0，缩小比例，调整旋转角度（数值可根据效果自行调节），然后在效果和预设中找到中间值并添加到六边形上，勾选在Alpha通道上运行，为半径属性添加关键帧，最后为整体关键帧添加缓动，然后调节运动曲线。

**拓展应用:** 可为字体添加此效果，也可为照片添加调整半径值可以去噪点等等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/2f1007951e606862954121add45499d1_eI8u79e_gG.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/51a9e57720f60f0363fa89e0c22b54d1_QQI0apVGEV.gif)

# \*\*39.马赛克  \*\*

**原理:** 效果和预设中的马赛克。

**步骤:** 新建合成，绘制一个六边形，为旋转属性添加关键帧，并为其添加马赛克效果(马赛克在之前效果里有使用过)，调整水平和垂直的数值无需添加关键帧。

**拓展应用:** 可结合文字或其他图形，也可为照片添加此效果，由马赛克到真实等状态。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/94352bd9d5358d5971ef87569d91c723__VjiRtGHTA.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/f6631b15f6f5506380a52f286f930a02_eyxzSy23YY.gif)

# **40.不透明度**

**原理:** 图层的不透明度属性。

**步骤:** 新建合成，绘制一个圆形为不透明度添加关键帧。

**拓展应用:** 可为文字或图形添加转场的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/b96cf8cea14f6df1da29daa1358aa63e_vZv0va7gb3.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/e2c86138ac1cf92a1c26748c6e377e84_qvUfPZ8xlI.gif)

# \*\*41.镜头光晕  \*\*

**原理:** 效果和预设中的生成-镜头光晕。

**步骤:** 新建合成，建立一个纯色层，然后新建调整层，在效果和预设中找到镜头光晕并为调整层添加，为光晕中心添加关键帧，最后为整体关键帧添加缓动。

**拓展应用:** 可为实景照片添加此效果。原作者使用了插件“OpticalFlare”。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/7681758e1dc590e75b35dd94f906d268_YPdeCbt5rq.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/b2dc2e962fdd42ac99ab088b6cf5e341_mC26tl-xj4.gif)

# **42.交叉模糊**

**原理:** 效果和预设中的CC CrossBlur。

**步骤:** 新建合成，绘制一个正矩形，在效果和预设中找到CC CrossBlur并为正矩形添加，然后为RadiusX与y添加关键帧并调节它们的数值。

**拓展应用:** 可为其他图形添加此效果也可结合蒙版。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/05ef70029e2c40dc4d47d30eadb10a76_UA8RhBiVtO.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/fd47a875025566c11007ca5d04c4e05c__jGT9o5iWe.gif)

# \*\*43.高斯模糊  \*\*

**原理:** 效果和预设中的高斯模糊。

**步骤:** 新建合成，绘制一个圆形，在效果和预设中找到高斯模糊并拖拽到圆形图层上，为模糊度添加关键帧，最后所有关键帧添加缓动，调整速度。

**拓展应用:** 可为路径或文字添加此效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/935e870a1a34814f19689a37fe8a3c3b_wk4l9E94rZ.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/37ce7c01c9bc026d253cc1ed9de18c69_6D-nbi19jV.gif)

# **44.景深**

**原理:** 调整摄像机的光圈和模糊层次，然后改变图形的位置。

**步骤:** 新建合成，绘制一个矩形和圆形，创建摄像机，勾选启用景深，为图层开启3D，在摄像机属性中调整光圈和模糊层次（光圈越大，景深越浅），然后为矩形和圆形的位置添加关键帧，最后为所有关键帧添加缓动。

**拓展应用:** 可为网格调整景深效果，调节角度可出伪3D效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/370b43d64399163d3ae9bcc915f8ad83_kbfxeCqEK7.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/3130d3637ec8e6690ee0b59a661bde74_NzvOLaSNgT.gif)

# **45.运动模糊**

**原理:** 运动模糊开关。

**步骤:** 新建合成，绘制一个圆形，调整位置关键帧，然后添加缓动，开启运动模糊开关。

**拓展应用:** 可在制作其他运动图形或文字时加上运动模糊的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/dafc49263b3d2207bbdb5e4206c86ce6_6JAesnUE8Z.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d5f2837f24ad97762f7990b3674094b4_F9NNzhKOrS.gif)

# **46.发光**

**原理:** 效果和预设中的发光效果。

**步骤:** 新建合成，绘制一个圆形，在效果和预设中找到发光并为圆形添加，调整发光半径的数值添加关键帧。

**拓展应用:** 可为真实图片添加此效果，也可用在绘制灯光上。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6dc9985556465f99faa8c0f2f064b7b4__WZTyArEI3.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/928a8e91cc93ec8a9ff47bc28542c805_Dkd6YDbt3b.gif)

# **47.径向模糊**

**原理:** 效果和预设中的CC Radial Blur效果。

**步骤:** 新建合成，绘制一个矩形，在效果和预设中找到CC Radial Blur并为矩形添加，调整类型并为程度添加关键帧。然后为矩形的缩放属性添加关键帧，最后为整体关键帧添加缓动。

**拓展应用:** 可结合其他效果尝试做出太阳光的感觉。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/152389f16af8c8f203d7a7453697fe8b_pkwS240fPT.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/ec4a95cd68e802fdcd65a653ea017d06_CCzgUTq97P.gif)

# **48.移动**

**原理:** 位置属性。

**步骤:** 新建合成，绘制一个矩形，为位置属性添加关键帧即可。

**拓展应用:** 这个非常简单也会经常用到任何场景中。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/677e7b528274a68c674bb420b7c26f23_ohQBgpPAyu.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/3c264f643f376f5958e70cc4b20392f2_BK3kZGIhqb.gif)

# **49.对称移动**

**原理:** 利用表达式-1，使方向相反。步骤:新建合成，绘制一个矩形，进行复制，为第一个矩形的位置属性添加关键帧，为第二个矩形的位置属性添加表达式。

**拓展应用:** 可在文字和数字两侧设置辅助图案来完成转场效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/5c6a3be00dafc3264c60d20835b6f658_RCXdeM7zS-.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/76d470d03ab59a236f4438c306391c9e_YMD62bTyxG.gif)

# **50.连续移动**

**原理:** 中继器。

**步骤:** 新建合成，绘制一个矩形，角度改为45°，添加中继器，副本为5，并为位置属性添加关键帧（数值可根据自己图形大小来调节）。

**拓展应用:** 可以制作卡片分开集合的效果等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/0c059be278a1a186e9e0eeccc74b5ef8_qhtQL6xDzv.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/c778d2d9f306d42d0c3e1b016f624b32_k5lOWGOlzG.gif)

# \*\*51.摆动移动  \*\*

**原理:** 随机表达式。

**步骤:** 新建合成，绘制一个圆形，为位置属性添加表达式(下图解释)最后可以添加运动模糊。

**拓展应用:** 可在其他图形上执行此表达式也可复制多个图形调整数值。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/4adba2fa2a3d2da908d1b8e21a48aebf_bwvKLtKovF.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/55cac3e013bea1a800e07f8ef16e7b3a_vFkhcakf2U.gif)

# **52.残影**

**原理:** 效果预设中找到残影。

**步骤:** 可以在51的效果基础上制作，在效果和预设中找到残影，可调整衰减的时间，强度，并为数量添加关键帧。

**拓展应用:** 可以结合颜色的改变来处理出其他有趣的效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/787dacaadf64fa889c84d2a7b426ee1f_w-Gx9Sw-Wv.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/e5d96c876dfaf5e1be1d3e4af97c978e_Sdc9SwrloM.gif)

# **53.旋转**

**原理:** 基本属性旋转。

**步骤:** 新建合成，绘制矩形，调整旋转（快捷键R）属性的关键帧。

**拓展应用:** 基本的属性，经常使用应用范围很广。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/5391ab321074a637007e5ab22bad3f44_tkgAxA6Od4.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/082e3ea6f3ea4d73d481a50a3c9bd654_FwLDKcNNWy.gif)

# **54.对称旋转**

**原理:** 旋转表达式

**步骤:** 新建合成，绘制矩形，设置旋转属性，然后复制矩形为旋转属性添加表达式（方法个第49个类似）只是一个是位置属性一个是旋转属性。

**拓展应用:** 可绘制齿轮旋转效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/c3b45be66c101ecbc73ff79ebd9ad57b_Wiq1TiwZpx.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/dcbf09f2b880042aab6d136d04ffad4d_O6T9zTg9n2.gif)

# **55.连续旋转**

**原理:** 中继器。

**步骤:** 新建合成，绘制一个矩形，添加中继器，副本为4，并为旋转属性添加关键帧，数值如下图所示，最后为关键帧添加缓动。

**拓展应用:** 可做旋转CD，换成其他图形都可以。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/81df070799b164206263257752df418f_7A1m0KdcWp.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d1fefef2581b0241da9edb49250b2b16_DySy9veDM1.gif)

# **56.摆动回弹**

**原理:** 随机表达式。

**步骤:** 新建合成，绘制一个圆形,添加修剪路径设置结束数值，然后为旋转属性添加表达式（下图解释）。

**拓展应用:** 可制作钟表或机械的指针。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/ba758a85d8f7cc5061f25754ab5beb2a_dQdRHQHJD-.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/125f58ccec43ccfbde5582bc34da3caa_3J9kcu78QW.gif)

# **57.三维旋转**

**原理:** 通过打开3D开关来调节更多维度的旋转角度。

**步骤:** 新建合成，绘制一个圆形,复制多个打开3D属性，分别调整不同图形的不同方向的旋转角度如下图，最后添加关键帧缓动。

**拓展应用:** 可为其他效果打开3D开关，从而可以多一个维度的来实现更多效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/edce7fa179f6c34d93d9be57aea91dea_54jq9_NhF6.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/573e66eb44bfba2b6c9f9a9ca2ba2cb3_lqfpF5HxpN.gif)

# **58.比例**

**原理:** 调整形状的大小，缩放比例。

**步骤:** 新建合成，绘制一个矩形,调整路径大小以及缩放，中间设有停顿等待，最后整体关键帧添加缓动然后调整速度。

**拓展应用:** 调整大小，方向，比例很常用，多处场景均可。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/22a17a45e119c004cb3f4adcb78f7c0b_gzhuV6Nb8f.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/5b13f9604a7fbd3d83d1114ae2481f73_4e3X0LqUdD.gif)

# \*\*59.对称缩放  \*\*

**原理:** 调整形状的缩放数值。

**步骤:** 新建合成，绘制两个矩形，分别调整缩放的数值，并错开图形的位置，最后为关键帧添加缓动。

**拓展应用:** 也可使用表达式来设定。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/cf44687ee17e4ae88152c2fa0d3dbf2b_8hcbyhCBu1.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/2eb861d97ea22bc5be283f37c4ea3156_fOnvl8tEgb.gif)

# **60.连续伸缩**

**原理:** 利用比例属性来调节。

**步骤:** 新建合成，绘制一个矩形（只保留描边），旋转角度45°，添加中继器，副本为5，然后调整中继器中的比例的关键帧数值，最后为所有关键帧添加缓动。

**拓展应用:** 可结合修剪路径来进行操作。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1773dab429f0293233eba43441dca5ab_gFgAQF9uSk.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/af871be85691bb752500905dac823b9e_oMd0tm6IvY.gif)

# **61.随机摆动**

**原理:** 随机表达式。

**步骤:** 新建合成，绘制一个圆形，为缩放属性添加摆动表达式。

**拓展应用:** 可制作心跳的动态等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/8a462aba825809bd7835ae949b00a4e3_pWiX6KD97N.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/a63cdfc1f9980144657be1dc3fae0276_yIQCeavFFS.gif)

# **62.点**

**原理:** 利用中继器来实现。

**步骤:** 新建合成，绘制一个圆形，添加中继器，横向副本多一些，再次添加中继器，纵向副本多一些，（调整位置X，Y的数值可以改变横纵以及间距），然后为圆形的大小添加关键帧，最后为整体关键帧添加缓动，调整速度。

**拓展应用:** 可用来当做背景等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6e3d2275ec358ce6238c3978f0aac08d_D3X7-HSrEg.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/b9e21df172233bea736055786cee8444_wdx35Z101T.gif)

# **63.线条修剪**

**原理:** 修剪路径。

**步骤:** 新建合成，用钢笔工具绘制一条线段，取消填充保留描边，添加修剪路径，为开始和结束属性添加关键帧（如下图）最后为关键帧添加缓动。

**拓展应用:** 很常用的一个功能，很多地方都可以用到修剪路径。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/aa747d84384f93a32998f67d9dde46a5_HbBJaz3eEA.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/cc0b637bbee0d8ec7a96bc6b4c5d6ee6_zChEWv0PZm.gif)

# **64.图形修剪**

**原理:** 修剪路径的应用。

**步骤:** 新建合成，绘制一个圆形保留描边，添加修剪路径，调整开始和结束的关键帧（方向可调整椭圆的路径），大致操作方法和63几乎一致。

**拓展应用:** 很常用，可做转场效果。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/13b1777d017ae292e3da959abdc161e7_BBovv6Xtbw.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/3ae9972cf150c641d292ed383e86664e_S373a1syAs.gif)

# **65.连续伸缩**

**原理:** 修剪路径并错开时间。

**步骤:** 新建合成，绘制一个圆形保留描边，添加修剪路径，调整开始和结束的关键帧，复制多个，错开时间（间隔可自行调整）。

**拓展应用:** 灵活度更高，应用范围比63和64更广一些。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/99f24cbc2c51e10f44f7e775a1499fbb_uayPM5YxLH.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/e1bc21836a9d9cb291a8e0223f67b8f9_NKTwBNMK0u.gif)

# **66.饼形修剪**

**原理:** 修剪路径。

**步骤:** 新建合成，绘制一个圆形，只保留描边，使描边充满整个圆形，添加修剪路径，调节开始的关键帧数值，最后为所有关键帧添加缓动。

**拓展应用:** 转场动画，场景切换等等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/e5daf87d27a713a510b5bb9aca2f8092_J7cLVgFbBq.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/8554d16fffe10c136e4db53517e46cc8_VD_gcQBzSX.gif)

# **67.流动线条**

**原理:** 修剪路径加蒙版。

**步骤:** 新建合成，绘制一个圆形，在内部复制多个，建立蒙版，然后添加修剪路径，复制一层，一层作为背景改变颜色，一层调节数值。

**拓展应用:** 可制作传输带等等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d3420115fd25bcfb222a61470d473d8c_ERB0jceijf.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/f2da9133f9d791252fe0f1036ea6aed9_FLYzsIPgnv.gif)

# **68.分形噪波**

**原理:** 分形杂色的应用。

**步骤:** 新建合成，新建纯色层，应用效果和预设中的分形杂色，形成噪波的形式。

**拓展应用:** 可模拟水，火，山脉等等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/b0a4e71147d388bc33ae524dec1eec07_dpfagArtnA.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/70074ece24327e7b82b02185c532d6f6_s3hnsZdby4.gif)

# **69.粗糙边缘**

**原理:** 粗糙边缘。

**步骤:** 新建合成，绘制一个圆形，在效果和预设中找到粗糙边缘（汉意为画笔描边），调整数值。

**拓展应用:** 增加粗糙感。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/4d1c2512392e5c716471e04cb217ba29_vVlAMNOryi.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/f177ffe4ebc3a257614cff1b26510596_MSi-FetDyJ.gif)

# **70.湍流置换**

**原理:** 效果和预设中的湍流置换。

**步骤:** 新建合成，绘制纯色层，在效果和预设中找到湍流置换并为纯色层添加，调整参数。

**拓展应用:** 模拟特殊效果时可以使用。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/a02c53a03dda7eb56b972a9013beb019__jQiAAfwJW.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/51bb35552d095a944c8703fc7fd70971_6G8oi-MiEW.gif)

# **71.噪声**

**原理:** 分形杂色与添加颗粒。

**步骤:** 新建合成，绘制一个纯色层，在效果和预设中找到分形杂色并为纯色层添加，分形类型为动态，在效果和预设中找到添加颗粒，拖拽到纯色层上，可以调节强度，速度等等。

**拓展应用:** 彩色或者黑白的效果均可制作。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d1e5d8e3788e91ce49fdb152e3e4d36f_EJqtrEQ5sm.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/69a757802cbcc6a45635cf81368cade7_fCP3lYaaka.gif)

# **72.随机路径**

**原理:** 为图形添加摆动路径。

**步骤:** 新建合成，绘制一个圆形，为路径添加摆动路径，调整大小，摆动时间的数值。

**拓展应用:** 可加入其它属性来模拟烟花效果等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1f69885e0fff1ccf0a605cccbb90ad4b_P-GDCFemVV.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/efcee4512cd5e891809e053acbf9695c_0xgoqCFCEI.gif)

# **73.雷电**

**原理:** 效果和预设中的高级闪电。

**步骤:** 新建合成，绘制纯色层，在效果和预设中找到生成-高级闪电并为纯色层添加，调节参数（如下图）。

**拓展应用:** 可制作闪电的效果来作为点缀。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/973ab42490d6823240d1fab001311d2c_0uZHRS8qsh.jpeg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/804969d7f87c787894ae6ecd8c634039_8veqCFrKfZ.gif)
