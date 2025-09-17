

![ComfyUI Node Menu - Primitive Primitive Node](https://comfyui-wiki.com/utils/Primitive.jpg)

元节点可以识别连接的节点输入类型，并可以为其提供输入数据,当这个节点连接不同输入类型时将会转为不同的输入状态，可以用于在多个不同节点间使用统一参数，如在多个Ksampler 中使用同个seed等

目前`Primitive元节点` 支持连接的数据类型如下

- 字符串 string
- 数字 float / Int

使用示例

![ComfyUI Node - Primitive Usage Example](https://comfyui-wiki.com/img/utils/Primitive.jpg)