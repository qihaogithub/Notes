---
类型: 模型缺失
---

```
Error occurred when executing ControlNetLoader:
argument of type 'NoneType' is not iterable

File "D:\APP\ComfyUI-aki\ComfyUI-aki-v1.3\execution.py", 
line 317, in execute
output_data, output_ui, has_subgraph = get_output_data(
    obj, input_data_all, 
    execution_block_cb=execution_block_cb, 
    pre_execute_cb=pre_execute_cb
)

File "D:\APP\ComfyUI-aki\ComfyUI-aki-v1.3\execution.py", 
line 192, in get_output_data
return_values = _map_node_over_list(
    obj, input_data_all, 
    obj.FUNCTION, 
    allow_interrupt=True, 
    execution_block_cb=execution_block_cb, 
    pre_execute_cb=pre_execute_cb
)

File "D:\APP\ComfyUI-aki\ComfyUI-aki-v1.3\execution.py", 
line 169, in _map_node_over_list
process_inputs(input_dict, i)

File "D:\APP\ComfyUI-aki\ComfyUI-aki-v1.3\execution.py", 
line 158, in process_inputs
results.append(getattr(obj, func)(**inputs))

File "D:\APP\ComfyUI-aki\ComfyUI-aki-v1.3\nodes.py", 
line 758, in load_controlnet
controlnet = comfy.controlnet.load_controlnet(controlnet_path)

File "D:\APP\ComfyUI-aki\ComfyUI-aki-v1.3\comfy\controlnet.py", 
line 455, in load_controlnet
diffusers_keys = comfy.utils.unet_to_diffusers(controlnet_config)

File "D:\APP\ComfyUI-aki\ComfyUI-aki-v1.3\comfy\utils.py", 
line 220, in unet_to_diffusers
if "num_res_blocks" not in unet_config:
```

这个错误是由于在执行 ControlNetLoader 时，`unet_config` 对象为 NoneType，即没有正确加载或传递 UNet 的配置信息。这通常意味着在加载 ControlNet 模型或处理其配置时出现了问题。
为了解决这个问题，您可以按照以下步骤操作：
1. **检查 ControlNet 模型路径**：确保 `controlnet_path` 变量指向了正确的 ControlNet 模型文件路径。
2. **验证 ControlNet 配置**：检查 ControlNet 的配置文件，确保其中包含了必要的配置项，例如 `num_res_blocks`。
3. **检查模型文件**：确保 ControlNet 模型文件没有损坏，并且是兼容的格式。
4. **查看完整错误日志**：如果可能，请提供更完整的错误日志，以便进一步分析问题。
5. **环境问题**：确认您的 Python 环境和依赖库都正确安装且版本兼容。
如果您在尝试这些步骤后仍然遇到问题，请提供更多的信息，例如 ControlNet 模型的来源、您的完整错误日志等，以便进行更深入的分析。
