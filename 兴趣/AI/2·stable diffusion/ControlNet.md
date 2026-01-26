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
[[兴趣/AI/2·stable diffusion/Canny 硬边缘]]
[[兴趣/AI/2·stable diffusion/MLSD 直线]]
[[兴趣/AI/2·stable diffusion/Lineart 线稿]]
[[兴趣/AI/2·stable diffusion/SoftEdge 软边缘]]
[[Scribble-Sketch 涂鸦-草图]]
[[兴趣/AI/2·stable diffusion/Segmentation 语义分割]]
### 景深类
通过画面中物体的前后景深关系来控制图像
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230928144008.png)

[[兴趣/AI/2·stable diffusion/Depth 深度]]
[[兴趣/AI/2·stable diffusion/NormalMap 法线贴图]]
### 对象类
通过人物的骨架特征或面部轮廓来控制图像
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230928144110.png)

[[兴趣/AI/2·stable diffusion/OpenPose 姿态]]
### 重绘类
通过原图参考来绘制，没有可视化的特征提取，类似图生图
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230928144232.png)

[[兴趣/AI/2·stable diffusion/Inpaint 局部重绘]]
[[兴趣/AI/2·stable diffusion/Tile 分块]]
[[兴趣/AI/2·stable diffusion/InstructP2P 指导图生图]]
[[兴趣/AI/2·stable diffusion/Shuffle 随机洗牌]]
## 社区模型
社区模型的使用频率并不高，很多效果也是对现有功能的优化或调整，大致了解其功能即可，如果有特定需求可以下载对应模型进行尝试，其中有些已经支持配合 SDXL 使用。

[[兴趣/AI/2·stable diffusion/Reference 参考]]
[[兴趣/AI/2·stable diffusion/Recolor 重新上色]]
[[兴趣/AI/2·stable diffusion/T2I-Adapter 文生图适配器]]
[[兴趣/AI/2·stable diffusion/IP-Adapter 图生图适配器]]
## 应用场景
[[兴趣/AI/2·stable diffusion/一键换背景]] · [[兴趣/AI/2·stable diffusion/人物与背景融合]] · [[兴趣/AI/2·stable diffusion/控制图片光源]] · [[兴趣/AI/2·stable diffusion/变更风格]] · [[兴趣/AI/2·stable diffusion/手势控制]] · [[兴趣/AI/2·stable diffusion/局部重绘图片融合]] · [[兴趣/AI/2·stable diffusion/三视图]] · [[兴趣/AI/2·stable diffusion/生成手绘图]]
