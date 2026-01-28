切换模型的 VAE
--------

随着我们的模型越来越多，我们会发现模型需要配套的 VAE 是不一样的，有时候切来切去会很麻烦，这时候我们可以利用 SD 原有的功能来实现快速切换 VAE

![](https://pic2.zhimg.com/80/v2-687e505a71f6c74ef3748e1eb00b1105_1440w.webp)

快速切换 VAE

先进入到设置页面，选择用户界面

![](https://pic3.zhimg.com/80/v2-0b5535a42ac80b9a60d0933da3746c22_1440w.webp)

找到快捷设置列表

在 sd\_model\_checkpoint 后面输入, sd_vae

变成 sd\_model\_checkpoint, sd_vae，保存设置并重启 UI 即可