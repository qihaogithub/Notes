
![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-78.jpg)

T2I-Adapter 由腾讯 ARC 实验室和北大视觉信息智能学习实验室联合研发的一款小型模型，它的作用是为各类文生图模型提供额外的控制引导，同时又不会影响原有模型的拓展和生成能力。名称中 T2I 指的是的 text-to-image，即我们常说的文生图，而 Adapter 是适配器的意思。

T2I-Adapter 被集成在 ControlNet 中作为某一控制类型的选项，但实际上它提供了 Lineart、Depth、Sketch、Segmentation、Openpose 等多个类型的控图模型来使用。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-79.jpg)

T2I-Adapter 的特点是体积小，参数级只有 77M，但对图像的控制效果已经很好，且就在 9 月 8 日，它们针对 SDXL 训练的控图模型刚刚发布，是目前最推荐用于 SDXL 的 ControlNet 模型，但需要注意的是 SDXL 类模型对硬件要求较高，官方建议至少需要 15GB 的显卡内存，想体验的小伙伴可在下面地址中自行下载安装到本地。

T2I-Adapter 控图模型代码仓库地址： [https://huggingface.co/TencentARC/T2I-Adapter/tree/main/models](https://link.uisdc.com/?redirect=https%3A%2F%2Fhuggingface.co%2FTencentARC%2FT2I-Adapter%2Ftree%2Fmain%2Fmodels)

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-80.jpg)