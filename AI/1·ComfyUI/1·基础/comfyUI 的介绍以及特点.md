

首先提到 comfyUI 需要先介绍的就是 diffusion model，这里贴一下原版的论文链接。

[https://arxiv.org/abs/2112.10752](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/2112.10752)

Diffusion model 简单的解释就是在一个潜在空间，将像素空间的内容拆分成为潜在空间的信息记录下来

![](https://pic2.zhimg.com/v2-8545b6a4d4390cf419124eac25ba6729_b.jpg)

直观的内容如上图是一个逐渐添加噪点的步骤，这就是将图片信息训练的部分。反过来降噪也就是将噪点信息降噪成为图片，也就是 AI 生成的过程。

![](https://pic4.zhimg.com/v2-30a98afb47d572611f01343531c653b3_b.jpg)

以图中内容举例。整个流程可以简化作为将图片信息或者文字信息转化为潜空间的信息。然后通过采样转换为目标的图片信息。最终再转换出来成为图片信息的流程。

那么其中转换的每个环节之间需要的也就是各种的功能性节点。整个节点链接在一起的也就是 comfyUI 的工作流。

例如输入文字需要 clip 编码器，一个训练好的模型加载器，在潜空间通过采样器调节生成对应信息，再通过解码器输出为图像。

这部分会在后面的内容上详细拆分讲解。

![](https://pic4.zhimg.com/v2-69150ffb830cf746ef30bb028aa51123_b.jpg)

这里顺便也延申一下最近的 SDXL 的工作流程，Stable Diffusion XL 是一个二阶段的级联扩散模型，包括 Base 模型和 Refiner 模型。其中 Base 模型的主要工作和 Stable Diffusion 一致，具备文生图，图生图，图像 inpainting 等能力。在 Base 模型之后，级联了 Refiner 模型，对 Base 模型生成的图像 Latent 特征进行精细化，本质上是在做图生图的工作。

