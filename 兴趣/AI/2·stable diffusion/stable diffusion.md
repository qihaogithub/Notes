# 原理
[【轻科普】StableDiffusion那些事儿，关于LoRA、DreamBooth、模型分层融合等\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1RT411D7h7/?buvid=YC4895C5E5F744FF4F6CA224338A37806FCF&is_story_h5=false&mid=d7BydoIBvlkH8DGmM39nxA%3D%3D&p=1&plat_id=114&share_from=ugc&share_medium=iphone&share_plat=ios&share_session_id=C2617F25-E1F4-446C-BF8D-A9FEF68269F4&share_source=COPY&share_tag=s_i&timestamp=1681657143&unique_k=veFVAEY&up_id=291593914)

# 安装
 **AutoDl**
[[AutoDl 笔记]]
[基于 AutoDL 云端搭建 SD](app://obsidian.md/%E5%9F%BA%E4%BA%8E%20AutoDL%20%E4%BA%91%E7%AB%AF%E6%90%AD%E5%BB%BA%20SD)
[[AutoDl迁移实例]]
**colab 部署**
[[colab 部署]]
**揽睿星舟**
[揽睿星舟云部署](https://zhuanlan.zhihu.com/p/620958643)


# 操作教程
[[基础操作]]
[[模型使用]]
[[进阶教程]]
[[AI绘画/stable diffusion/模型/-stable diffusion 模型]]
[[ComfyUI 1]]
[[模型预览图替换]]
# 插件
[[SD插件]]

#  [[·ComfyUI]]

# 训练
[[训练方法介绍]]
[[dream booth 训练方法]]
[[lora 训练方法]]
[embedding 模型训练](https://www.bilibili.com/video/BV1P84y1g7jS/?spm=wolai.workspace.0.0.392143a9Krlylg&vd_source=81223299ca5d449a34daaab3e1102d1d)

# 教程汇总
[【AI绘画】从零开始的AI绘画入门教程——魔法导论 - 哔哩哔哩](https://www.bilibili.com/read/cv22159609)
[Stable Diffusion 潜工具书-秋叶推荐](https://docs.qq.com/doc/p/230e7ada2a60d8e347d639edd5521f5e62332fe9)
[重绘学派法术绪论1.1](https://docs.qq.com/pdf/DR2V2ZlhHbnJUVHBa?)
#  常用的文件夹目录
#### 常见

1.  **文本到图像的目录 (`outputs/txt2img-images`)**: 存储从文本描述生成的图像。这类目录通常用于保存[用户输入](https://so.csdn.net/so/search?q=%E7%94%A8%E6%88%B7%E8%BE%93%E5%85%A5&spm=1001.2101.3001.7020)文本提示后，系统生成的图像。
    
2.  **图像到图像的目录 (`outputs/img2img-images`)**: 存储基于现有图像进行修改或再创作后生成的新图像。这是用于图像编辑或[风格迁移](https://so.csdn.net/so/search?q=%E9%A3%8E%E6%A0%BC%E8%BF%81%E7%A7%BB&spm=1001.2101.3001.7020)任务的输出位置。
    
3.  **附加或实验性质的输出目录 (`outputs/extras-images`)**: 可能用于存储实验性或不符合主要类别的其他[图像生成](https://so.csdn.net/so/search?q=%E5%9B%BE%E5%83%8F%E7%94%9F%E6%88%90&spm=1001.2101.3001.7020)结果。
    
4.  **文本到图像网格的目录 (`outputs/txt2img-grids`)**: 存储以网格形式展示的多个文本到图像的生成结果，这对于一次性查看和比较多个图像特别有用。
    
5.  **图像到图像网格的目录 (`outputs/img2img-grids`)**: 存储以网格形式展示的多个图像到图像的生成结果，同样便于比较和展示。
    
6.  **图像生成日志目录 (`log/images`)**: 存储与图像生成过程相关的日志信息，这对于调试和分析生成过程非常重要。
    
7.  **初始化图像的目录 (`outputs/init-images`)**: 用于保存在图像到图像转换过程中使用的初始图像或源图像。
    

#### 根目录

*   `.launcher`: 可能包含与项目启动器相关的配置文件。
*   `__pycache__`: 存储 Python 编译过的字节码文件，以加快加载时间。
*   `config_states`: 可能用于存储项目配置的状态或历史版本。
*   `configs`: 用于存放配置文件，通常包含项目运行所需的参数设置。
*   `detected_maps`: 可能存储自动生成的映射或检测结果。
*   **`embeddings`: 可能包含用于机器学习的嵌入向量数据。** 
*   **`extensions` 和 `extensions_builtin`: 存储项目的扩展或插件。** 
*   `git`: 通常是 Git 版本控制的相关目录。
*   `html`, `javascript`: 存储网页前端相关的 HTML 文件和 JavaScript 脚本。
*   `launcher`: 可能包含启动项目的脚本或可执行文件。
*   `localizations`: 包含项目的本地化文件，如翻译或语言资源。
*   `log`: 存储日志文件，记录项目运行时的活动或错误信息。
*   **`models`: 通常用于存储机器学习模型或项目中使用的数据模型。** 
*   **`modules`: 包含项目的代码模块或组件。** 
*   **`outputs`: 存储项目运行产生的输出文件，如生成的图像或报告。** 
*   `py310`: 可能指 Python 3.10 版本的特定文件或环境。
*   `repositories`: 可能用于存储与代码仓库相关的数据。
*   `scripts`: 包含用于项目构建、部署或其他自动化任务的脚本。
*   **`tags`: 可能用于版本标记或注释。** 
*   **`test`: 存储测试代码和测试数据。** 
*   **`textual_inversion`: 可能是一个特定的功能模块，用于文本相关的处理或转换。** 
*   **`textual_inversion_templates`: 存储文本逆向工程或模板化处理的文件。** 
*   `tmp`: 临时文件夹，用于存储临时数据或运行时产生的临时文件。