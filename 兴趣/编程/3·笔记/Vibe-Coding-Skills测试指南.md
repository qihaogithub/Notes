# Vibe Coding 极简测试指南

本指南介绍如何在 Vibe Coding 环境中使用极简的 Skills 配置进行自动化测试。

**核心理念：Skills 是固定的规则，代码文件是动态的内容。**

---

## 设计理念

### 核心原则

```
Skills = 固定的规则和流程（你维护）
代码文件 = 动态的内容和实现（AI 维护）
```

### 为什么这样设计？

**Skills 的特性**：

- ✅ 代表稳定的流程和规则
- ✅ 不应该经常变动
- ✅ 是 AI 行为的"宪法"

**代码文件的特性**：

- ✅ 包含经常变化的内容
- ✅ 可以随时修改
- ✅ 是 AI 执行的"具体实现"

### 对比

| 维度         | Skills           | 代码文件         |
| ------------ | ---------------- | ---------------- |
| **维护者**   | 你               | AI               |
| **稳定性**   | 固定             | 动态             |
| **内容**     | 规则、流程、标准 | 命令、代码、配置 |
| **变化频率** | 低（月/季度）    | 高（每次开发）   |

---

## 架构设计

### 只有一个 Skills

```
test_engineer（测试工程师）
  └─ 你维护的唯一 Skills
  └─ 包含：测试规则、质量标准、流程约定
  └─ 不包含：具体命令、代码实现
```

### AI 维护的代码文件

```
.vibe/
  ├── test_commands.yml      # 测试命令（AI 维护）
  └── test_engineer.yml      # 测试工程师 Skills（你维护）

tests/
  ├── conftest.py            # 共享 fixtures（AI 可以修改）
  ├── api/
  │   └── test_api.py        # 测试代码（AI 生成和修改）
  └── ...

src/frontend/src/test/
  └── *.test.tsx             # 前端测试（AI 生成和修改）
```

### 工作流程

```
用户需求
    ↓
[test_engineer Skills] 读取固定规则
    ↓
AI 自主规划：
  - 分析需求
  - 读取 test_commands.yml（动态命令）
  - 生成测试代码到 tests/
  - 运行测试
  - 验证结果
  - 修复问题（如果需要）
  - 更新 test_commands.yml（如果需要）
    ↓
完成 ✓
```

---

## 测试工程师 Skills 配置

### 核心配置文件

```yaml
# .vibe/test_engineer.yml

version: "1.0"
name: "测试工程师"
description: "定义测试的规则、标准和流程"

# 项目测试约定（固定规则）
project_conventions:
  backend:
    framework: "pytest"
    test_directory: "tests/"
    fixture_file: "tests/conftest.py"
    naming_pattern: "test_{feature}_{scenario}"
    coverage_target: 80%

  frontend:
    framework: "vitest"
    test_directory: "src/frontend/src/test/"
    naming_pattern: "{ComponentName}.test.tsx"
    coverage_target: 75%

# 测试质量标准（固定规则）
quality_standards:
  - 每个功能至少有 3 个测试用例
  - 必须包含正常场景和异常场景
  - 测试名称必须清晰描述测试内容
  - 使用项目现有的 fixtures
  - 遵循项目的代码风格

# 测试生成策略（固定规则）
generation_strategy:
  # 后端 API 测试
  api_test:
    required_scenarios:
      - 成功场景（200）
      - 未授权场景（401/403）
      - 资源不存在（404）
      - 参数验证失败（400）
    optional_scenarios:
      - 边界条件
      - 性能测试
      - 并发测试

  # 前端组件测试
  component_test:
    required_scenarios:
      - 正常渲染
      - 空状态处理
      - 错误状态处理
      - 用户交互
    optional_scenarios:
      - 响应式布局
      - 可访问性
      - 性能优化

# 测试流程（固定规则）
test_workflow: 1. 分析需求
  2. 读取 test_commands.yml 获取命令
  3. 生成测试代码
  4. 运行测试
  5. 验证结果
  6. 如果失败，分析原因
  7. 如果是测试代码问题，修复测试
  8. 如果是功能代码问题，提示用户
  9. 重新运行测试
  10. 更新 test_commands.yml（如果需要）

# 特殊情况处理（固定规则）
special_cases:
  - "文件上传功能需要测试大文件场景"
  - "同步功能需要测试并发场景"
  - "导出功能需要测试格式验证"

# 注意：此文件是固定的，不应该经常修改
# 动态的测试命令请参考 .vibe/test_commands.yml
```

### 关键特性

1. **只包含规则**：没有具体命令和代码
2. **固定不变**：一旦设定，长期有效
3. **AI 遵守**：AI 必须遵守这些规则
4. **可扩展**：可以添加新的规则，但不应该频繁修改

---

## 测试命令配置（AI 维护）

### 动态配置文件

