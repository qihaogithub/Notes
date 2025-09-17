---
类型:
  - ControlNet
---
![|325](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202407010928655.png)


阈值（数值区间：0-255）：

1. 低阈值：控制弱边缘检测阈值，数值越低线条越复杂/细节越丰富，数值越高线条越简单/细节越少；
2. 高阈值：控制强边缘检测阈值，数值越低线条越复杂/细节越丰富，数值越高线条越简单/细节越少；

对应模型：

1. SD1.5 模型：control_v11p_sd15_canny、t2iadapter_canny_sd1.5v2
2. SDXL 模型：control-lora-canny-rank128、control-lora-canny-rank256

效果预览：

![Stable Diffusion ComfyUI 进阶教程（一）：Controlnet 线条预处理器](https://image.uisdc.com/wp-content/uploads/2024/03/uisdc-xt-20240306-3.jpg)