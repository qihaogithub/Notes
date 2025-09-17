---
类型:
  - ControlNet
---

![](https://image.uisdc.com/wp-content/uploads/2024/03/uisdc-xt-20240306-24.jpg)

①介绍：Binary 二值化预处理器属于涂鸦类型的预处理器，使用涂鸦算法把图像颜色转换为黑白（Scribble 涂鸦预处理器的可调节版，控制效果没有 Canny 或 HED 严格）；

②阈值：当色值高于阈值的像素会被处理为 1（白色），低于阈值的像素会被处理为 0（黑色），（当阈值为 0 时，效果与 255 相同）

③对应模型：

1.  SD 1.5 模型：control\_v 11 p\_sd 15_scribble
2.  SDXL 模型：暂无

④效果预览：

![](https://image.uisdc.com/wp-content/uploads/2024/03/uisdc-xt-20240306-25.jpg)