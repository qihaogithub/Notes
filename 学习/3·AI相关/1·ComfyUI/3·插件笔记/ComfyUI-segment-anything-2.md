[Github](https://github.com/kijai/ComfyUI-segment-anything-2)
一组为ComfyUI设计的节点，可以合成图层达到类似Photoshop的功能。这些节点将PhotoShop的一部分基本功能迁移到ComfyUI，旨在集中工作流程，减少软件切换的频率。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151411323.png)
*此图工作流(title_example_workflow.json) 在 workflow 目录中.
## 节点说明
节点按照功能分为5组：LayerStyle, LayerColor, LayerMask, LayerUtility和LayerFilter。
- [LayerStyle](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#LayerStyle)节点组提供仿照Adobe Photoshop的图层样式。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418583.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/menu_layer_style.jpg)
    
- [LayerColor](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#LayerColor)节点组提供调整颜色功能。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418614.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/menu_layer_color.jpg)
    
- [LayerMask](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#LayerMask)节点组提供Mask辅助工具。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418104.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/menu_layer_mask.jpg)
    
- [LayerUtility](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#LayerUtility)节点组提供图层合成工具和工作流相关的辅助节点。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418772.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/menu_layer_utility.jpg)
    
- [LayerFilter](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#LayerFilter)节点组提供图像效果滤镜。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418907.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/menu_layer_filter.jpg)
    
# LayerStyle
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418533.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/layerstyle_title.jpg) [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418042.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/layerstyle_nodes.jpg)
### DropShadow
生成阴影。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418519.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/drop_shadow_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418919.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/drop_shadow_node.jpg)
- background_image1: 背景图像。
    
- layer_image1: 用于合成的层图像。
    
- layer_mask1,2: 层图像的遮罩，阴影按此生成。
    
- invert_mask: 是否反转遮罩。
    
- blend_mode3: 阴影的混合模式。
    
- opacity: 阴影的不透明度。
    
- distance_x: 阴影的水平方向偏移量。
    
- distance_y: 阴影的垂直方向偏移量。
    
- grow: 阴影扩张幅度。
    
- blur:阴影模糊程度。
    
- shadow_color4: 阴影颜色。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
### OuterGlow
生成外发光。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418400.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/outer_glow_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418834.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/outer_glow_node.jpg)
- background_image1: 背景图像。
    
- layer_image1: 用于合成的层图像。
    
- layer_mask1,2: 层图像的遮罩，外发光按此生成。
    
- invert_mask: 是否反转遮罩。
    
- blend_mode3: 发光的混合模式。
    
- opacity: 发光的不透明度。
    
- brightness: 发光亮度。
    
- glow_range: 发光范围。
    
- blur:发光模糊程度。
    
- light_color4: 发光中心颜色。
    
- glow_colo4: 辉光外围颜色。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
### InnerShadow
生成内阴影。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418357.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/inner_shadow_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418856.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/inner_shadow_node.jpg)
- background_image1: 背景图像。
    
- layer_image1: 用于合成的层图像。
    
- layer_mask1,2: 层图像的遮罩，阴影按此生成。
    
- invert_mask: 是否反转遮罩。
    
- blend_mode3: 阴影的混合模式。
    
- opacity: 阴影的不透明度。
    
- distance_x: 阴影的水平方向偏移量。
    
- distance_y: 阴影的垂直方向偏移量。
    
- grow: 阴影扩张幅度。
    
- blur:阴影模糊程度。
    
- shadow_color4: 阴影颜色。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
### InnerGlow
生成内发光。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418433.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/inner_glow_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418045.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/inner_glow_node.jpg)
- background_image1: 背景图像。
    
- layer_image1: 用于合成的层图像。
    
- layer_mask1,2: 层图像的遮罩，发光按此生成。
    
- invert_mask: 是否反转遮罩。
    
- blend_mode3: 发光的混合模式。
    
- opacity: 发光的不透明度。
    
- brightness: 发光亮度。
    
- glow_range: 发光范围。
    
- blur:发光模糊程度。
    
- light_color4: 发光中心颜色。
    
- glow_colo4: 辉光外围颜色。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
### Stroke
生成描边。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418533.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/stroke_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418089.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/stroke_node.jpg)
- background_image1: 背景图像。
    
- layer_image1: 用于合成的层图像。
    
- layer_mask1，2: 层图像的遮罩，描边按此生成。
    
- invert_mask: 是否反转遮罩。
    
- blend_mode3: 描边的混合模式。
    
- opacity: 不透明度。
    
- stroke_grow: 描边扩张/收缩幅度，正值是扩张，负值是收缩。
    
- stroke_width: 描边宽度。
    
- blur: 描边模糊。
    
- stroke_color4: 描边颜色。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
### GradientOverlay
渐变覆盖 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418655.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/gradient_overlay_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418208.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/gradient_overlay_node.jpg)
- background_image1: 背景图像。
    
- layer_image1: 用于合成的层图像。
    
- layer_mask1，2: 层图像的遮罩。
    
- invert_mask: 是否反转遮罩。
    
- blend_mode3: 描边的混合模式。
    
- opacity: 不透明度。
    
- start_color: 渐变开始端的颜色。
    
- start_alpha: 渐变开始端的透明度。
    
- end_color: 渐变结束端的颜色。
    
- end_alpha: 渐变结束端的透明度。
    
- angle: 渐变旋转角度。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
### ColorOverlay
颜色覆盖 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418744.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_overlay_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418255.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_overlay_node.jpg)
- background_image1: 背景图像。
    
- layer_image1: 用于合成的层图像。
    
- layer_mask1，2: 层图像的遮罩。
    
- invert_mask: 是否反转遮罩。
    
- blend_mode3: 描边的混合模式。
    
- opacity: 不透明度。
    
- color: 覆盖的颜色。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
# LayerColor
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418817.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/layercolor_title.jpg) [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418342.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/layercolor_nodes.jpg)
### LUT Apply
将LUT应用到图像。仅支持.cube格式的LUT文件。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418769.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/lut_apply_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418252.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/lut_apply_node.jpg)
- LUT*: 这里列出了LUT文件夹中可用的.cube文件列表，选中的LUT文件将被应用到图像。
    
- color_space: 普通图片请选择linear, log色彩空间的图片请选择log。
    
- strength: 范围0~100, LUT应用强度。数值越大，与原图的差别越大, 数值越小，越接近原图。
    
*LUT文件夹在`resource_dir.ini`中定义，这个文件位于插件根目录下, 默认名字是`resource_dir.ini.example`, 初次使用这个文件需将文件后缀改为.ini。用文本编辑软件打开，找到“LUT_dir=”开头的这一行，编辑“=”之后为自定义文件夹路径名。这个文件夹里面所有的.cube文件将在ComfyUI初始化时被收集并显示在节点的列表中。如果ini中设定的文件夹无效，将启用插件自带的LUT文件夹。
### AutoAdjust
自动调整图片的亮度，对比度和白平衡。提供一些手动调整选项以弥补自动调整的不足。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418779.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/auto_adjust_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418322.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/auto_adjust_node.jpg)
- strength: 调整的强度。数值越大，与原图的差别越大。
    
- brightness: 亮度手动调整。
    
- contrast: 对比度手动调整。
    
- saturation: 色彩饱和度手动调整。
    
- red: 红色通道手动调整。
    
- green: 绿色通道手动调整。
    
- blue: 蓝色通道手动调整。
    
### AutoAdjustV2
在AutoAdjust基础上增加遮罩输入, 仅计算遮罩内的内容进行自动调色。增加多种自动调整模式。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418938.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/auto_adjust_v2_example.jpg)
在AutoAdjust基础上进行了如下改变: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418459.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/auto_adjust_v2_node.jpg)
- mask:可选遮罩输入。
    
- mode: 自动调整模式。"RGB"按RGB三个通道自动调整，"lum + sat"按亮度和饱和度自动调整，"luminance"按亮度自动调整，"saturation"按饱和度自动调整, "mono"按灰度自动调整并输出单色。
    
### AutoBrightness
将过暗或过亮的图片自动调整到适中的亮度，支持遮罩输入。有遮罩输入时仅以遮罩部分的内容作为自动亮度的数据来源。输出仍然是整个调整后的图像。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418982.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/auto_brightness_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418392.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/auto_brightness_node.jpg)
- strength: 自动调整亮度的强度。数值越大，越偏向中间值，与原图的差别越大。
    
- saturation: 色彩饱和度。亮度改变通常会导致色彩饱和度发生变化，可在此适当调整补偿。
    
### ColorAdapter
自动调整图片色调，使之与参考图片相似。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418001.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_adapter_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418477.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_adapter_node.jpg)
- opacity: 图像调整色调之后的不透明度。
    
### Exposure
改变图像的曝光。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418069.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/exposure_example.jpg)
节点选项说明:
- exposure: 曝光值。更高的数值表示更亮的曝光。
    
### Color of Shadow & Highlight
调整图像暗部和亮部的颜色。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418554.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_of_shadow_and_highlight_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418055.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_of_shadow_and_highlight_node.jpg)
- image: 图像输入。
    
- mask: 可选输入。如果有输入，将只调整遮罩范围内的颜色。
    
- shadow_brightness: 暗部的亮度。
    
- shadow_saturation: 暗部的色彩饱和度。
    
- shadow_hue: 暗部的色相。
    
- shadow_level_offset: 暗部取值的偏移量，更大的数值使更多靠近明亮的区域纳入暗部。
    
- shadow_range: 暗部的过渡范围。
    
- highlight_brightness: 亮部的亮度。
    
- highlight_saturation: 亮部的色彩饱和度。
    
- highlight_hue: 亮部的色相。
    
- highlight_level_offset: 亮部取值的偏移量，更小的数值使更多靠近阴暗的区域纳入亮部。
    
- highlight_range: 亮部的过渡范围。
    
### ColorTemperature
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418584.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_temperature_example.jpg) 改变图像的色温。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418064.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_temperature_node.jpg)
- temperature: 色温值。范围在-100到100之间。值越高，色温越高(偏蓝)；越低，色温越低(偏黄)。
    
### ColorBalance
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151418636.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_balance_example.jpg) 改变图像的色彩平衡。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419221.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_balance_node.jpg)
- cyan_red: 青-红平衡。负值为偏青，正值为偏红。
    
- magenta_green: 品-绿平衡。负值为偏品，正值为偏绿。
    
- yellow_blue: 黄-蓝平衡。负值为偏黄，正值为偏蓝。
    
### Levels
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419646.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/levels_example.jpg) 改变图像色阶。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419065.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/levels_node.jpg)
- channel: 选择要调整的通道。有RGB, red, green, blue可供选择。
    
- black_point*: 图像输入黑点值。取值范围0-255, 默认值0。
    
- white_point*: 图像输入白点值。取值范围0-255, 默认值255。
    
- gray_point: 图像输入灰点值。取值范围0.01-9.99, 默认1。
    
- output_black_point*: 图像输出黑点值。取值范围0-255, 默认值0。
    
- output_white_point*: 图像输出黑点值。取值范围0-255, 默认值255。
    
*如果 black_point 或 output_black_point 数值大于 white_point 或 output_white_point，则两个数值将交换，较大的数值作为white_point使用，较小的数值作为black_point使用。
### Gamma
改变图像的Gamma值。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419466.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/gamma_node.jpg)
- gamma: 图像的Gamma值。
    
### Brightness & Contrast
改变图像的亮度、对比度和饱和度。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419933.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/brightness_&_contrast_node.jpg)
- brightness: 图像的亮度。
    
- contrast: 图像的对比度。
    
- saturation: 图像的色彩饱和度。
    
