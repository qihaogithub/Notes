
[Smart-connections](https://github.com/brianpetro/obsidian-smart-connections) 同样可以在单独的界面进行模型对话，这一点于 copilot 类似。不过它最吸引我的功能在于它可以实现通过 embedding 将库里的文章向量化，计算文章间相似度，然后在右侧栏展示一些相关的内容。向量化可以基于文章，也可以更细一步基于特定的 block。这样在进行文章查看回顾时可以直接参考，从某种程度上也是一种自动化的双向链接。  
特点：

- Obsidian 里直接调用模型进行对话。
- 基于本地库，通过相似度推荐和当前文章高相关性的文章或段落。  
    缺点：
- 插件设置较为繁琐，且近几次更新频繁导致界面较乱。
- embedding模型暂时无法自定义，且embedding速度较慢需要优化。  
    ![image.png](https://picgo-1306089623.cos.ap-nanjing.myqcloud.com/202410102314331.png)