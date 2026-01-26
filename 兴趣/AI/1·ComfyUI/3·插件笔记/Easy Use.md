---
github: https://github.com/yolain/ComfyUI-Easy-Use
分类:
  - 效率
---
[视频教程](https://www.youtube.com/@xueqinghuang5021/videos?view=0&sort=dd&shelf_id=1)
## 简介
**ComfyUI-Easy-Use** 是一个化繁为简的节点整合包, 在 [tinyterraNodes](https://github.com/TinyTerra/ComfyUI_tinyterraNodes) 的基础上进行延展，并针对了诸多主流的节点包做了整合与优化，以达到更快更方便使用ComfyUI的目的，在保证自由度的同时还原了本属于Stable Diffusion的极致畅快出图体验。
## 特色介绍
- 沿用了 [tinyterraNodes](https://github.com/TinyTerra/ComfyUI_tinyterraNodes) 的思路，大大减少了折腾工作流的时间成本。
- UI界面美化，首次安装的用户，如需使用UI主题，请在 Settings -> Color Palette 中自行切换主题并**刷新页面**即可
- 增加了预采样参数配置的节点，可与采样节点分离，更方便预览。
- 支持通配符与Lora的提示词节点，如需使用Lora Block Weight用法，需先保证自定义节点包中安装了 [ComfyUI-Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack)
- 可多选的风格化提示词选择器，默认是Fooocus的样式json，可自定义json放在styles底下，samples文件夹里可放预览图(名称和name一致,图片文件名如有空格需转为下划线'_')
- 加载器可开启A1111提示词风格模式，可重现与webui生成近乎相同的图像，需先安装 [ComfyUI_smZNodes](https://github.com/shiimizu/ComfyUI_smZNodes)
- 可使用`easy latentNoisy`或`easy preSamplingNoiseIn`节点实现对潜空间的噪声注入
- 简化 SD1.x、SD2.x、SDXL、SVD、Zero123等流程 
- 简化 Stable Cascade [示例参考](https://github.com/yolain/ComfyUI-Yolain-Workflows?tab=readme-ov-file#1-13-stable-cascade)
- 简化 Layer Diffuse [示例参考](https://github.com/yolain/ComfyUI-Yolain-Workflows?tab=readme-ov-file#2-3-layerdiffusion)
- 简化 InstantID [示例参考](https://github.com/yolain/ComfyUI-Yolain-Workflows?tab=readme-ov-file#2-2-instantid), 需先保证自定义节点包中安装了 [ComfyUI_InstantID](https://github.com/cubiq/ComfyUI_InstantID)
- 简化 IPAdapter, 需先保证自定义节点包中安装最新版v2的 [ComfyUI_IPAdapter_plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus)
- 扩展 XYplot 的可用性
- 整合了Fooocus Inpaint功能
- 整合了常用的逻辑计算、转换类型、展示所有类型等
- 支持节点上checkpoint、lora模型子目录分类及预览图 (请在设置中开启上下文菜单嵌套子目录)
- 支持BriaAI的RMBG-1.4模型的背景去除节点，[技术参考](https://huggingface.co/briaai/RMBG-1.4)
- 支持 强制清理comfyUI模型显存占用
- 支持Stable Diffusion 3 多账号API节点
- 支持IC-Light的应用 [示例参考](https://github.com/yolain/ComfyUI-Yolain-Workflows?tab=readme-ov-file#2-5-ic-light) | [代码整合来源](https://github.com/huchenlei/ComfyUI-IC-Light) | [技术参考](https://github.com/lllyasviel/IC-Light)
- 中文提示词自动识别，使用[opus-mt-zh-en模型](https://huggingface.co/Helsinki-NLP/opus-mt-zh-en)
- 支持 sd3 模型 

## 安装
将存储库克隆到 **custom_nodes** 目录并安装依赖
```shell
#1. git下载
git clone https://github.com/yolain/ComfyUI-Easy-Use
#2. 安装依赖
双击install.bat安装依赖
```
## 节点详情
### 实用工具
书签
设置点
获取点
[[显示推理时间]]
显示加载器参数名称
[[Easy Slider Control ]]
Ckpt Names
ControlNet Names
### 随机种
[[随机种]]
[[全局随机种]]
### 提示词
正面提示词
负面提示词
通配符提示词
[[easy·提示词]]
[[兴趣/AI/1·ComfyUI/3·插件笔记/节点笔记/提示词列表]]
[[提示词行]]
[[PromptConcat 提示词联结]]
[[兴趣/AI/1·ComfyUI/3·插件笔记/节点笔记/提示词替换]]
风格提示词选择器
[[肖像大师]]
### 加载器
简易加载器（完整版）
简易加载器 (A1111)
简易加载器(Comfy)
简易加载器(SVD) 
简易加载器(SV3D)
简易加载器 (Zero123) 
简易加载器(DynamiCrafter) 
简易加载器(Cascade)
EasyLoader (HunYuanDiT)
EasyLoader (PixArt) 
简易Lora堆
EasyControlnetStack 
简易Controlnet 
简易Controlnet(高级) 
简易LLLite
### Adapter 
应用IPAdapter 
应用IPAdapter(高级) 
应用IPAdapter(编码) 
应用IPAdapter(嵌入组)
Easy Apply IPAdapter (Regional)
Easy Apply IPAdapter(From Params) 
应用IPAdapter(风格合成) 
应用InstantID 
应用InstantID(高级)
Easy Apply PuLID
Easy Apply PuLID (Advanced)
Easy Apply StyleAlign
Easy Apply ICLight
### 内补
Easy Apply Fooocus Inpaint
Easy Apply BrushNet
Easy Apply PowerPaint
Easy Apply Inpaint
### Latent 
噪波Latent(Sigma乘积)
Latent遮罩复合（带条件） 
插入噪波到Latent
### 预采样
预采样参数（基础） 
预采样参数（高级） 
预采样参数（插入噪波） 
预采样参数（自定义） 
预采样参数(SDTurbo)
预采样参数（动态CFG)
预采样参数(Cascade) 
预采样参数(LayerDiffusion)
预采样参数(LayerDiffusioni前景背景）
动态CFG
### 采样器
简易k采样器（完整版）
简易K采样器
简易k采样器（分块解码） 
简易k采样器 (LayerDiffusion)
简易K采样器（内补）
简易K采样器（收缩Unet) 
简易k采样器 (SDTurbo) 
简易级联k采样器（完整版） 
简易级联k采样器
逆（不）采样器
### 修复
[[兴趣/AI/1·ComfyUI/3·插件笔记/节点笔记/高清修复]]
预细节修复
预遮罩细节修复
检测加载器（细节修复节点束）
Sam模型加载器（细节修复节点束） 
[[细节修复]]
### 节点束
节点束输入
节点束输出
节点束编辑
节点束转换基础节点束
节点束批次索引
简易XY图表
简易XY图表（高级）
### XY输入 
XY输入：随机种个数 
XY输入：步数 
XY输入：CFG 
XY输入：采样调度器 
XY输入：降噪 
XY输入：模型
XY输入：Lora
XY输入：模型融合 X
Y输入：替换提示词
XY输入：ControlNet
XY输入：正面条件x4
Y输入：正面条件列表
Y输入：负面条件x4
XY输入：负面条件列表
### API
Stable Diffusion 3 (API)
### 图像
图像尺寸 (边）
图像尺寸（长边） 
图像完美像素
图像缩小
图像缩小（按比例） 
图像缩小（按边） 
图像比率
图片到遮罩
[[imageConcat]]
Image List To Image Batch
Image Batch To Image List 
图像拆分
imageSplitGrid
imagesSplitImage
imageCropFromMask
imageUncropFromBBOX
图像保存
图像背景移除
[[兴趣/AI/1·ComfyUI/3·插件笔记/Image Color Match   图像颜色匹配]]
[[兴趣/AI/1·ComfyUI/3·插件笔记/Image Detail Transfer]]
[[兴趣/AI/1·ComfyUI/3·插件笔记/Image To Prompt]]
Image To Base64 
合并图像批次
Remove Local Image 
[[姿势编辑器]]
### Segmentation 
Human Segmentation
### 逻辑
#### 类型
字符串
整数
整数（范围） 
浮点数
浮点数（范围） 
布尔
#### 数学
比较
if判断
#### 切换
图像切换
Text Switch
#### 其他
判断SDXL
任意XY输入
[[兴趣/AI/1·ComfyUI/3·插件笔记/节点笔记/转换任何]]
展示任何
显示Tensor形状
Clear Cache Key
Clear Cache All
清理GPU占用

## 工作流
## 相关节点
| 节点名 (搜索名)                      | 相关的库                                                                                    | 库相关的节点                  |
| :----------------------------- | :-------------------------------------------------------------------------------------- | :---------------------- |
| easy setNode                   | [ComfyUI-extensions](https://github.com/diffus3/ComfyUI-extensions)                     | diffus3.SetNode         |
| easy getNode                   | [ComfyUI-extensions](https://github.com/diffus3/ComfyUI-extensions)                     | diffus3.GetNode         |
| easy bookmark                  | [rgthree-comfy](https://github.com/rgthree/rgthree-comfy)                               | Bookmark 🔖             |
| easy portraitMarker            | [comfyui-portrait-master](https://github.com/florestefano1975/comfyui-portrait-master)  | Portrait Master         |
| easy LLLiteLoader              | [ControlNet-LLLite-ComfyUI](https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI)      | LLLiteLoader            |
| easy globalSeed                | [ComfyUI-Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack)                | Global Seed (Inspire)   |
| easy preSamplingDynamicCFG     | [sd-dynamic-thresholding](https://github.com/mcmonkeyprojects/sd-dynamic-thresholding)  | DynamicThresholdingFull |
| dynamicThresholdingFull        | [sd-dynamic-thresholding](https://github.com/mcmonkeyprojects/sd-dynamic-thresholding)  | DynamicThresholdingFull |
| easy imageInsetCrop            | [rgthree-comfy](https://github.com/rgthree/rgthree-comfy)                               | ImageInsetCrop          |
| easy poseEditor                | [ComfyUI_Custom_Nodes_AlekPet](https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet) | poseNode                |
| easy if                        | [ComfyUI-Logic](https://github.com/theUpsider/ComfyUI-Logic)                            | IfExecute               |
| easy preSamplingLayerDiffusion | [ComfyUI-layerdiffusion](https://github.com/huchenlei/ComfyUI-layerdiffusion)           | LayeredDiffusionApply等  |
| easy dynamiCrafterLoader       | [ComfyUI-layerdiffusion](https://github.com/ExponentialML/ComfyUI_Native_DynamiCrafter) | Apply Dynamicrafter     |
| easy imageChooser              | [cg-image-picker](https://github.com/chrisgoringe/cg-image-picker)                      | Preview Chooser         |
| easy styleAlignedBatchAlign    | [style_aligned_comfy](https://github.com/chrisgoringe/cg-image-picker)                  | styleAlignedBatchAlign  |
| easy icLightApply              | [ComfyUI-IC-Light](https://github.com/huchenlei/ComfyUI-IC-Light)                       | ICLightApply等           |


