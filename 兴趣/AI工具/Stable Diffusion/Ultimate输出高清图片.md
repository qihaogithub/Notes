利用 Ultimate 输出高清图片

[https://github.com/Coyote-A/ultimate-upscale-for-automatic1111.git](https://link.uisdc.com/?redirect=https%3A%2F%2Fgithub.com%2FCoyote-A%2Fultimate-upscale-for-automatic1111.git)



Stabel diffusion 在生成大尺寸图时容易爆显存，而且生成速度非常慢。这个插件能很好地解决这个问题。

使用方法是在“图生图”里上传一张我们希望高清放大的图片，然后点击脚本选择 Ultimate 插件

![Stable diffusion入门教程！如何快速搞定安装和插件（附插件打包）](https://image.uisdc.com/wp-content/uploads/2023/05/uisdc-cy-20230505-15.jpg)

虽然这里参数很多，但其实只需要关注几个参数：

把 Target size type 改到 custom size 定义具体尺寸或者改成 scale from image size 选择放大倍数。把重绘幅度（Denoising）改到 0.2，最后点生成。

![Stable diffusion入门教程！如何快速搞定安装和插件（附插件打包）](https://image.uisdc.com/wp-content/uploads/2023/05/uisdc-cy-20230505-16.jpg)

因为是做放大处理，需要的时间可能比较久一些。我放大一张 1536x2256 的图到 3072x4544，花了 3 分 46 秒。

![Stable diffusion入门教程！如何快速搞定安装和插件（附插件打包）](https://image.uisdc.com/wp-content/uploads/2023/05/uisdc-cy-20230505-17.jpg)

左边是放大前的图，右边是放大后的图