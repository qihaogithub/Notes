---

database-plugin: basic

---

```yaml:dbfolder
name: stable diffusion 模型库
description: stable diffusion 模型库
columns:
  column1:
    input: text
    key: column1
    accessorKey: column1
    label: 简介
    position: 2
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 297
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
    width: 213
    position: 1
    isHidden: false
    sortIndex: 0
    isSorted: true
    isSortedDesc: false
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: true
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  newColumn2:
    input: tags
    accessorKey: newColumn2
    key: newColumn2
    id: newColumn2
    label: 标签
    position: 5
    width: 128
    skipPersist: false
    isHidden: false
    sortIndex: -1
    isSorted: false
    isSortedDesc: false
    options:
      - { label: "卡通", value: "卡通", color: "hsl(30, 95%, 90%)"}
      - { label: "万能", value: "万能", color: "hsl(266, 95%, 90%)"}
      - { label: "2.5D", value: "2.5D", color: "hsl(342, 95%, 90%)"}
      - { label: "真实", value: "真实", color: "hsl(267, 95%, 90%)"}
      - { label: "二次元", value: "二次元", color: "hsl(286, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  链接:
    input: text
    accessorKey: 链接
    key: 链接
    id: 链接
    label: 链接
    position: 3
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
  评级:
    input: number
    accessorKey: 评级
    key: 评级
    id: 评级
    label: 评级
    position: 4
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 59
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
config:
  remove_field_when_delete_column: false
  cell_size: normal
  sticky_first_column: true
  group_folder_column: 
  remove_empty_folders: true
  automatically_group_files: false
  hoist_files_with_empty_attributes: true
  show_metadata_created: false
  show_metadata_modified: false
  show_metadata_tasks: false
  show_metadata_inlinks: false
  show_metadata_outlinks: false
  source_data: current_folder
  source_form_result: 
  source_destination_path: /
  row_templates_folder: /
  current_row_template: 
  pagination_size: 105
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
  show_metadata_tags: false
filters:
  enabled: false
  conditions:
```