### RGB
对图像的RGB各通道进行调整。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419341.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/RGB_node.jpg)
- R: 图像的R通道。
    
- G: 图像的G通道。
    
- B: 图像的B通道。
    
### YUV
对图像的YUV各通道进行调整。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419749.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/YUV_node.jpg)
- Y: 图像的Y通道。
    
- U: 图像的U通道。
    
- V: 图像的V通道。
    
### LAB
对图像的LAB各通道进行调整。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419280.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/LAB_node.jpg)
- L: 图像的L通道。
    
- A: 图像的A通道。
    
- B: 图像的B通道。
    
### HSV
对图像的HSV各通道进行调整。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419778.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/HSV_node.jpg)
- H: 图像的H通道。
    
- S: 图像的S通道。
    
- V: 图像的V通道。
    
# LayerUtility
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419403.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/layerutility_nodes.jpg)
### ImageBlendAdvance
用于合成图层，允许在背景图片上合成与之不同尺寸的图层图片，并且设置位置和变换。提供多种混合模式供选择，可设置透明度。
节点提供了图层变换方法和抗锯齿选项。有助于提高合成画质。
节点提供了mask输出可用于后续工作流。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419923.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_blend_advance_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419471.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_blend_advance_node.jpg)
- background_image: 背景图像。
    
- layer_image5: 用于合成的层图像。
    
- layer_mask2,5: 层图像的遮罩。
    
- invert_mask: 是否反转遮罩。
    
- blend_mode3: 图层混合模式。
    
- opacity: 不透明度。
    
- x_percent: 图层在背景图上的水平位置，用百分比表示，最左侧是0，最右侧是100，可以是小于0或者超过100，那表示图层有部分内容在画面之外。
    
- y_percent: 图层在背景图上的垂直位置，用百分比表示，最上侧是0，最下侧是100。例如设置为50表示垂直居中，20是偏上，80则是偏下。
    
- mirror: 镜像翻转。提供2种翻转模式, 水平翻转和垂直翻转。
    
- scale: 图层放大倍数，1.0 表示原大。
    
- aspect_ratio: 图层长宽比。1.0 是原始比例，大于此值表示拉长，小于此值表示压扁。
    
- rotate: 图层旋转度数。
    
- transform_method: 用于图层放大和旋转的采样方法，包括lanczos、bicubic、hamming、bilinear、box和nearest。不同的采样方法会影响合成的画质和画面处理时间。
    
- anti_aliasing: 抗锯齿，范围从0-16，数值越大，锯齿越不明显。过高的数值将显著降低节点的处理速度。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
### CropByMask
将图片按照mask范围裁切，可设置四周边框保留大小。这个节点与[RestoreCropBox](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#RestoreCropBox)和[ImageScaleRestore](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#ImageScaleRestore)配合使用，可以对图片的局部进行裁切，放大修改后贴回原处。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419088.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/corp_by_mask_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419501.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/corp_by_mask_node.jpg)
- image5: 输入的图像。
    
- mask_for_crop5: image的遮罩，将自动按照遮罩范围进行裁切。
    
- invert_mask: 是否反转遮罩。
    
- detect: 探测方法，`min_bounding_rect`是大块形状最小外接矩形, `max_inscribed_rect`是大块形状最大内接矩形, `mask_area`是遮罩像素有效区域。
    
- top_reserve: 裁切顶端保留大小。
    
- bottom_reserve: 裁切底部保留大小。
    
- left_reserve: 裁切左侧保留大小。
    
- right_reserve: 裁切右侧保留大小。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
输出:
- croped_image: 裁切后的图片。
    
- croped_mask: 裁切后的遮罩。
    
- crop_box: 裁切box数据，在RestoreCropBox节点恢复时使用。
    
- box_preview: 裁切位置预览图，红色是探测到的范围，绿色是加上保留边框后裁切的范围。
    
### CropByMaskV2
CropByMask的V2升级版。支持crop_box输入，方便裁切相同尺寸的图层。
在CropByMask基础上做了如下改变: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419004.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/corp_by_mask_v2_node.jpg)
- `mask_for_crop`更名为`mask`。
    
- 增加`crop_box`可选输入，如果这里有输入将忽略遮罩探测，直接使用此数据裁切。
    
- 增加`round_to_multiple`选项，使裁切边长倍数取整。例如设置为8，宽和高将强制设置为8的倍数。
    
### RestoreCropBox
将被[CropByMask](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#CropByMask)裁切后的图片恢复到原图。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419447.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/restore_crop_box_node.jpg)
- background_image: 裁切前的原图。
    
- croped_image5: 裁切后的图片。如果中间经过放大处理，恢复前需将尺寸还原。
    
- croped_mask2,5: 裁切后的遮罩。
    
- crop_box: 裁切时的box数据。
    
- invert_mask: 是否反转遮罩。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
### CropBoxResolve
将 `corp_box` 解析为 `x` , `y` , `width` , `height` 。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419964.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/corp_box_resolve_node.jpg)
### ImageScaleRestore
图像缩放。此节点成对使用时，在第二个节点可自动还原图像到原始大小。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419640.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_scale_restore_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419076.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_scale_restore_node.jpg)
- image5: 输入的图像。
    
- mask2,5: 图像的遮罩。
    
- original_size: 可选输入，用于恢复图片到原始大小。
    
- scale: 缩放比例。当有original_size输入，或者scale_by_longest_side设置为True时，此项设置将被忽略。
    
- scale_by_longest_side: 允许按长边尺寸缩放。
    
- longest_side: scale_by_longest_side被设置为True时，此项将作为是图像长边的长度。当有original_size输入时，此项设置将被忽略。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
输出:
- image: 缩放后的图像。
    
- mask: 如果有mask输入，将输出缩放后的mask。
    
- original_size: 图像的原始大小数据，用于后续节点进行恢复。
    
- width: 输出图片的宽。
    
- height: 输出图片的高。
    
### ImageScaleRestoreV2
ImageScaleRestore的V2升级版。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419563.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_scale_restore_v2_node.jpg) 在ImageScaleRestore基础上做了如下改变:
- scale_by: 允许按长边、短边、宽度、高度或总像素指定尺寸缩放。此处选项设为by_scale时使用scale值，其他选项时使用scale_by_lengtt值。
    
- scale_by_length: 这里的数值作为scale_by指定边的长度。
    
### ImageMaskScaleAs
将图像或遮罩缩放到参考图像（或遮罩）的大小。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419074.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_mask_scale_as_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419505.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_mask_scale_as_node.jpg)
- scale_as*: 参考大小。可以是图像image，也可以是遮罩mask。
    
- image: 待缩放的图像。此选项为可选输入，如果没有输入将输出纯黑图片。
    
- mask: 待缩放的遮罩。此选项为可选输入，如果没有输入将输出纯黑遮罩。
    
- fit: 缩放画幅宽高比模式。当原图与缩放尺寸画幅宽高比例不一致时，有3种模式可以选择, letterbox模式保留完整的画幅，空白处用黑色补足；crop模式保留完整的短边，长边超出部分将被切除；fill模式不保持画幅比例，宽高各自填满画面。
    
- method: 缩放的采样方法，包括lanczos、bicubic、hamming、bilinear、box和nearest。
    
*仅限输入image和mask, 如果强制接入其他类型输入，将导致节点错误。
输出:
- image: 如果有image输入，将输出缩放后的图像。
    
- mask: 如果有mask输入，将输出缩放后的遮罩。
    
- original_size: 图像的原始大小数据，用于后续节点进行恢复。
    
- width: 输出图片的宽。
    
- height: 输出图片的高。
    
### ImageScaleByAspectRatio
将图像或遮罩按宽高比缩放。可设置将缩放后的尺寸按8或者16的倍数取整，可按长边尺寸缩放。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419057.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_scale_by_aspect_ratio_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419555.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_scale_by_aspect_ratio_node.jpg)
- aspect_ratio: 宽高比。此处提供了几个常见画幅比例。也可选"original"保持原图比例或者"custom"自定义比例。
    
- proportional_width: 比例宽。如果aspect_ratio选项不是"custom"，此处设置将被忽略。
    
- proportional_height: 比例高。如果aspect_ratio选项不是"custom"，此处设置将被忽略。
    
- fit: 缩放画幅宽高比模式。有3种模式可以选择, letterbox模式保留完整的画幅，空白处用黑色补足；crop模式保留完整的短边，长边超出部分将被切除；fill模式不保持画幅比例，宽高各自填满画面。
    
- method: 缩放的采样方法，包括lanczos、bicubic、hamming、bilinear、box和nearest。
    
- round_to_multiple: 倍数取整。例如设置为8，宽和高将强制设置为8的倍数。
    
- scale_by_longest_side: 允许按长边尺寸缩放。
    
- longest_side: scale_by_longest_side被设置为True时，此项将作为是图像长边的长度。
    
输出:
- image: 如果有image输入，将输出缩放后的图像。
    
- mask: 如果有mask输入，将输出缩放后的遮罩。
    
- original_size: 图像的原始大小数据，用于后续节点进行恢复。
    
- width: 输出图片的宽。
    
- height: 输出图片的高。
    
### ImageScaleByAspectRatioV2
ImageScaleByAspectRatio的V2升级版
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419077.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_scale_by_aspect_ratio_v2_node.jpg) 在ImageScaleByAspectRatio基础上做了如下改变:
- scale_to_side: 允许按长边、短边、宽度、高度或总像素指定尺寸缩放。
    
- scale_to_length: 这里的数值作为scale_to_side指定边的长度, 或者总像素数量(kilo pixels)。
    
- background_color4: 背景色。
    
