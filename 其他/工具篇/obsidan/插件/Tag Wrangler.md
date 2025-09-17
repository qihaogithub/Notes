---
介绍: 在标签窗格中重命名、合并、切换和搜索标签
标签:
  - 功能增强
评级: "3"
---

# Obsidian Tag Wrangler Plugin

> NEW in 0.5.5 - you can now drag tags from the tag pane to an editor pane to insert them as text.

此插件为[Obsidian.md](https://obsidian.md/)标签窗格)中的标签添加上下文菜单，并提供以下操作：

![Image of tag wrangler's context menu](https://raw.githubusercontent.com/pjeby/tag-wrangler/master/contextmenu.png)

-   打开或创建 [标签页](app://obsidian.md/index.html#tag-pages) (**NEW in 0.5.0**)
-   [Rename the tag](app://obsidian.md/index.html#renaming-tags)(及其所有子标签)
-   开始新的标签搜索(类似于简单的点击)
-   将标签添加为要求 ('tag:# whatever') 到当前搜索
-  在当前搜索中添加标签排除项(`-tag：#Whatever`)
- 打开带有该标签的随机便笺(如果您安装并启用了[智能随机Note](https://github.com/erichalldev/obsidian-smart-random-note/)插件])
-  折叠标签窗格中同一级别的所有标签
- 在标签窗格中展开同一级别的所有标签

根据搜索和标记窗格的当前状态，某些操作可能不可用。(例如，仅当标签窗格在层次结构中显示标签时，展开和折叠才可用。
**请注意**：重命名标签可能是一个不可逆的操作：在开始重命名之前，您可能希望备份数据。有关更多信息，请参阅下面的[重命名tags](app://obsidian.md/index.html#renaming-tags)]一节。

## 标记页面

人们经常争论使用标签还是页面链接来组织笔记的优点。使用标记页面，您可以将两者的优点结合在一起：标记的可见性和流畅的输入，以及页面的集中内容和出站链接。

要创建标签页，只需在标签面板中右键点击任何标签，然后选择“创建标签页”。将使用所选标记的别名创建新便笺。您可以重命名注释或将其移动到Vault中的任意位置，只要它保留将其链接到标记的别名。(重命名与标记页关联的标记(请参阅下面的“重命名标记”)将自动更新别名。)
要打开_Existing_Tag页面，您可以按住Alt键并单击标签窗格中的任何标签或任何便笺，无论是在编辑视图中还是在阅读视图中。按住Ctrl/Cmd并单击或中键单击将在新的窗格中打开标记页。(注意：如果不存在标记页面，则将应用全局搜索标记的正常点击行为。)
或者，你可以在黑玉岩的“快速切换器”(默认热键：Ctrl/Cmd-O)中输入标签的名称，从键盘上打开页面。您还可以在标签窗格或任何标记视图中悬停预览任何标签，以弹出标签页面的预览。
(如果你不熟悉悬停预览，基本的想法是，通过按住Ctrl/Cmd键，同时将鼠标指针移动到黑碧岩中的项目上，通常会出现一个弹出式窗口，其中包含相关页面的一个小版本。你也可以进入内置的“页面预览”插件的设置，有选择地禁用使用Ctrl/Cmd键的需要，如果你更喜欢在没有Ctrl/Cmd键的情况下悬停。Tag Wrangler尊重您在编辑器和预览视图中悬停链接的现有设置，并为“Tag Pane”添加了额外的设置，该设置控制在标记窗格中悬停标记时是否需要Ctrl/Cmd键。)
Tag Wrangler目前还不支持标记引用到页面链接的自动转换，反之亦然，尽管它可能会在未来的版本中出现。然而，与此同时，你可以使用黑铁矿的反向链接来查找和更改标签页面中的此类引用。具体地说，查看标记页面的“未链接提及”将向您显示使用该标记的所有位置，以及可用于将它们转换为页面链接的“链接”按钮。(将页面链接转换为标签需要手动编辑。)

### 手动创建和管理标签页

您不必使用“创建标签页面”菜单命令来创建标签页面：任何页面（甚至是看板或Excalidraw图纸！）都可以是标签页面，只要它有一个标签作为**有效的黑曜石别名**。您可以通过以下两种方式之一验证特定页面是否具有有效的别名：

- 打开黑曜石快速切换器（默认为 Ctrl/Cmd-O）并键入“#”，后跟标签名称：页面应以标签作为别名显示
- 切换笔记进行预览，并查看笔记顶部元数据框中的“别名”是否具有包含标签的形状（前面有一个箭头和一个“#”）

如果它未显示在上述任一位置，则可能是您的笔记的元数据在某些方面语法不正确。黑曜石识别名为“别名”或“别名”（不区分大小写）的第一个字段，并期望它是字符串的 YAML 列表或以逗号分隔的单个别名字符串。要被识别为标签别名，字符串 _must_ 必须用引号括起来。以下是包含标签的别名或别名字段的一些有效示例，每个示例都会导致注释被视为“#some/tag”的标签页面：

```yaml
---
Alias: "#some/tag"
---
Aliases: [ "#some/tag", "another alias" ]
---
alias:
  - some alias
  - "#some/tag"
  - another alias
---
aliases: "some alias, #some/tag, another alias"
---
```

Notice that either each item must be quoted and be in a valid YAML list (`[ ]` or lines with `-`), or else the _entire_ alias collection should be quoted and comma-separated. A tag alias must also not contain any whitespace or other text.

When a tag is renamed, Tag Wrangler will automatically update the alias. You can also manually edit or remove the aliases to disconnect a tag page, add additional tags (in case you want more than one tag sharing the same page), or change what tag the page is for.

Finally, note that nothing prevents you from adding the same alias to more than one note, but in such a case Tag Wrangler will select the tag page at random from the available options. To fix this, use the quick switcher to search for notes with that alias (i.e., by typing `#` and the tag name), then remove the alias(es) from the note(s) you don't want to use as tag pages.

## Renaming Tags

Just like renaming notes, renaming tags involves making substitutions in all the files that reference them. In order to ensure only actual tags are renamed, Tag Wrangler uses Obsidian's own parse data to identify the tag locations. That way, if you have a markdown link like `[foo](#bar)`, it won't consider the `#bar` to be an instance of a `#bar` tag.

Because tags exist only in the files that contain them, certain renaming operations are _not reversible_. For example, if you rename `#foo` to `#bar`, and you already have a `#bar` tag, then afterwards there will be no way to tell which files originally had `#foo` and which had `#bar` any more, without consulting a backup or revision control of some kind.

For this reason, Tag Wrangler checks ahead of time if you are renaming tags in a way that will merge any tags with existing tags, and ask for an additional confirmation, warning about the lack of undo. (Not that _any_ renames are really undoable, it's just that if no merging takes place, you can generally rename the tag back to its old name!)

If you are using some type of background sync (e.g. Dropbox, GDrive, Resilio, etc.), and it causes any files to be changed _while_ Tag Wrangler is doing a rename, Tag Wrangler may skip the changed file(s), resulting in a partial rename. Generally, repeating the same rename option should work to finish the process, but in case of merges you may have to be more careful. (It's probably best you make sure any sync operations are completed before beginning any rename operations.)

If many files need to be changed, or if renaming proceeds slowly, a progress dialog will be displayed, giving you the option to abort the renaming process. This will not undo changes made prior to that point, only stop further changes from occurring.

### Tags With Child Tags

Obsidian allows hierarchical tags of the form `#x/y/z`. When you rename a parent tag (like `#x/y`), all of its child tags will be renamed as well.

So for example, if you rename `#x/y` to `#a/b`, then a tag that was previously named `#x/y/z` will be renamed to `#a/b/z`. (There is no way to rename only the parent tag, except by individually renaming all its child tags to move them under another parent.)

If you want to refactor your tag hierarchy, note that you can rename a tag and its children to have either more or fewer path parts than it did before. That is, you can rename `#x/y` to just `#x`, and then your `#x/y/z` tag will become `#x/z`. Or conversely, you can rename `#x/y` to `#letters/x/y`, which will move `#x/y/z` to `#letters/x/y/z`.

Many possibilities are available for refactoring your tags. Just be sure to make a backup before you start, keep track of what you're changing, and check on the results before you sync or commit your changes.

### Metadata / Front Matter

Obsidian allows tags to be specified as part of a note's metadata via YAML front matter. Tag Wrangler will attempt to rename these as well as those found in a note's body.

In most cases, this will not cause any issues. However, you are using advanced YAML features to specify your tags (YAML aliases or block scalars), there are two points you should be aware of.

首先，如果使用 YAML 块标量（“<”或“|”）来指定标记，则重命名的标记 [可能会影响标记字段的缩进、间距或换行]（https://github.com/eemeli/yaml/issues/349）。其次，如果您在标记列表中使用 YAML 别名 （'  *'  ），重命名别名标记将 [就地扩展别名，而不是更改定义它的锚点]（https://github.com/pjeby/tag-wrangler/issues/13#issuecomment-826264213）。

缩进问题已报告给上游库，希望将来会有某种解决方案。对于别名，当前行为是有意避免更改元数据中的非标记值的选择。因此，如果您正在使用这些更高级的 YAML 功能中的任何一个，则在执行任何保管库范围的重命名之前，您可能应该在草稿中尝试一些假标签。

### Case Insensitivity

Tag Wrangler uses the same case-insensitive comparison as Obsidian when matching tags to change, and checking for clashes. Please note, however, that because Obsidian uses the _first_ occurrence of a tag to determine how it is displayed in the tag pane, renaming tags without consistent upper/lowercase usage may result in _apparent_ changes to the names of "other" tags in the tag pane.

Let's say you have a tag named `#foo/bar` and you rename `#foo` to `#Bar/baz`. But in the meantime, you already _had_ a tag called `#bar/bell`. This _might_ cause you to now see that tag displayed in the tag pane as `#Bar/bell`, even though Tag Wrangler did not actually replace any existing `#bar/bell` tags in your text! (As you will see if you search for them.)

Rather, this kind of thing will happen if the `#Bar/baz` tag is the first tag beginning with some variant of `bar` that Obsidian encounters when generating the tag pane. Obsidian just uses the first-encountered string of a particular case as the "display name" for the tag, and then counts all subsequent occurrences as the same tag.

This is just how Obsidian tags work, and not something that Tag Wrangler can work around. But you can easily fix the problem by renaming anything that's in the "wrong" case to the "right" case. It just means that (as is already the case in Obsidian) you can't have more than one casing of the same tag name displayed in the tag pane, and that now you can easily rename tags to a consistent casing, if desired.
