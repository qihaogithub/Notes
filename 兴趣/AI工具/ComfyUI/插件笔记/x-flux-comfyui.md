[Github 地址](https://github.com/XLabs-AI/x-flux-comfyui)
对于 flux 模型使用 ControlNet，需要使用此插件
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/new/20240817112137.png)
插件所使用的 [ControlNet 模型地址](https://huggingface.co/XLabs-AI/flux-controlnet-collections)


# ## 安装：
1. 转至`ComfyUI/custom_nodes`
2. 克隆此 repo，路径应为`ComfyUI/custom_nodes/x-flux-comfyui/*`，其中 * 是此 repo 中的所有文件
3. 转到 `ComfyUI/custom_nodes/x-flux-comfyui/`并运行`python setup.py`
4. 安装后运行 ComfyUI 并享受！

首次启动后，将自动创建`ComfyUI/models/xlabs/loras`和文件夹。 因此，要使用 lora 或 controlnet，只需将模型放入这些文件夹中。 之后，您可能需要在用户友好界面中单击“刷新”才能使用模型。 对于 controlnet，您需要安装[https://github.com/Fannovel16/comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)`ComfyUI/models/xlabs/controlnets`