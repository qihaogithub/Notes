# bump 

<https://www.jianshu.com/p/af1fc1c13cd4>

#### Bump mapping 凹凸贴图

*   利用凹凸贴图可以模拟不完美表面，比如凹痕、划痕等。与置换贴图不同，凹凸贴图并不会改变几何体的结构，只是在视觉上进行模拟；

*   有两种模式：**bump2d**和**bump3d**，两者功能相似，区别在于使用的是2D贴图还是3D贴图；

接下来看一下具体操作： &#x20;
1、新建一个Arnold着色器网络：创建→着色器→Arnold Shader Network，创建成功后会自动跳出着色器网络编辑器。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-3d804632e90737bd.png)

创建着色器网络

2、将材质赋予给球体和立方体。在这里，我们用躁波（noise）来控制表面凹凸。 &#x20;

在着色器网络中新建standard\_surface节点（会自动连接到Arnold Beauty）→新建bump2d节点（选择Main>Geometry>normal），连接到standard\_ surface节点→新建noise节点（选择Bump map），连接到bump2d节点：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-f3f74ac2ab1281b8.gif)

创建bump2d

**p.s.新旧版本的Arnold节点连接逻辑有所不同，旧版中的节点连接顺序是：standard→noise→bump→Arnold Beauty；新版：noise→bump→standard\_surface→Arnold Beauty**。新版中材质节点连接逻辑大多都是standard\_surface连接到Arnold Beauty，之后跟随其他节点，各节点参数也有所调整，这里不多展开说了，后面遇到再仔细讲解。各位童鞋自己打开软件看看就会很明白。多试，多练。

3、建立好所需个节点之后，可以根据需要再调节相关参数。 &#x20;

选中standard\\\_surface节点，可以调节材质，颜色等，首先将材质调整为红色外观：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-39bb442eb060fd83.png)

standard\\\_surface节点属性

这里我们是要用躁波来呈现一种表面凹凸效果，从上图可以看出凹凸效果不明显，所以要再通过调节各项属性参数来实现。选中bump2d节点，调出其属性，将Bump height调节为5cm：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-edd577a7d1ab52c5.png)

bump2d节点属性

然后再调节noise节点属性：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-14dc60fa9668a92d.png)

noise节点属性

属性调节好之后渲染结果如下：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-0951782735256967.png)

渲染图像结果

4、除了用noise控制凹凸，也可以加载一张图片作为凹凸贴图（白色突起，黑色凹陷）：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-f7667c30a1339cad.gif)

imag控制凹凸

#### Normal map 法线贴图

*   普通灰度贴图只能在上下两个方向产生凹凸，而法线贴图基于RGB通道，凹凸方向更加随机；

*   可以使用bump2d贴图直接加载法线贴图（替换image节点图片），不过最好还是使用normal\\\_map节点；

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-47993786ab679688.gif)

normal\\\_map法线贴图，方法与bump2d类似

*   可以根据需要选择法线贴图的模式：

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-7f762b8221016ab8.png)

    法线贴图连接模式

*   调节图片在法线贴图中的属性：

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-146bdf48a0d25274.png)

    选中image节点即可调出属性菜单

*   法线贴图部分属性不同参数示例：

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-1ac016166110b090.png)

    Mipmap Bias

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-20ed00bd5eb4c7de.png)

    Multiply

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-157a9befe2283714.png)

    Offset：均匀的变暗或减轻纹理或色彩

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-a6f20a571534f4cd.png)

    Offset U

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-9ec97920e843f6de.png)

    Offset V

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-2583420dbc919588.png)

Wrap：控制图像在大表面的重复模式

**“文件”模式**是指，使用其本身的编码设置，这种模式只适用于OpenEXR文件（视觉效果行业使用的一种文件格式，适用于高动态范围图像。该胶片格式具有适合用于电影制作的颜色高保真度和动态范围。OpenEXR 由 Industrial Light and Magic 工业光魔开发，支持多种无损或有损压缩。OpenEXR 胶片可以包含任意数量的通道，并且该格式同时支持 16 位图像和 32 位图像）；这种模式能够有效的保存当贴图没有进行后期手动校正时，该如何包裹对象表面的信息；在某些情况下，“文件”模式能够防止图像产生杂色。 &#x20;

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-724c7de754a8206b.png)