### QWenImage2Prompt
根据图片反推提示词。这个节点是[ComfyUI_VLM_nodes](https://github.com/gokayfem/ComfyUI_VLM_nodes)中的`UForm-Gen2 Qwen Node`节点的重新封装，感谢原作者。 请从[huggingface](https://huggingface.co/unum-cloud/uform-gen2-qwen-500m)或者[百度网盘](https://pan.baidu.com/s/1ztnVX_Sh800xsWZhMDe-Ww?pwd=esyt)下载模型到`ComfyUI/models/LLavacheckpoints/files_for_uform_gen2_qwen`文件夹。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419645.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/qwen_image2prompt_example.jpg)
节点选项说明:
- question: 对UForm-Gen-QWen模型的提示词。
    
### PromptTagger
根据图片反推提示词，可以设置替换词。这个节点目前使用Google Gemini API作为后端服务，请确保网络环境可以正常使用Gemini。 请在[Google AI Studio](https://makersuite.google.com/app/apikey)申请你的API key, 并将其填到`api_key.ini`, 这个文件位于插件根目录下, 默认名字是`api_key.ini.example`, 初次使用这个文件需将文件后缀改为.ini。用文本编辑软件打开，在`google_api_key=`后面填入你的API key并保存。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419350.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/prompt_tagger_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419866.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/prompt_tagger_node.jpg)
- api: 使用的Api。有"gemini-1.5-flash"和"google-gemini"两个选项。
    
- token_limit: 生成提示词的最大token限制。
    
- exclude_word: 需要排除的关键词。
    
- replace_with_word: 替换exclude_word的关键词。
    
### PromptEmbellish
输入简单的提示词，输出经过润色的提示词，支持输入图片作为参考，支持中文输入。这个节点目前使用Google Gemini API作为后端服务，请确保网络环境可以正常使用Gemini。 请在[Google AI Studio](https://makersuite.google.com/app/apikey)申请你的API key, 并将其填到`api_key.ini`, 这个文件位于插件根目录下, 默认名字是`api_key.ini.example`, 初次使用这个文件需将文件后缀改为.ini。用文本编辑软件打开，在`google_api_key=`后面填入你的API key并保存。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419557.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/prompt_embellish_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419239.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/prompt_embellish_node.jpg)
- image: 可选项，输入图像作为提示词参考。
    
- api: 使用的Api。有"gemini-1.5-flash"和"google-gemini"两个选项。
    
- token_limit: 生成提示词的最大token限制。
    
- discribe: 在这里输入简单的描述。支持中文。
    
### Florence2Image2Prompt
使用florence2模型反推提示词。本节点部分的代码来自[yiwangsimple/florence_dw](https://github.com/yiwangsimple/florence_dw)，感谢原作者。 *首次使用时将自动下载模型，请在可以访问huggingface.co的网络环境下使用。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419792.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/florence2_image2prompt_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419279.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/florence2_image2prompt_node.jpg)
- florence2_model: Florence2模型输入。
    
- image: 图片输入。
    
- task: 选择florence2任务。
    
- text_input: florence2任务文本输入。
    
- max_new_tokens: 生成文本的最大token数量。
    
- num_beams: 生成文本的beam search数量。
    
- do_sample: 是否使用文本生成采样。
    
- fill_mask: 是否使用文本标记掩码填充。
    
### ImageShift
使图片产生位移。此节点支持位移接缝遮罩的输出，方便制作连续贴图。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419851.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_shift_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419337.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_shift_node.jpg)
- image5: 输入的图像。
    
- mask2,5: 图像的遮罩。
    
- shift_x: 位移的横向距离。
    
- shift_y: 位移的纵向距离。
    
- cyclic: 位移出界的部分是否循环。
    
- background_color4: 背景颜色。如果cyclic设置为False,将使用这里的设置作为背景颜色。
    
- border_mask_width: 接缝遮罩宽度。
    
- border_mask_blur: 接缝遮罩模糊。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
### ImageBlend
一个用于合成图层的简单节点，提供多种混合模式供选择，可设置透明度。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419951.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_blend_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419393.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_blend_node.jpg)
- background_image1: 背景图像。
    
- layer_image1: 用于合成的层图像。
    
- layer_mask1,2: 层图像的遮罩。
    
- invert_mask: 是否反转遮罩。
    
- blend_mode3: 图层混合模式。
    
- opacity: 不透明度。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
### ImageOpacity
调整图像不透明度。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419897.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_opacity_example.jpg)
节点选项说明:
- image5: 图像输入，支持RGB和RGBA输入。
    
- mask2,5: 遮罩输入。
    
- invert_mask: 是否反转遮罩。
    
- opacity: 不透明度。
    
- [节点注解](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#%E8%8A%82%E7%82%B9%E6%B3%A8%E8%A7%A3)
    
### ColorPicker
在色板上选取颜色并输出。 改自[mtb nodes](https://github.com/melMass/comfy_mtb)的web extensions，感谢原作者。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419449.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_picker.jpg)
节点选项说明:
- mode： 输出格式，可选十六进制(HEX)或十进制(DEC)。
    
输出:
- value: 字符串格式。
    
### RGBValue
将色值输出为单独的R, G, B三个10进制数值。支持ColorPicker节点输出的HEX和DEC格式。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419983.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/RGB_value_example.jpg)
节点选项说明:
- color_value： 支持十六进制(HEX)或十进制(DEC)色值，应是string或tuple类型，强行接入其他类型将导致错误。
    
### HSVValue
将色值输出为单独的H, S, V三个10进制数值(最大值255)。支持ColorPicker节点输出的HEX和DEC格式。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419464.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/hsv_value_node.jpg)
节点选项说明:
- color_value： 支持十六进制(HEX)或十进制(DEC)色值，应是string或tuple类型，强行接入其他类型将导致错误。
    
### GetColorTone
从图片中获取主颜色或平均色。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419071.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/get_color_tone_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419563.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/get_color_tone_node.jpg)
- mode： 模式，有两种可选择，主颜色main_color和平均色average。
    
输出:
- RGB color in HEX: 使用16进制RGB字符串格式描述，例如 '#FA3D86'。
    
- HSV color in list: HSV颜色值，使用list格式描述。
    
### GetColorToneV2
GetColorTone的V2升级版。可以指定获取主体或背景的主色或平均色。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419669.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/get_color_tone_v2_example.jpg) [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419294.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/get_color_tone_v2_example2.jpg)
在GetColorTong基础上做了如下改变: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419756.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/get_color_tone_v2_node.jpg)
- color_of: 提供4个选项，mask, entire, background和subject, 分别表示选择遮罩区域，整个图片，背景，或主体的颜色。
    
- remove_background_method: 背景识别的方法, 有BiRefNet和RMBG V1.4两种可以选择。
    
- invert_mask: 是否反转遮罩。
    
- mask_grow: 遮罩扩张。对于subject, 更大的值使获得的颜色更接近主体中心的颜色。
    
输出:
- image: 纯色图片输出, 尺寸与输入的图片相同。
    
- mask: 遮罩输出。
    
### ExtendCanvas
扩展画布。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419384.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/extend_canvas_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419855.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/extend_canvas_node.jpg)
- invert_mask: 是否反转遮罩。
    
- top: 顶部扩展值。
    
- bottom: 底部扩展值。
    
- left: 左侧扩展值。
    
- right: 右侧扩展值。
    
- color; 画布颜色
    
### ExtendCanvasV2
ExtendCanvas的V2升级版。
在ExtendCanvas基础上修改了color为字符串类型，支持外接`ColorPicker`输入。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419367.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/extend_canvas_v2_node.jpg)
### XY to Percent
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419229.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/xy2percent_example.jpg) 将绝对坐标转换为百分比坐标。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419764.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/xy2percent_node.jpg) 节点选项说明:
- x: 坐标x值。
    
- y: 坐标y值。
    
### LayerImageTransform
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419400.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/layer_image_transform_example.jpg) 这个节点用于单独对layer_image进行变换，可改变大小，旋转，改变长宽比以及镜像翻转。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419950.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/layer_image_transform_node.jpg) 节点选项说明:
- x: 坐标x值。
    
- y: 坐标y值。
    
- mirror: 镜像翻转。提供2种翻转模式, 水平翻转和垂直翻转。
    
- scale: 图层放大倍数，1.0 表示原大。
    
- aspect_ratio: 图层长宽比。1.0 是原始比例，大于此值表示拉长，小于此值表示压扁。
    
- rotate: 图层旋转度数。
    
- transform_method: 用于图层放大和旋转的采样方法，包括lanczos、bicubic、hamming、bilinear、box和nearest。不同的采样方法会影响合成的画质和画面处理时间。
    
- anti_aliasing: 抗锯齿，范围从0-16，数值越大，锯齿越不明显。过高的数值将显著降低节点的处理速度。
    
### LayerMaskTransform
与LayerImageTransform类似，这个节点用于单独对layer_mask进行变换，可改变大小，旋转，改变长宽比以及镜像翻转。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419491.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/layer_mask_transform_node.jpg) 节点选项说明:
- x: 坐标x值。
    
- y: 坐标y值。
    
- mirror: 镜像翻转。提供2种翻转模式, 水平翻转和垂直翻转。
    
- scale: 图层放大倍数，1.0 表示原大。
    
- aspect_ratio: 图层长宽比。1.0 是原始比例，大于此值表示拉长，小于此值表示压扁。
    
- rotate: 图层旋转度数。
    
- transform_method: 用于图层放大和旋转的采样方法，包括lanczos、bicubic、hamming、bilinear、box和nearest。不同的采样方法会影响合成的画质和画面处理时间。
    
- anti_aliasing: 抗锯齿，范围从0-16，数值越大，锯齿越不明显。过高的数值将显著降低节点的处理速度。
    
### ColorImage
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419178.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_image_example.jpg) 生成一张指定颜色和大小的图片。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419656.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_image_node.jpg) 节点选项说明:
- width: 图像宽度。
    
- height: 图像高度。
    
- color4: 颜色。
    
### ColorImageV2
ColorImage的V2升级版。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419091.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_image_v2_node.jpg) 在ColorImage基础上做了如下改变:
- size_as*: 此处输入图像或遮罩，将按照其尺寸生成输出图像。注意，此输入优先级高于其他的尺寸设置。
    
- size**: 尺寸预设。预设可以用户自定义。如果有size_as输入，此处选项将被忽略。
    
- custom_width: 图像宽度。当size设置为"custom"时有效。如果有size_as输入，此处选项将被忽略。
    
- custom_height: 图像高度。当size设置为"custom"时有效。如果有size_as输入，此处选项将被忽略。
    
*仅限输入image和mask, 如果强制接入其他类型输入，将导致节点错误。 **预设尺寸在custom_size.ini中定义，这个文件位于插件根目录下。用文本编辑软件打开，编辑自定义尺寸。每行表示一个尺寸，第一个数值是宽度，第二个是高度，中间用小写的"x"分隔。为避免错误请不要输入多余的字符。
### GradientImage
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419701.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/gradient_image_example.jpg) 生成一张指定大小和指定颜色渐变的图片。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419471.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/gradient_image_node.jpg) 节点选项说明:
- width: 图像宽度。
    
- height: 图像高度。
    
- angle: 渐变角度。
    
- start_color4: 开始端颜色。
    
- end_color4: 结束端颜色。
    
### GradientImageV2
GradientImage的V2升级版。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419996.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/gradient_image_node_v2.jpg) 在GradientImage基础上做了如下改变:
- size_as*: 此处输入图像或遮罩，将按照其尺寸生成输出图像。注意，此输入优先级高于其他的尺寸设置。
    
- size**: 尺寸预设。预设可以用户自定义。如果有size_as输入，此处选项将被忽略。
    
- custom_width: 图像宽度。当size设置为"custom"时有效。如果有size_as输入，此处选项将被忽略。
    
- custom_height: 图像高度。当size设置为"custom"时有效。如果有size_as输入，此处选项将被忽略。
    
*仅限输入image和mask, 如果强制接入其他类型输入，将导致节点错误。 **预设尺寸在`custom_size.ini`中定义，这个文件位于插件根目录下, 默认名字是`custom_size.ini.example`, 初次使用这个文件需将文件后缀改为.ini。用文本编辑软件打开，编辑自定义尺寸。每行表示一个尺寸，第一个数值是宽度，第二个是高度，中间用小写的"x"分隔。为避免错误请不要输入多余的字符。
### ImageRewardFilter
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419120.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_reward_filter_example.jpg) 对批量图片评分并输出排名靠前的图片。这个节点使用了[ImageReward](https://github.com/THUDM/ImageReward)作为图片评分，感谢原作者。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419720.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_reward_filter_node.jpg) 节点选项说明:
- prompt: 可选输入。将prompt在此输入将作为依据判定其与图片的符合程度。
    
- output_nun: 输出的图片数量。此数值应小于图片批量。
    
输出：
- images: 按评分顺序从高到低输出的批量图片。
    
- obsolete_images: 淘汰的图片。同样按评分顺序从高到低输出。
    
### SimpleTextImage
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419618.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/simple_text_image_example.jpg) 从文字生成简单排版的图片以及遮罩。这个节点参考了[ZHO-ZHO-ZHO/ComfyUI-Text_Image-Composite](https://github.com/ZHO-ZHO-ZHO/ComfyUI-Text_Image-Composite)的部分功能和代码，感谢原作者。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419195.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/simple_text_image_node.jpg) 节点选项说明:
- size_as*: 此处输入图像或遮罩，将按照其尺寸生成输出图像和遮罩。注意，此输入优先级高于下面的width和height。
    
- text: 文字输入。
    
- font_file**: 这里列出了font文件夹中可用的字体文件列表，选中的字体文件将被用来生成图像。
    
- align: 对齐选项。有居中，靠左和靠右三个选项。
    
- char_per_line: 每行字符数量，超过的部分将自动换行。
    
- leading: 行间距。
    
- font_size: 字体大小。
    
- text_color: 文字颜色。
    
- stroke_width: 描边宽度。
    
- stroke_color: 描边颜色。
    
- x_offset: 文字位置的水平偏移量。
    
- y_offset: 文字位置的垂直偏移量。
    
- width: 画面的宽度。如果有size_as输入，此设置将被忽略。
    
- height: 画面的高度。如果有size_as输入，此设置将被忽略。
    
*仅限输入image和mask, 如果强制接入其他类型输入，将导致节点错误。 **font文件夹在`resource_dir.ini`中定义，这个文件位于插件根目录下, 默认名字是`resource_dir.ini.example`, 初次使用这个文件需将文件后缀改为.ini。用文本编辑软件打开，找到“FONT_dir=”开头的这一行，编辑“=”之后为自定义文件夹路径名。这个文件夹里面所有的.ttf和.otf文件将在ComfyUI初始化时被收集并显示在节点的列表中。如果ini中设定的文件夹无效，将启用插件自带的font文件夹。
### TextImage
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419922.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/text_image_example.jpg) 从文字生成图片以及遮罩。支持字间距行间距调整，横排竖排调整，可设置文字的随机变化，包括大小和位置的随机变化。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419435.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/text_image_node.jpg) 节点选项说明:
- size_as*: 此处输入图像或遮罩，将按照其尺寸生成输出图像和遮罩。注意，此输入优先级高于下面的width和height。
    
