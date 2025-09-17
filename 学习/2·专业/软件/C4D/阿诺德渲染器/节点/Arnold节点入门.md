# Arnold节点入门

<https://www.zcool.com.cn/article/ZNTU4MjM2.html>

# **一、节点这么多，怎么连**

先后接触过 Cycles，RedShift 和阿诺德（Arnold），发现在材质怎么连这个事情上，都大同小异。它们的材质节点连接，遵循下面的流程：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01cd3a59c0e89ea801212fb7a69851.jpg@800w_1l_2o_100sh.jpg)

*   **输入信息：** 一些基本信息的输入（这里和下文说的信息，也可以理解为数据）。

*   **处理：** 对输入信息的进行处理，调整，让它输出合适值给下一个节点。

*   **Shader：** 它是决定让信息控制材质的哪个属性。比如控制材质的粗糙度，控制材质的漫反射颜色。这个真不知用中文怎么说，叫 “着色器” 还是觉得不够贴切。

*   **材质：** 表面，置换，体积等。用得最多的是表面（Arnold beauty）。

连接材质节点的时候，就是按照上面的流程连的，像套公式一样，简单。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01d6ba59c0e94ea801212fb75a6e56.jpg@800w_1l_2o_100sh.jpg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/0156b659c0e94ea8012075341b045d.jpg@800w_1l_2o_100sh.jpg)

当然了，还有一些较为复杂的材质。由多个 Shader 混合后再输出到材质表面，包含有多个

“输入→处理→Shader” 的流程。

比如下面这个：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01c8c859c1008ea801207534454ae2.jpg@800w_1l_2o_100sh.jpg)

看晕了吧。但无论多复杂，总的来说，都离不开 “输入→处理→Shader”。

了解材质节点的流程又怎么样，我还是不懂得材质节点都有哪些，有什么功能。莫急，请看下一节。

# **二、材质节点的分类**

材质节点那么多，但是看了上面的流程公式，按照在流程公式中的位置来分类，就简单多了。下面就是这么分类，并列举一些常用的节点做介绍。

## **输入的节点**

### 贴图

> 作用：导入一张图片。

image 节点，RedShift 的 texture 节点，Cycles 的 image texture。

### 程序化纹理

> 作用：根据输入的参数来生成的纹理。

noise 节点，噪波。这个不解释，需要注意的是不同渲染器的 noise 差别蛮大的。

curvature 节点，物体凸起或者凹陷的地方生成白色或者黑色，可以用来做物体边缘磨损的样子。

Facing-ratio/Fresnel 节点，菲尼尔，根据光线 / 视线和物体表面的夹角生成白色或者黑色。

wireframe 节点，线框。有布线的地方生成白色或者黑色。

ambient\_occlusion/AO，物体相交靠近的地方生成黑色。有些文档把 AO，Fresnel 叫做 Shader，这里根据用途，把它们归为程序化纹理（procedural texture）这一类。

### 对象信息：

跟对象本身直接相关的信息，比如坐标位置，粒子的年龄，TFD 的通道之类的。user\_data 分组里的所有节点，xparticles 节点，Cycles 里的 Object Info。关于这些节点，我没怎么用过，也了解得不多，只知道它们存在而已。可以用 data，info，object 或 attribute 作为关键词搜索出来了。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01573959c3b7d0a801218e18de743d.jpg)

## **处理的节点**

对贴图的调整，对材质的调节很多都发生在这个环节。

### 图片 / 纹理的处理

ramp\_float：曲线调整，最常用。RedShift 里对应是 Color Change Range 节点，但不是用曲线调的，不太好用。

color\_correct 节点，调节色相饱和度对比度之类的。

color\_jitter 节点，颜色抖动，让颜色在一定的色相 / 饱和度 / 对比度范围内随机变化，很有用的节点。常和克隆一起使用，制作出五彩斑斓的颜色。

layer\_color ，多个颜色的混合，可以选择混合模式，不透明度（熟悉 PS/AE 的小伙伴终于找到一丝丝亲切感了）。RedShift 里对应的是 Color Composite，Cycles 里的是 MixRGB，但都只能混合两种颜色。

### 各种转化类的

数据转颜色，ramp\_rgb 节点，Cycles 里的 Color Ramp 节点。还有 blackbody 节点，输入一个温度值，输出颜色。

####

### 其他的转化类节点

RBG，矢量，浮点的相互转化，矢量的分离等。

数学运算类：加减乘除，三角函数，幂运算什么的。

## **Shader 节点**

一般对应渲染器里的万能材质 / 标准材质。

standard\_surface 节点，RedShift 里的 RS Architectural，Cycles 里的 Principled BSDF。还有一些特殊的材质，比如 Arnold 的毛发 standard\_hair。不管是哪个渲染器，最好熟悉这个节点里的每一个参数，**这是基础的基础**。

## 其他节点

layer 节点：可以认为是专门对 shader 进行混合处理的节点。对多个 shader 节点进行混合后输出，根据贴图来控制 shader 层的混合强度（相当于 PS 里的蒙版，AE 里的遮罩），做复杂材质必不可少。以前的阿诺德可以用 layer\_color 来混合材质，新版的不能那么用了。在 RedShift 里对应的是 Material Blender，Cycles 里的是 Mix Shader。

[bump](bump.md)

