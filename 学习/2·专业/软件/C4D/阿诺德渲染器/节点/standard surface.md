# standard surface

标准材质

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image_qoEcJkNjEC.png)

# Base 基础色

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image_tsyyOnGdQe.png)

根据日常经验基础颜色最好不要使用 100% 白色或黑色尤其是 ACES 工作流中，通常最白的 RGB 值为 235\~240 黑色大约 40%\~60% 纯白和纯黑在自然界很少见，所以保持基础颜色在真实的色彩范围内。

金属预设

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image_CH5R-ZpyS1.png)

# Specular镜面反射

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image_i0or0WSuD0.png)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image_aYEKf08Zxb.png)

# Transimission 透射

透射允许灯光穿过表面发生散射可以创建折射或透射材质,像玻璃、水、蜂蜜、巧克力、焦糖等等。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1602140183756-d8b6f57a-bdd1-4d9a-8167-98f55ba4b330.png)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image_--v6suU6yu.png)

# SubSurface 次表明

SSS材质是Sub-Surface-Scattering的简写

SSS 用于大理石、皮肤、树叶、蜡和牛奶等材质的真实渲染效果。

主要调节的参数是半径，这个直接影响 SSS 的通透感。

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1602141027844-e1d5d27d-b0d0-4bb6-9b15-af5e4de91afd.png)

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image_orEO8P7Fpx.png)

# Coat 涂层

可将涂层部分看作覆盖整个材质之上的第二层镜面反射可以用于一切之上来得到非常清晰的透明涂层。比如车漆或在镜面反射之上包裹一个更清晰的镜面反射以看起来更真实

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1602143033674-a47a1e09-fd3d-4900-bd85-a662d7fb3e00.png)

涂层法线参数可以用于较平滑基础上的凹凸不平的涂层,这些用法可以包括下雨效果、碳纤维材质或汽车材质(也就 是可以为涂层和底层使用不同的法线)

# Sheen 光泽

光泽可以模拟超细纤维布料状曲面或者任何表面上的一种绒毛等等

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/1602146604185-0ef4a85e-fcd2-4c68-bec3-bfecdc8dc45e.png)

通常光泽的颜色和基础的颜色，色相一致，然后光泽的颜色的明度要更高一些。

案例

一个亮一点的绒布效果，一个暗一点的绒布效果，通过 layer\_shader 融合到一起。

![](https://cdn.nlark.com/yuque/0/2020/png/351283/1602146711907-b7015c7e-9171-4f56-9a86-dc474987ff7c.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_bmFuZ29uZ2hhbg%3D%3D%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10%2Fresize%2Cw_1492)

![](https://cdn.nlark.com/yuque/0/2020/png/351283/1602146752826-442e5df9-5d0e-4627-b9a1-94dc271a8331.png?x-oss-process=image%2Fresize%2Cw_690)

![](https://cdn.nlark.com/yuque/0/2020/png/351283/1602147559098-ea0d23fb-a833-4a9f-837e-03084e4f6abe.png?x-oss-process=image%2Fresize%2Cw_618)

# Thin Film 薄膜

![](https://cdn.nlark.com/yuque/0/2020/png/351283/1602148411061-7d2d3b31-7113-4172-9556-cb32ae37452e.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_14%2Ctext_bmFuZ29uZ2hhbg%3D%3D%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10%2Fresize%2Cw_1492)

![](https://cdn.nlark.com/yuque/0/2020/png/351283/1602148433942-62dd004c-0936-4977-8d75-fd1fb1776521.png?x-oss-process=image%2Fwatermark%2Ctype_d3F5LW1pY3JvaGVp%2Csize_20%2Ctext_bmFuZ29uZ2hhbg%3D%3D%2Ccolor_FFFFFF%2Cshadow_50%2Ct_80%2Cg_se%2Cx_10%2Cy_10%2Fresize%2Cw_1492)

# Emission自发光

# Geometry几何体

# ID

# Advanced高级