- font_file**: 这里列出了font文件夹中可用的字体文件列表，选中的字体文件将被用来生成图像。
    
- spacing: 字间距,以像素为单位。
    
- leading: 行间距,以像素为单位。
    
- horizontal_border: 侧边边距。此处数值表示的是百分比，例如50表示起点位于两侧的正中央。如果文字是横排，是左侧边距，竖排则是右侧边距。
    
- vertical_border: 顶部边距。此处数值表示的是百分比，例如10表示起点位于距顶部10%的位置。
    
- scale: 文字总体大小。文字的初始大小是根据画面尺寸和文字内容自动计算，默认以最长的行或者列适配画面宽或者高。调整此处数值将整体放大和缩小文字。此处数值表示的是百分比，例如60表示缩放到60%。
    
- variation_range: 字符随机变化范围。此数值大于0时，字符将产生大小和位置的随机变化，数值越大，变化幅度越大。
    
- variation_seed: 随机变化的种子。固定此数值，每次产生的单个文字的变化不会改变。
    
- layout: 文字排版。有横排和竖排可选择。
    
- width: 画面的宽度。如果有size_as输入，此设置将被忽略。
    
- height: 画面的高度。如果有size_as输入，此设置将被忽略。
    
- text_color: 文字颜色。
    
- background_color4: 背景颜色。
    
*仅限输入image和mask, 如果强制接入其他类型输入，将导致节点错误。 **font文件夹在`resource_dir.ini`中定义，这个文件位于插件根目录下, 默认名字是`resource_dir.ini.example`, 初次使用这个文件需将文件后缀改为.ini。用文本编辑软件打开，找到“FONT_dir=”开头的这一行，编辑“=”之后为自定义文件夹路径名。这个文件夹里面所有的.ttf和.otf文件将在ComfyUI初始化时被收集并显示在节点的列表中。如果ini中设定的文件夹无效，将启用插件自带的font文件夹。
### LaMa
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419024.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/lama_example.jpg) 根据图像遮罩擦除物体。本节点是对[IOPaint](https://www.iopaint.com/)的封装，由 SOTA AI 模型提供支持， 感谢原作者。 提供[LaMa](https://github.com/advimman/lama), [LDM](https://github.com/CompVis/latent-diffusion), [ZITS](https://github.com/DQiaole/ZITS_inpainting),[MAT](https://github.com/fenglinglwb/MAT), [FcF](https://github.com/SHI-Labs/FcF-Inpainting), [Manga](https://github.com/msxie92/MangaInpainting) 模型以及 SPREAD 擦除方法。请查看链接了解各个模型的介绍。 请下载模型文件 [lama models(百度网盘)](https://pan.baidu.com/s/1LllR9TJHP1G9uEwWT3Mvkg?pwd=tvzv) 或者 [lama models(Google Drive)](https://drive.google.com/drive/folders/1Aq0a4sybb3SRxi7j1e1_ZbBRjaWDdP9e?usp=sharing), 将文件放到`ComfyUI/models/lama`
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419444.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/lama_node.jpg)
- lama_model: 选择模型或方法。
    
- device: 在正确安装torch和Nvidia CUDA驱动程序后，使用cuda将明显提高运行速度。
    
- invert_mask: 是否反转遮罩。
    
- grow: 遮罩扩张幅度。正值是向外扩张，负值是向内收缩。
    
- blur: 遮罩模糊幅度。
    
### ImageChannelSplit
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419012.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_channel_split_example.jpg) 将图像通道拆分为单独的图片。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419447.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_channel_split_node.jpg)
- mode: 通道模式。包含RGBA, YCbCr, LAB和HSV。
    
### ImageChannelMerge
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419057.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_channel_merge_example.jpg) 将各通道合并为一张图片。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419505.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_channel_merge_node.jpg)
- mode: 通道模式。包含RGBA, YCbCr, LAB和HSV。
    
### ImageRemoveAlpha
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419087.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_remove_alpha_example.jpg) 移除图片的alpha通道，将图片转换为RGB模式。可选择填充背景以及设置背景颜色。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419511.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_remove_alpha_node.jpg)
- RGBA_image: 输入的图像，支持RGBA或RGB模式。
    
- mask:可选输入遮罩。如果有输入遮罩将优先使用, 忽略RGBA_image自带的alpha。
    
- fill_background: 是否填充背景。
    
- background_color4: 背景颜色。
    
### ImageCombineAlpha
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419011.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_combine_alpha_node.jpg) 将图片与遮罩合并为包含alpha通道的RGBA模式的图片。
### ImageAutoCrop
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419666.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_auto_crop_example.jpg) 自动抠图并按照遮罩裁切图片。可指定生成图片的背景颜色、长宽比和大小。这个节点是为生成训练模型的图片素材而设计的。 *请参照 [SegmentAnythingUltra](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#SegmentAnythingUltra) 和 [RemBgUltra](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/README_CN.MD#RemBgUltra) 节点的模型安装方法安装模型。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419296.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_auto_crop_node.jpg)
- background_color4: 背景颜色。
    
- aspect_ratio: 输出的宽高比。这里提供了常见的画幅比例， "custom"为自定义比例。
    
- proportional_width: 比例宽。如果aspect_ratio选项不是"custom"，此处设置将被忽略。
    
- proportional_height: 比例高。如果aspect_ratio选项不是"custom"，此处设置将被忽略。
    
- scale_by_longest_side: 允许按长边尺寸缩放。
    
- longest_side: scale_by_longest_side被设置为True时，此项将作为是图像长边的长度。
    
- detect: 探测方法，min_bounding_rect是最小外接矩形, max_inscribed_rect是最大内接矩形。
    
- border_reserve: 保留边框。在探测到的遮罩主体区域之外扩展裁切范围。
    
- ultra_detail_range: 遮罩边缘超精细处理范围，0为不处理，可以节省生成时间。
    
- matting_method: 生成遮罩的方法。有Segment Anything和 RMBG 1.4两种方法。RMBG 1.4运行速度更快。
    
- sam_model: 此处选择Segment Anything所使用的sam模型。
    
- grounding_dino_model: 此处选择Segment Anything所使用的grounding_dino模型。
    
- sam_threshold: Segment Anything的阈值。
    
- sam_prompt: Segment Anything的提示词。
    
输出: cropped_image: 裁切并更换背景后的图像。 box_preview: 裁切位置预览。 cropped_mask: 裁切后的遮罩。
### ImageAutoCropV2
`ImageAutoCrop`的V2升级版，在之前基础上做了如下改变： [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419904.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_auto_crop_v2_node.jpg)
- 增加`mask`可选输入。当有mask输入时，直接使用该输入跳过内置遮罩生成。
    
- 增加`fill_background`, 当此项设置为False时将不处理背景，并且超出画幅的部分不纳入输出范围。
    
- `aspect_ratio`增加`original`(原始画面宽高比)选项。
    
- scale_by: 允许按长边、短边、宽度或高度指定尺寸缩放。
    
- scale_by_length: 这里的数值作为scale_by指定边的长度。
    
### HLFrequencyDetailRestore
使用低频滤波加保留高频来恢复图像细节。相比[kijai's DetailTransfer](https://github.com/kijai/ComfyUI-IC-Light), 这个节点在保留细节的同时，与环境的融合度更好。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419551.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/hl_frequency_detail_restore_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419052.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/hl_frequency_detail_restore_node.jpg)
- image: 背景图片输入。
    
- detail_image: 细节原图输入。
    
- mask: 可选输入，如果有遮罩输入则仅恢复遮罩部分的细节。
    
- keep_high_freq: 保留的高频部分范围。数值越大，保留的高频细节越丰富。
    
- erase_low_freq: 擦除的低频部分范围。数值越大，擦除的低频范围越多。
    
- mask_blur: 遮罩边缘模糊度。仅在有遮罩输入的情况下有效。
    
### GetImageSize
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419577.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/get_image_size_node.jpg) 获取图片的宽度和高度。
输出:
- width: 图像宽度。
    
- height: 图像高度。
    
- original_size: 图像的原始大小数据，用于后续节点进行恢复。
    
### ImageHub
从多路输入图片和遮罩中切换其中一组输出，支持9组输入。所有的输入项都是可选项。如果一组输入中只有image或者只有mask, 缺失项将输出为None。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419216.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_hub_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419769.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_hub_node.jpg)
- output: 切换输出。数值是对应的输入组。当`random_output`选项为True时，此项设置将被忽略。
    
- random_output: 当此项为True时, 将忽略`output`设置，在所有的有效输入中随机输出一组。
    
### BatchSelector
从批量图片或遮罩中获取指定的图片或遮罩。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419287.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/batch_selector_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419787.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/batch_selector_node.jpg)
- images: 批量图片输入。此输入为可选项。
    
- masks: 批量遮罩输入。此输入为可选项。
    
- select: 选择输出的图片或遮罩在批量的索引值，0为第一张。可以输入多个值，中间用任意非数字字符分隔，包括不仅限于逗号，句号，分号，空格或者字母，甚至中文。 注意:如果数值超出批量，将输出最后一张。如果没有对应的输入，将输出一个空的64x64图片或64x64黑色遮罩。
    
### TextJoin
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419233.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/text_join_example.jpg) 将多段文字组合为一段。
### PrintInfo
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419929.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/print_info_node.jpg) 用于给工作流调试提供辅助。当运行时，任何接上这个节点的对象的属性将被打印到控制台。
这个节点允许任意类型的输入。
### TextBox
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419611.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/text_box_node.jpg) 输出字符串。
### String
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419733.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/string_node.jpg) 输出字符串。与TextBox作用相同。
### Integer
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419133.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/integer_node.jpg) 输出一个整数。
### Float
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419245.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/float_node.jpg) 输出一个浮点数，精度是小数点后5位。
### Boolean
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419033.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/boolean_node.jpg) 输出一个布尔值。
### NumberCalculator
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419819.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/number_calculator_node.jpg) 对两个数值进行数学运算并输出整数和浮点数结果*。支持的运算包括`+`、`-`、`*`、`/`、`**`、`//`、`%`。
* 输入仅支持布尔值、整数和浮点数，强行接入其他数据将导致错误。

