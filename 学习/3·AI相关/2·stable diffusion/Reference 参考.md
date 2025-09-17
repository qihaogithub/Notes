

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-70.jpg)

Reference 使用时不需要使用模型，它的功能很简单，就是参考原图生成一张新的图像，想使用它需要将 ControlNet 更新到至少 v1.1.153 以上。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-71.jpg)

Reference 的实际效果类似 InstructP2P 的图生图，这里提供了 3 个预处理器 adain、adain+attn、only。其中 adain、adain+attn 是 V1.1.171 版本后新增的预处理器，其中 adain 表示 Adaptive Instance Normalization 自适应实例规范化，+attn 表示 Attention 链接。

根据作者测试，adain+attn 使用的是目前最先进的算法，但有时效果过于强烈，因此依旧建议使用默认的 only 预处理。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-72.jpg)

Reference 启用后下方会出现 Style Fidelity 风格保真度的参数项，数值越大则画面的稳定性越强，原图的风格保留痕迹会越明显。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-73.jpg)