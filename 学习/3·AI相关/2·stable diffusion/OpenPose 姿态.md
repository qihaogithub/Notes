  
![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-49.jpg)

OpenPose 特点是可以检测到人体结构的关键点，比如头部、肩膀、手肘、膝盖等位置，而将人物的服饰、发型、背景等细节元素忽略掉。它通过捕捉人物结构在画面中的位置来还原人物姿势和表情。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-50.jpg)

在 OpenPose 中为我们内置了 openpose、face、faceonly、full、hand 这 5 种预处理器，它们分别用于检测五官、四肢、手部等人体结构。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-51.jpg)

1. openpose 是最基础的预处理器，可以检测到人体大部分关键点，并通过不同颜色的线条连接起来。
2. face 在 openpose 基础上强化了对人脸的识别，除了基础的面部朝向，还能识别眼睛、鼻子、嘴巴等五官和脸部轮廓，因此 face 在人物表情上可以实现很好的还原。
3. faceonly 只针对处理面部的轮廓点信息，适合只刻画脸部细节的场景。
4. hand 相当于在 openpose 基础上增加了手部结构的刻画，可以很好的解决常见的手部变形问题。
5. full 是对以上所有预处理功能的集合，可以说是功能最全面的预处理器。

想要将上面的处理器挨个记下十分麻烦，平时使用时建议直接选择包含了全部关键点检测的 full 预处理器即可。

![万字干货！一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://image.uisdc.com/wp-content/uploads/2023/09/uisdc-sx-20230925-52.jpg)

除了基本的人体姿势，预处理器中包含了对人物五官和手部的结构信息，因此 OpenPose 在处理表情和手部等人体细节上是很不错的控图工具。