现在再回过头来看刚才那张图：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01efce59c10078a801212fb7380537.jpg@800w_1l_2o_100sh.jpg)

现在看是不是没有那么晕了呢。

再回顾一遍材质节点流程公式。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01addf59c0eb0ba801207534fdb047.jpg@800w_1l_2o_100sh.jpg)

如果已经了解上面的材质节点，但是怎么用它们来做出一些看起来很牛逼的材质效果呢。虽然我不知道怎么定义牛逼的材质效果，但是下一节的内容，或许可以帮到你。

**三、例子**

在做材质的时候，**根据材质的特征，把材质分为不同的层的来看待，逐一实现，再混合。** 下面的例子就是按照这个思路来做的。这里说的层在节点里对应的是 shader，一般指 standard\_surface。

例子来自 mograph+ 的教程 Developing Realistic shaders in Arnold 。并按新版的阿诺德（C4DtoA v2.1.1）进行一些小调整。

**第一个例子**，小飞机，也是教程里的第一个内容，最基础最简单。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01f4ed59c0ebb0a801212fb7627dbf.jpg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01d08d59c0ebd6a801212fb73997d7.jpg@800w_1l_2o_100sh.jpg)

两个层的混合（用 layer 节点）。两个层除了高光的粗糙度不同，其他参数都一样。用菲尼尔来控制粗糙度小的这层的混合强度（layer2 alpha）。这里的 utility 节点，shade mode 选择  ndoteye 后，就跟菲尼尔节点（facing\_ratio）差不多。不同的是，utility 只作用于摄像机光线，而 facing\_ratio 作用于所有光线，官方文档是这么说的。 &#x20;

对比下 RedShift 的节点。这里我没有让贴图和 noise 混合，至于原因，RedShift 的 noise 我用不好，别笑，真的就是。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01df9f59c0ec37a80120753416bfb7.jpg@800w_1l_2o_100sh.jpg)

**第二个例子**。老式电话机。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01792759c0ec7da801207534dc55cd.jpg@800w_1l_2o_100sh.jpg)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01e2b559c0ec93a801212fb716ba47.jpg@800w_1l_2o_100sh.jpg)

这个例子，把 **“分层看待逐一实现，混合输出**” 的思路发挥得淋漓致尽。一共包括四个层：两个层表现不同的高光，边缘磨损后漏出来的材质，白色的污泽。

curvature 节点在制作边缘磨损效果的时候，非常方便给力。

下面是 RedShift 的节点。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01233459c0ecd3a801207534b70f52.jpg@800w_1l_2o_100sh.jpg)

心里默念一遍 **“分层看待逐一实现，混合输出**”。

一定要这样吗，当然不一定。在做到教程里的保龄球的时候，不知道是电脑抽筋还是我抽筋了。 RedShift 的材质混合节点 Material Blender 失效了，死活出不了预期的效果。于是我决定，只用一个层来实现。

教程里人家做出的效果是这样的：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01c22359c0ed48a80120753440244b.jpg@800w_1l_2o_100sh.jpg)

而我做出来的却是这样的：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01ea4459c0ed75a80120753413a1b7.jpg@800w_1l_2o_100sh.jpg)

明明想要一个沾满尘土的保龄球，而你却帮我擦干净了。不对，是尘土没法粘上去。。。

我不服，把参数调大，要大要对比要突出……

然后成了这样：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01460559c0eda3a801212fb725e9f8.jpg@800w_1l_2o_100sh.jpg)

而此时我的材质节点是这样的：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01e29e59c0edbfa801207534777b45.jpg@800w_1l_2o_100sh.jpg)

你看得懂吗，我也看不懂啊，差点让我连出心理阴影了。

用 “分层看待逐一实现，混合输出” 的话，是这样的：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01396459c0edf1a801212fb7cdb2b4.jpg@800w_1l_2o_100sh.jpg)

真是没有对比就没有伤害！这里没有针对哪个渲染器，而是说这个思路，思路思路思路。实际上只用一个层，也是可以实现上面教程中的效果的。但后来我也没有去弄，因为用贴图之后 RedShift 的 IPR 反应比较慢（可能是电脑配置的原因），Color Change Range 节点又不好调。 &#x20;

**总结** &#x20;

一张图一句话。

**一张图：**&#x20;

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/01437859c0efb6a801207534c3b7b2.jpg@800w_1l_2o_100sh.jpg)

**一句话：**&#x20;

**“分层看待逐一实现，混合输出”**

当有一天你发现这句话是有漏洞的时候，说明你已经是老司机了。如果你等不了那么久也没关系，现在我就给你一个成为老司机的机会，看题！！

请问：上面的两张图，小飞机，和电话机，哪个是用阿诺德渲染的，哪个是用 RedShift 渲染的。

答对说明你就是拥有超高分辨率像素眼的老司机。 &#x20;

欢迎留言。到底上面两张图：**小飞机和电话机，哪个是阿诺德渲染，哪个是 RedShift 渲染的呢？** 过一段时间后在留言公布答案。看看你是不是像素眼老司机，请留言。

[https://www.zcool.com.cn/article/ZNTU4MjM2.html](https://www.zcool.com.cn/article/ZNTU4MjM2.html "https://www.zcool.com.cn/article/ZNTU4MjM2.html")
