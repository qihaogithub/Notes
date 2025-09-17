#### VAE 简介

VAE 全称 Variational Auto Encoder （变分自编码器），是 stable diffusion 整个模型算法的组成部分之一，位于运作流程的末端，作用是让 stable diffusion 生成的图像颜色更鲜艳、细节更锐利；同时也能在一定程度上改善局部细节的生成质量，如手部、服装、脸部等，我们可以简单地把它理解为一种“滤镜”。

![Stable Diffusion WebUI 出图颜色发灰？用好VAE立马解决~](https://image.uisdc.com/wp-content/uploads/2023/08/1.png)
#### 如何判断是否需要使用 VAE 模型

VAE 模型不能单独使用，要配合大模型一起使用。但不是所有大模型都需要使用 VAE, 因为一些稳定的大模型本身就自带 VAE ，可以直接生成色彩正常的图像，再使用 VAE 可能会起到反作用。而有一些大模型在融合训练的时候 VAE 被损坏了，导致生成的图像色彩不佳，就需要搭配外挂 VAE。我们可以通过以下 2 种方式判断一款大模型是否需要配合 VAE 使用：

**① 根据图像生成效果判断**  
判断是否需要使用 VAE 最直接的方式就是看生成图像的效果，如果颜色发灰、发白，与你看到的参考图像效果有明显差异，那么就需要启用 VAE。

**② 看大模型的发布提示**  
一些大模型在发布的时候，如果需要使用外挂 VAE，会在发布声明里说明。如下图的Aniflatmix 大模型，在模型介绍页面就明确有提到需要配合 VAE模型使用。我们可以按提示在网上搜索相关资源 ，然后下载使用就可以了。

![Stable Diffusion WebUI 出图颜色发灰？用好VAE立马解决~](https://image.uisdc.com/wp-content/uploads/2023/08/2.png)

#### 3）VAE 模型下载

C 站可用 VAE 模型：[https://civitai.com/models](https://link.uisdc.com/?redirect=https%3A%2F%2Fcivitai.com%2Fmodels)

VAE 模型和其他 AI 绘画模型一样，资源主要集中在 Civitai 和 Huggingface 两个平台上。我们可以在 Civitai 上通过筛选查看所有可用 VAE 资源，或者直接在互联网上搜索你需要的 VAE 的名称寻找资源。

![Stable Diffusion WebUI 出图颜色发灰？用好VAE立马解决~](https://image.uisdc.com/wp-content/uploads/2023/08/3.png)

这里也为大家推荐几款常用的 VAE 模型，可以解决大部分的图像色彩发灰问题。

**① 通用 VAE**

ema-560000: [stabilityai/sd-vae-ft-ema-original at main](https://link.uisdc.com/?redirect=https%3A%2F%2Fhuggingface.co%2Fstabilityai%2Fsd-vae-ft-ema-original%2Ftree%2Fmain) （文末有资源包）  
mse-840000: [stabilityai/sd-vae-ft-mse-original at main](https://link.uisdc.com/?redirect=https%3A%2F%2Fhuggingface.co%2Fstabilityai%2Fsd-vae-ft-mse-original%2Ftree%2Fmain) （文末有资源包）

Stability AI 官方推出过 2 款 VAE ，vae-ft-ema-560000-ema-pruned 和 vae-ft-mse-840000-ema-pruned，它们适用于各种风格的大模型，能有效提升画面色彩的鲜艳程度。从使用经验来说，ema-560000 会明显地修改画面的细节，mse-840000 则没有那么明显。

![Stable Diffusion WebUI 出图颜色发灰？用好VAE立马解决~](https://image.uisdc.com/wp-content/uploads/2023/08/4.png)

**② 风格化 VAE**

ClearVAE：[ClearVAE - v2.3 | Stable Diffusion VAE | Civitai](https://link.uisdc.com/?redirect=https%3A%2F%2Fcivitai.com%2Fmodels%2F22354%2Fclearvae) （文末有资源包）  
kl-f8-anime2：[https://civitai.com/models/23906](https://link.uisdc.com/?redirect=https%3A%2F%2Fcivitai.com%2Fmodels%2F23906) （文末有资源包）  
Anything：[https://civitai.com/models/110630/anything-model-vae-v40](https://link.uisdc.com/?redirect=https%3A%2F%2Fcivitai.com%2Fmodels%2F110630%2Fanything-model-vae-v40) （文末有资源包）

有些 VAE 则只适合特定风格的大模型，大家在下载的时候可以仔细阅读 VAE 制作者的使用说明。比如 ClearVAE、kl-f8-anime2、anything 等，都是适合动漫风大模型的 VAE。

不同的 VAE 下，图像生成效果会略有差异，大家可以根据实际情况对比选择：

![Stable Diffusion WebUI 出图颜色发灰？用好VAE立马解决~](https://image.uisdc.com/wp-content/uploads/2023/08/06.png)

**4）VAE 的使用与管理**

VAE 模型下载后，需要放进根目录的 models\VAE 文件夹内；如果要卸载某个VAE，也是在VAE 文件夹中删除对应的文件就可以了。

![Stable Diffusion WebUI 出图颜色发灰？用好VAE立马解决~](https://image.uisdc.com/wp-content/uploads/2023/08/7.png)

在 WebUI 中，选择好大模型后，在“外挂 VAE ” 的下拉栏中选择对应的模型就可以了；不需要 VAE 的话，默认“自动”或者“无”。

![Stable Diffusion WebUI 出图颜色发灰？用好VAE立马解决~](https://image.uisdc.com/wp-content/uploads/2023/08/8.png)

如果你使用的是 @秋葉aaaki 大佬的整合包，也可以进入启动器的“模型管理”界面，选择“VAE模型”版块，立马有多个 VAE 模型可以直接下载，下载完成后文件会自动放入根目录。

![Stable Diffusion WebUI 出图颜色发灰？用好VAE立马解决~](https://image.uisdc.com/wp-content/uploads/2023/08/9.png)

以上就是本期为大家分享的 [Stable Diffusion WebUI](https://www.uisdc.com/tag/stable-diffusion-webui) 中「外挂 VAE」的相关内容，喜欢本期推荐的话记得点赞收藏支持一波，之后会继续为大家推荐更多实用的 AI 绘画干货。有关于本文或者设计的问题可以在评论区提出 ，我会第一时间回复。

获取更多优质 AI 绘画干货知识，欢迎访问 「优设AI自学网」 ，超多 AI 绘画神器与教程等你探索。

访问链接： [https://ai.uisdc.com/](https://ai.uisdc.com/)

参考资料：  
[https://blog.csdn.net/naisongwen/article/details/132040012](https://link.uisdc.com/?redirect=https%3A%2F%2Fblog.csdn.net%2Fnaisongwen%2Farticle%2Fdetails%2F132040012)  
[https://zhuanlan.zhihu.com/p/631452035](https://link.uisdc.com/?redirect=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F631452035)