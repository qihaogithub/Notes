# UV变换 uv transform

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image_VdoNSIW3JI.png)

此着色器可用于本地修改 UV，从而控制 2D 纹理放置到曲面上的方式（使用曲面的 UV 坐标将纹理放置到曲面上）。

可以使用“缩放”(Scale)、“平移帧”(Translate Frame)和“旋转帧”(Rotate Frame)属性控制图像在曲面上的位置、大小和旋转。

还可以使用“重复”(Repeat)、“旋转”(Rotate)、“偏移”(Offset)、“镜像”(Mirror)、“交错”(Stagger)和“包裹”(Wrap)属性控制纹理在帧内的平铺方式。

**passthrough**

首先对穿过输入求值，然后将其按原样传递到输出。

**unit**

将旋转角度单位设置为“弧度”(radians)、“度”(degrees)或“规格化(normalized)”。

**uv\_set**

用于对图像进行采样的具有 UV 集名称的字符串。默认情况下，当 UV 集参数为空时，将使用多边形网格中的主 UV 集。

示例：如果您在名为“UVset2”的多边形网格节点中创建了 UV 集，那么您可以将 UV 集设置为“UVset2”来使用此 UV 集。

**coverage**

控制曲面中有多大部分将被纹理帧覆盖。

**scale\_frame**

控制曲面中有多大部分将被纹理覆盖。默认值（1、1、0）表示将覆盖整个曲面。减小这些值可使纹理变小。

例如，如果将“U 向比例”(Scale U)更改为 0.5，则纹理将在 U 方向仅覆盖曲面的一半。

**translate\_frame**

控制纹理相对于枢轴帧值的位置（默认值为 0、0、0）。增大这些值可远离枢轴移动纹理帧。

例如，当“平移 U 向帧”(Translate Frame U)设置为 0.5 时，纹理将沿曲面偏移一半。

**rotate\_frame**

控制纹理帧相对于曲面的旋转量。

**pivot\_frame**

控制纹理帧相对于曲面的原点。

**wrap\_frame\_u**

控制纹理如何在一个大型曲面上重复。选择“周期”(periodic)、“颜色”(color)、“区间限定”(clamp)或“镜像”(mirror)。默认包裹模式为“周期”(periodic)。请参见下面各种不同的模式。

**wrap\_frame\_v**

控制纹理如何在一个大型曲面上重复。选择“周期”(periodic)、“颜色”(color)、“区间限定”(clamp)或“镜像”(mirror)。默认包裹模式为“周期”(periodic)。

**wrap\_frame\_color**

定义“颜色”(color)包裹模式中使用的颜色。另外，还可以将着色器链接到此参数。

**repeat**

控制纹理的重复次数。

**offset**

偏移 Offsets the image in the U direction. This offset takes place before scaling, flipping, or swapping of the S and T coordinates.

**rotate**

控制纹理在纹理帧内的旋转量（帧本身不旋转）。要旋转帧，请改用“旋转帧”(Rotate Frame)属性。

**pivot**

对任何值的修改均基于此原点值。

**noise**

U 和 V 的 2D 噪波。

**mirror\_u**

控制纹理平铺如何彼此并排放置。启用后，纹理的每个副本将是该纹理在其 U 侧的镜像图像，其共享边是反射的 (V) 轴。

**mirror\_v**

控制纹理平铺如何彼此并排放置。启用后，纹理的每个副本将是该纹理在其 V 侧的镜像图像，其共享边是反射的 (U) 轴。

**flip\_u**

水平镜像

**flip\_v**

垂直镜像

**swap\_uv** 交换轴心。

**stagger**

控制彼此并排放置的纹理平铺的对齐情况。启用后，纹理平铺会每隔一行偏移其宽度的一半，类似于砖墙砖块的堆叠方式。
