# AE·效果·火焰灼烧转场

教程原文：[https://www.bilibili.com/video/BV1E441157tF?from=search\&seid=10073658713123527440](https://www.bilibili.com/video/BV1E441157tF?from=search\&seid=10073658713123527440 "https://www.bilibili.com/video/BV1E441157tF?from=search\&seid=10073658713123527440")

*   给转场前的画面添加效果-风格化-CC Burn Film

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/179feaa38a7e6e811642d4317916bce4_TQC7GX9gVC.png)

*   在Burn添加关键帧

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/e8eb8a57cf66263cbbfedc21795b8e83_FF0whA7eaQ.png)

*   新建纯色层

*   把图层1的效果复制给纯色层

*   给纯色层添加效果-颜色调整-色阶，通道选择Alpha，调整输入黑色

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/09cf0198b73c942d68e7e2e6e213e319_wlcSY3hHcB.png)

*   复制纯色层，作为下层的alpha反转轨道遮罩

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/33d9267cea9c2aefa71a4f69306ada4d_O8dHvaJqLq.png)

*   调整纯色2的alpha输入黑色，可以得到黑色边缘

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/7869fc61687573a971b8c5ae32fe6315_rvgUksG_QK.png)

*   将两个纯色层预合成，命名为“边缘”

*   打开“边缘”预合成，新建调整图层，添加效果-风格化-查找边缘

*   添加效果-颜色调整-三色调，颜色分别是#FF9211、#FF000F、#CF0000

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/5b242dee39150cd476a9b5b4331dc8c8_LsgoF4dEso.png)

*   添加效果-风格化-发光

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/f11567675df4cf19bba58b3a3e171a45_fqALREaba1.png)

*   复制发光效果，更改数值

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/7e52cd6827b291413a9c5933afc0341a_8IgyUvnoV5.png)

*   添加效果-颜色矫正-曲线

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/ecb366b48014289a8c762e2a42e13767_l0RxMWx__q.png)

*   给蒙版添加效果-风格化-毛边，调整边界数值，并给演化添加公式：time\*500

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/274712bfe4fe41928eb3cd502c5fb429_x0WszcX1gA.png)

*   给调整图层添加效果-杂色和颗粒-湍流杂色，放在曲线的上面

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/d3325591cfd7648935382ab9224dbc38_22beCB0wcx.png)

*   在“边缘”外面新建纯色层，添加效果-RG Trapcode-Particular

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/fd70753f77c083cee46d79a799c9de8f_l71QC5HptB.png)

*   在项目中复制一层“边缘”,改名为“粒子发射器”

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/08f741867ea1b4d9d1ab4283c2b648ef_nTYSV73mJn.png)

*   打开【粒子发射器】的3D开关，关闭图层显示

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/59efe9565d02af03f3d9396df7d19ac4_UMcxUDdJql.png)

选中黑色-纯色1，将粒子的发射器类型改为“层”

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/e4ee1a62d031417733d9c53e718288a5_IQPYSRPwKP.png)

更改层发射器，层选择粒子发射器合成，层采样选择粒子出身时间

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/c24142c5a0b79e756b3ba7bb3020f39c_2yc6Yqcr9G.png)

粒子生命值1，粒子类型：发光球体

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/24edb82d577b4887037ef3d0a5854bb4_EqI4FDaLTn.png)

修改尺寸为8，调整不透明度曲线

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/cd9dd64c64d07813bb43b9273e43044b_V02wDeyrNW.png)

给各个方向上的风一些数值

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/9052e5aed55ead702edd23e4e2f63444_IiDXgawpxY.png)

打开运动模糊，快门角度600

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/aa1cd67999f72055853e18f474d7033c_BVU28XqJJj.png)

湍流场打关键帧

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/c0f2806357b776917c11a3acf880dfe9_8sKv9e8GYl.png)
