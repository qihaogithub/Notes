Hello，这里是东哥。这节课，我们要学习的是，「长乐未央全栈系列：Node. Js 项目实践」课程的第 9 回：使用 Sequelize ORM，在这节课里，我们将探讨：

*   ORM 是什么？
*   Sequelize 的安装使用
*   Sequelize 的目录结构

_1\. ORM 是什么_
-------------

大家学习了上一节的 `SQL` 语句后，应该会觉得，日常工作中去写这些东西，还是挺麻烦的。书写 `SQL` 语句，非常容易写错，而且要记忆的东西相当的多，这对于新手来说是非常不友好的。

但实际上我们在日常开发中，其实很少写 `SQL` 语句，因为我们还有更简便的方式，也就是使用 `ORM` 来操作数据库。`ORM` 是在数据库和编程语言之间建立一种映射关系，这样可以让我们有非常简单的代码，来实现各种数据库的操作。

我们这节课的重点就是如何使用 `Sequelize ORM` 来操作数据库。例如我们上一课学习的，要查询文章表的所有内容，应该写

```
SELECT * FROM `Articles`; 
```

使用 ORM，我们就写成

```
Article.findAll() 
```

`Article`，表示先找到 `Article` 这个模型。注意下，这里 `Article` 是单数形式，这并不是我写错了，而是 ORM 的就这么规定的。模型名是单数，对应的表名是复数。这样子，它就会自动找到 `Articles` 表上。`findAll()`，就是查询所有的数据了。整行的意思就是，查询 `Articles` 表的所有数据。

同样的，如果我想查询 `id=2` 的这条记录，也不用写

```
SELECT * FROM `Articles` WHERE `id`=2; 
```

而会改为

```
Article.findByPk(2) 
```

这里的 `findByPk`，里面的 `Pk`，就是 `primary key`，也就是 `主键` 的缩写。我们表里 `id` 就是主键，说白了就是通过 `id` 来查找数据。

大家看，这样使用 `ORM` 来操作数据库后，明显要比写 `SQL` 简单的太多了，再也不用背那么多可恶的 `SQL` 语句了。但这也不是说用了 `ORM` 以后，就一点也不用懂 `SQL` 语句了。`ORM` 它只是把我们写的代码，自动转换成 `SQL` 了再运行，在底层，实际上一样跑的还是 `SQL` 语句。

而且当我们开发中碰到问题了，要调试错误，依然要看命令行里面运行的 `SQL` 语句。所以就算开发中不写 `SQL`，也一定要能看懂是什么意思。

_2\. Sequelize ORM 的使用_
-----------------------

那么，现在我们就来一起玩玩 `Sequelize ORM`。第一步当然是要来安装了。先安装 `sequelize` 的命令行工具，需要全局安装，这样更方便使用

```
npm i -g sequelize-cli 
```

接着确保命令行是在当前项目的命令行里，还要安装当前项目所依赖的 `sequelize` 包和对数据库支持依赖的 `mysql2`

```
npm i sequelize mysql2 
```

最后，来初始化项目。

```
sequelize init 
```

[![](https://assets.clwy.cn/uploads/zzn2jcgmdhesodkfjmgo7ar5jek8!large)


可以看到，提示我们，创建了一个 `config` 配置文件和三个目录，这些就是 `sequelize` 所需要的东西了。

_3\. Windows 上出现错误_
-------------------

注意，部分 Windows 电脑，由于环境变量错误或其他问题，导致出现错误提示：`basedir=$(dirname "$(echo "$0" | sed -e 's,\\,/,g')")`

[![](https://assets.clwy.cn/uploads/dcw5olcqy88z6thz5ntrd7xwb7l9!large)
]( https://assets.clwy.cn/uploads/dcw5olcqy88z6thz5ntrd7xwb7l9!large )

可以尝试按以下方法解决：

```
# 卸载全局安装的 sequelize-cli
npm uninstall -g sequelize-cli

# 改为使用 nxp 方式运行命令。出现提示后，直接按回车
npx sequelize-cli init 
```

后续课程中使用 `sequelize` 命令，都需要自行改为使用 `npx sequelize-cli`

_4\. 目录结构_
----------

[![](https://assets.clwy.cn/uploads/hfew9lz3o60azspney5f143bjey4!large)
]( https://assets.clwy.cn/uploads/hfew9lz3o60azspney5f143bjey4!large )

```
.
├── config
│   └── config.json
├── migrations
├── models
│   └── index.js
└── seeders 
```

在编辑器中，也可以看到项目中新增了这些东西，现在一一看看，它们是用来干嘛的。

*   **config**：是配置的意思，这里放的也就是 `sequelize` 所需要的连接数据库的配置文件。
*   **migrations**：是迁移的意思，如果你需要对数据库做新增表、修改字段、删除表等等操作，就需要在这里添加迁移文件了。而不是像以前那样，使用客户端软件来直接操作数据库。
*   **models**：这里面存放的是模型文件，当我们使用 `sequelize` 来执行增删改查时，就需要用这里的模型文件了。每个模型都对应数据库中的一张表。
*   **seeders**，是存放的种子文件。一般会将一些需要添加到数据表的测试数据存在这里。只需要运行一个命令，数据表中就会自动填充进一些用来测试内容的了。

_5\. 总结_
--------

| 文件或目录 | 说明 |
| --- | --- |
| config/config. Js | 数据库连接配置 |
| migrations | 迁移文件 |
| models | 模型文件 |
| seeders | 种子文件 |

好了，这节课就先到这里了，只要大家看到自己项目里出现了这些东西，就算大功告成了。我们下一节课再来详细说一说它们该怎么使用。