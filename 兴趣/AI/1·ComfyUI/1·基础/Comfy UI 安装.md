[Github 地址](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#installing)

# [[云端安装]]


# Apple Mac 芯片安装教程

[视频教程](https://www.bilibili.com/video/BV1ux4y1C7o4/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=81223299ca5d449a34daaab3e1102d1d)

### 克隆 comfyui 项目
在想要安装的位置用终端打开
```
git clone https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#dependencies
```
克隆完之后
将您的 SD checkpoints（巨大的 ckpt/safetensors 文件）放入：models/checkpoints
将您的 VAE 放入：models/vae

### 安装步骤
在终端打开刚刚克隆好的 comfyui 文件夹
然后分别运行以下命令

```
##创建了一个新的虚拟环境
Python3 -m venv venv   

##激活了上面创建的虚拟环境，并使用该环境中的 `pip` 命令来安装三个Python库：`torch`、`torchvision` 和 `torchaudio`
./venv/bin/pip install torch torchvision torchaudio   

##使用虚拟环境中的 `pip` 来安装项目依赖。
./venv/bin/pip install -r requirements.txt

##使用虚拟环境中的 `python` 解释器来运行 `main.py` 脚
./venv/bin/python main.py --force-fp16
```
中途出现以下提示，则复制命令直接运行
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202406221516623.png)


### 运行
1.通过运行启动 ComfyUI `python main.py`
> **注意**：请记住将您的模型、VAE、LoRA 等添加到相应的 Comfy 文件夹中。