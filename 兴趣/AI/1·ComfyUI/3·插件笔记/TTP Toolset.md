这是一个用于 DIT 模型的简单逻辑惊人放大节点的工作流。它可以通用于 Flux、Hunyuan、SD3 等模型。它可以简单地将初始图像分割成小块,然后使用图像询问器获取每个小块的提示,以实现更精确的放大过程。条件将被适当处理,幻觉将显著减少。


# 操作说明：

# 图像分块批处理节点:

这个节点会根据你设置的宽度和高度自动将图像切割成小块。
记录后续使用所需的必要信息。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202410171727768.png)
width: 分块图像的宽度
height: 分块图像的高度
image: 要被分块的图像

# 图像组装节点:
这个节点将图像小块重新组装成一个完整图像,并防止图像小块之间可能出现的线条。它在像素模式下工作。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202410171727769.png)

tiles: 输入分块后的图像批次,如果你想的话,可以通过其他批处理节点替换其中的一个

postion: 与图像分块批处理节点配对
original size: 与图像分块批处理节点配对
grid size: 与图像分块批处理节点配对

Padding: 用于合并图像的填充。

# 分块图像大小节点:

这个节点用于决定你想通过图像分块批处理节点分成多少块,它将从原始图像获取信息并计算分块图像的分辨率:

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202410171727771.png)

只需输入宽度和高度因子,它就会进行切割。2,3 表示宽度切成 2 块,高度切成 3 块。总共 6 块。

# 坐标分离器节点:

将位置信息转换为坐标,连接到 positions。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202410171727772.png)

# 条件转批处理节点:

将条件列表转换为批处理,我保留这个节点以便未来功能扩展。将它连接到 conditions。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202410171727773.png)

# 条件合并节点:

这个节点将所有分块的条件合并成一个,为构建图像做好准备!
只需将它与坐标分离器节点和条件转批处理节点连接。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202410171727774.png)

对于即时 Flux 示例:请参考这个包含工作流的图像。
像素示例(推荐):
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202410171728115.png)

潜在空间示例:
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202410171729180.png)

如果你准备好了,它可以支持 controlnet Tile 来增强放大效果,这里是一个使用 tile for Hunyuan DiT 的示例
你可以从我的 huggingface 找到 tile https://huggingface.co/TTPlanet
以及从这里找到 hunyuan 1.2 https://huggingface.co/comfyanonymous/hunyuan_dit_comfyui/blob/main/hunyuan_dit_1.2.safetensors
这里是示例工作流:
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202410171729340.png)


