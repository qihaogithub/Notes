---
name: requesting-code-review
description: 在完成任务、实现重大功能或合并之前使用，以验证工作是否符合要求。
---

# 请求代码审查

派发 superpowers:code-reviewer 子代理，在问题产生连锁反应之前将其捕捉。

**核心原则：** 早审，常审。

## 何时请求审查

**必须：**
- 子代理驱动开发中的每个任务执行之后
- 完成重大功能后
- 合并到 main 分支前

**可选但有价值：**
- 被卡住时（寻找新视角）
- 重构前（基准检查）
- 修复复杂 Bug 后

## 如何请求

**1. 获取 git SHA：**
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # 或 origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

**2. 派发 code-reviewer 子代理：**

使用 Task 工具调用 superpowers:code-reviewer，填写 `code-reviewer.md` 中的模板。

**占位符：**
- `{WHAT_WAS_IMPLEMENTED}` - 你刚构建的内容
- `{PLAN_OR_REQUIREMENTS}` - 它应该实现的功能
- `{BASE_SHA}` - 起始提交
- `{HEAD_SHA}` - 结束提交
- `{DESCRIPTION}` - 简要总结

**3. 根据反馈采取行动：**
- 立即修复“关键 (Critical)”问题
- 在继续之前修复“重要 (Important)”问题
- 记录“次要 (Minor)”问题留待后效
- 如果审查意见有误，请予以回绝（提供理由）

## 信号灯

**绝不：**
- 因为“很简单”而跳过审查
- 忽略关键问题
- 在未修复重要问题的情况下继续

**如果审查者有误：**
- 以技术理由予以回绝
- 展示证明其工作正常的代码/测试
- 请求澄清
