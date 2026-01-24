# 根本原因追踪 (Root Cause Tracing)

## 概述

Bug 往往显现在调用栈的深处（例如：在错误的目录初始化了 git，在错误的位置创建了文件）。你的直觉可能是去修复报错的地方，但这只是在治疗症状。

**核心原则：** 沿着调用链向后追踪，直到找到原始触发点，然后在源头解决问题。

## 何时使用

*(此处省略 DOT 图解翻译)*

**在以下情况下使用：**
- 错误发生在执行深处（而非入口点）
- 堆栈追踪显示了很长的调用链
- 不清楚无效数据源自何处
- 需要找出是哪个测试或哪段代码触发了问题

## 追踪流程

### 1. 观察症状
例如：`Error: git init failed in /Users/jesse/project/packages/core`

### 2. 寻找直接原因
哪段代码直接导致了此结果？

### 3. 询问：是什么调用了它？
查看调用堆栈，向上追溯。

### 4. 持续向上追踪
传递了什么值？这个值从哪里开始变坏的？

### 5. 找到原始触发点
在数据最初变得异常的地方进行修复。

## 添加堆栈追踪技巧

当你无法手动追踪时，添加埋点：

```typescript
// 在有问题的操作之前
async function gitInit(directory: string) {
  const stack = new Error().stack;
  console.error('调试 git init:', {
    directory,
    cwd: process.cwd(),
    stack,
  });

  await execFileAsync('git', ['init'], { cwd: directory });
}
```

**关键：** 在测试中使用 `console.error()`（不要用 logger，因为输出可能会被抑制）。

## 核心原则

**绝不只修复错误显现的地方。** 务必追溯到原始触发点。
修复源头，不仅解决了当前问题，还防止了类似问题在其他路径上产生。