```yaml
# .vibe/test_commands.yml

version: "1.0"
name: "测试命令集合"
description: "由 AI 维护的测试命令，可以随时更新"

# 后端测试命令
backend:
  run_all: "./scripts/run-tests.sh"
  run_specific: "python -m pytest {test_path} -v"
  run_with_coverage: "python -m pytest --cov=src --cov-report=term-missing"
  run_specific_class: "python -m pytest {test_path}::{class_name} -v"
  run_specific_test: "python -m pytest {test_path}::{class_name}::{test_name} -v"

# 前端测试命令
frontend:
  run_all: "cd src/frontend && npm test"
  run_specific: "cd src/frontend && npx vitest run {test_file}"
  run_watch: "cd src/frontend && npm test -- --watch"
  run_ui: "cd src/frontend && npx vitest --ui"

# 环境变量
environment:
  backend:
    - DATABASE_URL
    - FIGMA_TOKEN
  frontend:
    - Node.js >= 18
    - npm >= 9

# 注意：此文件由 AI 维护，可以随时更新
# 如果需要修改，请直接修改，不需要经过审批
```

### 维护说明

- **AI 完全自主**：AI 可以随时读取和修改
- **不需要审批**：AI 可以根据需要更新命令
- **你可以查看**：偶尔检查命令是否正确
- **可以手动修改**：如果需要特殊配置

---

## 实际使用示例

### 示例 1：为新 API 生成测试

```
用户: 为 POST /api/files/rename 生成测试
AI: [读取 test_engineer Skills]

    分析需求：
    - 这是一个后端 API 端点
    - 需要遵循 API 测试策略（来自 Skills）

    [读取 test_commands.yml]
    获取命令：python -m pytest {test_path} -v

    生成测试计划（根据 Skills 规则）：
    ✓ 成功场景（200）
    ✓ 未授权场景（401）
    ✓ 参数验证失败（400）
    ✓ 文件不存在（404）

    [生成测试代码到 tests/api/test_api.py]

    [运行测试]
    结果：4 个测试全部通过 ✓

    完成！
```

### 示例 2：为 React 组件生成测试

```
用户: 为 FileGallery 组件生成测试
AI: [读取 test_engineer Skills]

    分析需求：
    - 这是一个前端组件
    - 需要遵循组件测试策略（来自 Skills）

    [读取 test_commands.yml]
    获取命令：cd src/frontend && npx vitest run {test_file}

    生成测试计划（根据 Skills 规则）：
    ✓ 正常渲染
    ✓ 空状态处理
    ✓ 错误状态处理
    ✓ 用户交互（点击、搜索）

    [生成测试代码到 src/frontend/src/test/FileGallery.test.tsx]

    [运行测试]
    结果：3 个通过，1 个失败

    [分析失败原因]
    失败测试：test_error_state
    原因：组件未实现错误状态

    [修复测试代码]
    已调整测试以匹配当前实现

    [重新运行测试]
    结果：4 个测试全部通过 ✓

    完成！
```

### 示例 3：测试命令更新

```
用户: 运行所有后端测试
AI: [读取 test_engineer Skills]

    [读取 test_commands.yml]
    获取命令：./scripts/run-tests.sh

    [运行测试]
    结果：测试失败，命令不存在

    [分析问题]
    发现：scripts/run-tests.sh 被重命名为 scripts/test.sh

    [更新 test_commands.yml]
    已更新命令为：./scripts/test.sh

    [重新运行测试]
    结果：13 个测试全部通过 ✓

    完成！已自动更新 test_commands.yml
```

---

## 维护指南

### Skills 维护（你负责）

**何时需要修改**：

1. 项目技术栈改变（如从 pytest 换到其他框架）
2. 测试质量标准提高（如覆盖率从 80% 提高到 90%）
3. 新增测试类型（如性能测试、安全测试）
4. 测试流程需要调整

**修改原则**：

- ✅ 保持简单，不要过于详细
- ✅ 信任 AI 的判断，给 AI 自主权
- ✅ 只定义规则，不定义实现
- ✅ 修改后长期有效，不要频繁变动

**示例**：

```yaml
# 修改前
coverage_target: 80%

# 修改后
coverage_target: 90%

# 这个修改会影响未来所有生成的测试
# 但不需要经常修改
```

### 代码文件维护（AI 负责）

**AI 可以自由修改**：

- `.vibe/test_commands.yml`：测试命令
- `tests/conftest.py`：共享 fixtures
- `tests/*.py`：测试代码
- `src/frontend/src/test/*.test.tsx`：前端测试

**你只需要**：

- ✅ 偶尔查看 test_commands.yml 是否正确
- ✅ 审核关键测试代码（可选）
- ✅ 如果发现问题，让 AI 修复

**示例**：

```yaml
# AI 可以随时更新
backend:
  run_all: "./scripts/run-tests.sh"

# 如果脚本位置改变，AI 会自动更新
backend:
  run_all: "./scripts/test.sh"
```

---

## 最佳实践

### 1. Skills 保持简洁

```yaml
# 好的 Skills（简洁）
quality_standards:
  - 每个功能至少有 3 个测试用例
  - 必须包含正常场景和异常场景

# 不好的 Skills（太详细）
quality_standards:
  - 每个功能至少有 3 个测试用例
  - 测试 1 必须测试正常情况
  - 测试 2 必须测试边界情况
  - 测试 3 必须测试错误情况
  - 每个测试必须使用 pytest
  - 每个测试必须使用 assert
  # ... 太多细节，限制 AI 的灵活性
```

