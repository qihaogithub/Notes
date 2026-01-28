就在不久前 Adobe 官方出台了更加严厉的政策，市面上所有 ps ai 爱国版全部被封禁，无一幸免。相信很多人最恋恋不舍的就是 ps ai 的**创成式填充功能**了，不用担心，今天就教你用 stable diffusion 一键扩展画面。

首先强调一下放大和扩展是两个不同的概念，放大是指将原有画面进行优化放大，例如高清修复、附加功能的放大，而扩展是在增加画面的同时，**增添新的内容元素在画面当中**，我们今天要介绍的 sd 扩图就是属于后面这种。

**sd 进行扩图推荐在文生图界面完成，图生图会对画面产生较大的改变，不推荐**

首先来到文生图界面，输入提示词随机生成四张 512×768 的图片，挑选其中较为满意的一张哈哈哈，手还是有点问题，但是修手并不是我们今天要讲的主要内容，我们暂时跳过

![](https://picx.zhimg.com/80/v2-b4c9131ba77c6da73873998a60d2bc03_1440w.png?source=d16d100b)

挑选一张满意的图片

![](https://picx.zhimg.com/80/v2-d450f0dae25bd1fbfc236fb95f23648f_1440w.png?source=d16d100b)

512×768

挑选其中较为满意的一张拖入 controlnet，**勾选启用和完美像素模式，显存低于 8 G 的建议勾选低显存模式**

控制类型（Contrlo Type）选择**局部绘制（inpaint）**，需要注意这里的**预处理器需要选择 inpaint_only＋lama**，模型选择 control\_v 11 p\_sd 15 inpaint

![](https://picx.zhimg.com/80/v2-160baa5633943bf41a96728d88230a84_1440w.png?source=d16d100b)

添加图片注释，不超过 140 字（可选）

控制类型（Control Mode）选择 ControlNet is more important，**缩放模式一定要选择 Resize and Fill（缩放后填充空白）**

![](https://pic1.zhimg.com/80/v2-72b21a2c61d9fb9d8cda5d0ec3ffe9b2_1440w.png?source=d16d100b)

添加图片注释，不超过 140 字（可选）

一切准备就绪，接下来我们把图片尺寸修改为 1000×768，增加图片的宽度

![](https://pica.zhimg.com/80/v2-a1f1594a9a34af5508b068b1acb99a86_1440w.png?source=d16d100b)

1000×768

然后我们把图片尺度改为 512×1200，增加图片的高度

![](https://pica.zhimg.com/80/v2-e0f6dfa0342218569d5897bf93c65d5b_1440w.jpeg?source=d16d100b)

512×1200

同时增加宽度和高度，尺度改为 1000×1000

![](https://picx.zhimg.com/80/v2-aab268b612e3f233b291c8412ca227a5_1440w.png?source=d16d100b)

1000×1000

或者我们也可以将之前保存的图片进行扩展，我这里选择一张之前做的橘猫和兰博基尼作为示例

![](https://picx.zhimg.com/80/v2-825ed711c76ceb10d4eefcda392833f9_1440w.png)

橘猫

![](https://picx.zhimg.com/80/v2-21a6bd6cfb60b264de107e2fa278c31a_1440w.png)

兰博基尼

提示词我们就输入一些最简单的画面描述词即可，这里我们启用两个 controlnet，第一个 controlent 选择 inpaint（同上），第二个 controlnet 选择 Reference（**保持画面风格的统一，非必要**），预处理器选择 reference_only，调整图片的尺度点击生成即可

![](https://picx.zhimg.com/80/v2-507ae85746d72b2476079456f6ccd013_1440w.png)

Controlent 选择 Reference

![](https://picx.zhimg.com/80/v2-5d0a3f8f9522cec5362b51af314ad074_1440w.png)

效果图

![](https://picx.zhimg.com/80/v2-43a64da1cac9d9541be257c1beefc5a8_1440w.png)

效果图

![](https://pic1.zhimg.com/80/v2-48ca38ffe863db2a3e6712290b2893b7_1440w.png)

效果图

![](https://picx.zhimg.com/80/v2-2d93e3d4697fbb535611dca72c4ace4a_1440w.png)

效果图

很多小伙伴可能会发现扩展之后的**图片光影关系不对或许尺寸过小太模糊了**，这个时候我们可以将图片发送到图生图继续进行**图片拟合处理以及进一步的放大**，这一步就留给大家自行操作了。

**大家可以对比一下效果，我个人对这个效果还是非常满意的，和 ps ai 的创成式填充有得一拼，而且可控性更强，没有任何限制！**