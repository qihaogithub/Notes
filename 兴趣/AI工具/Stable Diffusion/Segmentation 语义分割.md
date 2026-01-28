Seg 语义分割

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-30.jpg)

Segmentation 的完整名称是 Semantic Segmentation 语义分割，很多时候简称为 Seg。和以上其他线稿类控制类型不同，它可以在检测内容轮廓的同时将画面划分为不同区块，并对区块赋予语义标注，从而实现更加精准的控图效果。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-31.jpg)

观察下图我们可以看到，Seg 预处理器检测后的图像包含了不同颜色的板块图，就像现实生活中的区块地图。画面中不同的内容会被赋予相应的颜色，比如人物被标注为红色、屋檐是绿色、路灯是蓝色等，这样限定区块的方式有点类似局部重绘的效果，在生成图像时模型会在对应色块范围内生成特定对象，从而实现更加准确的内容还原。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-32.jpg)

针对不同颜色色值表示的含义，我这边已经为大家整理好完整的色值语义标注文档，需要的小伙伴可以在文章结尾处获取。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-33.jpg)

Seg 也提供了三种预处理器可供选择：OneFormer ADE20k、OneFormer COCO、UniFormer ADE20k。尾缀 ADE20k 和 COCO 代表模型训练时使用的 2 种图片数据库，而前缀 OneFormer 和 UniFormer 表示的是算法。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-34.jpg)

其中 UniFormer 是旧算法，但由于实际表现还不错依旧被作者作为备选项保留下来，新算法 OneFormer 经过作者团队的训练可以很好的适配各种生产环境，元素间依赖关系被很好的优化，平时使用时建议大家使用默认的 OneFormer ADE20k 即可。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-35.jpg)

再来看看不同预处理器的实际出图效果，这里我们将环境由白天切换到黑夜，可以发现由于算法数据库不同，可识别的物体会稍有差异，比如第二种算法 OneFormer COCO 对书店雨棚的还原效果不是很好。实际使用时大家也可以根据语义数据表自行填充色块来标识对应的画面元素。