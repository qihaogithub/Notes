![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-13.jpg)

下面我们再来看第二种控图类型：MLSD 直线。MLSD 提取的都是画面中的直线边缘，在下图中可以看到 mlsd（M-LSD 直线线条检测）预处理后只会保留画面中的直线特征，而忽略曲线特征。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-14.jpg)

因此 MLSD 多用于提取物体的线型几何边界，最典型的就是几何建筑、室内设计、路桥设计等领域。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-15.jpg)

MLSD 预处理器同样也有自己的定制参数，分别是 MLSD Value Threshold 强度阈值和 MLSD Distance Threshold 长度阈值。MLSD 阈值控制的是 2 个不同方向的参数：强度和长度，它们的数值范围都是 0～20 之间。

Value 强度阈值用于筛选线稿的直线强度，简单来说就是过滤掉其他没那么直的线条，只保留最直的线条。通过下面的图我们可以看到随着 Value 阈值的增大，被过滤掉的线条也就越多，最终图像中的线稿逐渐减少。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-16.jpg)

Distance 长度阈值则用于筛选线条的长度，即过短的直线会被筛选掉。在画面中有些被识别到的短直线不仅对内容布局和分析没有太大帮助，还可能对最终画面造成干扰，通过长度阈值可以有效过滤掉它们。不过该参数对线稿密度的影响没有那么明显，在下图中可以看到在极值情况下会有少部分线条被过滤掉。
![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-17.jpg)