  
![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-42.jpg)

另一种可以体现景深关系的图像叫 NormalMap 法线贴图，要理解它的工作原理，我们需要先回顾下法线的概念。

我们在中学时期有学过法线，它是垂直与平面的一条向量，因此储存了该平面方向和角度等信息。我们通过在物体凹凸表面的每个点上均绘制法线，再将其储存到 RGB 的颜色通道中，其中 R 红色、G 绿色、B 蓝色分别对应了三维场景中 XYX 空间坐标系，这样就能实现通过颜色来反映物体表面的光影效果，而由此得到的纹理图我们将其称为法线贴图。由于法线贴图可以实现在不改变物体真实结构的基础上也能反映光影分布的效果，被广泛应用在 CG 动画渲染和游戏制作等领域。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-43.jpg)

ControlNet 的 NormalMap 模型就是根据画面中的光影信息，从而模拟出物体表面的凹凸细节，实现准确还原画面内容布局，因此 NormalMap 多用于体现物体表面更加真实的光影细节。下图案例中可以看到使用 NormalMap 模型绘图后画面的光影效果立马有了显著提升。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-44.jpg)

NormalMap 有 Bae 和 Midas2 种预处理器，MiDaS 是早期 v1.0 版本使用的预处理器，官方已表示不再进行维护，平时大家使用默认新的 Bae 预处理器即可，下图是 2 种预处理器的提取结果。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-45.jpg)

当我们选择 MiDaS 预处理器时，下方会多出 Background Threshold 背景阈值的参数项，它的数值范围在 0～1 之间。通过设置背景阈值参数可以过滤掉画面中距离镜头较远的元素，让画面着重体现关键主题。下图中可以看到，随着背景阈值数值增大，前景人物的细节体现保持不变，但背景内容逐渐被过滤掉。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-46.jpg)

对比 Bae 和 Midas 预处理器的出图效果，也能看出 Bae 在光影反馈上明显更胜一筹。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-47.jpg)