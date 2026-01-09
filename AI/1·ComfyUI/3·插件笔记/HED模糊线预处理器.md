![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202407010930757.png)
相对于 Canny 处理的锐利边缘线，HED 提供了边缘过渡，可以保留更多柔和的边缘细节，类似手绘效果（好处：通过线条区分画面层次，以及图像中的柔和边缘。能更好的融入画面，减少画面细节的突兀）

稳增：开启后会使提取的线条明暗对比更明显，模糊内容也会减少。选择是否增稳，具体看图片生成效果。

对应模型：

1. SD1.5 模型：control_v11p_sd15_softedge
2. SDXL 模型：暂无

效果预览：

![Stable Diffusion ComfyUI 进阶教程（一）：Controlnet 线条预处理器](https://image.uisdc.com/wp-content/uploads/2024/03/uisdc-xt-20240306-5.jpg)