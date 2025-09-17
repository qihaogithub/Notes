steps

这不是一个可以设置的参数，但是必须要提，true_step = epochs * num_img / batch_size。

比如，你训练 8个 epochs，图片文件夹 10_dogs，里面有 50 张狗的图片。意味着重复10次，每个epoch 训练 500 steps。如果你的 batch_size = 4，还要除以 4，实际每个 epochs 只有 125steps。8 个 epochs 后 steps 是 1000。

还记得我们前面说的吗？更大的batch_size需要更多epochs。batch_size = 4 并不是意味着更新四次梯度，而意味着一次计算4张图片的梯度。业界常见的做法是让学习率随batch_size线性增加，不过我并不确定在这里是否使用。