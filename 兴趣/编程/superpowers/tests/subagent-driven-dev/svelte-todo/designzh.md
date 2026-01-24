# Svelte 待办事项列表 - 设计

## 概述
一个使用 Svelte 构建的简单待办事项应用。支持创建、完成、删除待办事项，并使用 localStorage 进行持久化。

## 功能
- 添加、勾选、删除项。
- 过滤功能（全部/进行中/已完成）。
- 持久化至本地存储。

## 组件结构
- `App.svelte`：主应用，状态管理。
- `TodoInput.svelte`：输入框。
- `TodoList.svelte`：列表容器。
- `store.ts`：状态存储。
