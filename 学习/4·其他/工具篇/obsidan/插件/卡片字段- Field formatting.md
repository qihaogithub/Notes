---
{}
---

以 anki 的默认卡片模板 basic 为例

```
START
Basic
Front: This is a test.
Back: Test successful!
<!--ID: 1700727738267-->
END
```
这会在 Anki 中生成以下卡片：
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20231123151555.png)
除了第一个字段之外，每个字段都必须填写字段名称，并且加冒号。
为了方便起见，您可以省略第一个字段的前缀：
```
START
Basic
This is a test.
Back: Test successful!
<!--ID: 1700809372801-->
END
```
您可以在同一字段中继续换行：

```
START
Basic
This is a test.
And the test is continuing.
Back: Test successful!
<!--ID: 1700727738276-->
END
```
![image.png](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/20231123151819.png)
您必须在新行上开始每个新字段。但除此之外，您可以随意省略任意数量的字段，或者更改字段的顺序！