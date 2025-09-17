
[秋叶的教程，利用Autodl云端训练](https://www.bilibili.com/video/BV1SR4y1y7Lv/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d)

安装镜像
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20230428115101.png)


以下是笔记

## 训练参数
### max_train_steps[](http://region-41.seetacloud.com:37050/jupyter/lab/tree/autodl-tmp/dreambooth-aki/dreambooth-aki.ipynb#max_train_steps)

训练步数

### learning_rate[](http://region-41.seetacloud.com:37050/jupyter/lab/tree/autodl-tmp/dreambooth-aki/dreambooth-aki.ipynb#learning_rate)

学习率 这里设置的5e-6是科学计数法的(5乘以10的-6次方)。一般就用这个值就可以了，有时候这个默认值有点大，可以小一些比如3e-6。如果你还是觉得太大可以缩小到1e-6、甚至是5e-7等等。

### lr_scheduler[](http://region-41.seetacloud.com:37050/jupyter/lab/tree/autodl-tmp/dreambooth-aki/dreambooth-aki.ipynb#lr_scheduler)

学习率调整策略 一般 lr_scheduler 就用cosine、cosine_with_restarts 就可以了。 想了解更多关于 lr_scheduler 可以看看这个 [知乎](https://www.zhihu.com/question/315772308/answer/2384958925)

### batch_size[](http://region-41.seetacloud.com:37050/jupyter/lab/tree/autodl-tmp/dreambooth-aki/dreambooth-aki.ipynb#batch_size)

一般是1。我推荐不要超过3。调整 batch_size 需要同时调整学习率 详情参考我的视频 [BV1A8411775m](https://www.bilibili.com/video/BV1A8411775m/)

### num_class_images[](http://region-41.seetacloud.com:37050/jupyter/lab/tree/autodl-tmp/dreambooth-aki/dreambooth-aki.ipynb#num_class_images)

class image 的数量。如果 class-images 文件夹内的图片数量小于这个值，则会 AI 自动生成一些图片。 如果关闭了下面的 with_prior_preservation，那么这个参数就没用了。

### with_prior_preservation[](http://region-41.seetacloud.com:37050/jupyter/lab/tree/autodl-tmp/dreambooth-aki/dreambooth-aki.ipynb#with_prior_preservation)

关闭了这个参数以后，训练将不会再用 class images，变为 native training。训练画风需要关闭这个参数

更深入的细节可以参考这个 [DreamBooth讲解](https://guide.novelai.dev/advanced/finetuning/dreambooth)



# dream booth 训练经验
[使用 Diffusers 通过 DreamBooth 来训练 Stable Diffusion - 知乎](https://zhuanlan.zhihu.com/p/601410397?utm_medium=social&utm_oi=1016698504294465536&utm_psn=1630675493367205888&utm_source=ZHShareTargetIDMore)