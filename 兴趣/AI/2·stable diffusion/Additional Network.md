上一期我们介绍了模型的融合和训练，如果能生成自己的模型，那将是一次巨大的飞跃。本期我们讲一下 Additional Network（简称 AddNet）这个插件，它能帮我们控制多个 LoRA 模型生成混合风格的图像。

### **一、下载和安装**

下载方式有两种，一种是在“**扩展-从网站安装**”输入 [github.com/kohya-ss/sd-webui-additional-networks](https://link.zhihu.com/?target=http%3A//github.com/kohya-ss/sd-webui-additional-networks) 就可以安装了，如果不行的话就自行下载压缩包解压放到 SD 的 extensions 目录下。

安装完之后一定**要重启 sd 进程**！仅仅应用更改并重启前端是不够的。之后我们可以看到选项卡上多了一个 Additional Network 选项：

![](https://pic1.zhimg.com/v2-16b638e292de7492fd16ff368e5c01cc_b.jpg)

并且类似于 ControlNet 在主页面有一个下拉框：

![](https://pic3.zhimg.com/v2-3c5fe5e259312a392dbdcab546f4fcce_b.jpg)

看起来有点复杂。鉴于网上资料约等于 0，我只能看项目源码的 Github，作者是个小日子，所以介绍页面英日混杂 WTF。不过幸好笔者自学过一点日语（君日本语本当上手），能 get 到大概的意思。

![](https://pic1.zhimg.com/v2-941b1ec245b7b4084df3be5b0174e71c_b.jpg)

AddNet 扩展允许在原始 SD 模型中添加一些网络（如 LoRA）来生成图像。目前仅支持 LoRA。这种添加是即时的，不需要模型合并。

> **注意**
> 
> LoRA 模型只有放到**extensions\\sd-webui-additional-networks\\models\\lora**目录下然后点击“刷新模型列表”之后才会出现。
> 
> 当然如果你将**models\\Lora**下的模型复制到上述目录会造成空间的浪费。我们建议是创建一个**符号链接**（不是快捷方式），把 models/LoRA 路重复利用。
> 
> 方法：以命令行模式打开 cmd  
> 输入：mklink /D {你的 sd 路径}\\extensions\\sd-webui-additional-networks\\models\\lora {你的 sd 路径}\\models\\Lora  
> 你看到这样带有箭头的文件夹就证明成功了：

![](https://pic3.zhimg.com/v2-9125753ad0b34893b707c6536b59ed42_b.jpg)

### **二、基础使用**

我们可以任意任意地组合最多 5 个不同的 LoRA 模型并设置它们的权重，权重范围-1~2。权重范围为什么不是 0~1 呢，为什么会有负权重？

我们用 hanfu 这个 LoRA 模型为例，看一下权重对画面的影响：

![](https://pic1.zhimg.com/v2-5b8b277b42b3faef4b4ffc928ffb54f0_b.jpg)

可以看到大于 1 和小于 0 的权重的画面都是噪点，根本无法使用。在 0~0.5，LoRA 模型才真正发挥作用，我们在这个范围进一步细化：

![](https://pic4.zhimg.com/v2-8a8d331218073a44879ed61a8f0d67ab_b.jpg)

对于 hanfu 这个模型最佳权重在 0.5 左右。  

下面我们来生成一张胡桃图像，使用 anything-v 4.5 这个模型，我们希望画面的背景是中国古建筑。为此我专门下载了 hutao 和 qing 两个 lora 模型（可以自行去 C 站下载）。  

咒语 (控制随机数种子不变)：  

```text
1girl, solo, :d, bangs, sitting, hands on head, black_hair, long hair, blush, small breasts, brown_hair, loose clothes, short pants, long hair, long_sleeves, side view, open_mouth, red_eyes, sitting, smile, (thin thighs: 1.4) , closed thighs, hat, white legwear
```

**需要注意的是对于有触发词的 LoRA，需要将触发词加到 prompt 中。**   

**(1) hutao 权重 0，qing 权重 0**

生成的图像如下图所示，没有任何“胡桃”和“中式古建筑”的迹象。

![](https://pic3.zhimg.com/v2-3adc2ceb66e79f8bb00476698cb0d966_b.jpg)

**(2) hutao 权重 0.5，qing 权重 0**

可以看出是胡桃嗷，但是背景不是我们相要的。

![](https://pic1.zhimg.com/v2-6447c4d9f4c892f0806475ab6f94ba90_b.jpg)

**(2) hutao 权重 0.5，qing 权重 0.5**

这次完美了，一张坐在古楼里的胡桃。

![](https://pic4.zhimg.com/v2-7481534adc34537d3565033bc6bd8277_b.jpg)

可惜的是 AI 不会画星形瞳孔，不然就更像惹~

### **三、高级使用**

现在我们有这样一个需求，画面中有两个人，一个人是 A 风格，另一个人是 B 风格。如果我们想单纯依靠文生图或者图生图是很难做到的。

但是借助 AddNet 我们就很容易实现这些。点击“Extra args”下拉框，我们就能看到一个掩膜导入窗口：

![](https://pic1.zhimg.com/v2-bed96cbc7565795f5f77bffdc940981c_b.jpg)

掩膜中纯红色的区域表示第一个 LoRA 模型作用范围，纯绿色区域表示第二个 LoRA 模型作用范围，纯蓝色区域表示第三个 LoRA 模型作用范围，黄色区域表示第一个和第二个 LoRA 模型的重叠区域，以此类推。  

下面的实验我们用 ControlNet 来控制人物姿势，没有 LoRA 情况下得到的图像：

![](https://pic3.zhimg.com/v2-d7aabbdaf85f803c89afb7386ec19752_b.jpg)

有 LoRA，没有掩膜得到的图像：  

![](https://pic2.zhimg.com/v2-b66b312e8f9805bc745a7b94d02b55d1_b.jpg)

有 LoRA 和掩膜得到的图像：

![](https://pic4.zhimg.com/v2-6d6072df9944be5ca84ab30f8f83f9ab_b.jpg)

![](https://pic4.zhimg.com/v2-b683966b2ac4156a3e341cc45181d5e7_b.jpg)

左边的女孩用的是一种风格，右边女孩用的是另外一种风格，在重叠区域也做到了很好的过渡。

### **四、总结**

AddNet 可以让我们非常轻松地融合多种 LoRA 模型。但是目前该功能仍在开发之中，有诸多不完善的地方，如果功能完善一些也是非常不错的!

本期就到这里啦。下一期的话讲什么还没想好，请持续关注哟~

我是迹寒，下期再见！

参考资料：

[https://github.com/kohya-ss/sd-webui-additional-networks](https://link.zhihu.com/?target=https%3A//github.com/kohya-ss/sd-webui-additional-networks)

**往期内容**

[AIGC初体验——Stable Diffusion（四）模型融合与训练(LoRA)](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzkxMTMzMTIwNw%3D%3D%26mid%3D2247484494%26idx%3D1%26sn%3D842d9c31a3c85ae45c936e25474aada6%26chksm%3Dc11c9ea6f66b17b0cc2d4a387ec4c282e2cb7c3658047fcdbd9edbf354fdd48aa39f4a7d0710%26scene%3D21%23wechat_redirect)  

[AIGC初体验——Stable Diffusion制作超棒图像（三）ControlNet功能](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzkxMTMzMTIwNw%3D%3D%26mid%3D2247484454%26idx%3D1%26sn%3D3817bbe454936bea9ca2588b6d1ab1e2%26chksm%3Dc11c9ecef66b17d8196737fc684d6bd5419d181000c1ae6081f56f19398b9f7b9caddf3bd2d4%26scene%3D21%23wechat_redirect)

欢迎关注公众号【**迹寒编程**】，了解最新 AIGC 资讯！