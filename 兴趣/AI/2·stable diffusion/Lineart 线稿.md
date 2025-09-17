Lineart 同样也是对图像边缘线稿的提取，但它的使用场景会更加细分，包括 Realistic 真实系和 Anime 动漫系 2 个方向。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-18.jpg)

在 ControlNet 插件中，将 lineart 和 lineart_anime2 种控图模型都放在「Lineart（线稿）」控制类型下，分别用于写实类和动漫类图像绘制，配套的预处理器也有 5 个之多，其中带有 anime 字段的预处理器用于动漫类图像特征提取，其他的则是用于写实图像。

在下图中我们可以看到，Canny 提取后的线稿类似电脑绘制的硬直线，粗细统一都是 1px 大小，而 Lineart 则是有的明显笔触痕迹线稿，更像是现实的手绘稿，可以明显观察到不同边缘下的粗细过渡。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-19.jpg)

虽然官方将 Lineart 划分为 2 种风格类型，但并不意味着他们不能混用，实际上我们可以根据效果需求自由选择不同的绘图类型处理器和模型。

下图中为大家展示了不同预处理器对写实类照片上的处理效果，可以发现后面 3 种针对真实系图片使用的预处理器 coarse、realistic、standard 提取的线稿更为还原，在检测时会保留较多的边缘细节，因此控图效果会更加显著，而 anime、anime_denoise 这 2 种动漫类则相对比较随机。具体效果在不同场景下各有优劣，大家酌情选择使用。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-20.jpg)

为方便对比模型的控图效果，选用一张更加清晰的手绘线稿图分别使用 lineart 和 lineart_anime 模型进行绘制，可以发现 lineart_anime 模型在参与绘制时会有更加明显的轮廓线，这种处理方式在二次元动漫中非常常见，传统手绘中描边可以有效增强画面内容的边界感，对色彩完成度的要求不高，因此轮廓描边可以替代很多需要色彩来表现的内容，并逐渐演变为动漫的特定风格。可以看出 lineart_anime 相比 lineart 确实更适合在绘制动漫系图像时使用。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-21.jpg)