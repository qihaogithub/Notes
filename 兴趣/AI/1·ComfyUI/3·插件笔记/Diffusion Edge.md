

![Stable Diffusion ComfyUI 进阶教程（一）：Controlnet 线条预处理器](https://image.uisdc.com/wp-content/uploads/2024/03/uisdc-xt-20240306-20.jpg)

①介绍：从图像提取边简单边缘线（此预处理器我为找到未找到官方介绍以及算法介绍）；

② environment：针对 indoor（室内）、urban（城市）、natrual（自然）图像进行选择处理；

③patch_batgh_size：未发现明显区别；（数值区间：1-16）

④对应模型：未找到官方推荐模型，图像处理效果偏向于 canny、lineart，可使用这几种预处理器对应的模型，我试了一下，效果都挺不错的；

⑤效果预览：

![Stable Diffusion ComfyUI 进阶教程（一）：Controlnet 线条预处理器](https://image.uisdc.com/wp-content/uploads/2024/03/uisdc-xt-20240306-21.jpg)