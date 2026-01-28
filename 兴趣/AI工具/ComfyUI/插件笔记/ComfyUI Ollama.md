
自定义[ComfyUI](https://github.com/comfyanonymous/ComfyUI)节点，用于使用[ollama python 客户端与](https://github.com/ollama/ollama-python)[Ollama](https://ollama.com/)交互。[](https://github.com/ollama/ollama-python)

轻松将 LLM 的强大功能集成到 ComfyUI 工作流程中，或者只是尝试使用 GPT。

要正确使用此功能，您需要一个可从运行 ComfyUI 的主机访问的正在运行的 Ollama 服务器。

## 具有查询输入图像能力的节点。

[![图片](https://github.com/stavsap/comfyui-ollama/raw/main/.meta/OllamaVision.png)](https://github.com/stavsap/comfyui-ollama/blob/main/.meta/OllamaVision.png)

模型名称应为具有视觉能力的模型，例如：[https://ollama.com/library/llava](https://ollama.com/library/llava)。

### 奥拉玛生成

能够通过给定的提示查询 LLM 的节点。

[![图片](https://github.com/stavsap/comfyui-ollama/raw/main/.meta/OllamaGenerate.png)](https://github.com/stavsap/comfyui-ollama/blob/main/.meta/OllamaGenerate.png)

### 奥拉玛生成进阶


该节点能够通过给定的提示查询 LLM，并具有微调参数和保留上下文以生成链接的能力。

检查[ollama api 文档](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-completion)以获取有关参数的信息。

更多[参数信息](https://github.com/ollama/ollama/blob/main/docs/modelfile.md#parameter)

[![图片](https://github.com/stavsap/comfyui-ollama/raw/main/.meta/generate-advance.png)](https://github.com/stavsap/comfyui-ollama/blob/main/.meta/generate-advance.png)

## 使用示例


考虑以下工作流程：查看图像，并使用所需的 LLM 执行其他文本处理。在 OllamaGenerate 节点中将提示设置为输入。

[![图片](https://github.com/stavsap/comfyui-ollama/raw/main/.meta/CombinedUsage1.png)](https://github.com/stavsap/comfyui-ollama/blob/main/.meta/CombinedUsage1.png)

示例中的自定义文本节点可以在这里找到：[https://github.com/pythongosssss/ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)