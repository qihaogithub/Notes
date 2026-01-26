用到 XYZ plot 脚本验证各种 LoRA 模型在哪个权重值的表现较佳。

![](https://i0.hdslb.com/bfs/article/e177079af4dc2b840aceaaf84c32f1c357b6f880.png@942w_392h_progressive.webp)

## 方法一

还是以测试 LoRA 模型为例，我们把自己训练出来的 LoRA 模型放入 novelai-webui\\models\\Lora。我们炼制的模型训练了 5 轮，生成了 5 个 LoRA 模型，注意编号为 000001 到 000005，下面有用。

![](https://i0.hdslb.com/bfs/article/1a07c9243deabb13da9324ec536c9e497f32c01e.png@942w_642h_progressive.webp)

然后打开 Stable Diffusion，基本操作先来一遍，选模型、输入提示词模版、再使用下 LoRA（不懂的可以去看本人同名头条主页《Stable Diffusion 人工智能绘图教程（从安装到精通）》合集的入门教程）。如下图所示。

![](https://i0.hdslb.com/bfs/article/f34dcabd1f9ea8abcdb19ff14bacfb0d1d929399.png@942w_582h_progressive.webp)

**重点来了！**我们点击 LoRA 模型会自动把<lora:y_v1-000001:1>提示词写入输入框。

提示词前面序号代表我们炼制的模型序号，有 000001-000005，冒号后面的 1 代表权重值为 1，我们可以设置为 0.1 到 1 之间的任何数字。**这时候我们把模型序号（NUM）和权重值（STRENGTH）这两个值设为变量，则提示词可以改为<lora:y_v1-NUM:STRENGTH>。** 

![](https://i0.hdslb.com/bfs/article/bccc89e6f2d0559705ea8b879899e571c3d2c5ad.png@942w_296h_progressive.webp)

下拉在最下面的脚本中选择 XYZplot 脚本。

![](https://i0.hdslb.com/bfs/article/fa389dc100a63b23d02e9c98604c62e01deafcb5.png@941w_350h_progressive.webp)

X 轴类型和 Y 轴类型我们都选择“提示词搜索/替换”（Prompt S/R）。

![](https://i0.hdslb.com/bfs/article/018f28f0508a3fdad06b2cbe11048e0b5389e083.png@942w_492h_progressive.webp)

然后 X 轴值输入 NUM, 000001,000002,000003,000004,000005，Y 轴值输入 STRENGTH, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1

**原理其实就是：在提示词中搜索 NUM，然后依次替换为 000001……000005，在提示词搜索 STRENGTH，然后依次替换为 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1，这样就形成了 XY 轴不同数值图表。** 

![](https://i0.hdslb.com/bfs/article/5514ada1a8c05c8e74291faa4e99ce0cee8a7e3b.png@942w_632h_progressive.webp)

设置完毕，点击最上面生成，即可以生成对比图。通过此对比图，我们可以检测对比出 5 个 LoRA 模型在不同权重下的表现，以此来选出较佳模型和较好表现的权重值。

![](https://i0.hdslb.com/bfs/article/de230ed8171434592dc95b58826e2aebb85114d5.png@942w_945h_progressive.webp)

## 方法二

还是以测试 LoRA 模型为例，我们把自己训练出来的 LoRA 模型放入 novelai-webui\\extensions\\sd-webui-additional-networks\\models\\lora

![](https://i0.hdslb.com/bfs/article/e819dc720b11dcd48490efdde9d7b5419831e0e0.png@942w_911h_progressive.webp)

刷新回到 Stable Diffusion，在文生图界面下方找到可选附加网络（LoRA 插件），点击启用。**先点击下方刷新模型列表**，然后随便选择一个 LoRA 模型。

![](https://i0.hdslb.com/bfs/article/8aa8d61250cde0c60c36271733f0169341aed1df.png@932w_1608h_progressive.webp)

下拉选择 XYZplot 脚本，X 轴类型选择“可选附加网络模型 1”（AddNet Model 1）。

然后点击小黄书图标可以看到所有可用的 LoRA 模型，我们选择我们需要的模型，其他的删除即可（注意这里是文本，不需要的直接删除）。

![](https://i0.hdslb.com/bfs/article/9b6cb3803b132c20d2c950113aa0dfd3ef78c9c1.png@942w_1145h_progressive.webp)

然后设置 Y 轴类型为“可选附加网络权重 1”（AddNet Weight 1），值输入为：0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1

（与方法一相比，去掉了 STRENGTH）

![](https://i0.hdslb.com/bfs/article/52040a8cf0f7c25b658a0e82e9de4b168ceeff53.png@942w_720h_progressive.webp)

设置完毕，点击最上面生成，即可以生成对比图。
