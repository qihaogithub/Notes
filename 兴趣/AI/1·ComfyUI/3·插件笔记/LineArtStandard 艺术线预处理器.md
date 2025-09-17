![|375](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202407010934194.png)
相较于 LineArt 艺术线预处理器，增加了亮面和暗面过渡区域（美术生小伙伴肯定熟悉，这就是我们画画时常说的明暗交界线）


Guassian_sigma：用来控制高斯模糊的数值大小；数值越小，亮暗面过渡区域越小；数值越大，亮暗面过渡区域越大；（数值区间：0-100）

强度阈值：数值越小，亮暗面过度区域越大；数值越大，亮暗面过度区域越小；（数值区间：0-16）

对应模型：

1. SD1.5 模型：control_v11p_sd15_lineart
2. SDXL 模型：暂无

效果预览：

![Stable Diffusion ComfyUI 进阶教程（一）：Controlnet 线条预处理器](https://image.uisdc.com/wp-content/uploads/2024/03/uisdc-xt-20240306-13.jpg)