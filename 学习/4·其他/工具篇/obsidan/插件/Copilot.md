[Copilot](https://github.com/logancyang/obsidian-copilot) 名字和微软推出的 copilot 重名，旨在 obsdian 进行模型的对话。在设置好在线或者本地（ollama）模型后，其可以在右侧的对话框中直接进行问答。当然可以提前设定好并调用特定的 prompt，得到更加无缝的体验。完整的回答可以直接保存到 Obsidian 文件中，方便后续参考。  
另外它可以进行长文的回答和整个知识库的回答。通过设定的 embedding 模型将文章全部向量化，你就可以对单篇文章甚至这个 Obsidian 库中进行提问，当然这会耗费大量的 token，效果上目前不算太好，但是作者一直在进行改进优化，未来可期。  
特点：

- Obsidian 里直接调用模型进行对话。并有着高效的模型增加和替换的流程。
- 实验性质的长文和知识库回答。  
    缺点：
- 不能够删除预置模板的模型，显得模型列表非常臃肿。
- 知识库回答效果暂时不太好，应该和 RAG 流程优化有关。  
    ![image.png](https://picgo-1306089623.cos.ap-nanjing.myqcloud.com/202410102322446.png)