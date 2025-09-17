---
github: https://github.com/huchenlei/ComfyUI-IC-Light-Native
---
# ComfyUI-IC-Light-Native
ComfyUI原生实现 [IC-Light](https://github.com/lllyasviel/IC-Light).

## 安装

下载存储库并解压到ComfyUI安装目录中的custom_nodes文件夹中。

Or clone via GIT, starting from ComfyUI installation directory:

```bash
cd custom_nodes
git clone git@github.com:huchenlei/ComfyUI-IC-Light-Native.git
```

### Download models
IC-Light主仓库基于扩散器。为了在ComfyUI中使用UnetPlayer加载它，需要将State_dict密钥转换为ldm格式。您可以在此处下载带有ldm密钥的模型： https://huggingface.co/huchenlei/IC-Light-ldm/tree/main

有2种型号：
- iclight_sd15_fc_unet_ldm: Use this in FG workflows
- iclight_sd15_fbc_unet_ldm: Use this in BG workflows

下载这些模型后，请将它们放在“ComfyUI/models/unet”下，并使用“UNETLoader”节点加载它们。

### [重要！] 所需的节点
您必须先安装以下节点，才能让IC-Light正常工作。
- [ComfyUI-layerdiffuse](https://github.com/huchenlei/ComfyUI-layerdiffuse): Although not used in the workflow, the patching of weight load in layerdiffuse is a dependency for IC-Light nodes to work properly.
  
### 推荐节点
- [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes): 提供各种遮罩节点来创建灯光图。
- [ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use): 一个包含所有东西的巨型节点包。工作流程中使用的删除背景节点来自此包。
- [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials): 许多有用的工具节点。工作流程中使用的图像大小调整节点来自此包。
- [ComfyUI-IC-Light](https://github.com/kijai/ComfyUI-IC-Light): 来自kijai的IC-Light impl。它包括一个非常有用的“DetailTransfer”节点，以帮助从输入fg图像中预反高频细节。

## 工作流
请确保在将前景图像传递给 VAE 之前，其遮罩/透明区域是灰色的。否则，在 FC 工作流中会得到被遮挡的背景，或在 FBC 工作流中得到变暗的背景。您可以使用 `IC Light Apply Mask Grey` 来确保遮罩区域的颜色是正确的。请参考以下示例:
![12 05 2024_16 22 48_REC](https://github.com/huchenlei/ComfyUI-IC-Light-Native/assets/20929282/702c7b3a-54f7-44e2-a6d7-39220aa6ffef)
![12 05 2024_16 19 02_REC](https://github.com/huchenlei/ComfyUI-IC-Light-Native/assets/20929282/6d2d504f-65be-47cb-9597-2e64fe239939)

### [Given FG, Generate BG and relight](https://github.com/huchenlei/ComfyUI-IC-Light/blob/main/examples/fg.json)
![image](https://github.com/huchenlei/ComfyUI-IC-Light-Native/assets/20929282/6b801a2d-f37c-44f4-b52d-ad7de1748f8e)
如果您想保留前景对象的原始颜色，可以将FG对象放入潜在空间中进一步指导生成。 [workflow](https://github.com/huchenlei/ComfyUI-IC-Light-Native/blob/main/examples/ic_light_preserve_color.json)
![image](https://github.com/huchenlei/ComfyUI-IC-Light-Native/assets/20929282/6fb8c01e-727c-4fa7-b72f-f91ea3dce004)

### [Given FG and light map, Genereate BG and relight](https://github.com/huchenlei/ComfyUI-IC-Light/blob/main/examples/fg_lightmap.json)
光从右起
![image](https://github.com/huchenlei/ComfyUI-IC-Light-Native/assets/20929282/045e4f0e-6083-496f-af32-41de4821afbf)

左边的光
![image](https://github.com/huchenlei/ComfyUI-IC-Light-Native/assets/20929282/74750b9e-bda7-43f7-944f-d75cb7b5fb7e)

### [Given FG and BG, Put FG on BG and relight](https://github.com/huchenlei/ComfyUI-IC-Light/blob/main/examples/fg_bg_combine.json)
![image](https://github.com/huchenlei/ComfyUI-IC-Light-Native/assets/20929282/ea87538a-15d8-43d8-874d-bcddab9f4f0e)

### [从原始输入图像中恢复高频细节（文本等）](https://github.com/huchenlei/ComfyUI-IC-Light-Native/blob/main/examples/ic_light_detail_transfer.json)
![06 06 2024_12 19 35_REC](https://github.com/huchenlei/ComfyUI-IC-Light-Native/assets/20929282/7fbd66e9-5468-4644-9edb-abbc5aa55b77)
- Input image:
  ![image](https://github.com/huchenlei/ComfyUI-IC-Light-Native/assets/20929282/ebdd9f49-41ee-47e3-a334-299fd1ee0385)
- Raw generation:
  ![image](https://github.com/huchenlei/ComfyUI-IC-Light-Native/assets/20929282/040a59ff-1aaf-4df9-bb00-1e50ae67db1e)
- After detail transfer:
  ![image](https://github.com/huchenlei/ComfyUI-IC-Light-Native/assets/20929282/86ddfc4d-7077-43ea-979f-8dcf243aaaf9)

## 常见问题
IC-Light's unet is accepting extra inputs on top of the common noise input. FG model accepts extra 1 input (4 channels). BG model accepts 2 extra input (8 channels).
The original unet's input is 4 channels as well. 

If you see following issue, it means IC-Light's unet is not properly loaded, and you need to install [ComfyUI-layerdiffuse](https://github.com/huchenlei/ComfyUI-layerdiffuse) first.

```
RuntimeError: Given groups=1, weight of size [320, 4, 3, 3], expected input[2, 8, 64, 64] to have 4 channels, but got 8 channels instead
```

If you see following error, it means you are using FG workflow but loaded the BG model.

```
RuntimeError: Given groups=1, weight of size [320, 8, 3, 3], expected input[2, 12, 64, 64] to have 8 channels, but got 12 channels instead
```

If you see following error, it means you are using FG workflow but loaded the BG model.

```
RuntimeError: Given groups=1, weight of size [320, 12, 3, 3], expected input[2, 8, 64, 64] to have 12 channels, but got 8 channels instead
```
