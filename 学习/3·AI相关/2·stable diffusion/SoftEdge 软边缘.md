  
![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-22.jpg)

Soft Edge 是一种比较特殊的边缘线稿提取方法，它的特点是可以提取带有渐变效果的边缘线条，由此生成的绘图结果画面看起来会更加柔和且过渡自然。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-23.jpg)

在 SoftEdge 中提供了 4 种不同的预处理器，分别是 HED、HEDSafe、PiDiNet 和 PiDiNetSafe。

在官方介绍的性能对比中，模型稳定性排名为 PiDiNetSafe > HEDSafe > PiDiNet > HED，而最高结果质量排名 HED > PiDiNet > HEDSafe > PiDiNetSafe，综合考虑后 PiDiNet 被设置为默认预处理器，可以保证在大多数情况下都能表现良好。在下图中我们可以看到 4 种预处理器的实际检测图对比。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-24.jpg)

下图中分别使用不同预处理器进行绘图效果对比，体感上没有太大差异，正常情况下使用默认的 PiDiNet 即可。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-25.jpg)