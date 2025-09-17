---
类型:
  - 控图
---
## 简介
IPAdapter，是腾讯 AI 实验室发布的类似于 MJ 的垫图功能，但又强于 MJ 的垫图功能。 可以迁移图片的风格，可以实现多张图片风格的融合，还可以搭配 ControlNet 来实现更多样化的功能。
## 视频教程
https://www.bilibili.com/video/BV16x421D7aW/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d

## 节点介绍

![|400](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406231542945.png)
### FaceID
这个节点用于识别和标记图像中的面部位置。
### 分块 
分块节点用于将输入图像分割成多个较小的部分或块。这在处理大图像或执行局部操作时很有用，可以提高处理效率和控制精度。

### 嵌入组
嵌入组节点通常用于将图像或其他数据转换成向量表示，这种向量表示（也称为嵌入）可以捕捉到输入数据的关键特征，对于后续的模型训练或推理至关重要。

### 风格合成
风格合成节点用于将一种图像的风格转移到另一种图像上。这是通过学习并应用源图像的风格特征到目标图像来实现的，从而创造出具有新风格的图像。
### 参数组
参数组节点用于组织和管理模型的参数设置。它允许用户定义一组参数，这些参数可以被其他节点引用和使用，从而简化了参数管理和配置。
### 加载器
加载器节点用于从磁盘读取模型权重、图像或其他资源。它是一个关键组件，确保了模型和其他资源的可用性
### 实用工具
实用工具节点包含一系列辅助功能，如图像缩放、裁剪、颜色空间转换等，它们帮助预处理输入数据或后处理输出数据，确保数据符合模型的要求或用户的期望
### 权重
权重节点用于调整模型内部不同部分的贡献度。通过改变权重值，可以控制模型对某些特征的重视程度，从而影响最终输出的质量和特性。
### 应用IPAdapter 
应用IPAdapter节点是IPAdapter的核心，它接收图像和可能的附加条件作为输入，然后使用预训练的IPAdapter模型生成新的图像。这个过程通常涉及将输入图像的特征与附加条件融合，以生成符合条件的新图像。
[[应用IPAdapter(高级)]]
### 应用IPAdapter(批次) 
批次版本的应用IPAdapter节点用于同时处理多个图像。它接收一个图像列表和相应的条件，然后批量生成图像，提高了处理大量数据的效率。
### IPAdapter加载器
IPAdapter加载器节点专门用于加载和初始化IPAdapter模型。它确保模型在开始生成之前正确加载，避免了每次生成时重复加载模型的时间开销。
## 基础运用
复制听雨的工作流以后，我们只需要上传我们想要借鉴的风格的图片，然后选择大模型，输入提示词点击生成就会生成风格类似的图片了。

工作流见：IPAdapter\_00001\_. Png
![[Drawing 2024-06-25 21.18.30.excalidraw]]
![](https://pic1.zhimg.com/80/v2-3421b5cc986b866e1a1f660352bfce34_1440w.webp)


### ControlNet 融合
可以结合 ipadapter 和 ControlNet 来实现两张图片的融合。

比如我们想要把图一的风格迁移到图二上，那就只需要再加上 ControlNet 的 **Canny** 模型就可以。这样就可以得到一张图一风格但是又保留了图二整体轮廓的图片了。**这种方式也可用于装修风格的迁移。** 

工作流见：IPAdapter_Canny. Png

![](https://pic2.zhimg.com/80/v2-ccf98db1b424cae302a7a6954d73a075_1440w.webp)


### 换脸
ipadapter 还提供了一中专门换脸的模型，我们只需要上传一张脸部的图片，然后输入我们想要的提示词就可以替换我们生成图片中人物的脸。Sd 1.5 和 sdxl 模型分别是「ip-adapter-plus-face\_sd 15. Bin」和「ip-adapter-plus-face\_sdxl_vit-h.bin」，这两个模型都要使用 sd 1.5 的**图像编码器**哦!

工作流见：IPAdapter_face. Png

![](https://pic1.zhimg.com/80/v2-dffc42ae4ab1ffbcbd73f858a28bbc60_1440w.webp)


### 画风融合
还可以上传多张图来融合图片风格。

工作流见：IPAdapter\_batch\_images. Png

![](https://pic1.zhimg.com/80/v2-60a958aec84d32187fbc719711dffa08_1440w.webp)


### 画风权重融合
当上传多张图片时，还可以结合 IPAdapterEncoder 控制每张图片的融合权重，最多可以设置 4 张图片。

工作流见：IPAdapter_weighted. Png

![](https://pic4.zhimg.com/80/v2-5540f0e2ce36bc556c5bd481214d13af_1440w.webp)



来源：[ComfyUI + ipAdapter = 创意无限 - 知乎](https://zhuanlan.zhihu.com/p/664201523)

