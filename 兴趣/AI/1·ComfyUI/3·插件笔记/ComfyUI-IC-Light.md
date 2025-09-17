---
github: https://github.com/kijai/ComfyUI-IC-Light
---

国内模型地址： https://www.codewithgpu.com/m/IC_Light_Models

## 简介
给图片重新打光

## 安装

下载存储库并解压到 ComfyUI 安装目录中的 custom_nodes 文件夹中。

或者通过 GIT 克隆，从 ComfyUI 安装目录开始：

```shell
cd custom_nodes
git clone git@github.com:huchenlei/ComfyUI-IC-Light-Native.git
```

### 下载模型
IC-Light 主 repo 基于扩散器。为了在 ComfyUI 中使用 UnetLoader 加载它，state_dict 键需要转换为 ldm 格式。您可以在此处下载带有 ldm 键的模型：[https://huggingface.co/huchenlei/IC-Light-ldm/tree/main](https://huggingface.co/huchenlei/IC-Light-ldm/tree/main)

有两种型号：
- iclight_sd15_fc_unet_ldm：在 FG 工作流程中使用它
- iclight_sd15_fbc_unet_ldm：在 BG 工作流程中使用它

下载这些模型后，请将它们放在下面`ComfyUI/models/unet`并使用节点加载它们`UNETLoader`。

### [重要！] 必需节点
您必须首先安装以下节点才能使 IC 灯正常工作。

- [ComfyUI-layerdiffuse](https://github.com/huchenlei/ComfyUI-layerdiffuse)：虽然在工作流程中没有使用，但是在 layerdiffuse 中修补权重负载是 IC-Light 节点正常工作的依赖项。

### 推荐节点

- [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)：提供各种遮罩节点来创建光照图。
- [ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)：一个包含所有内容的巨型节点包。工作流中使用的 remove bg 节点来自此包。
- [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)：许多有用的工具节点。工作流程中使用的图像调整大小节点来自此包。
- [ComfyUI-IC-Light](https://github.com/kijai/ComfyUI-IC-Light)：kijai 的 IC-Light 实现。它包含一个非常有用的`DetailTransfer`节点，可帮助从输入 fg 图像中预测高频细节。

## 工作流程

在将 fg 图像传递给 VAE 之前，请确保其蒙版/透明区域为灰色。否则，在 FC 工作流程中，背景会变得模糊；在 FBC 工作流程中，背景会变得暗淡。您可以使用它 `IC Light Apply Mask Grey` 来确保蒙版区域的颜色正确。请参阅以下示例：
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406250934168.png)
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406250935306.png)
给定 FG，生成 BG 并重新点亮
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406250936620.png)
如果想保留fg对象的原始颜色，可以将fg对象放入潜在空间中，以进一步指导生成。[工作流程](https://github.com/huchenlei/ComfyUI-IC-Light-Native/blob/main/examples/ic_light_preserve_color.json)
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406250936021.png)
给定 FG 和光照贴图，生成 BG 并重新点亮
右侧有光
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406250937776.png)
左侧有光
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406250937949.png)
给定 FG 和 BG，将 FG 放在 BG 上并重新点亮
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406250937601.png)
从原始输入图像中恢复高频细节（文本等）
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406250937761.png)
输入图像![|91](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406250937318.png)
原始生成
![|137](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406250938934.png)

明细转移后：
![|131](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406250938228.png)