### NumberCalculatorV2
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419803.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/number_calculator_v2_node.jpg) NumberCalculator的升级版，增加了节点内数值输入，增加了开方运算。开方运算选项为`nth_root` 注意:数值输入更优先，当有输入时节点内数值将无效。
### BooleanOperator
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419427.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/boolean_operator_node.jpg) 对两个数值进行布尔运算并输出结果*。支持的运算包括`==`、`!=`、`and`、`or`、`xor`、`not`、`min`、`max`。
* 输入仅支持布尔值、整数和浮点数，强行接入其他数据将导致错误。数值之间的`and`运算输出较大的数，`or`运算输出较小的数。

### BooleanOperatorV2
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419117.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/boolean_operator_v2_node.jpg) BooleanOperator的升级版，增加了节点内数值输入，增加了大于、小于、大于等于、小于等于的判断。 注意:数值输入更优先，当有输入时节点内数值将无效。
### StringCondition
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419169.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/string_condition_example.jpg) 判断文本中是否包含或不包含子字符串，输出布尔值。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419692.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/string_condition_node.jpg)
- text: 输入的文本。
    
- condition: 判断条件。`include`判断是否包含子字符串，`exclude`判断是否不包含子字符串。
    
- sub_string: 子字符串文本。
    
### CheckMask
检测遮罩是否包含足够的有效区域, 输出布尔值。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419510.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/check_mask_node.jpg)
- white_point: 判断遮罩是否有效的白点值，高于此值被计入有效。
    
- area_percent: 有效区域所占百分比。检测有效区域占比超过此值则输出True。
    
### If
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151419790.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/if_example.jpg) 根据布尔值条件输入切换输出。可用于任意类型的数据切换，包括且不限于数值、字符串、图片、遮罩、模型、latent、pipe管线等。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420588.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/if_node.jpg)
- if_condition: 条件输入。支持布尔值、整数、浮点数和字符串输入。输入数值时，0被判断为False；输入字符串时，空字符串被判断为Flase。
    
- when_True: 当条件为True时，将输出此项。
    
- when_False: 当条件为False时，将输出此项。
    
### SwitchCase
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420260.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/switch_case_example.jpg) 根据匹配字符串切换输出。可用于任意类型的数据切换，包括且不限于数值、字符串、图片、遮罩、模型、latent、pipe管线等。最多支持3组case切换。 将case与`switch_condition`进行比较，如果相同，则输出对应的输入项。如果有相同的case则按顺序优先输出。如果没有匹配的case，则输出默认的输入项。请注意，字符串区分大小写和中英文全角半角。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420884.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/switch_case_node.jpg)
- input_default: 用于默认输出的输入项。此输入是必选项。
    
- input_1: 用于匹配`case_1`的输入项。此输入是可选项。
    
- input_2: 用于匹配`case_2`的输入项。此输入是可选项。
    
- input_3: 用于匹配`case_3`的输入项。此输入是可选项。
    
- switch_condition: 用于与case判断的字符串。
    
- case_1: case_1字符串。
    
- case_2: case_2字符串。
    
- case_3: case_3字符串。
    
### QueueStop
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420452.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/queue_stop_example.jpg) 停止当前的队列。执行到此节点时，队列将停止。上图工作流示意了如果图片大于1Mega像素时，队列将停止执行。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420076.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/queue_stop_node.jpg)
- mode: 停止模式。如果选择`stop`,将按输入条件决定是否停止。如果选择`continue`则忽略条件继续执行队列
    
- stop: 如果为True，队列将停止。如果为False，队列将继续执行。
    
### PurgeVRAM
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420685.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/purge_vram_example.jpg) 清理GPU显存。可以接入任意类型的输入，当执行到这个节点时将清理VRAM以及RAM中的垃圾对象。通常放置在推理任务完成的节点之后，例如VAE Decode节点。
节点选项说明:
- purge_cache: 清理缓存。
    
- purge_models: 清理已加载的模型。
    
### SaveImagePlus
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420553.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/saveimage_plus_example.jpg) 增强版的保存图片节点。可自定义保存图片的目录，文件名增加时间戳，选择保存格式，设置图片压缩率，设置是否保存工作流，以及可选给图片添加隐形水印(以肉眼无法觉察的方式添加信息，使用配套的`ShowBlindWaterMark`节点可以解码水印)。可选择是否同时输出工作流的json文件。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420261.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/saveimage_plus_node.jpg)
- iamge: 输入的图片。
    
- custom_path*: 用户自定义目录，请按正确的格式输入目录名。如果为空则保存在ComfyUI默认的output目录。
    
- filename_prefix*:文件名前缀。。
    
- timestamp: 为文件名加上时间戳，可选择日期、时间到秒和时间到毫秒。
    
- format:图片保存格式。目前提供png和jpg两种。注意RGBA模式的图片仅支持png格式。
    
- quality:图片质量，数值范围10-100，数值越高，图片质量越好，文件的体积也对应增大。
    
- meta_data:是否保存元数据即工作流信息到png文件。如果不希望泄露工作流，请把这里设置为false。
    
- blind_watermark:这里输入的文字（不支持多语言）将被转换为二维码作为隐形水印保存，使用`ShowBlindWaterMark`节点可以解码水印。注意有水印的图片建议保存为png格式，质量较低的jpg格式将导致水印信息丢失。
    
- save_workflow_as_json: 是否同时输出工作流为json文件(输出的json与图片在同一目录)。
    
- preview: 预览开关。
    
*输入`%date`表示当前日期(YY-mm-dd)，`%time`表示当前时间(HH-MM-SS)。可以输入`/`表示子目录。例如`%date/name_%time` 将输出图片到`YY-mm-dd`文件夹下，以`name_HH-MM-SS`为文件名前缀。
### AddBlindWaterMark
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420249.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/watermark_example.jpg) 给图片添加隐形水印。以肉眼无法觉察的方式添加水印图片，使用`ShowBlindWaterMark`节点可以解码水印。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420757.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/add_blind_watermark_node.jpg)
- iamge: 输入的图片。
    
- watermark_image: 水印图片。这里输入的图片将自动转为正方形的黑白图片作为水印。建议使用二维码作为水印。
    
### ShowBlindWaterMark
对`AddBlindWaterMark` 和 `SaveImagePlus` 节点添加的隐形水印解码。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420656.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/show_blind_watermark_node.jpg)
### CreateQRCode
生成一个正方形的二维码图片。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420437.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/create_qrcode_node.jpg)
- size: 生成图片的边长。
    
- border: 二维码四周边框的大小，数值越大，边框越宽。
    
- text: 这里输入二维码文字内容，不支持多语言。
    
### DecodeQRCode
解码二维码。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420237.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/decode_qrcode_node.jpg)
- image: 输入二维码图片。
    
- pre_blur: 预模糊，对难以识别的二维码可以尝试调整此数值。
    
### LoadPSD
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420107.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/load_image_example_psd_file.jpg) [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420001.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/load_image_example.jpg) 加载PSD格式文件，并导出图层。 注意这个节点需要安装psd_tools依赖包，如果安装psd_tool中出现`ModuleNotFoundError: No module named 'docopt'`错误，请下载[docopt的whl](https://www.piwheels.org/project/docopt/)手动安装。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420920.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/load_image_node.jpg)
- image: 这里列出了`ComfyUI/input`下的*.psd文件，之前加载过的psd图片可以从这里选择。
    
- file_path: psd文件的完整路径以及文件名。
    
- include_hidden_layer: 是否包括隐藏图层。
    
- find_layer_by: 查找图层的方法，可选择按图层索引编号或者图层名称查找。图层组被作为一个图层对待。
    
- layer_index: 图层索引编号，0是最下面的图层，依次递增。如果include_hidden_layer设置为false，隐藏的图层不计入。设为-1则输出最上层的图层。
    
- layer_name: 图层名称。注意大小写和标点符号必须完全匹配。
    
输出: flat_image: psd预览图。 layer_iamge: 查找的图层输出。 all_layers: 包含全部图层的批量图片。
### SD3NegativeConditioning
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420556.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/sd3_negative_conditioning_node_note.jpg) 把SD3的Negative Conditioning 的4个节点封装为一个单独节点。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420051.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/sd3_negative_conditioning_node.jpg)
- zero_out_start: 设置Negative ConditioningZeroOut的ConditioningSetTimestepRange start值, 此数值与Negative的ConditioningSetTimestepRange end值相同。
    
# 遮罩 LayerMask
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420824.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/layermask_nodes.jpg)
### BlendIfMask
Photoshop图层样式-混合颜色带功能的复现。该节点输出一个mask，用于在ImageBlend或者ImageBlendAdvance节点进行图层合成。 mask为可选输入项，如果这里输入遮罩，将作用于输出结果。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420535.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/blendif_mask_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420122.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/blendif_mask_node.jpg)
- invert_mask: 是否反转遮罩。
    
- blend_if: 混合色带的通道选择。有`gray`, `red`, `green`, `blue`四个选项。
    
- black_point: 黑点值，取值范围从0-255。
    
- black_range: 暗部过渡范围。数值越大，暗部遮罩的过渡层次越丰富。
    
- white_point: 白点值，取值范围从0-255。
    
- white_range: 亮部过渡范围。数值越大，亮部遮罩的过渡层次越丰富。
    
### MaskBoxDetect
探测mask所在区域，并输出位置和大小。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420873.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_box_detect_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420975.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_box_detect_node.jpg)
- detect: 探测方法，`min_bounding_rect`是大块形状最小外接矩形, `max_inscribed_rect`是大块形状最大内接矩形, `mask_area`是遮罩像素有效区域。
    
- x_adjust: 修正探测之后的水平偏移。
    
- y_adjust: 修正探测之后的垂直偏移。
    
- scale_adjust: 修正探测之后的缩放偏移。
    
输出：
- box_preview: 探测结果预览图。红色表示探测到的结果，绿色表示加上修正后的输出结果。
    
- x_percent: 水平位置以百分比输出。
    
- y_percent: 垂直位置以百分比输出。
    
- width: 宽度输出。
    
- height: 高度输出。
    
- x: 左上角位置x坐标输出。
    
- y: 左上角位置y坐标输出。
    
## Ultra节点组
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420833.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/ultra_nodes.jpg) 一组使用了超精细边缘遮罩处理方法的节点，最新版节点包括SegmentAnythingUltraV2, RmBgUltraV2, BiRefNetUltra, PersonMaskUltraV2, SegformerB2ClothesUltra 和 MaskEdgeUltraDetailV2。 这些节点有3种边缘处理方法:
- `PyMatting` 通过遮罩 trimap, 对遮罩进行closed-form matting优化边缘。
    
