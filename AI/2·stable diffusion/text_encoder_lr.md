text_encoder_lr

> 为与 ext 编码器关联的 LoRA 模块使用不同于正常学习率（使用 --learning_rate 选项指定）的学习率时指定。 有人说最好将Text Encoder设置为稍微低一点的学习率（比如5e-5）。

text_encoder 的学习率，常取定值5e-5，也有许多人将他调成 unet_lr 的 10-15分之一，调整到 unet_lr 1/8 附近也是常见的做法。有人说调低该参数有助于更多学习文本编码器（对 tag 更敏感）。