File mode “文件”模式示例，分别使用不同模式出现的情况，第三个图像使用“文件”模式后，比较第二张图像，可以明显的看到中间小圆点消失了

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-6270acbdb5ed7b2e.png)

ScaleU/V:等比例增加图像数量

#### Subdivision 细分贴图

这里用一个简单的立方体来做演示。 &#x20;

1、首先，将立方体C掉（细分曲面，快捷键C）。创建一个Utility着色器，将其赋予立方体。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-eb49f719087cc0b7.png)

创建→Arnold→Surface→utility

2、双击utility调出属性菜单栏，将着色模式（Shade mode）改为lambert，叠加模式（Color mode）改为polywire（这时可以在IPR Window中看到对象的边框了）：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-5eda3bdeab1efe69.png)

调整utility属性

3、给立方体添加一个Arnold参数标签，看一下细分设置（Subdivision）。

*   **类型**（Type）：none/catclark/linear。

*   **迭代**（Iteration）：迭代定义了细分次数，前提是开启一种细分类型。细分类型为linear时，提高迭代值会增加多边形的数量但不会变圆滑，每细分一次，一个多边形就会变为四个多边形，但是模型的结构（外形）并没有改变；细分类型为catclark时，不仅会增加多边形的数量，还会使模型变平滑； &#x20;

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-ba02467d3b577b3d.png)

    不同细分类型迭代对比

*   **自适应度**（Adaptive metric）：用于定义对象的细分级别是否随着距离远近而变化（比如近景细分级别较高，远景细分级别较低）。有两种模式：edge\_length/flatness。edge\_length使用边的长度进行判断，flatness使用面的曲率进行判断，若设置为auto，当对象没有使用置换贴图时，使用flatness模式，反之使用edge\_length，大部分情况下使用auto即可； &#x20;

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-4a152677196fe6d0.png)

    Adaptive metric

*   **自适应度误差**（Adaptive error）：配合自适应度使用，提高自适应误差，可以看到当镜头拉远，球体的细分就会降低，因为远景对象是不需要呈现细节的。同样的若拉近镜头，球体的细分就会提高，这是一种很好的场景优化方式。如果将自适应误差将为0，那么细分级别就不会随着距离进行变化了；（同样道理的还有之前讲过的Mip-mapping）；

*   **自适应空间**（Adaptive space）：有raster（栅格）和对象（object）两种模式，尽量使用栅格模式，当场景中有实例对象时切换为对象模式；

*   **Dicing camera**：可以定义控制自适应细分的摄像机，也就是说根据对象距离该摄像机的远近控制细分值。如果一个对象的细分级别在不断变化，自然会发生闪烁，该选项可以解决运动场景中因自适应细分产生的闪烁问题（新版中去掉了这一选项，智能优化为最佳效果）；

*   **平滑UV**（UV smoothing）：用于定义当对象被细分时，UV如何固定——固定转角 Pin\_conters/固定边缘Pin\_borders/完全固定 linear/完全不固定 smooth； &#x20;

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-49b89478093cdfef.png)

    UV smoothing

*   **平滑切线**（Smooth targents）：当对象上有各向异性高光时，高光可能会产生锯齿，可以通过开启Smooth targets来解决这个问题； &#x20;

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-ac1d9f4952008f2e.png)

    Smooth targets

#### Displacement mapping 置换贴图

置换贴图可以实现真实的置换细节，与凹凸贴图不同，凹凸只是视觉欺骗，而置换是真的会改变模型外形。置换分两种类型——法线 normal/向量 vector，**法线置换**是传统的置换方式，会根据灰度贴图产生上下变形，而**向量置换**会在多个方向上产生变形

#### 法线置换 Normal\\\_displacement

