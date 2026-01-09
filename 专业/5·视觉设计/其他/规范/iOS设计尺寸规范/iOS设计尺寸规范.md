# iOS设计尺寸规范

## 字体 (默认) Typography

中文字体：PingFang SC

英文字体：SF UI Text 、SF UI Display

其中 SF UI Text 适用与小于 19pt 的文字，SF UI Display 适用于大于 20pt 的文字

| 元素        | 字重        | 字号 (pt) | 行距   | 字间距   |
| --------- | --------- | ------- | ---- | ----- |
| Title 1   | Light     | 28pt    | 34pt | 13pt  |
| Title 2   | Regular   | 22pt    | 28pt | 16pt  |
| Title 3   | Regular   | 20pt    | 24pt | 19pt  |
| Headline  | Semi-Bold | 17pt    | 22pt | -24pt |
| Body      | Regular   | 17pt    | 22pt | -24pt |
| Callout   | Regular   | 16pt    | 21pt | -20pt |
| Subhead   | Regular   | 15pt    | 20pt | -16pt |
| Footnote  | Regular   | 13pt    | 18pt | -6pt  |
| Caption 1 | Regular   | 12pt    | 16pt | 0pt   |
| Caption 2 | Regular   | 11pt    | 13pt | 6pt   |

| 元素                | 字号（pt） | 字重               | 字距（pt） | 类型      |
| ----------------- | ------ | ---------------- | ------ | ------- |
| Nav Bar Title     | 17     | Medium           | 0.5    | Display |
| Nav Bar Button    | 17     | Regular          | 0.5    | Display |
| Search Bar        | 13.5   | Regular          | 0      | Text    |
| Tab Bar Button    | 10     | Regular          | 0.1    | Text    |
| Table Header      | 12.5   | Regular          | 0.25   | Text    |
| Table Row         | 16.5   | Regular          | 0      | Text    |
| Table Row Subline | 12     | Regular          | 0      | Text    |
| Table Footer      | 12.5   | Regular          | 0.2    | Text    |
| Action Sheets     | 20     | Regular / Medium | 0.5    | Display |

# 点和像素

![](https://uiiiuiii.com/screen/images/specification/iosPic01.jpg)

# 图标

#### 应用图标 App Icon

| 设备名称                                             | 应用图标         | App Store 图标   | Spotlight 图标  | 设置图标       |
| ------------------------------------------------ | ------------ | -------------- | ------------- | ---------- |
| iPhone X, 8+, 7+, 6s+, 6s                        | 180 x 180 px | 1024 x 1024 px | 120 x 120 px  | 87 x 87 px |
| iPhone X, 8, 7, 6s, 6, SE，5s, 5c, 5,  &#xA;4s, 4 | 120 x 120 px | 1024 x 1024 px | 80 x 80 px    | 58 x 58 px |
| iPhone 1, 3G, 3GS                                | 57 x 57 px   | 1024 x 1024 px | 29 x 29 px    | 29 x 29 px |
| iPad Pro 12.9, 10.5                              | 167 x 167 px | 1024 x 1024 px | 80 x 80 px    | 58 x 58 px |
| iPad Air 1 & 2, Mini 2 & 4,  &#xA;3 & 4          | 152 x 152 px | 1024 x 1024 px | 80 x 80 px \| | 58 x 58 px |
| iPad 1, 2, Mini 1                                | 76 x 76 px   | 1024 x 1024 px | 40 x 40 px    | 29 x 29 px |

#### 自定义图标

| 设备名称                      | 导航栏和工具栏图标尺寸 | 标签栏图标尺寸                    |
| ------------------------- | ----------- | -------------------------- |
| iPhone 8+, 7+, 6+, 6s+    | 66 x 66 px  | 75 x 75 px　　最大 144 x 96 px |
| iPhone 8, 7, 6s, 6, SE    | 44 x 44 px  | 50 x 50 px　　最大 96 x 64 px  |
| iPad Pro, iPad, iPad mini | 44 x 44 px  | 50 x 50 px　　最大 96 x 64 px  |

#### 分辨率和显示规格

| 设备名称                              | 屏幕尺寸    | PPI | Asset | 竖屏点（point）  | 竖屏分辨率（px）   |
| --------------------------------- | ------- | --- | ----- | ----------- | ----------- |
| iPhone X                          | 5.8 in  | 458 | @3x   | 375 x 812   | 1125 x 2436 |
| iPhone 8+, 7+, 6s+, 6+            | 5.5 in  | 401 | @3x   | 414 x 736   | 1242 x 2208 |
| iPhone 8, 7, 6s, 6                | 4.7 in  | 326 | @2x   | 375 x 667   | 750 x 1334  |
| iPhone SE, 5, 5S, 5C              | 4.0 in  | 326 | @2x   | 320 x 568   | 640 x 1136  |
| iPhone 4, 4S                      | 3.5 in  | 326 | @2x   | 320 x 480   | 640 x 960   |
| iPhone 1, 3G, 3GS                 | 3.5 in  | 163 | @1x   | 320 x 480   | 320 x 480   |
| iPad Pro 12.9                     | 12.9 in | 264 | @2x   | 1024 x 1366 | 2048 x 2732 |
| iPad Pro 10.5                     | 10.5 in | 264 | @2x   | 834 x 1112  | 1668 x 2224 |
| iPad Pro, iPad Air 2, Retina iPad | 9.7 in  | 264 | @2x   | 768 x 1024  | 1536 x 2048 |
| iPad Mini 4, iPad Mini 2          | 7.9 in  | 326 | @2x   | 768 x 1024  | 1536 x 2048 |
| iPad 1, 2                         | 9.7 in  | 132 | @1x   | 768 x 1024  | 768 x 1024  |

# UI 组件布局

#### 状态栏 Status Bar

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image_Yr_07GM_Od.png)

#### 导航栏 Navigation Bar

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image_stJzMPlMU7.png)

### 搜索栏 Search Bar

![](https://uiiiuiii.com/screen/images/specification/iosPic05.jpg)

### 标签栏 Tab Bar

![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/image_QElaBHlM7D.png)

### 表格视图 Table View

![](https://uiiiuiii.com/screen/images/specification/iosPic07.jpg)

### Modals

![](https://uiiiuiii.com/screen/images/specification/iosPic08.jpg)

### 行为区 Actions

![](https://uiiiuiii.com/screen/images/specification/iosPic09.jpg)

### 提示框 Alerts

![](https://uiiiuiii.com/screen/images/specification/iosPic10.jpg)

### Segment Controls

![](https://uiiiuiii.com/screen/images/specification/iosPic11.jpg)

### 滑动条 Sliders

![](https://uiiiuiii.com/screen/images/specification/iosPic12.jpg)

### 切换按钮 Switch

![](https://uiiiuiii.com/screen/images/specification/iosPic13.jpg)

### 计步器 Stepper

![](https://uiiiuiii.com/screen/images/specification/iosPic14.jpg)

*   参考文献：

    [https://uiiiuiii.com/screen/ios.htm](https://uiiiuiii.com/screen/ios.htm "https://uiiiuiii.com/screen/ios.htm")
