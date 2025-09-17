[[flux Hyper加速]]

官网地址： https://blackforestlabs.ai/#get-flux
Github 地址： https://github.com/black-forest-labs/flux
Hugging face： https://huggingface.co/black-forest-labs/FLUX.1-dev

cfg 官方推荐3.5，大家可以自行调节。
采样步数默认20，可酌情提高。
在WEBUI使用目前采样方法只支持FlowMatchEuler，Embedding兼容SD1.5的，用SDXL的可能会有问题（不绝对）。

## 使用
FLUX 需要下载 Flux.1模型、VAE 模型和两个Clip模型

### 下载Flux.1模型
官方提供了Flux.1系列模型，共有三个：
Flux.1[pro]是闭源的，可以从官方 API 申请访问权限，同时支持企业定制。
Flux.1[dev]开源，不可商用，直接从 FLUX.1 [pro] 蒸馏而来，具备相似的图像质量和提示词遵循能力，但是更高效。
Flux.1[schnell]：开源模型，可商用，专门为本地开发和个人使用量身定制，生成速度最快，内存占用也最小。

#### 官方Dev 版本：
电脑运行内存不低于32G,实测4090占满显存
_ https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main_

#### 社区dev -fp8版本-11 G 显存
小显存可使用
[FLUX.1哩布在线可运行-黑暗森林工作室](https://www.liblib.art/modelinfo/488cd9d58cd4421b9e8000373d7da123?from=search)
https://huggingface.co/Kijai/flux-fp8

flux1-dev-fp8.safetensors 属于[FLUX.1 [dev]非商业许可证]( https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md )。
flux1-schnell-fp8.safetensors 属于 [Apache-2.0 许可证](https://huggingface.co/datasets/choosealicense/licenses/blob/main/markdown/apache-2.0.md)。

> **推荐fp8版本**，速度会快一些，并且稳定。
> fp16版本会在加载上略慢，且容易爆显存。
> schnell是turbo版本，效果一般，不推荐。

### 社区 NF 4 版本-6 G 显存可用
NF4模型地址：https://huggingface.co/lllyasviel/flux1-dev-bnb-nf4/tree/main NF4插件地址：https://github.com/comfyanonymous/ComfyUI_bitsandbytes_NF4

将该模型下载到 `/ComfyUI/models/unet/` 文件夹下

### VAE 模型
下载调用Flux所需的VAE
https://huggingface.co/black-forest-labs/FLUX.1-dev/tree/main
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408161534266.png)

将ae.safetensors下载到 `/ComfyUI/models/vae/`文件夹下。

### Clip模型
下载所需的两个Clip编码器（t5.xxl和clip_l）

_https://huggingface.co/stabilityai/stable-diffusion-3-medium/tree/main/text_encoders_

![图片](https://mmbiz.qpic.cn/mmbiz_png/jOXg3NiawibehztUKq07Rl42rf9WLOrYTuzTpghCwqantfhN2X1A8REMAz2yGy8l8cazpxiaEX7R3334ypxQnvJjg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

放置在models文件下的clip文件中即可

下载clip_l和t5xxl模型，其中t5xxl模型有两个，根据自己的显卡情况二选一下载（如果你有超过 16GB 的 ram，建议使用 fp32），放置在 `ComfyUI/models/clip/`文件夹下。

### ControlNet
  
Xlabs-ControlNet模型地址： https://huggingface.co/XLabs-AI/flux-controlnet-collections Xlabs-ControlNet插件地址： https://github.com/XLabs-AI/x-flux-comfyui 

[[Flux 高清放大模型]]

### Lora
Lora模型下载地址：https://huggingface.co/XLabs-AI/flux-lora-collection

## 工作流

[Liblib 工作流](https://www.liblib.art/modelinfo/ec6223dccd7b47658464eaf7b94d7dc5?from=feed)

官方工作流：

进入网站：Flux Examples | ComfyUI_examples (comfyanonymous.github.io)并将下图下载，然后拖入Comfy UI中：

![图片](https://mmbiz.qpic.cn/mmbiz_png/FJvxHdqSMsq6bmXu5yX4t3iblpsdvx5sxulwar5uETlCq64EBRVoT7Ou8BP4jicvNIN6meGmrpicHcNuUJq8haZTA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

然后你的ComfyUI中应该会出选相应的工作流，类似下图:

![图片](https://mmbiz.qpic.cn/mmbiz_png/FJvxHdqSMsq6bmXu5yX4t3iblpsdvx5sxBq9sU0Hib1DO1zcJl5ZOM18tJTubOziaXicFtdzxYE6hZVZuxTzIxNcsA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

至此Flux.1模型就部署在Comfy UI中了，开启你的探索之旅吧！、

## [[Lora 训练]]
