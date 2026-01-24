# 代码质量审查代理提示词模板

当派发代码质量审查子代理时，请使用此模板。

**目的：** 验证实现是否构建良好（简洁、经过测试、可维护）。

**仅在规范合规性审查通过后派发。**

```
Task 工具 (superpowers:code-reviewer):
  使用位于 requesting-code-review/code-reviewer.md 的模板

  WHAT_WAS_IMPLEMENTED: [来自执行者的报告]
  PLAN_OR_REQUIREMENTS: [计划文件] 中的任务 N
  BASE_SHA: [任务开始前的提交]
  HEAD_SHA: [当前提交]
  DESCRIPTION: [任务摘要]
```

**代码审查者返回：** 优势、问题（关键/重要/次要）、评估。
