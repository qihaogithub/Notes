## 前言

![](https://pic4.zhimg.com/v2-c79f60f36b5ce0c5e54be51282b4855b_b.jpg)

这篇文章主要还是偏向 comfyUI 的基础向介绍和分享，主要是梳理相关的原理，对比 webUI 的一些相关功能，同时对于 comfyUI 优势的一些梳理。基础向工作流的拆解和一些插件的介绍和分享。关于 comfyUI 相关的内容可能会偏向长期的几个文章来介绍。

![](https://pic2.zhimg.com/v2-b74a9d79aefdc2d6f69e255745699481_b.jpg)

关于 comfyUI 这边分为四个部分。第一个部分是介绍 comfyUI 本身的简介，相关的基础原理。本体的一些功能性节点相关的介绍。然后一些基础工作流的梳理和简介。后续的总结和相关常用插件工具的分享。

##  [[Comfy UI 安装]]

##  [[comfyUI 的介绍以及特点]]

##  [[comfyUI 的界面功能]]
## 更新

1. 我们在“ComfyUI_windows_portable\update”文件下可以看到“update_comfyui”、“update_comfyui_and_python_dependencies”这两个文件。分别是用来更新 ComfyUI 和配置环境的。

![超详细的 Stable Diffusion ComfyUI 基础教程（一）：安装与常用插件](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sd-20230924-8.jpg)

2. 我们点击“update_comfyui”进行更新 ComfyUI，等出现“Done”就说明更新成功了。

![超详细的 Stable Diffusion ComfyUI 基础教程（一）：安装与常用插件](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sd-20230924-9.jpg)

3. 至于配置环境能跑就不要动，而且更新的几率也不大。

我们已经安装好 ComfyUI 了，但是为了让我们更好的使用，我们添加几个插件。这几个插件有的是需要用在流程中的，有的是 UI 界面调整（以及汉化），需要用在流程中的功能我会穿插在后面的流程教学中。
## 文件夹说明

插件文件夹位置：
/Users/qh 2/pinokio/api/comfyui. Git/app/custom_nodes ^hzdolm
ComfyUI\\custom_nodes  自定义节点目录
k.zhihu. Com/? Target=https%3 A//github. Com/ltdrdata/ComfyUI-Manager)

必备插件了属于是，很多时候导入一些其他人的工作流会出现一些模型缺少或者插件工具缺少等内容。这个工具相当于是 webUI 中的从网页安装的这个插件。能够快速的结合各种工具和模型使得插件安装更加方便快捷。

 ##  [[comfyui模型配置]]