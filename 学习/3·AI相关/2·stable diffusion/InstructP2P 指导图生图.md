  
![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-64.jpg)

InstructP2P 的全称为 Instruct Pix2Pix 指导图生图，使用的是 Instruct Pix2Pix 数据集训练的 ControlNet。它的功能可以说和图生图基本一样，会直接参考原图的信息特征进行重绘，因此并不需要单独的预处理器即可直接使用。

下图中为方便对比，我们将重绘幅度降低到 0.1，可以发现开启 InstructP2P 后的出图效果比单纯图生图能保留更多有用细节。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-65.jpg)

IP2P 目前还处于试验阶段，并不是一种成熟的 ControlNet 模型，平时使用并不多，大家大致了解其功能即可。

