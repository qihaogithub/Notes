在VS Code中，打开终端（可以通过点击视图-> 终端）
在终端中，使用以下命令设置你的Git用户名和邮箱地址
```
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱地址"
```
将"你的用户名"`和`"你的邮箱地址"替换为你希望在Git提交中使用的用户名和邮箱地址。这里的`--global`标志意味着这些设置将应用于你在该计算机上进行的所有Git仓库。
![](https://qhdtc.oss-cn-chengdu.aliyuncs.com/obsidian/202404071613108.png)


**检查配置**： 为了确认你的配置是否成功，可以使用以下命令查看当前的Git配置：

```
git config user.name
git config user.email
```
`
如果配置正确，这些命令将输出你刚才设置的用户名和邮箱地址。