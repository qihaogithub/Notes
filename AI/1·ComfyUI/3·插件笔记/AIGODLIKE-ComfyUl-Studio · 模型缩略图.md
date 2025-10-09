---
类型:
  - 界面
  - 效率
简介: ComfyUI 模型的加载更加直观、更轻松地创建模型缩略图
---
来源：[AIGODLIKE-ComfyUI-Studio/README.md 在 main · AIGODLIKE/AIGODLIKE-ComfyUI-Studio](https://github.com/AIGODLIKE/AIGODLIKE-ComfyUI-Studio/blob/main/README.md)

## 摘录内容 
C# AIGODLIKE-ComfyUI-Studio 改善使用 ComfyUI 的交互体验，例如使 ComfyUI 模型的加载更加直观、更轻松地创建模型缩略图
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408160944121.png)

## 功能介绍

| 功能 | 细节 |
| :-- | :-- |
| 装载机模型管理器 | 更直观的模型管理（模型排序、标签、搜索、评级等） |
| 模型缩略图 | 一键生成模型缩略图或使用本地图片作为缩略图 |
| 模型屏蔽 | 排除某些模型出现在加载器中 |
| 自动模型标签 | 自动标记模型外层文件夹，如\\ComfyUI\\models\\checkpoints\\SD 1.5\\real\\A.ckpt，并添加“SD 1.5”和“real”作为A.ckpt 标签 |
| 模型匹配工作流程 | 为模型匹配匹配的工作流程，支持搜索、添加、加载、删除、复制到剪贴板 |
| 多种语言 | 支持英文、简体中文和繁体中文 |

## 如何使用

找到一个 loader，**左键点击**模型开关弹出 ComfyUI Studio Manager。如果仍然需要使用原始模型列表，请使用**Shift+左键**点击模型开关弹出原始模型列表

## 支持的加载器列表

1**标准节点**：自动支持 ComfyUI 官方节点和标准命名的\*自定义节点类型，当它们需要访问模型文件夹时会自动接管。

标准名称：ckpt\_name、vae\_name、clip\_name、gligen\_name、control\_net\_name、lora\_name、style\_model\_name、hypernetwork\_name、unet\_name。

2**非标准节点**：一些开发人员出于某种目的重新定义了模型加载器，这意味着非标准命名会阻止程序自动适应，需要手动适应，这需要一些时间和反馈才能添加到支持列表中

| 节点名称 | 标题 |
| :-- | :-- |
| 图像检查点加载器 | 检查点加载器 (仅图片) |
| CheckpointLoader 简单 | Checkpoint 加载器（简易） |
| 加载器 | unCLIPCheckpoint 加载器 |
| 检查点加载器 | Checkpoint 加载器 |
| VAE 加载器 | VAE 加载器 |
| CLIPVision 加载器 | CLIP 视觉加载器 |
| GLIGEN 装载机 | GLIGEN 加载器 |
| 控制网络加载器 | ControlNet 加载器 |
| 差异控制网络加载器 | DiffControlNet 加载器 |
| LoraLoader 仅模型 | LoRA 加载器 (仅模型) |
| 劳拉装载机 | LoRA 加载器 |
| 样式模型加载器 | 风格模型加载器 |
| 高档模型加载器 | 放大模型加载器 |
| 超网络加载器 | 超网络加载器 |
| CLIP 加载器 | CLIP 视觉加载器 |
| 双 CLIP 加载器 | 双 CLIP 加载器 |
| UNET 加载器 | UNET 加载器 |
| 扩散器装载机 | 扩散加载器 |
