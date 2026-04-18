[GitHub 地址](https://github.com/city96/ComfyUI-GGUF?tab=readme-ov-file)
降低 flux 模型的配置要求

# ComfyUI-GGUF
GGUF 量化支持原生 ComfyUI 模型

目前，这在很大程度上仍处于开发阶段。这些自定义节点为以[llama.cpp](https://github.com/ggerganov/llama.cpp)流行的 GGUF 格式存储的模型文件提供支持。

虽然量化不适用于常规 UNET 模型 (conv2d)，但 flux 等 transformer/DiT 模型似乎受量化的影响较小。这允许在低端 GPU 上以低得多的比特/权重变量比特率量化运行它。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20240817121650.png)

注意：“强制/设置 CLIP 设备”不是**此**节点包的一部分。如果您只有一个 GPU，请不要安装它。如果您不明白它的用途，请不要将其设置为 cuda:0，然后抱怨 OOM 错误。无需复制上述工作流程，只需使用您自己的工作流程并将常用的“加载扩散模型”替换为“Unet Loader (GGUF)”节点。

## 安装

```ad-note
title: 重要的
确保您的 ComfyUI 是足够新的版本，以便在加载仅限 UNET 时支持自定义操作。
```
要正常安装自定义节点，请 git clone 此存储库并安装推理的唯一依赖项（`pip install --upgrade gguf`）
```
git clone https://github.com/city96/ComfyUI-GGUF
```
要在独立服务器上安装自定义节点，请在“ComfyUI_windows_portable”文件夹（您的文件所在的位置）内打开 CMD`run_nvidia_gpu.bat`并使用以下命令：
```
git clone https://github.com/city96/ComfyUI-GGUF ComfyUI/custom_nodes/ComfyUI-GGUF
.\python_embeded\python.exe -s -m pip install -r .\ComfyUI\custom_nodes\ComfyUI-GGUF\requirements.txt
```

## 用法
只需使用类别下的 GGUF Unet 加载器即可`bootleg`。将 .gguf 模型文件放在您的`ComfyUI/models/unet`文件夹中。
预量化模型：
- [flux1-dev GGUF](https://huggingface.co/city96/FLUX.1-dev-gguf)
- [flux1-schnell GGUF](https://huggingface.co/city96/FLUX.1-schnell-gguf)

```ad-attention
title: 警告
由于权重被量化，LoRA / Controlnet / 等目前不受支持。
```
