
> [!建议] 
> alpha 被推荐设置为 network_dimension 的一半，一些封装的训练脚本也默认这么设置。 

指定 alpha 值以防止下溢并稳定学习。默认值为 1。如果您指定与 network_dimension相同的值，它的行为与以前的版本相同。