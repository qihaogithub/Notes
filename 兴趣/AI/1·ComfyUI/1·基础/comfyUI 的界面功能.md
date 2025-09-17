

![](https://pic1.zhimg.com/v2-60d0b56db149817190b0d65ea0098f64_b.jpg)

上面就是 comfyUI 的工作界面。主要是两个部分。一个是中间的工作流界面，一个是右下角的设置界面。

工作界面这里以基础的文生图流程以转换的思路进行解释。

最左边是预训练好的模型加载器，加载训练好的大模型。

第二个环节是编码器，一个是将文字信息转为潜空间信息的 clip 编码器，一个是正向的描述词。一个是负面的描述词。下面的一个是图片相关的信息这里连接的位置是图片的尺寸。

第三个环节是采样器，主要是将编码好的内容信息进行整理输入。选择不同的采样器，调整种子信息步数等相关的内容。然后输出。

第四个环节就是解码器了，输出为图片的时候需要 vae 解码（同理输入图片的时候需要 vae 编码），

最后一个环节就是图片解码输出后的预览以及保存等效果的输出结果了。

![](https://pic2.zhimg.com/v2-60e1effb58cfaad5228a5417f0317e15_b.jpg)

基础的界面主要是以工作流结合相关的内容。包含储存加载运行的基础操作。简介信息如上。

![](https://pic3.zhimg.com/v2-5a718d0ce1259b93f702e5f5fceadfce_b.jpg)

文件夹的界面中第一个部分是主要的 comfyUI 的内容，默认的包有两个开始工具分别是 cpu 运行和 gpu 运行。也可以下载辣椒酱的铁锅炖启动器。

[https://pan.quark.cn/s/dee558d71aea#/list/share](https://link.zhihu.com/?target=https%3A//pan.quark.cn/s/dee558d71aea%23/list/share)

![](https://pic4.zhimg.com/v2-0894c5a0cded1fec7f81f292fe78accb_b.jpg)

整体的模型库和 webUI 类似，主要区别是 stable diffusion 的文件夹名字在这里是 checkpoint 文件。

有 webUI 的同学可以使用 MKlink 来进行模型库的重定向。

例如:

_1、打开开始菜单，搜索：cmd 在命令提示符上单击右键，选择【以管理员身份运行】；_

![](https://pic2.zhimg.com/v2-bc95c117851f86794b66688a7f14c849_b.jpg)

_2、在命令提示符中键入：mklink /? 系统会给出 mklink 命令的帮助：_

_3、删除掉原本的 checkpoint 文件夹，创建一个副本。_

_4、输入_ _mklink /d 文件夹路径目标文件夹路径_

![](https://pic3.zhimg.com/v2-032455d4edbe14c4fbd146fd0e2ba2e6_b.jpg)

插件相关的内容放在这个路径。

### **1.3 comfyUI 与 webUI 的区别与特点**

ComfyUI 的特点在于它是一个基于节点流程的工具，通过将 stable diffusion 的流程拆分成节点，实现了更加精准的工作流定制和完善的可复现性。但节点式的工作流也提高了一部分使用门槛。

![](https://pic2.zhimg.com/v2-5d95f5fde186e2af88234cad3d6e2209_b.jpg)

作为基础上手的内容上，comfyUI 上手门槛更高，同时也具有更高的可自定义性。同时各种节点功能的拆分使得 comfyUI 能够实现很多 webUI 无法实现的效果和思路。存储的工作流分享也使得对于多环节合作和相互分享资源变得更加简单易用。

**2\. 功能性节点介绍**

![](https://pic4.zhimg.com/v2-155c034d3a4bebf3f98cb56cf292d537_b.jpg)

介绍了主界面和 comfyUI 相关的内容, 下面主要介绍下 comfyUI 的常用节点和它们在工作流之中的主要功能。

![](https://pic3.zhimg.com/v2-9e83344830d076b8ca1a4bf03be4ee26_b.jpg)

这里可以将 comfyUI 的节点分布大致分为上面提到的 6 种类型，以功能类型进行分类，下面会详细解释一下每一个的内容和对应 sdwebUI 相关的功能类型。

**2.1 采样器**

![](https://pic1.zhimg.com/v2-c14393652d90185d6b08ecb09fbbb21c_b.jpg)

首先介绍的是采样器，目前的 comfyUI 采样器主要是分为普通的 KSampler, 和高级版 KSampler（Advanced）。基础的采样器对比 webUI 的功能界面的内容大致相同。

![](https://pic1.zhimg.com/v2-310cb2cc6dc33afe483f30cfc00cde98_b.jpg)

种子对应 webUI 的种子类型，常用的是处理种子的固定和随机性。步数和 cfg 也是相同的。其中差异化的是画面尺寸，在 comfyUI 之中需要作为图片编码的信息节点链接至 latent_image 之中。

另一个差异点就是批次和单位数量。WebUI 的单批次数量是 8 个，而 comfyUI 没有这个限制。取决于工作流之中产出的图片数量内容。

![](https://pic2.zhimg.com/v2-5ee0a163df21493387eb648d0461de65_b.jpg)

对于升级版本的 KSamlper 而言主要的区别在于增加了与种子，noise 相关的参数设置。同时步数的范围也进行了更多的调整。

这部分更多的是用于 SDXL 的模型训练之中。

**2.2 加载器**

![](https://pic1.zhimg.com/v2-fc8e12222e16a874b581ca375151c9d8_b.jpg)

加载器这里是加载不同的模型，模型大致可以分为几个大类。分别是模型库相关，插件预训练模型相关，文字输入相关，放大器相关。

模型库这里的加载器最常用的就是 ckpt 和 lora 了。这里比较明显的是对标 webUI 之中选择不同模型的菜单界面。

![](https://pic4.zhimg.com/v2-2a1e55ae6e65a5fd190441d7160f89bf_b.jpg)

其中 ckpt 模型是必须的，常驻作为左边第一个起始节点。中间的部分对于 Lora 等模型进行串联。

![](https://pic2.zhimg.com/v2-81fc6e521c8f941bb69f1223cfdbc4a5_b.jpg)

这里以 lora 的 workflow 举例。需要从左边的 model 和 clip 进行接入，让 ckpt 在接入 clip 编码器时候进行一个内容变化。同时也可以在 clip 之中通过写入 lora 的词和权重进行添加。

![](https://pic2.zhimg.com/v2-55effaf23db31c05a8263ad5c09162e9_b.jpg)

然后 controlnet 加载器这部分比较特殊，相比 lora 的串联效果，controlnet 的做法更加复杂是一个并联的内容。上图举一个 controlnet canny 的例子。

Controlnet 主要影响到的是正向的描述词，其中需要在其中添加一个调节器（后面会提到）。这个调节器的功能是将多个加载器并联的内容进行一个汇总。然后输入到采样器的正向描述之中。

这里最左边的就是常驻的 ckpt 节点，中间是 3 组并联内容，上面的是 clip 编码器正向部分。

中间的是 controlnet 的预训练模型加载器。对标 controlnet 无预处理器的设置。

![](https://pic4.zhimg.com/v2-4e06b2ba0c047a6bcd78f112bf719053_b.jpg)

下面的是输入图像的加载器。对标 webUI 的这个环节。

![](https://pic2.zhimg.com/v2-31cd06fae2dd0d03f06aea64049d9ded_b.jpg)

这里提前介绍这个调节器。分为简易和复杂

![](https://pic3.zhimg.com/v2-80a1689cbec2ba3c66b2cdc897ebe39a_b.jpg)

上图中的简易版本对应只有控制权重的滑块。

![](https://pic1.zhimg.com/v2-87c244da3d8cea85f2c3e9e8d9ca8e78_b.jpg)

复杂的版本具有更加全的控制范围。可以做一些深度的操作（例如二维码隐藏图之类的效果）。

GlGENL，style Model 和 Clip Vison 一类的偏向风格和插件相关的加载器这里具体工作流具体分析。再提到一个常用的就是 Upscale 模型。

这个对应的就是 webUI 的后期处理或者说是放大菜单。

![](https://pic3.zhimg.com/v2-83dad1746aea8d2d7d3cee6992251c6a_b.jpg)

同样思路在使用加载了放大器进行输出入的时候也是需要并联这个加载器。同样需要一个 Upscale image 的调节器来将本身 Vae 解码器解码的内容与放大器模型的信息进行混合输出到后续环节

![](https://pic4.zhimg.com/v2-f46b66202fa207b5fdff6eafe5875ca3_b.jpg)