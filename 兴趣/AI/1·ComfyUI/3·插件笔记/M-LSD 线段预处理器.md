![|375](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202407010936162.png)
介绍：从图片中提取直线线段，弯曲线条不会被提取，多用于建筑设计、室内设计；

刻痕阈值：低于阈值的线条不被检测为边缘，数值越小线越多/也会越乱，数值越大线越少/也会越简单；

距离阈值：线条间的距离低于阈值时会被合并，数值越小线越多/也会越乱，数值越大线越少/也会越简单；

对应模型：

1. SD1.5 模型：control_v11p_sd15_mlsd
2. SDXL 模型：暂无

效果预览：

![Stable Diffusion ComfyUI 进阶教程（一）：Controlnet 线条预处理器](https://image.uisdc.com/wp-content/uploads/2024/03/uisdc-xt-20240306-19.jpg)