- `GuideFilter` 使用 opencv guidedfilter 根据颜色相似度对边缘进行羽化，对于边缘具有很强的颜色分离时效果最佳。 以上两种方法的代码来着spacepxl的[ComfyUI-Image-Filters](https://github.com/spacepxl/ComfyUI-Image-Filters)的Alpha Matte节点，感谢原作者。
    
- `VitMatte` 使用transfromer vit模型进行高质量的边缘处理，保留边缘细节，甚至可以生成半透明遮罩。
    
- VitMatte的选项:`device` 设置是否使用cuda进行vitmatte运算，cuda运算速度比cpu快5倍左右。`max_megapixels`设置vitmatte运算的最大图片尺寸，超大的图片将缩小处理。对于16G显存建议设置为3。
    
请下载[所有的 vitmatte 模型文件](https://huggingface.co/hustvl/vitmatte-small-composition-1k/tree/main)到`ComfyUI/models/vitmatte`文件夹。
下图为三种方法输出区别的示例。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420789.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_edge_ultra_detail_v2_example.jpg)
### SegmentAnythingUltra
对[ComfyUI Segment Anything](https://github.com/storyicon/comfyui_segment_anything)的改进，使遮罩有更具细节的边缘，感谢原作者。 *请参照ComfyUI Segment Anything的安装方法安装模型。如果已经正确安装了ComfyUI Segment Anything，可跳过此步骤。
- 从 [这里](https://huggingface.co/bert-base-uncased/tree/main) 下载 config.json，model.safetensors，tokenizer_config.json，tokenizer.json 和 vocab.txt 5个文件到 `ComfyUI/models/bert-base-uncased`文件夹。
    
- 下载 [GroundingDINO_SwinT_OGC config file](https://huggingface.co/ShilongLiu/GroundingDINO/resolve/main/GroundingDINO_SwinT_OGC.cfg.py), [GroundingDINO_SwinT_OGC model](https://huggingface.co/ShilongLiu/GroundingDINO/resolve/main/groundingdino_swint_ogc.pth), [GroundingDINO_SwinB config file](https://huggingface.co/ShilongLiu/GroundingDINO/resolve/main/GroundingDINO_SwinB.cfg.py), [GroundingDINO_SwinB model](https://huggingface.co/ShilongLiu/GroundingDINO/resolve/main/groundingdino_swinb_cogcoor.pth) 到 `ComfyUI/models/grounding-dino`文件夹。
    
- 下载 [sam_vit_h](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth)，[sam_vit_l](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth), [sam_vit_b](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth), [sam_hq_vit_h](https://huggingface.co/lkeab/hq-sam/resolve/main/sam_hq_vit_h.pth), [sam_hq_vit_l](https://huggingface.co/lkeab/hq-sam/resolve/main/sam_hq_vit_l.pth), [sam_hq_vit_b](https://huggingface.co/lkeab/hq-sam/resolve/main/sam_hq_vit_b.pth), [mobile_sam](https://github.com/ChaoningZhang/MobileSAM/blob/master/weights/mobile_sam.pt) 这几个文件到`ComfyUI/models/sams`文件夹。
    
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420864.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/segment_anything_ultra_compare.jpg) [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420511.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/segment_anything_ultra_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420955.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/segment_anything_ultra_node.jpg)
- sam_model: 选择SAM模型。
    
- ground_dino_model: 选择Grounding DINO模型。
    
- threshold: SAM阈值。
    
- detail_range: 边缘细节范围。
    
- black_point: 边缘黑色采样阈值。
    
- white_point: 边缘黑色采样阈值。
    
- process_detail: 此处设为False将跳过边缘处理以节省运行时间。
    
- prompt: SAM的prompt输入。
    
### SegmentAnythingUltraV2
SegmentAnythingUltra的V2升级版，增加了VITMatte边缘处理方法。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420647.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/ultra_v2_nodes_example.jpg)
在SegmentAnythingUltra的基础上做了如下改变: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420507.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/segment_anything_ultra_v2_node.jpg)
- detail_method: 边缘处理方法。提供了VITMatte, VITMatte(local), PyMatting, GuidedFilter。
    
- detail_erode: 遮罩边缘向内侵蚀范围。数值越大，向内修复的范围越大。
    
- detail_dilate: 遮罩边缘向外扩张范围。数值越大，向外修复的范围越大。
    
- device: 设置是否使用cuda。
    
- max_megapixels: 设置vitmatte运算的最大尺寸。
    
### Florence2Ultra
使用 Florence2 模型的分割功能，同时具有超高的边缘细节。 本节点部分的代码来自[spacepxl/ComfyUI-Florence-2](https://github.com/spacepxl/ComfyUI-Florence-2)，感谢原作者。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420398.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/florence2_ultra_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420098.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/florence2_ultra_node.jpg)
- florence2_model: Florence2模型输入。
    
- image: 图片输入。
    
- task: 选择florence2任务。
    
- text_input: florence2任务文本输入。
    
- detail_method: 边缘处理方法。提供了VITMatte, VITMatte(local), PyMatting, GuidedFilter。如果首次使用VITMatte后模型已经下载，之后可以使用VITMatte(local)。
    
- detail_erode: 遮罩边缘向内侵蚀范围。数值越大，向内修复的范围越大。
    
- detail_dilate: 遮罩边缘向外扩张范围。数值越大，向外修复的范围越大。
    
- black_point: 边缘黑色采样阈值。
    
- white_point: 边缘黑色采样阈值。
    
- process_detail: 此处设为False将跳过边缘处理以节省运行时间。
    
- device: 设置是否使用cuda。
    
- max_megapixels: 设置vitmatte运算的最大尺寸。
    
### LoadFlorence2Model
Florence2 模型加载器。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420960.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/load_florence2_model_node.jpg) 目前有 base, base-ft, large, large-ft, DocVQA, SD3-Captioner 和 base-PromptGen模型可以选择。
### RemBgUltra
去除背景。与类似的背景移除节点相比，这个节点具有超高的边缘细节。 本节点结合了spacepxl的[ComfyUI-Image-Filters](https://github.com/spacepxl/ComfyUI-Image-Filters)的Alpha Matte节点，以及ZHO-ZHO-ZHO的[ComfyUI-BRIA_AI-RMBG](https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG)的功能，感谢原作者。
*将[BRIA Background Removal v1.4](https://huggingface.co/briaai/RMBG-1.4)模型文件(model.pth)下载至`ComfyUI/models/rmbg/RMBG-1.4`文件夹。该模型由 BRIA AI 开发，可作为非商业用途的开源模型。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420050.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/rembg_ultra_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420738.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/rembg_ultra_node.jpg)
- detail_range: 边缘细节范围。
    
- black_point: 边缘黑色采样阈值。
    
- white_point: 边缘黑色采样阈值。
    
- process_detail: 此处设为False将跳过边缘处理以节省运行时间。
    
### RmBgUltraV2
RemBgUltra的V2升级版，增加了VITMatte边缘处理方法。
在RemBgUltra的基础上做了如下改变: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420427.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/rmbg_ultra_v2_node.jpg)
- detail_method: 边缘处理方法。提供了VITMatte, VITMatte(local), PyMatting, GuidedFilter。如果首次使用VITMatte后模型已经下载，之后可以使用VITMatte(local)。
    
- detail_erode: 遮罩边缘向内侵蚀范围。数值越大，向内修复的范围越大。
    
- detail_dilate: 遮罩边缘向外扩张范围。数值越大，向外修复的范围越大。
    
- device: 设置是否使用cuda。
    
- max_megapixels: 设置vitmatte运算的最大尺寸。
    
### BiRefNetUltra
使用BiRefNet模型去除背景，有更好的识别能力，同时具有超高的边缘细节。 本节点模型部分的代码来自vipery的[ComfyUI-BiRefNet](https://github.com/viperyl/ComfyUI-BiRefNet)，感谢原作者。
*从[https://huggingface.co/ViperYX/BiRefNet](https://huggingface.co/ViperYX/BiRefNet/tree/main)下载`BiRefNet-ep480.pth`,`pvt_v2_b2.pth`,`pvt_v2_b5.pth`,`swin_base_patch4_window12_384_22kto1k.pth`, `swin_large_patch4_window12_384_22kto1k.pth`5个文件至`ComfyUI/models/BiRefNet`文件夹。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420988.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/birefnet_ultra_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420806.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/birefnet_ultra_node.jpg)
- detail_method: 边缘处理方法。提供了VITMatte, VITMatte(local), PyMatting, GuidedFilter。如果首次使用VITMatte后模型已经下载，之后可以使用VITMatte(local)。
    
- detail_erode: 遮罩边缘向内侵蚀范围。数值越大，向内修复的范围越大。
    
- detail_dilate: 遮罩边缘向外扩张范围。数值越大，向外修复的范围越大。
    
- black_point: 边缘黑色采样阈值。
    
- white_point: 边缘黑色采样阈值。
    
- process_detail: 此处设为False将跳过边缘处理以节省运行时间。
    
- device: 设置是否使用cuda。
    
- max_megapixels: 设置vitmatte运算的最大尺寸。
    
### TransparentBackgroundUltra
使用transparent-background模型去除背景，有更好的识别能力和识别速度，同时具有超高的边缘细节。
*从 [googledrive](https://drive.google.com/drive/folders/10KBDY19egb8qEQBv34cqIVSwd38bUAa9?usp=sharing) 或 [百度网盘](https://pan.baidu.com/s/1CYZ4VwvU06e-02BKRUj9QQ?pwd=jjt9) 下载全部文件至`ComfyUI/models/transparent-background`文件夹。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420388.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/transparent_background_ultra_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420241.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/transparent_background_ultra_node.jpg)
- model: 选择模型。
    
- detail_method: 边缘处理方法。提供了VITMatte, VITMatte(local), PyMatting, GuidedFilter。如果首次使用VITMatte后模型已经下载，之后可以使用VITMatte(local)。
    
- detail_erode: 遮罩边缘向内侵蚀范围。数值越大，向内修复的范围越大。
    
- detail_dilate: 遮罩边缘向外扩张范围。数值越大，向外修复的范围越大。
    
- black_point: 边缘黑色采样阈值。
    
- white_point: 边缘黑色采样阈值。
    
- process_detail: 此处设为False将跳过边缘处理以节省运行时间。
    
- device: 设置是否使用cuda。
    
- max_megapixels: 设置vitmatte运算的最大尺寸。
    
### PersonMaskUltra
为人物生成脸、头发、身体皮肤、衣服或配饰的遮罩。与之前的A Person Mask Generator节点相比，这个节点具有超高的边缘细节。 本节点的模型代码来自[a-person-mask-generator](https://github.com/djbielejeski/a-person-mask-generator)，边缘处理代码来自spacepxl的[ComfyUI-Image-Filters](https://github.com/spacepxl/ComfyUI-Image-Filters)，感谢原作者。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420023.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/person_mask_ultra_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420809.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/person_mask_ultra_node.jpg)
- face: 脸部识别。
    
- hair: 头发识别。
    
- body: 身体皮肤识别。
    
- clothes: 衣服识别。
    
- accessories: 配饰(例如背包)识别。
    
- background: 背景识别。
    
- confidence: 识别阈值，更低的值将输出更多的遮罩范围。
    
- detail_range: 边缘细节范围。
    
- black_point: 边缘黑色采样阈值。
    
- white_point: 边缘黑色采样阈值。
    
- process_detail: 此处设为False将跳过边缘处理以节省运行时间。
    
### PersonMaskUltraV2
PersonMaskUltra的V2升级版，增加了VITMatte边缘处理方法。
在PersonMaskUltra的基础上做了如下改变: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420559.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/person_mask_ultra_v2_node.jpg)
- detail_method: 边缘处理方法。提供了VITMatte, VITMatte(local), PyMatting, GuidedFilter。如果首次使用VITMatte后模型已经下载，之后可以使用VITMatte(local)。
    
- detail_erode: 遮罩边缘向内侵蚀范围。数值越大，向内修复的范围越大。
    
- detail_dilate: 遮罩边缘向外扩张范围。数值越大，向外修复的范围越大。
    
- device: 设置是否使用cuda。
    
- max_megapixels: 设置vitmatte运算的最大尺寸。
    
### SegformerB2ClothesUltra
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420405.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/segformer_ultra_example.jpg) 为人物生成脸、头发、手臂、腿以及服饰的遮罩，主要用于分割服装。模型分割代码来自[StartHua](https://github.com/StartHua/Comfyui_segformer_b2_clothes)，感谢原作者。 与comfyui_segformer_b2_clothes节点相比，这个节点具有超高的边缘细节。
*从[这里](https://huggingface.co/mattmdjaga/segformer_b2_clothes/tree/main)下载全部文件至`ComfyUI/models/segformer_b2_clothes`文件夹。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420137.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/segformer_ultra_node.jpg)
- face: 脸部识别。
    
- hair: 头发识别。
    
- hat: 帽子识别。
    
- sunglass: 墨镜识别。
    
- left_arm:左手臂识别。
    
- right_arm:右手臂识别。
    
- left_leg:左腿识别。
    
- right_leg:右腿识别。
    
- skirt:短裙识别。
    
- pants:裤子识别。
    
- dress:连衣裙识别。
    
- belt:腰带识别。
    
- shoe:鞋子识别。
    
- bag:背包识别。
    
- scarf:围巾识别。
    
- detail_method: 边缘处理方法。提供了VITMatte, VITMatte(local), PyMatting, GuidedFilter。如果首次使用VITMatte后模型已经下载，之后可以使用VITMatte(local)。
    
- detail_erode: 遮罩边缘向内侵蚀范围。数值越大，向内修复的范围越大。
    
- detail_dilate: 遮罩边缘向外扩张范围。数值越大，向外修复的范围越大。
    
- black_point: 边缘黑色采样阈值。
    
- white_point: 边缘黑色采样阈值。
    
- process_detail: 此处设为False将跳过边缘处理以节省运行时间。
    
- device: 设置是否使用cuda。
    
- max_megapixels: 设置vitmatte运算的最大尺寸。
    
### SegformerUltraV2
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420925.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/segformer_clothes_example.jpg) [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420700.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/segformer_fashion_example.jpg) 使用segformer模型分割服饰，具有超高的边缘细节。目前支持segformer b2 clothes, segformer b3 clothes, segformer b3 fashion。
*从[这里](https://huggingface.co/mattmdjaga/segformer_b2_clothes/tree/main)下载全部文件至`ComfyUI/models/segformer_b2_clothes`文件夹。 *从[这里](https://huggingface.co/sayeed99/segformer_b3_clothes/tree/main)下载全部文件至`ComfyUI/models/segformer_b3_clothes`文件夹。 *从[这里](https://huggingface.co/sayeed99/segformer-b3-fashion/tree/main)下载全部文件至`ComfyUI/models/segformer_b3_fashion`文件夹。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420507.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/segformer_ultra_v2_node.jpg)
- image: 图像输入。
    
- segformer_pipeline: segformer管线输入。管线由SegformerClothesPipeline和SegformerFashionPipeline节点输出。
    
- detail_method: 边缘处理方法。提供了VITMatte, VITMatte(local), PyMatting, GuidedFilter。如果首次使用VITMatte后模型已经下载，之后可以使用VITMatte(local)。
    
- detail_erode: 遮罩边缘向内侵蚀范围。数值越大，向内修复的范围越大。
    
- detail_dilate: 遮罩边缘向外扩张范围。数值越大，向外修复的范围越大。
    
- black_point: 边缘黑色采样阈值。
    
- white_point: 边缘黑色采样阈值。
    
- process_detail: 此处设为False将跳过边缘处理以节省运行时间。
    
- device: 设置是否使用cuda。
    
- max_megapixels: 设置vitmatte运算的最大尺寸。
    
### SegformerClothesPipiline
选择segformer clothes模型，并选择分割内容。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420168.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/segformer_clothes_pipeline_node.jpg)
- model: 模型选择。目前有两种模型可供选择segformer b2 clothes, segformer b3 clothes。
    
- face: 脸部识别。
    
- hair: 头发识别。
    
- hat: 帽子识别。
    
- sunglass: 墨镜识别。
    
- left_arm:左手臂识别。
    
- right_arm:右手臂识别。
    
- left_leg:左腿识别。
    
- right_leg:右腿识别。
    
- left_shoe: 左鞋子识别。
    
- right_shoe: 右鞋子识别。
    
- skirt:短裙识别。
    
- pants:裤子识别。
    
- dress:连衣裙识别。
    
- belt:腰带识别。
    
- bag:背包识别。
    
- scarf:围巾识别。
    
### SegformerFashionPipiline
选择segformer fashion模型，并选择分割内容。
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420962.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/segformer_fashion_pipeline_node.jpg)
- model: 模型选择。目前只有一种模型可供选择segformer b3 fashion。
    
- shirt: 衬衫、罩衫识别。
    
- top: 上衣、t恤、运动衫识别。
    
- sweater: 毛衣识别。
    
- cardigan: 开襟毛衫识别。
    
- jacket: 夹克识别。
    
- vest: 背心识别。
    
- pants: 裤子识别。
    
- shorts: 短裤识别。
    
- skirt: 短裙识别。
    
- coat: 外套识别。
    
- dress: 连衣裙识别。
    
- jumpsuit: 连身裤识别。
    
- cape: 斗篷识别。
    
- glasses: 眼镜识别。
    
- hat: 帽子识别。
    
- hairaccessory: 头带、头巾、发饰识别。
    
- tie: 领带识别。
    
- glove: 手套识别。
    
- watch: 手表识别。
    
- belt: 皮带识别。
    
- legwarmer: 腿套识别。
    
- tights: 紧身裤和长筒袜识别。
    
- sock: 袜子识别。
    
- shoe: 鞋子识别。
    
- bagwallet: 背包、钱包识别。
    
- scarf: 围巾识别。
    
- umbrella: 雨伞识别。
    
- hood: 兜帽识别。
    
- collar: 衣领识别。
    
- lapel: 翻领识别。
    
- epaulette: 肩章识别。
    
- sleeve: 袖子识别。
    
- pocket: 口袋识别。
    
- neckline: 领口识别。
    
- buckle: 带扣识别。
    
- zipper: 拉链识别。
    
- applique: 贴花识别。
    
- bead: 珠子识别。
    
- bow: 蝴蝶结识别。
    
- flower: 花识别。
    
- fringe: 刘海识别。
    
- ribbon: 丝带识别。
    
- rivet: 铆钉识别。
    
- ruffle: 褶饰识别。
    
- sequin: 亮片识别。
    
- tassel: 流苏识别。
    
### MaskEdgeUltraDetail
处理较粗糙的遮罩使其获得超精细边缘。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420690.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_edge_ultra_detail_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420491.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_edge_ultra_detail_node.jpg)
- method: 提供PyMatting和OpenCV-GuidedFilter两种方法处理边缘。PyMatting处理速度较慢，但是对于视频，建议使用这种方法获得更平滑的遮罩序列。
    
- mask_grow: 遮罩扩张幅度。正值是向外扩张，负值是向内收缩。对于较粗糙的遮罩，通常使用负值使其边缘收缩以获得更好的效果。
    
- fix_gap: 修补遮罩中的空隙。如果遮罩中有比较明显的空隙，适当调高此数值。
    
- fix_threshold: 修补遮罩的阈值。
    
- detail_range: 边缘细节范围。
    
- black_point: 边缘黑色采样阈值。
    
- white_point: 边缘黑色采样阈值。
    
### MaskEdgeUltraDetailV2
MaskEdgeUltraDetail的V2升级版，增加了VITMatte边缘处理方法，此方法适合处理半透明区域。 在MaskEdgeUltraDetail的基础上做了如下改变: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420238.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_edge_ultra_detail_v2_node.jpg)
- method: 边缘处理方法。增加了VITMatte和VITMatte(local)方法。如果首次使用VITMatte后模型已经下载，之后可以使用VITMatte(local)。
    
- edge_erode: 遮罩边缘向内侵蚀范围。数值越大，向内修复的范围越大。
    
- edge_dilate: 遮罩边缘向外扩张范围。数值越大，向外修复的范围越大。
    
- device: 设置是否使用cuda。
    
- max_megapixels: 设置vitmatte运算的最大尺寸。
    
### YoloV8Detect
使用YoloV8模型检测人脸、手部box区域，或者人物分割。支持输出所选择数量的通道。 请在 [GoogleDrive](https://drive.google.com/drive/folders/1I5TISO2G1ArSkKJu1O9b4Uvj3DVgn5d2) 或者 [百度网盘](https://pan.baidu.com/s/1ImoJrzL1zDgaCqaSzrNEtw?pwd=5xgk) 下载模型文件并放到 `ComfyUI/models/yolo` 文件夹。
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420092.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/yolov8_detect_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420831.jpg)![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420831.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/yolov8_detect_node.jpg)https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/yolov8_detect_node.jpg
- yolo_model: yolo模型选择。带有`seg`名字的模型可以输出分割的mask, 否则只能输出box区域的遮罩。
    
- mask_merge: 选择合并的遮罩。`all`是合并全部遮罩输出。选数值是输出多少个遮罩，按识别置信度排序合并输出。
    
输出:
- mask: 输出的遮罩。
    
- yolo_plot_image: yolo识别结果预览图。
    
- yolo_masks: yolo识别出来的所有遮罩，每个单独的遮罩输出为一个mask。
    
### MediapipeFacialSegment
使用Mediapipe模型检测人脸五官，分割左右眉、眼睛、嘴唇和牙齿。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420796.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mediapipe_facial_segment_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420551.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mediapipe_facial_segment_node.jpg)
- left_eye: 左眼识别开关。
    
- left_eyebrow: 左眉识别开关。
    
- right_eye: 右眼识别开关。
    
- right_eyebrow: 右眉识别开关。
    
- lips: 嘴唇识别开关。
    
- tooth: 牙齿识别开关。
    
### MaskByColor
根据颜色生成遮罩。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420369.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_by_color_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420404.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_by_color_node.jpg)
- image: 图像输入。
    
- mask: 遮罩输入。此输入是可选项，如果有遮罩则仅遮罩内的颜色被纳入范围。
    
- color: 颜色选择器。点击色块选择颜色，可以使用选色器面板上的吸管拾取屏幕颜色。注意:使用吸管时，需将浏览器窗口最大化。
    
- color_in_HEX4: 输入色值。如果此项有输入，则优先使用，忽略`color`选取的颜色。
    
- threshold: 遮罩范围阈值，数值越大，遮罩范围越大。
    
- fix_gap: 修补遮罩中的空隙。如果遮罩中有比较明显的空隙，适当调高此数值。
    
- fix_threshold: 修补遮罩的阈值。
    
- invert_mask: 是否反转遮罩。
    
### ImageToMask
将图片转为遮罩。支持以LAB，RGBA, YUV 和 HSV模式的任意通道转换为遮罩，同时提供色阶调整。支持mask可选输入以获取仅包括有效部分的遮罩。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420281.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_to_mask_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420171.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/image_to_mask_node.jpg)
- image: 图像输入。
    
