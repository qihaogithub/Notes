---
类型:
  - 控图
---


[github 项目地址](https://github.com/cubiq/ComfyUI_InstantID)


1. 什么是 InstantID
--------------

InstantID 是一种全新无需微调的最先进方法，它只需要单张图像，即可实现生成新图像的同时保留原图像中的人员身份信息，支持各种后续任务，例如人脸识别、人脸属性分析任务。

简单讲就是类似 IPA-faceID, Reactor 这些模型，能保持人脸部的一致性。

2. ComfyUI InstantID 插件
---------------------

[cubiq/ComfyUI_InstantID (github.com)](https://link.zhihu.com/?target=https%3A//github.com/cubiq/ComfyUI_InstantID)

目前有几个支持 InstantID 的节点，我个人还是喜欢这个作者的，它是原生的 InstantID 节点。作者同时也是 [cubiq/ComfyUI\_IPAdapter\_plus (github.com)](https://link.zhihu.com/?target=https%3A//github.com/cubiq/ComfyUI_IPAdapter_plus) 的作者。

### 1）节点安装

在 custome_nodes 通过 git, 克隆插件

```text
git clone https://github.com/cubiq/ComfyUI_InstantID.git
```

或者通过 GitHub 下载 zip 包，解压到 custom_node 1 节点下。

### 2）依赖安装

一般重启后，comfyUI 会自动安装依赖，也可以通过命令行手动安装依赖

```text
E:\ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI_InstantID>..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
```

这里注意的是 InstantID 要求 `insightface`, 你需要安装 `onnxruntime和onnxruntime-gpu`. 这两个库.

### 3）模型下载

**a）脸部识别模型**

和 FaceID, Reactor，roop 不同的是，这个 InstantID 用的 The InsightFace 模型是**antelopev 2，**而不是常用的经典模型 buffalo_l

你可以在这里下载 [MonsterMMORPG/tools at main (huggingface.co)](https://link.zhihu.com/?target=https%3A//huggingface.co/MonsterMMORPG/tools/tree/main)

下载后把模型文件放入**ComfyUI/models/insightface/models/antelopev 2**。

**b）主模型**

主模型可以从 Hugging Face 网站下载，并放置在 `ComfyUI/models/instantid` 目录中。（请注意，该模型基于 `IPAdapter` 模型，因此命名为 `ip_adapter`。）

[https://huggingface.co/InstantX/InstantID/resolve/main/ip-adapter.bin?download=true](https://link.zhihu.com/?target=https%3A//huggingface.co/InstantX/InstantID/resolve/main/ip-adapter.bin%3Fdownload%3Dtrue)

**C）Controlnet 模型**

它还需要一个 controlnet 模型，下载地址。

[https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion\_pytorch\_model.safetensors?download=true](https://link.zhihu.com/?target=https%3A//huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors%3Fdownload%3Dtrue)

你可以直接把它放到 ComfyUI/models/controlnet 路径下，我给它改了名字后保存，你也可以不改。

### 4) 插件使用

**去除水印！**

作者提醒大家，训练数据中充斥着水印，为了避免它们出现在你的生成图像中，你可以使用与 1024×1024 稍有不同的分辨率，例如 1016×1016，通常能起到很好的效果。

**降低 CFG**

将 CFG 降低到至少 4/5 或者您可以使用“RescaleCFG”节点非常重要。

下面是几个主要节点的介绍

![](https://pic3.zhimg.com/v2-ab658b5dfe1b822426aa1825030940ce_b.jpg)

A. Load Instant ID Model 节点：（加载主模型，models/instantID 路径下的模型）

B.InstantID Face Analysis（脸部识别节点）：（加载脸部识别模型：ComfyUI/models/insightface/models/antelopev 2）也就是 insightface 模型

C. Apply InstanID 节点：需要注意的是 image-feature 是原脸部的图，

D. Face Keypoint Processors 节点：一个是原图，一个目标图的

E. Load Controlnet Model 节点：加载 controlnet 模型节点，是上一步下载的 contronet 模型，我自己的环境改成 control_instantID 了，大家可以根据自己的来修改。

### 5）例子流程

在 ComfyUI\\custom\_nodes\\ComfyUI\_InstantID\\examples 里面有几个示例，小伙伴们可以使用测试一下。

![](https://pic4.zhimg.com/v2-cbab3ed19132e4a59da5afc6c7d41ad3_b.jpg)

3. 使用写实照片模型测试
------------

通过改变基础模型和提示词，加上 face++的脸部识别算法。看到 InstantID 对于脸部图像的保持还是不错的。居然可以接近 94 分，这是很高的得分了。

![](https://pic3.zhimg.com/v2-9b2d20af5032aea63eae2658dae11a72_b.jpg)

![](https://pic2.zhimg.com/v2-0ef9e61a75722bf09ef5167440dd2229_b.jpg)

这张能体现 InstantID 的不足，鼻子上的纹络就是不应该出现的。

![](https://pic2.zhimg.com/v2-ebeaacbca53b89c1a602de13c06efc21_b.jpg)

4. 总结
----

总结以下几点（目前测试量较少，结论有受影响，欢迎指正)：

1. 使用上算是比较简单易用。

2. 脸部相似性确实很不错的。但是有点受原图影响较大

3. 对于图像的扩展性和多样性上欠缺，生成图片对提示词很迟钝。这点不太使用上很不友好。

4. 需要通过其它的图片提示词来调整体。

总体感觉不如 faceid 灵活好用，适用照片写实风格不如 reactor。某些特定的对脸部相似度要求高的出图可以选择。

本文相关的模型和节点都通过百度网盘共享如下：

链接：[](https://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1PRYnrtU12cTgMdjNSZS2ew%3Fpwd%3Dsolw) [https://pan.baidu.com/s/1PRYnrtU12cTgMdjNSZS2ew](https://pan.baidu.com/s/1PRYnrtU12cTgMdjNSZS2ew) [https://pan.baidu.com/s/1PRYnrtU12cTgMdjNSZS2ew](https://pan.baidu.com/s/1PRYnrtU12cTgMdjNSZS2ew) [https://pan.baidu.com/s/1PRYnrtU12cTgMdjNSZS2ew](https://pan.baidu.com/s/1PRYnrtU12cTgMdjNSZS2ew)? pwd=solw

提取码：solw