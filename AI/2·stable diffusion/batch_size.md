只要显存够大，能多大就多大

Batch_size 代表了同时送进去训练的数据量，理论上是应该第一个被确定的超参数。当数量为 1 时，等同于随机梯度下降法（SGD）。

-   **较大的 batch size**往往会导致训练速度更**快**（每个 epoch 的 iteration 数小），内存占用更**大**，但收敛得**慢**（需要更多 epoch 数）。
-   **较小的 batch size**往往会导致训练速度更**慢**（每个 epoch 的 iteration 数大），内存占用更**小**，但收敛得**快**（需要更少 epoch 数）。[[1]] ( https://zhuanlan.zhihu.com/p/618758020?utm_id=0#ref_1 )

实际训练时，能多大就多大往往就能取得不错效果（那种 batch_size 几千时性能下降的情况只有在超恐怖的 gpu/tpu 上才会发生，谁让我们显存小）。Nmist 手写数字训练集可能 3090 24 G 可能才能达到 1024。所以……

下面是一些参考：

-   1024*768 分辨率下，24 GB VRAM 最大 batch_size = 4
-   1024*1024 分辨率下，24 GB VRAM 最大 batch_size = 3（推荐为 2）
-   512*512 分辨率 12 GB VRAM 最大 batch_size = 6

理论上，batch_size = 2� 时计算速度更快。