- mask: 遮罩输入。此输入是可选项，如果有遮罩则仅遮罩内的颜色被纳入范围。
    
- channel: 通道选择。可以选择LAB，RGBA, YUV 和 HSV模式的任意一个通道。
    
- black_point*: 遮罩黑点值。取值范围0-255, 默认值0。
    
- white_point*: 遮罩白点值。取值范围0-255, 默认值255。
    
- gray_point: 遮罩灰点值。取值范围0.01-9.99, 默认1。
    
- invert_output_mask: 是否反转遮罩。
    
*如果 black_point 或 output_black_point 数值大于 white_point 或 output_white_point，则两个数值将交换，较大的数值作为white_point使用，较小的数值作为black_point使用。
### Shadow & Highlight Mask
生成图像暗部和亮部的遮罩。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420153.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/shadow_and_highlight_mask_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420147.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/shadow_and_highlight_mask_node.jpg)
- image: 图像输入。
    
- mask: 可选输入。如果有输入，将只调整遮罩范围内的颜色。
    
- shadow_level_offset: 暗部取值的偏移量，更大的数值使更多靠近明亮的区域纳入暗部。
    
- shadow_range: 暗部的过渡范围。
    
- highlight_level_offset: 亮部取值的偏移量，更小的数值使更多靠近阴暗的区域纳入亮部。
    
