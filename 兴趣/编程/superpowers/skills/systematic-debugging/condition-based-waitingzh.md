# 基于条件的等待 (Condition-Based Waiting)

## 概述

不稳定的测试（Flaky tests）通常会使用随意的延迟来猜测时间。这会产生竞争条件：测试在高性能机器上通过，但在高负载或 CI 环境中失败。

**核心原则：** 等待你真正关心的实际条件，而不是猜测它需要多长时间。

## 何时使用

*(此处省略 DOT 图解翻译)*

**在以下情况下使用：**
- 测试中包含随意的延迟（`setTimeout`, `sleep`, `time.sleep()`）
- 测试不稳定（有时通过，高负载下失败）
- 测试在并行运行时发生超时
- 等待异步操作完成

**在以下情况下不要使用：**
- 测试实际的时间精度行为（如防抖 debounce、节流 throttle 间隔）
- 如果必须使用随意延迟，请务必记录“为什么”

## 核心模式

```typescript
// ❌ 之前：猜测时间
await new Promise(r => setTimeout(r, 50));
const result = getResult();
expect(result).toBeDefined();

// ✅ 之后：等待条件
await waitFor(() => getResult() !== undefined);
const result = getResult();
expect(result).toBeDefined();
```

## 快速实现

通用轮询函数：
```typescript
async function waitFor<T>(
  condition: () => T | undefined | null | false,
  description: string,
  timeoutMs = 5000
): Promise<T> {
  const startTime = Date.now();

  while (true) {
    const result = condition();
    if (result) return result;

    if (Date.now() - startTime > timeoutMs) {
      throw new Error(`等待 ${description} 超时，已耗时 ${timeoutMs}ms`);
    }

    await new Promise(r => setTimeout(r, 10)); // 每 10ms 轮询一次
  }
}
```

## 常见错误

- **❌ 轮询过快**：浪费 CPU。每 10ms 轮询一次即可。
- **❌ 没有超时**：如果条件从未达成，将陷入死循环。
- **❌ 陈旧数据**：在循环外缓存状态。应在循环内调用获取函数以获得新鲜数据。
