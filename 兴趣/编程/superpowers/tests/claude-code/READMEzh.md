# Claude Code 技能测试

使用 Claude Code CLI 对 superpowers 技能进行自动化测试。

## 概述
该测试套件用于验证技能是否正确加载，以及 Claude 是否按预期遵循它们。测试通过无头模式 (`claude -p`) 调用 Claude Code。

## 运行测试
- 运行所有快速测试：`./run-skill-tests.sh`
- 运行集成测试（较慢）：`./run-skill-tests.sh --integration`

---
*(详细说明参见原 README.md)*
