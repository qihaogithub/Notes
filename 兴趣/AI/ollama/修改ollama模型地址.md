# Mac

[视频教程](https://www.bilibili.com/video/BV1Qs421K7Vu/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d)
[文字教程](https://blog.maktubcn.info/archives/ru-he-zai-macosshang-geng-huan-ollamade-mo-xing-wei-zhi)
## 具体操作
所以我们只需要通过更改Mac的环境变量，并且重启Ollama就可以达到目的。

```
launchctl setenv OLLAMA_MODELS "你的模型文件夹路径"
```

例如，终端输入
```
launchctl setenv OLLAMA_MODELS "/Volumes/祁昊ssd/软件/ollama models/models"
```
然后重启软件
重启后在终端输入ollama list，即可查看当前模型

```
(base) qh2@qihao-2 ~ % ollama list

NAME               ID              SIZE      MODIFIED   

qwen2.5:latest     845dbda0ea48    4.7 GB    9 days ago    

llama3.2:latest    a80c4f17acd5    2.0 GB    9 days ago
```

当然你还需要把原来文件夹中的内容手动复制过去。这里你要注意的是，

~/.ollama/models是一个隐藏文件夹，你需要通过Command⌘+Shift⇧+。来让它显形。或者直接执行下方命令（确认后可以删除之前文件夹中内容）。

```
cp -R ~/.ollama/models 你的模型文件夹路径
```

重新启动Ollama APP

# win
[ollama模型目录地址切换,C盘切换其他盘符小技巧_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1tC411a7X5/?spm_id_from=333.337.search-card.all.click&vd_source=81223299ca5d449a34daaab3e1102d1d)

环境变量修改后，重启才生效