- highlight_range: 亮部的过渡范围。
    
### PixelSpread
对图像的遮罩边缘部分进行像素扩张预处理，可有效改善图像合成的边缘。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420224.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/pixel_spread_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420192.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/pixel_spread_node.jpg)
- invert_mask: 是否反转遮罩。
    
- mask_grow: 遮罩扩张幅度。
    
### MaskByDifferent
计算两张图像不同之处，并输出为遮罩。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420244.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_by_different_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420063.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_by_different_node.jpg)
- gain: 计算增益。调高此值，微弱的差异将更显著的呈现。
    
- fix_gap: 修补遮罩内部缝隙。更高的值将修补更大的缝隙。
    
- fix_threshold: 修补阈值。
    
- main_subject_detect: 此项设为True将开启主体侦测，忽略主体之外的差异。
    
### MaskGrow
对mask进行扩张收缩边缘和模糊处理 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420810.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_grow_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420861.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_grow_node.jpg)
- invert_mask: 是否反转遮罩。
    
- grow: 扩张幅度。正值是向外扩张，负值是向内收缩。
    
- blur: 模糊。
    
### MaskEdgeShrink
使mask边缘平滑地过渡收缩，并保留边缘细节。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420676.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_edge_shrink_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420435.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_edge_shrink_node.jpg)
- invert_mask: 是否反转遮罩。
    
- shrink_level: 收缩平滑级别。
    
- soft: 平滑幅度。
    
- edge_shrink: 边缘收缩幅度。
    
- edge_reserve: 保留边缘细节幅度, 100为完全保留，0为完全不保留。
    
MaskGrow与MaskEdgeShrink效果对比 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420289.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_edge_compare.jpg)
### MaskMotionBlur
使mask产生运动模糊。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420584.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_motion_blur_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151420294.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_motion_blur_node.jpg)
- invert_mask: 是否反转遮罩。
    
- blur: 模糊大小。
    
- angle: 模糊角度。
    
### MaskGradient
使mask从一侧产生渐变。请注意此节点与CreateGradientMask的区别。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421263.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_gradient_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421029.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_gradient_node.jpg)
- invert_mask: 是否反转遮罩。
    
- gradient_side: 从哪个边产生渐变。有四个方向：顶侧top、底侧bottom、左侧left、右侧right。
    
- gradient_scale: 渐变距离。默认值100表示渐变产生一侧完全透明，另一侧完全不透明。数值越小，从透明到不透明的距离越短。
    
- gradient_offset: 渐变位置偏移。
    
- opacity: 渐变的不透明度。
    
### CreateGradientMask
创建一个渐变的遮罩。请注意此节点与MaskGradient的区别。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421049.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/create_gradient_mask_example.jpg) [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421931.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/create_gradient_mask_example2.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421666.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/create_gradient_mask_node.jpg)
- size_as*: 此处输入图像或遮罩，将按照其尺寸生成输出图像和遮罩。注意，此输入优先级高于下面的width和height。
    
- width: 画面的宽度。如果有size_as输入，此设置将被忽略。
    
- height: 画面的高度。如果有size_as输入，此设置将被忽略。
    
- gradient_side: 从哪个边产生渐变。有5个方向：顶侧top、底侧bottom、左侧left、右侧right和中央center。
    
- gradient_scale: 渐变距离。默认值100表示渐变产生一侧完全透明，另一侧完全不透明。数值越小，从透明到不透明的距离越短。
    
- gradient_offset: 渐变位置偏移。`gradient_side`为center时这里调整渐变区域的大小，正值是变小，负值是扩大。
    
- opacity: 渐变的不透明度。
    
*仅限输入image和mask, 如果强制接入其他类型输入，将导致节点错误。
### MaskStroke
产生mask轮廓描边。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421844.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_stroke_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421697.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_stroke_node.jpg)
- invert_mask: 是否反转遮罩。
    
- stroke_grow: 描边扩张/收缩幅度，正值是扩张，负值是收缩。
    
- stroke_width: 描边宽度。
    
- blur: 描边模糊。
    
### MaskGrain
为遮罩生成噪声。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421504.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_grain_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421442.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_grain_node.jpg)
- grain: 噪声强度。
    
- invert_mask: 是否反转遮罩。
    
### MaskPreview
预览mask [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421489.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_invert.jpg)
### MaskInvert
mask反转 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421262.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/mask_invert_node.jpg)
# 滤镜 LayerFilter
[![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421120.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/layerfilter_nodes.jpg)
### Sharp & Soft
为图像增强细节或抹平细节。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421121.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/sharp_and_soft_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421822.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/sharp_and_soft_node.jpg)
- enhance: 提供四个预设档位，分别是very sharp、sharp、soft和very soft。选None则不做任何处理。
    
### SkinBeauty
磨皮效果。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421749.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/skin_beauty_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421552.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/skin_beauty_node.jpg)
- smooth: 皮肤平滑度。
    
- threshold: 磨皮范围。数值越小范围越大。
    
- opacity: 磨皮的不透明度。
    
### WaterColor
水彩画效果。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421413.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/water_color_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421167.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/water_color_node.jpg)
- line_density: 线条密度。
    
- opacity: 水彩效果的不透明度。
    
### SoftLight
柔光效果。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421001.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/soft_light_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421883.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/soft_light_node.jpg)
- soft: 柔光大小。
    
- threshold: 柔光范围。柔光从画面最明亮的部分呈现。数值越低范围越大，越高范围越小。
    
- opacity: 柔光的不透明度。
    
### ChannelShake
通道错位。类似抖音logo的效果。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421696.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/channel_shake_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421484.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/channel_shake_node.jpg)
- distance: 通道分离的距离。
    
- angle: 通道分离的角度。
    
- mode: 通道错位排列顺序。
    
### HDR Effects
增强图像的动态范围。 这个节点是[HDR Effects (SuperBeasts.AI)](https://github.com/SuperBeastsAI/ComfyUI-SuperBeasts)的重新封装。感谢原作者。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421312.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/hdr_effects_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421088.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/hdr_effects_node.jpg)
- hdr_intensity: 范围0-5, 控制HDR效果的整体强度, 数值越高，效果越明显。
    
- shadow_intensity: 范围0-1，调整图像阴影部分的强度，较高的值会使阴影变暗并增加对比度。
    
- highlight_intensity: 范围0-1，调整图像高光部分的强度，较高的值可使高光变亮并增加对比度。
    
- gamma_intensity: 范围0-1，用于图像的伽玛校正，值越高，整体亮度和对比度越高。
    
- contrast: 范围0-1，增强图像的对比度, 值越高，对比度越明显。
    
- enhance_color: 范围0-1，增强图像的色彩饱和度, 值越高，颜色越鲜艳。
    
### Film
模拟胶片的颗粒、暗边和边缘模糊，支持输入深度图模拟虚焦。 这个节点是[digitaljohn/comfyui-propost](https://github.com/digitaljohn/comfyui-propost)的重新封装，感谢原作者。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421455.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/film_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421283.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/film_node.jpg)
- image: 输入的图片。
    
- depth_map: 深度图输入，由此模拟虚焦效果。此项是可选输入，如果没有输入则模拟为图片边缘的径向模糊。
    
- center_x: 暗边和径向模糊的中心点位置横坐标，0表示最左侧，1表示最右侧，0.5表示在中心。
    
- center_y: 暗边和径向模糊的中心点位置纵坐标，0表示最上方，1表示最下方，0.5表示在中心。
    
- saturation: 颜色饱和度，1为原始值。
    
- grain_power: 噪点强度。数值越大，噪点越明显。
    
- grain_scale: 噪点颗粒大小。数值越大，颗粒越大。
    
- grain_sat: 噪点的色彩饱和度。0表示黑白噪点，数值越大，彩色越明显。
    
- grain_shadows: 暗部噪点强度。
    
- grain_highs: 亮部噪点强度。
    
- blur_strength: 模糊强度。数值越大越模糊。
    
- blur_focus_spread: 焦点扩散范围。数值越大，清晰的范围越大。
    
- focal_depth: 模拟虚焦的焦点距离。0表示焦点在最远，1表示焦点在最近。此项设置只在depth_map有输入时才生效。
    
### FilmV2
Film节点的升级版, 在之前基础上增加了fastgrain方法，生成噪点速度加快了10倍。fastgrain的代码来自[github.com/spacepxl/ComfyUI-Image-Filters](https://github.com/spacepxl/ComfyUI-Image-Filters)的BetterFilmGrain部分，感谢原作者。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421180.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/film_v2_node.jpg)
### LightLeak
模拟胶片漏光效果。请下载[light_leak.pkl(百度网盘)](https://pan.baidu.com/s/1QY1ZyYm885krrqDB2t8lPg?pwd=yvs3)或[light_leak.pkl(Google Drive)(https://drive.google.com/file/d/1DcH2Zkyj7W3OiAeeGpJk1eaZpdJwdCL-/view?usp=sharing)将文件复制到`ComfyUI/models/layerstyle` 文件夹。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421983.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/light_leak_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421789.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/light_leak_node.jpg)
- light: 提供了32种光斑。random为随机选择。
    
- corner: 光斑出现的角落，有左上、右上、左下和右下4个选项。
    
- hue: 光斑的色相。
    
- saturation: 光斑的色彩饱和度。
    
- opacity: 光斑的不透明度。
    
### ColorMap
伪彩色热力图效果。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421064.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/colormap_result.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421259.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/color_map_node.jpg)
- color_map: 效果类型。共22种，各种类型的效果如上图所示。
    
- opacity: 伪彩色效果的不透明度。
    
### MotionBlur
运动模糊。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421072.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/motion_blur_example.jpg)
节点选项说明:
- angle: 模糊角度。
    
- blur: 模糊大小。
    
### GaussianBlur
高斯模糊。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421930.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/gaussian_blur_example.jpg)
节点选项说明:
- blur: 模糊大小。
    
### AddGrain
给图片增加噪声。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421715.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/add_grain_example.jpg)
节点选项说明: [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421399.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/add_grain_node.jpg)
- grain_power: 噪声强度。
    
- grain_scale: 噪声的大小。
    
- grain_sat: 噪声的色彩饱和度。
    
## 节点注解
1 image、mask和background_image(如果有输入)这三项必须是相同的尺寸。
2 mask不是必须的输入项，默认使用image的alpha通道，如果image输入不包含alpha通道将自动创建整个图像的alpha通道。如果输入mask，原本的alpha通道将被mask覆盖。
3 混合模式 包括normal、multply、screen、add、subtract、difference、darker、lighter、color_burn、color_dodge、linear_burn、linear_dodge、overlay、soft_light、hard_light、vivid_light、pin_light、linear_light、hard_mix, 共19种混合模式。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421573.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/blend_mode_result.jpg) *混合模式预览
3 混合模式V2 包括nomal, dissolve, darken, multiply, color burn, linear burn, darker color, lighten, screen, color dodge, linear dodge(add), lighter color, dodge, overlay, soft light, hard light, vivid light, linear light, pin light, hard mix, difference, exclusion, subtract, divide, hue, saturation, color, luminosity, grain extract, grain merge共30种模式。 混合模式V2的部分代码来自[Virtuoso Nodes for ComfyUI](https://github.com/chrisfreilich/virtuoso-nodes)的`Blend Modes`节点。感谢原作者。 [![image](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202408151421454.jpg)](https://github.com/chflame163/ComfyUI_LayerStyle/blob/main/image/blend_mode_v2_example.jpg) *混合模式V2版预览
4 颜色使用16进制RGB字符串格式描述，例如 '#FA3D86'。
5 image和mask这两项必须是相同的尺寸。
