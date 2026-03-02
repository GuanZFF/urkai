# 排序算法项目

这个项目实现了多种排序算法，包含完整的测试和性能比较工具。

## 📁 文件结构

```
sorting/
├── merge_sort.py          # 归并排序实现
├── quick_sort.py          # 快速排序实现（基本+三路变体）
├── sort_cli.py            # 命令行排序工具
├── sort_comparison.py     # 排序算法性能比较工具
└── README.md              # 本文件
```

## 🚀 快速开始

### 运行归并排序
```bash
python3 merge_sort.py
```

### 运行快速排序
```bash
python3 quick_sort.py
```

### 使用命令行工具
```bash
# 交互模式
python3 sort_cli.py

# 直接排序
python3 sort_cli.py 5 2 8 1 9
```

### 性能比较
```bash
# 运行全面性能测试
python3 sort_comparison.py benchmark

# 交互模式
python3 sort_comparison.py
```

## 📊 算法特性

### 归并排序 (`merge_sort.py`)
- **算法类型**: 分治算法
- **时间复杂度**: O(n log n)
- **空间复杂度**: O(n)
- **稳定性**: 稳定
- **特点**: 适合链表排序，外部排序

### 快速排序 (`quick_sort.py`)
- **算法类型**: 分治算法
- **时间复杂度**: 平均 O(n log n)，最坏 O(n²)
- **空间复杂度**: O(log n)
- **稳定性**: 不稳定
- **变体**:
  - **基本快速排序**: 标准实现
  - **三路快速排序**: 优化处理重复元素
- **优化**:
  - 随机化pivot选择
  - 小数组插入排序优化
  - 尾递归优化

## 🧪 测试功能

### 1. 单元测试
每个算法都包含完整的测试用例：
- 普通数组
- 已排序数组
- 逆序数组
- 重复元素数组
- 空数组和单元素数组

### 2. 性能测试
比较不同算法的性能：
- Python内置排序 (`sorted()`)
- 归并排序
- 快速排序（基本）
- 快速排序（三路）

### 3. 数据场景测试
- 随机数据
- 已排序数据
- 逆序数据
- 大量重复数据

## 📈 性能比较结果

根据测试，性能排序（从快到慢）：
1. **Python内置排序** - 最快，C语言实现
2. **快速排序（基本）** - 平均情况优秀
3. **快速排序（三路）** - 处理重复元素优化
4. **归并排序** - 稳定但稍慢

**注意**: Python内置排序使用TimSort算法，是高度优化的混合排序算法。

## 🔧 使用示例

### 基本使用
```python
from merge_sort import merge_sort
from quick_sort import quick_sort

# 归并排序
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr.copy())
print(f"归并排序结果: {sorted_arr}")

# 快速排序（基本）
sorted_quick = quick_sort(arr, use_three_way=False)
print(f"快速排序结果: {sorted_quick}")

# 快速排序（三路）
sorted_three_way = quick_sort(arr, use_three_way=True)
print(f"三路快速排序结果: {sorted_three_way}")
```

### 性能比较
```python
from sort_comparison import SortingBenchmark

benchmark = SortingBenchmark()
test_data = benchmark.generate_test_data(1000, 'random')
results = benchmark.run_benchmark(test_data)

for algorithm, time_taken in results.items():
    print(f"{algorithm}: {time_taken:.6f}秒")
```

## 🎯 算法选择建议

| 场景 | 推荐算法 | 理由 |
|------|----------|------|
| 通用排序 | Python内置排序 | 最快，最稳定 |
| 需要稳定排序 | 归并排序 | 保持相等元素顺序 |
| 内存有限 | 快速排序 | 原地排序，空间效率高 |
| 大量重复元素 | 三路快速排序 | 专门优化重复元素 |
| 教学演示 | 所有算法 | 理解不同算法原理 |

## 📝 开发说明

### 代码规范
- 遵循 PEP 8 代码风格
- 使用类型提示
- 完整的文档字符串
- 详细的注释

### 测试覆盖率
每个算法都包含：
- 单元测试
- 边界测试
- 性能测试
- 正确性验证

### 扩展性
项目设计易于扩展：
1. 添加新排序算法
2. 扩展测试场景
3. 添加可视化功能
4. 支持更多数据类型

## 🤝 贡献

欢迎贡献新的排序算法或改进现有实现！

## 📄 许可证

MIT License

## ✨ 更新日志

### v1.0.0 (2024-03-02)
- 初始版本：归并排序实现
- 添加命令行工具

### v1.1.0 (2024-03-02)
- 添加快速排序算法
- 添加三路快速排序变体
- 添加性能比较工具
- 完善测试套件

---

**项目由 Claude Code 使用智普 GLM-4.7 模型协助开发**