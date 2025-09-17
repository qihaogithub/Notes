## 教程
[B 站教程](https://www.bilibili.com/video/BV1MU411o7et/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d)
[知乎教程](https://zhuanlan.zhihu.com/p/698647710)
## 安装
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202407030856108.png)
需要安装模型

## 工作流


![](https://pic1.zhimg.com/80/v2-8ed59558b5a6f0c447eefa4a6bc440e8_1440w.webp)
### 输入模块
输入模块，用到了两个加载图片节点，分别加载对象（产品、人物），和风格参考。


![](https://pic1.zhimg.com/80/v2-91da2c96af5f576af7aa6a97656e1d60_1440w.webp)
### 提示词处理

为了让流程极简，不需要手动输入提示词，我用到了LLava反推节点，读取输入图的对象，还有参考图的风格。  
提示词还串联了ICLight官方的对灯光描述的提示词。

![](https://pic1.zhimg.com/80/v2-eac14b7d344212c862b82d1ca6057e2c_1440w.webp)
官方灯光描述提示词：

```text
natural lighting
sunshine from window
neon light
sunset over sea
golden time
sci-fi RGB glowing, cyberpunk
warm atmosphere, at home, bedroom
code atmosphere, at home, bedroom
soft studio lighting
neon, Wong Kar-wai, warm
home atmosphere, cozy bedroom illumination
```

根据风格，在这个节点进行选择即可。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202407030850347.png)
然后把这些提示词串起来，作为正向提示词，传入采样器中。

### Brushnet换背景融图

用到了官方的Brushnet换背景流程，但这里加上IPAapter节点，用于生成参考风格的背景。还有通过Canny控制，让背景和主题产生关系。

​

![](https://pic1.zhimg.com/80/v2-d974b684ef88f668077a463010fbf35c_1440w.webp)

​

### 光照模块

通过ICLight工作流程，对上面生成的图进行打光处理。

​

![](https://pic2.zhimg.com/80/v2-dffebe9d1a968b875692dfd2df08d965_1440w.webp)

​

这里需要对合成图时，对蒙板进行处理，使其图片合并时，不会太生硬。

​

![](https://pic3.zhimg.com/80/v2-2d3fb69f8197f4c475cce01484f6fc2a_1440w.webp)

​

### 灯光贴图生成

当然，在ICLight工作前，需要生成一个灯光贴图。用到了KJNote，可以方便地生成，渐变图，代表灯光的走向。

​

![](https://pic2.zhimg.com/80/v2-d6e3ca0c1e018d9391b8d2f8563e3c69_1440w.webp)

​

### 调色

用到了HDR调整、色彩调整两个节点，使颜色看起来更合理些。

​

![](https://pic4.zhimg.com/80/v2-051012f901eedcc3b7dcd0b0f12cf4f7_1440w.webp)

​