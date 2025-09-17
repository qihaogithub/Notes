
**git push** 命令用于从将本地的分支版本上传到远程并合并。

命令格式如下：

```
git push <远程主机名>  <本地分支名>:<远程分支名>
```

如果本地分支名与远程分支名相同，则可以省略冒号：

```
git push <远程主机名>  <本地分支名>
```

### 实例

以下命令将本地的 master 分支推送到 origin 主机的 master 分支。

```
git push origin master
```

相等于：

```
$ git push origin master:master
```

如果本地版本与远程版本有差异，但又要强制推送可以使用 --force 参数：

```
git push --force origin master
```

删除主机的分支可以使用 --delete 参数，以下命令表示删除 origin 主机的 master 分支：

```
git push origin --delete master
```

以我的 [https://github.com/tianqixin/runoob-git-test](https://github.com/tianqixin/runoob-git-test) 为例，本地添加文件：

```
$ touch runoob-test.txt \# 添加文件 $ git add runoob-test.txt 
$ git commit -m "添加到远程" master 69e702d\]  添加到远程  1 file changed,  0 insertions(+),  0 deletions(-) create mode 100644 runoob-test.txt

$ git push origin master \# 推送到 Github
```

将本地的 master 分支推送到 origin 主机的 master 分支。

重新回到我们的 Github 仓库，可以看到文件已经提交上来了：

![](https://www.runoob.com/wp-content/uploads/2015/03/79A84530-7DC0-4D25-9F83-8776433A4C32.jpg)

[[强制推送]]