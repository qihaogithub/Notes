
![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-74.jpg)

Recolor 也是近期刚更新的一种 ControlNet 类型，它的效果是给图片填充颜色，非常适合修复一些黑白老旧照片。但 Recolor 无法保证颜色准确出现特定位置上，可能会出现相互污染的情况，因此实际使用时还需配合如打断等提示词语法进行调整。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-75.jpg)

Recolor 无需配合模型使用，这里也提供了 intensity 和 luminance2 种预处理器，通常推荐使用 luminance，预处理的效果会更好。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-76.jpg)

Recolor 的参数 Gamma Correction 伽马修正用于调整预处理时检测的图像亮度，下图中可以看到随着数值增大，预处理后的图像会越暗。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-77.jpg)