### 2. 信任 AI 的判断

```yaml
# 好的 Skills（给 AI 自主权）
generation_strategy:
  api_test:
    required_scenarios:
      - 成功场景
      - 未授权场景
      - 资源不存在
    # 让 AI 自己决定具体如何测试

# 不好的 Skills（限制 AI）
generation_strategy:
  api_test:
    required_scenarios:
      - 成功场景必须返回 200
      - 未授权场景必须返回 401
      - 资源不存在必须返回 404
      - 必须使用 client.get()
      # ... 太多限制，AI 无法灵活应对
```

### 3. 定期回顾 Skills

- 每月回顾一次 Skills
- 根据实际使用情况调整
- 收集 AI 生成的测试，评估质量
- 如果规则不合适，再调整

### 4. 让 AI 自由维护代码文件

- 不要限制 AI 修改 test_commands.yml
- 不要限制 AI 修改测试代码
- 相信 AI 的判断
- 如果有问题，让 AI 修复

---

## 常见问题

### Q1: 为什么 Skills 不应该经常变动？

**A**:

- Skills 代表固定的规则和流程
- 如果经常变动，AI 无法形成稳定的预期
- Skills 应该是 AI 行为的"宪法"，不是"日常法律"

### Q2: test_commands.yml 会被频繁修改吗？

**A**:

- 是的，这是正常的
- 测试命令可能会因为项目结构调整而改变
- AI 可以随时更新，不需要审批
- 这是动态内容，应该放在代码文件中

### Q3: 我可以修改 test_commands.yml 吗？

**A**:

- 可以，但通常不需要
- AI 会自动维护
- 如果需要特殊配置，可以直接修改
- AI 会尊重你的修改

### Q4: Skills 和代码文件如何协作？

**A**:

```
Skills（固定规则）→ AI 读取 → 生成测试代码 → 代码文件（动态内容）
                        ↓
                  读取 test_commands.yml
                        ↓
                  运行测试
```

### Q5: 如何知道 Skills 是否有效？

**A**:

- 观察 AI 生成的测试质量
- 检查测试覆盖率是否达标
- 看测试是否能够发现问题
- 根据实际情况调整 Skills

### Q6: AI 会修改 Skills 吗？

**A**:

- 不会，Skills 是你维护的
- AI 只会遵守 Skills 的规则
- AI 只会修改代码文件
- 如果 AI 认为需要修改 Skills，会提示你

---

## 与传统方案对比

### 传统方案（多个 Skills）

```
Skills:
  1. run_backend_tests（包含命令）
  2. run_frontend_tests（包含命令）
  3. generate_api_test（包含模板）
  4. check_test_coverage（包含命令）
  5. fix_failing_tests（包含步骤）
  6. generate_component_test（包含模板）

问题：
- Skills 包含动态内容，经常需要修改
- 维护成本高
- AI 自主性低
```

### 极简方案（1 个 Skills）

```
Skills:
  - test_engineer（只包含固定规则）

代码文件（AI 维护）：
  - test_commands.yml（动态命令）
  - tests/*.py（动态测试代码）

优势：
- Skills 是固定的，不需要经常修改
- 维护成本极低
- AI 自主性高
```

---

## 快速开始

### 第一步：创建测试工程师 Skills

创建文件 `.vibe/test_engineer.yml`，复制上面的配置

### 第二步：创建测试命令配置

创建文件 `.vibe/test_commands.yml`，复制上面的配置

### 第三步：开始使用

```
用户: 为 [功能] 生成测试
AI: [自动完成所有步骤]
```

---

## 总结

### 核心理念

**Skills = 固定的规则（你维护）**
**代码文件 = 动态的内容（AI 维护）**

### 关键优势

1. ✅ **Skills 稳定**：不需要经常修改
2. ✅ **AI 自主**：AI 可以自由维护代码文件
3. ✅ **职责清晰**：你维护规则，AI 维护内容
4. ✅ **降低门槛**：不需要了解技术细节
5. ✅ **灵活适应**：AI 可以根据具体情况调整

### 使用原则

- **信任 AI**：给 AI 自主权，不要限制太死
- **保持简单**：Skills 越简单，AI 越灵活
- **定期回顾**：根据实际情况调整 Skills
- **质量优先**：通过 Skills 的质量标准保证测试质量

---

## 配置文件位置

```
项目根目录/
└── .vibe/
    ├── test_engineer.yml     # 测试工程师 Skills（你维护，固定）
    └── test_commands.yml     # 测试命令（AI 维护，动态）

tests/
├── conftest.py              # 共享 fixtures（AI 可以修改）
└── api/
    └── test_api.py           # 测试代码（AI 生成和修改）

src/frontend/src/test/
└── *.test.tsx               # 前端测试（AI 生成和修改）
```

---

**祝您使用愉快！** 🚀
