---
类型:
  - ControlNet
---

[Github 地址](https://github.com/TheMistoAI/ComfyUI-Anyline)

Anyline 是一款新的线条类预处理模型，可以从大部分图像中快速提取高精度的线稿图。与其他常用的线条预处理器相比，Anyline 在轮廓精度、对象细节和字体识别（尤其是在大型场景中）方面具有显著优势。在大多数场景中，它在减少噪点方面也表现更好，能实现更清晰的图像处理。

如果是 ComfyUI，需要先安装一个名为 comfyui-anyline 的插件，可以从 manager 中安装，也可以通过 github 克隆。安装完成后，再进入插件文件夹中，打开终端执行 pip install -r requirements.txt 命令。然后重启 comfyui，搜索 “anyline” 即可找到对应节点。