![|300](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202407010932436.png)
介绍：与 HED 类似，从图像提取边缘以及柔和边缘过渡，但线条细节更丰富；

safe_steps：数值越小，柔和边缘过渡区域越小；数值越大柔和边缘过渡区域越大；（数值区间：0-10，0 与 10 效果相同）

对应模型：
1. SD1.5 模型：control_v11p_sd15_softedge
2. SDXL 模型：controlnet-sd-xl-1.0-softedge-dexined

效果预览：

![Stable Diffusion ComfyUI 进阶教程（一）：Controlnet 线条预处理器](https://image.uisdc.com/wp-content/uploads/2024/03/uisdc-xt-20240306-9.jpg)