Depth 深度

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-37.jpg)

深度图也被称为距离影像，可以将从图像采集器到场景中各点的距离（深度）作为像素值的图像，它可以直接体现画面中物体的三维深度关系。学习过三维动画知识的朋友应该听说过深度图，该类图像中只有黑白两种颜色，距离镜头越近则颜色越浅（白色），距离镜头越近则颜色越深（黑色）。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-38.jpg)

Depth 模型可以提取图像中元素的前后景关系生成深度图，再将其复用到绘制图像中，因此当画面中物体前后关系不够清晰时，可以通过 Depth 模型来辅助控制。下图中可以看到通过深度图很好的还原了建筑中的空间景深关系。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-39.jpg)

Depth 的预处理器有四种：LeReS、LeReS++、MiDaS、ZoE，下图中我们可以看到这四种预处理器的检测效果。

对比来看，LeReS 和 LeReS++的深度图细节提取的层次比较丰富，其中 LeReS++会更胜一筹。而 MiDaS 和 ZoE 更适合处理复杂场景，其中 ZoE 的参数量是最大的，所以处理速度比较慢，实际效果上更倾向于强化前后景深对比。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-40.jpg)

根据预处理器算法的不同，Depth 在最终成像上也有差异，下面案例中可以看到 MiDaS 算法可以比较完美的还原场景中的景深关系，实际使用时大家可以根据预处理的深度图来判断哪种深度关系呈现更加合适。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-41.jpg)