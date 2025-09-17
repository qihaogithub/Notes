
### 配置模型

**模型位置：**

1. ComfyUI 虽然部署好环境和依赖，但是里面没有模型，我们需要把模型放到对应位置，比如：

a. 大模型放入`ComfyUI_windows_portable\ComfyUI\models\checkpoints`

b. VAE 模型放入“ComfyUI_windows_portable\ComfyUI\models/vae”

c. Lora 模型“ComfyUI_windows_portable\ComfyUI\models/loras”

![超详细的 Stable Diffusion ComfyUI 基础教程（一）：安装与常用插件](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sd-20230924-4.jpg)

2. 如果装有 Web UI 的小伙伴先别着急，我们可以使 ComfyUI 和 Web UI 共用一套模型，以防复制大量模型浪费空间。

### ComfyUI 与 WebUI 之间共享模型

在 ComfyUI 目录中将 extra_model_paths.yaml.example文件复制一份
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202404021611180.png)
将此文件重命名为 extra_model_paths.yaml （去掉.example），修改完成后有文本编辑器打开（记事本就可以）。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202404021611179.png)
3. 把里面 base_path:的路径改成你需要共享的 webui 的安装地址。比如我的是“G:\sd-webui”

1. controlnet 是否修改取决于你的 controlnet 模型安装在哪个目录，如果和我一样是安装在 controlnet 插件下的，那就改成和我一样的“`extensions\sd-webui-controlnet\models`”。（如果你 a1111 还是遵循老目录 controlnet 的模型存放目录，还是放在 model\controlnet\ 下，那就不用改)



## 模型下载
realisticVisionV51_v51VAE.safetensors
https://download.tusiassets.com/users%2FCHECKPOINT%2F649580474594826652%2F97BaZatUp8Io1rK6VToMw.safetensors?auth_key=1719651380-a6f7109a0f5943c686f6b95caaa6731a-0-4803bda8078019d003dcd204d1c0de0d