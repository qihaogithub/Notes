optimizer_type

["AdamW", "AdamW8bit", "Lion", "SGDNesterov", "SGDNesterov8bit", "DAdaptation", "AdaFactor"]

关于优化器的原理可以自行查询，Lion 是很新的一种优化器。如果你不了解优化器，使用 AdamW、AdamW8bit、Lion 、 DAdaptation 即可。AdamW8bit 对于显存小的用户更友好。Lion 优化器的使用率也很高，学习率需要设置得很小（如AdamW优化器下的 1/3，或者更小）

使用 DAdaptation 时，应当将学习率设置在1附近，text_encoder_lr 可以设置成1，或者小一点，0.5之类。使用DAdaptation 时，推荐将学习率调整策略调整为 constant 。

> ### 关于指定优化器  
>   
> 使用 --optimizer_args 选项指定优化器选项参数。 可以以key=value的格式指定多个值。 此外，您可以指定多个值，以逗号分隔。 例如，要指定 AdamW 优化器的参数，``--optimizer_args weight_decay=0.01 betas=.9,.999``。  
>   
> 指定可选参数时，请检查每个优化器的规格。  
>   
> 一些优化器有一个必需的参数，如果省略它会自动添加（例如 SGDNesterov 的动量）。 检查控制台输出。  
>   
> D-Adaptation 优化器自动调整学习率。 学习率选项指定的值不是学习率本身，而是D-Adaptation决定的学习率的应用率，所以通常指定1.0。 如果您希望 Text Encoder 的学习率是 U-Net 的一半，请指定 ``--text_encoder_lr=0.5 --unet_lr=1.0``。  
>   
> 如果指定 relative_step=True，AdaFactor 优化器可以自动调整学习率（如果省略，将默认添加）。 自动调整时，学习率调度器被迫使用 adafactor_scheduler。 此外，指定 scale_parameter 和 warmup_init 似乎也不错。  
>   
> 自动调整的选项类似于``--optimizer_args "relative_step=True" "scale_parameter=True" "warmup_init=True"``。  
>   
> 如果您不想自动调整学习率，请添加可选参数 ``relative_step=False``。 在那种情况下，似乎建议将 constant_with_warmup 用于学习率调度程序，而不要为梯度剪裁范数。 所以参数就像``--optimizer_type=adafactor --optimizer_args "relative_step=False" --lr_scheduler="constant_with_warmup" --max_grad_norm=0.0``。