上层参考图
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230528215850.png)
点击启用，预处理器和模型要对应，如图都是 openpose

[一口气掌握14种 ControlNet 官方控图模型的使用方法！](https://www.uisdc.com/stable-diffusion-guide-6)
## 官方模型
 [官方模型下载地址](https://link.uisdc.com/?redirect=https%3A%2F%2Fhuggingface.co%2Flllyasviel%2FControlNet-v1-1%2Ftree%2Fmain)
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230928140748.png)

### 轮廓类
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230928142842.png)
通过元素轮廓的线稿和色块来控制图像
[[Canny 硬边缘]]
[[MLSD 直线]]
[[Lineart 线稿]]
[[SoftEdge 软边缘]]
[[Scribble-Sketch 涂鸦-草图]]
[[Segmentation 语义分割]]
### 景深类
通过画面中物体的前后景深关系来控制图像
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230928144008.png)

[[Depth 深度]]
[[NormalMap 法线贴图]]
### 对象类
通过人物的骨架特征或面部轮廓来控制图像
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230928144110.png)

[[OpenPose 姿态]]
### 重绘类
通过原图参考来绘制，没有可视化的特征提取，类似图生图
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230928144232.png)

[[Inpaint 局部重绘]]
[[Tile 分块]]
[[InstructP2P 指导图生图]]
[[Shuffle 随机洗牌]]
## 社区模型
社区模型的使用频率并不高，很多效果也是对现有功能的优化或调整，大致了解其功能即可，如果有特定需求可以下载对应模型进行尝试，其中有些已经支持配合 SDXL 使用。

[[Reference 参考]]
[[Recolor 重新上色]]
[[T2I-Adapter 文生图适配器]]
[[IP-Adapter 图生图适配器]]
## 应用场景
[[一键换背景]] · [[人物与背景融合]] · [[控制图片光源]] · [[变更风格]] · [[手势控制]] · [[局部重绘图片融合]] · [[三视图]] · [[生成手绘图]]
