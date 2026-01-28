  
![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-54.jpg)

先来看看我们熟悉的局部重绘 ，ControlNet 中的 Inpaint 相当于更换了原生图生图的算法，在使用时还是受重绘幅度等参数的影响。如下图的案例中我们使用较低的重绘幅度，可以实现不错的真实系头像转二次元效果，且对原图中的人物发型、发色都能比较准确的还原。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-55.jpg)

想配合 ControlNet 使用局部重绘 ，同样需要在图生图中进行操作，在涂抹完蒙版并设置参数后，我们打开 ControlNet 选择局部重绘控制项。注意在图生图板块使用 ControlNet 的局部重绘时默认无需再额外上传图片，ControlNet 会自动读取图生图中上传的图片。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-56.jpg)

下图是图生图中局部重绘关闭和开启 ControlNet 时的效果对比，同样是在重绘幅度=1 的情况下，开启 ControlNet 的画面稳定性会更强，在和环境融合方面也可以处理的更好。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-57.jpg)

局部重绘这里提供了 3 种预处理器，Global_Harmonious、only 和 only+lama，通过下图案例整体来看出图效果上差异不大，但在环境融合效果上 Global_Harmonious 处理效果最佳，only 次之，only+lama 最差。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-58.jpg)