还是用上一个立方体来做演示 &#x20;
1、创建一个Arnold标准曲面（Create→Arnold→Surface→standard\\\_surface），打开阿诺德网格编辑器（Arnold Shader Network Editor）；

2、新建一个normal\_displacement节点，链接到Arnold Dispalcement端口，接下来定义一张置换贴图（创建image节点，手动连接到normal\_ displacement节点，选择Main>Displacement，或快捷键：先按下Alt＋W，松开在按下T，选择Main>Displacement），调整scale参数为0.1，因为之前模型分段不足，所以调高Arnold参数标签细分属性中迭代值为6（选中Arnold标签调出属性）：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-b04d63cceafcfcf6.png)

用到的贴图

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-255821ce292b7773.png)

Displacement mapping演示，P.S.要获得置换细节，模型的分段一定要足够

*   **Scale**：控制着置换的强度（高度），正值向外，负值向内（尽量使用32位贴图以获得更好的置换结果）；

*   **标量值为零**（Scale zero value）：定义了置换高度为0时的颜色值。默认0代表黑色不发生置换，白色往外置换；设置为0.5那么50%灰色不发生置换，黑色向内置换，白色向外置换；设置为1，那么白色不发生置换，黑色向内置换。

如果Arnold Displacement端口未显示，可单击红色按钮调出：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-fc2864f7ad00b224.png)

端口选择

3、如果想要保持外形不变的话，将细分类型改为linear。选择linear后会发现置换有点问题，可以通过调整**边界填充**（Bounds padding，选中Arnold标签→置换（Displacement）→边界填充（Bounds padding））来解决： &#x20;

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-0aad1b9ce0fcca7e.png)

Bounds padding不同值对比

Bounds padding值可以扩展模型的边界框以囊括置换后的模型，可以将其理解为一个容器，变大才能盛下置换后的模型。谨慎提高该值，因为会增加渲染时间。如果要获得更多置换细节，可以继续提高细分值，不过也要谨慎。

4、接下来看一下Arnold参数标签置换栏的参数：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-102801367ddb07f7.png)

Dispalcement参数

*   **高度**（height）：与Scale配合使用，也控制着置换的高度；

*   **标量值为零**（Scale zero value）：尽量使用置换贴图的Scale zero value，不要修改这里的参数；

*   **自动凹凸**（Auto bump）：开启可以获得更多的置换细节，该参数会将置换贴图中较小的高频出现的图案应用到凹凸通道，这样就无需设置较高的细分值，也可以得到这些小的细节，建议尽量开启该选项，尤其是使用法线置换时。 &#x20;

#### 向量置换 vector\\\_displacement

与法线置换贴图不同，向量置换贴图可以在任意方向对模型进行置换。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-1ef163883168ec21.gif)

ear-vector-displacement

1、继续使用上面的场景来做演示，隐藏立方体，新建一个平面，C掉，添加一个Arnold参数标签，提高细分值（Subdivision→类型 Type：catclark，迭代 Iterations：5）。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-69ec9b912c2ebf32.png)

2、创建一个新的standard\_surface着色器，添加一个向量置换节点（vector\_ displacement），将其链接至置换端口（同法线置换创建方式）；给向量置换属性（不是置换属性）加载一张贴图（快捷键Alt+W→T，Main-vector\_displacement）；修改向量置换参数：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-d9ef6c66c9ab59bf.png)

注：这个设置不是固定的，要与你生向量贴图时的设置一致

得到一个比较完美的渲染结果：

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-aa26e86af7f774c8.png)

渲染结果参考

3、向量置换节点参数：

*   **Scale**：同法线置换；

*   **向量编码**（Vector encoding）：absolute模式针对16/32位图像，signed模式针对8位图像（这两种模式并无明显区别，可自行尝试）；

*   **向量空间**（Vector space）：根据生成贴图时的设置，可以选择word/object/tangent三种向量空间； &#x20;

    ![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/6534305-5c2287590f65843c.png)

    其他参数并不是很重要，不做过多讲解。
