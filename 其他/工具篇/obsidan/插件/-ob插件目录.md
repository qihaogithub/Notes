---

database-plugin: basic

---

```yaml:dbfolder
name: new database
description: new description
columns:
  标签:
    input: tags
    accessorKey: 标签
    key: 标签
    id: 标签
    label: 标签
    position: 2
    skipPersist: false
    isHidden: false
    sortIndex: -1
    options:
      - { label: "链接", value: "链接", color: "hsl(310, 95%, 90%)"}
      - { label: "图片", value: "图片", color: "hsl(263, 95%, 90%)"}
      - { label: "功能增强", value: "功能增强", color: "hsl(206, 95%, 90%)"}
      - { label: "编辑器增强", value: "编辑器增强", color: "hsl(301, 95%, 90%)"}
      - { label: "浏览及界面增强", value: "浏览及界面增强", color: "hsl(7, 95%, 90%)"}
      - { label: "主题", value: "主题", color: "hsl(294, 95%, 90%)"}
      - { label: "AI", value: "AI", color: "hsl(92, 95%, 90%)"}
      - { label: "canvas", value: "canvas", color: "hsl(129, 95%, 90%)"}
      - { label: "导出", value: "导出", color: "hsl(260, 95%, 90%)"}
      - { label: "自动化", value: "自动化", color: "hsl(163, 95%, 90%)"}
      - { label: "目录", value: "目录", color: "hsl(129, 95%, 90%)"}
      - { label: "词典", value: "词典", color: "hsl(1, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  更新状态:
    input: text
    accessorKey: 更新状态
    key: 更新状态
    id: 更新状态
    label: 更新状态
    position: 6
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  介绍:
    input: text
    accessorKey: 介绍
    key: 介绍
    id: 介绍
    label: 介绍
    position: 4
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 513
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
      content_alignment: text-align-left
  评级:
    input: text
    accessorKey: 评级
    key: 评级
    id: 评级
    label: 评级
    position: 1
    skipPersist: false
    isHidden: false
    sortIndex: 1
    isSorted: true
    isSortedDesc: true
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  预览图:
    input: text
    accessorKey: 预览图
    key: 预览图
    id: 预览图
    label: 预览图
    position: 5
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  database-plugin:
    input: text
    accessorKey: database-plugin
    key: database-plugin
    id: database-plugin
    label: database-plugin
    position: 7
    skipPersist: false
    isHidden: true
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  github:
    input: text
    accessorKey: github
    key: github
    id: github
    label: github
    position: 8
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  __file__:
    key: __file__
    id: __file__
    input: markdown
    label: File
    accessorKey: __file__
    isMetadata: true
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 3
    isHidden: false
    sortIndex: -1
    width: -18
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: true
      task_hide_completed: true
      footer_type: none
      persist_changes: false
      content_alignment: text-align-left
config:
  remove_field_when_delete_column: false
  cell_size: normal
  sticky_first_column: false
  group_folder_column: 
  remove_empty_folders: false
  automatically_group_files: false
  hoist_files_with_empty_attributes: true
  show_metadata_created: false
  show_metadata_modified: false
  show_metadata_tasks: false
  show_metadata_inlinks: false
  show_metadata_outlinks: false
  show_metadata_tags: false
  source_data: current_folder
  source_form_result: 
  source_destination_path: /
  row_templates_folder: /
  current_row_template: 
  pagination_size: 200
  font_size: 16
  enable_js_formulas: false
  formula_folder_path: /
  inline_default: false
  inline_new_position: last_field
  date_format: yyyy-MM-dd
  datetime_format: "yyyy-MM-dd HH:mm:ss"
  metadata_date_format: "yyyy-MM-dd HH:mm:ss"
  enable_footer: false
  implementation: default
filters:
  enabled: false
  conditions:
```