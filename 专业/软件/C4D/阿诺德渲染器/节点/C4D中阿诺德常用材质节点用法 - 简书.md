# C4D中阿诺德常用材质节点用法 - 简书

# C4D 中阿诺德常用材质节点用法

<https://www.jianshu.com/p/f3d77b8e9838>

\[

![](https://upload.jianshu.io/users/upload_avatars/1361504/13b2cc7d-e1de-4a01-a993-4a65cd27aa0c.png?imageMogr2/auto-orient/strip|https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/webp)

]\(/u/f4869f6b4883)

[九九重天](/u/f4869f6b4883 "九九重天")关注

0.2092020.06.01 20:36:29 字数 730 阅读 973

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-b681786fb17ee5a5.png)

HFIWTIF09GS\ \_\_ 8PHXOJJ{YX.png

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-e3409645ea82f2a0.png)

I7X6T\_CLU0\$\$L6)PFY4(\_ ZR.png

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-6d4dcf174e4db716.png)

IEJJJ4N3\~EZPMK\_KBT52{Q3.png

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-3850d9e48e681859.png)

IY}6L\\\~\~X59\_BMP96)L60WFM.png

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-24abdece8435c0ef.png)

image.png

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-89feebec1eee26f9.png)

image.png

阿诺德渲染卡通三步走 &#x20;
1：需要平行光； &#x20;
2：渲染设置：2.1 材质球勾选渲染边缘，2.2 渲染设置：调整 “默认过滤器类型：contour\_filter”，后接参数是控制线的宽度。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-4c70ee13d217a99c.png)

image.png

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-b2baaa8b2b99f676.png)

image.png

这个度数可以控制：边缘什么角度时可见。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-ceb441d026ddf5fb.png)

image.png

toon 材质： &#x20;

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-47c2ec0acd2ace01.png)

image.png

基础中：色调映射，用渐变控制高光、中间调和阴影。 &#x20;

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-f8f489f3fed3568f.png)

image.png

基础中：颜色：可以叠加整体的纹理。 &#x20;

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-71ca21f6b929e342.png)

image.png

镜面控制反射：一般卡通材质不需要

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-ca2b1b284dfb8f44.png)

image.png

阿诺德标签下，自适应细分：是基于摄像机跟物体的远近，远时减少细节。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-bfda83c8227189d9.png)

image.png

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-50ec9265feb5da60.png)

image.png

法线置换：根据灰度图产生上下方向的变化

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-28af079840bb0ae2.png)

image.png

失量置换：可以各个方向产生变化。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-0623d6e3f6d72567.png)

image.png

如何加载 sb 的成品材质球

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-657fce2a00472a1f.png)

image.png

快速渲染物体 id 通道：utility 材质：切换 flat+object 即可

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-8d67b1223be6590b.png)

image.png

阿诺德 布尔材质 / 切片材质：clip\_geo

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-eaa5f74d6a9f4d9e.png)

image.png

可以连接任何其他材质，用于显示切片材质；

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-1afd05fda771d243.png)

image.png

多功能数据输入类型节点：value：颜色 / 数据 / 浮点 / 向量等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-ef5052372c395ff3.png)

image.png

颜色分离节点：rgb 分离颜色通道出来，

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-c22af3e2270ae0c7.png)

image.png

分离的通道可以合成还原 rgb：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-17539401bcbd84bb.png)

image.png

状态节点：转 rgb 信息。 &#x20;

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-dff6b125fa3f2d97.png)

image.png

random：可以控制随机颜色。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-1bd7fa8d3185c790.png)

image.png

add：快速叠加图片：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-59452a66f0928828.png)

image.png

快速切换材质：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-c6b477811d5ed8bb.png)

image.png

uv 控制变化：常用 uv 缩放

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-1803abf23a60b0b3.png)

image.png

图像控制器中：可以控制 uv，可以控制单通道输出，RGB 通过 0、1、2，依次切换。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-39d5a5466b0cf158.png)

image.png

顶点贴图：配合域可以做消散动画；

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-264f8ce3a6235da1.png)

image.png

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-e91ab5cddfa399e9.png)

image.png

几种噪波类型：C4D 噪波类型种类最多好用。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-bbb08b7d89c062c5.png)

image.png

读取用户数据：克隆加个随机效果器，改变颜色，可以读取到随机颜色值。 &#x20;
可以自己添加用户数据。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-9db4f6d76d5f56fc.png)

image.png

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-6b2c1a52e5d739cc.png)

image.png

做体积光用的

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-03c5be0b62a4506c.png)

image.png

阿诺德常用快捷键：alt（阿诺德）+w 接 N 键，新建材质球

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-c205aceed699ddbd.png)

image.png

节点面板：ctrl+tab：快速调出节点搜索面板：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-62c4e0ff5051fa5c.png)

image.png

节点面：alt+w： &#x20;
接 1：快速链接当前材质到预览窗口； &#x20;

接 2：到置换 &#x20;
接 3：快速预览 &#x20;
接 A：快速对其所选的节点（美观用） &#x20;
接 R：开启 ipr 或关闭；

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-c32814ead4169d42.png)

image.png

阿诺德的 GPU 渲染流程：切换至 gpu，缓存 GPU，取消 tx 材质生成，

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-76dfb48197ef801d.png)

image.png

； &#x20;
做完以上后，第一次场景渲染也会预缓存，原因是阿诺德和 CPU 和 gpu 采用不同的算法，需后台进行转化。

灯光阴影控制： &#x20;

1、大气加个环境，

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-d6ba3b51d2459b9e.png)

image.png

2、灯光→细节→加个灯光（gobo）材质 &#x20;

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-1756d8c287b26b0f.png)

image.png

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-344207c34f669a16.png)

image.png

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1361504-8ce483e271e3d15c.png)

image.png

通过一张黑白图即可丰富投影细节。

5 人点赞

[阿诺德](/nb/46057152 "阿诺德")

"小礼物走一走，来简书关注我"

赞赏支持还没有人赞赏，支持一下

\[

![](https://upload.jianshu.io/users/upload_avatars/1361504/13b2cc7d-e1de-4a01-a993-4a65cd27aa0c.png?imageMogr2/auto-orient/strip|https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/webp)

]\(/u/f4869f6b4883)

[九九重天](/u/f4869f6b4883 "九九重天")

总资产 4 (约 0.22 元) 共写了 1.1W 字获得 80 个赞共 87 个粉丝

关注&#x20;

[https://www.jianshu.com/p/f3d77b8e9838](https://www.jianshu.com/p/f3d77b8e9838 "https://www.jianshu.com/p/f3d77b8e9838")
