[官方文档](https://help.aliyun.com/zh/oss/developer-reference/install-ossutil?spm=a2c4g.11174283.0.i3)

## sync
### 同步本地文件到oss
命令格式如下

```bash
./ossutil64 sync file_url cloud_url
```

其中./ossutil64 需要根据自己系统替换

| **系统**      | **Binary名称**   |     |
| ----------- | -------------- | --- |
| Linux 64位   | ./ossutil64    |     |
| Linux 32位   | ./ossutil32    |     |
| Windows 64位 | ossutil64.exe  |     |
| Windows 32位 | ossutil32.exe  |     |
| macOS 64位   | ./ossutilmac64 |     |
| macOS 32位   | ./ossutilmac32 |     |
| ARM 64位     | ./ossutilarm64 |     |
| ARM 32位     | ./ossutilarm32 |     |

同步mac 电脑文件到oss

```
./ossutilmac64 sync /Volumes/祁昊ssd/eagle/jietu.library oss://uiweb/images/jietu.library --update 
```

```
./ossutilmac64 sync /Volumes/祁昊ssd/eagle/jietu.library oss://uiweb/images/jietu.library  --update --delete -f
```