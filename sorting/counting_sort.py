#!/usr/bin/env python3
"""
计数排序算法实现
适用于整数排序，特别是范围有限的整数
"""

import time
import random
from typing import List, Tuple


class CountingSort:
    """计数排序类"""
    
    @staticmethod
    def counting_sort(arr: List[int], max_val: int = None) -> List[int]:
        """
        计数排序主函数
        
        Args:
            arr: 待排序数组（非负整数）
            max_val: 数组中最大值，如果为None则自动计算
            
        Returns:
            排序后的数组
        """
        if not arr:
            return []
        
        # 如果未提供最大值，则计算
        if max_val is None:
            max_val = max(arr)
        
        # 初始化计数数组
        count = [0] * (max_val + 1)
        
        # 统计每个元素的出现次数
        for num in arr:
            count[num] += 1
        
        # 计算累积计数
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        # 构建输出数组
        output = [0] * len(arr)
        
        # 从后往前遍历，保证稳定性
        for i in range(len(arr) - 1, -1, -1):
            num = arr[i]
            output[count[num] - 1] = num
            count[num] -= 1
        
        return output
    
    @staticmethod
    def counting_sort_simple(arr: List[int]) -> List[int]:
        """
        简化版计数排序（非稳定，但更易理解）
        
        Args:
            arr: 待排序数组（非负整数）
            
        Returns:
            排序后的数组
        """
        if not arr:
            return []
        
        max_val = max(arr)
        count = [0] * (max_val + 1)
        
        # 统计频率
        for num in arr:
            count[num] += 1
        
        # 直接构建排序结果
        result = []
        for i in range(len(count)):
            result.extend([i] * count[i])
        
        return result
    
    @staticmethod
    def counting_sort_with_negative(arr: List[int]) -> List[int]:
        """
        支持负数的计数排序
        
        Args:
            arr: 待排序数组（可包含负数）
            
        Returns:
            排序后的数组
        """
        if not arr:
            return []
        
        # 找到最小值和最大值
        min_val = min(arr)
        max_val = max(arr)
        
        # 计算偏移量
        offset = -min_val
        range_size = max_val - min_val + 1
        
        # 初始化计数数组
        count = [0] * range_size
        
        # 统计频率
        for num in arr:
            count[num + offset] += 1
        
        # 计算累积计数
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        # 构建输出数组
        output = [0] * len(arr)
        
        # 从后往前遍历，保证稳定性
        for i in range(len(arr) - 1, -1, -1):
            num = arr[i]
            index = num + offset
            output[count[index] - 1] = num
            count[index] -= 1
        
        return output
    
    @staticmethod
    def counting_sort_visual(arr: List[int]) -> List[Tuple[str, List[int]]]:
        """
        计数排序可视化过程
        
        Args:
            arr: 待排序数组
            
        Returns:
            每一步的状态和描述
        """
        steps = []
        
        if not arr:
            return steps
        
        max_val = max(arr)
        
        # 初始状态
        steps.append(("原始数组", arr.copy()))
        
        # 初始化计数数组
        count = [0] * (max_val + 1)
        steps.append(("初始化计数数组", count.copy()))
        
        # 统计频率
        for i, num in enumerate(arr):
            count[num] += 1
            steps.append((f"统计 arr[{i}]={num}", count.copy()))
        
        # 计算累积计数
        for i in range(1, len(count)):
            count[i] += count[i - 1]
            steps.append((f"累积计数 count[{i}]", count.copy()))
        
        # 构建输出数组
        output = [0] * len(arr)
        steps.append(("初始化输出数组", output.copy()))
        
        # 从后往前填充
        for i in range(len(arr) - 1, -1, -1):
            num = arr[i]
            pos = count[num] - 1
            output[pos] = num
            count[num] -= 1
            steps.append((f"放置 arr[{i}]={num} 到 output[{pos}]", output.copy()))
        
        steps.append(("最终排序结果", output.copy()))
        return steps


class CountingSortTester:
    """计数排序测试类"""
    
    @staticmethod
    def run_basic_tests() -> bool:
        """运行基本测试"""
        print("🧪 计数排序基本测试")
        print("=" * 50)
        
        test_cases = [
            ("普通数组", [4, 2, 2, 8, 3, 3, 1]),
            ("已排序数组", [1, 2, 3, 4, 5]),
            ("重复元素数组", [5, 5, 5, 2, 2, 1]),
            ("单个元素", [7]),
            ("空数组", []),
            ("小范围数组", [0, 1, 0, 1, 0, 1]),
            ("包含负数数组", [-5, -10, 0, -3, 8, 5, -1]),
        ]
        
        all_passed = True
        
        for name, test_arr in test_cases:
            print(f"\n测试: {name}")
            print(f"原始数组: {test_arr}")
            
            # 选择适当的计数排序版本
            if not test_arr:
                result = []
                expected = []
            elif min(test_arr) >= 0:
                # 使用标准计数排序
                result = CountingSort.counting_sort(test_arr)
                expected = sorted(test_arr)
            else:
                # 使用支持负数的版本
                result = CountingSort.counting_sort_with_negative(test_arr)
                expected = sorted(test_arr)
            
            passed = result == expected
            status = "✅" if passed else "❌"
            print(f"计数排序结果: {status}")
            
            if not passed:
                print(f"  结果: {result}")
                print(f"  期望: {expected}")
                all_passed = False
            
            # 测试简化版（仅非负数组）
            if test_arr and min(test_arr) >= 0:
                simple_result = CountingSort.counting_sort_simple(test_arr)
                simple_passed = simple_result == expected
                status = "✅" if simple_passed else "❌"
                print(f"简化版计数排序: {status}")
                
                if not simple_passed:
                    all_passed = False
        
        print(f"\n{'🎉 所有测试通过！' if all_passed else '⚠️  有测试失败'}")
        return all_passed
    
    @staticmethod
    def performance_test() -> None:
        """性能测试"""
        print("\n📊 计数排序性能测试")
        print("=" * 50)
        
        # 测试不同范围的数组
        test_cases = [
            ("小范围(0-10)", [random.randint(0, 10) for _ in range(1000)]),
            ("中等范围(0-100)", [random.randint(0, 100) for _ in range(1000)]),
            ("大范围(0-1000)", [random.randint(0, 1000) for _ in range(1000)]),
            ("包含负数(-100-100)", [random.randint(-100, 100) for _ in range(1000)]),
        ]
        
        for name, test_arr in test_cases:
            print(f"\n测试: {name}")
            
            # Python内置排序
            start = time.perf_counter()
            sorted(test_arr)
            builtin_time = time.perf_counter() - start
            
            # 计数排序
            start = time.perf_counter()
            if min(test_arr) >= 0:
                CountingSort.counting_sort(test_arr)
            else:
                CountingSort.counting_sort_with_negative(test_arr)
            counting_time = time.perf_counter() - start
            
            print(f"  Python内置排序: {builtin_time:.6f}秒")
            print(f"  计数排序: {counting_time:.6f}秒")
            
            if builtin_time > 0:
                ratio = counting_time / builtin_time
                print(f"  相对性能: {ratio:.2f}x")
                
                # 计数排序在小范围数据上应该更快
                if name == "小范围(0-10)" and ratio < 1:
                    print("  🎯 计数排序在小范围数据上表现优秀！")
    
    @staticmethod
    def visualize_sorting() -> None:
        """可视化排序过程"""
        print("\n🔍 计数排序过程可视化")
        print("=" * 50)
        
        sample_arr = [4, 2, 2, 8, 3, 3, 1]
        print(f"原始数组: {sample_arr}")
        
        steps = CountingSort.counting_sort_visual(sample_arr)
        
        print("\n排序步骤:")
        for i, (description, state) in enumerate(steps[:15]):  # 只显示前15步
            if "原始数组" in description or "最终" in description:
                print(f"{description}: {state}")
            elif i < 10:  # 显示前10个详细步骤
                print(f"  {description}: {state}")
        
        if len(steps) > 15:
            print(f"... 还有 {len(steps) - 15} 步")
    
    @staticmethod
    def compare_with_other_sorts() -> None:
        """与其他排序算法比较"""
        print("\n🔄 计数排序与其他算法比较")
        print("=" * 50)
        
        # 生成测试数据
        small_range = [random.randint(0, 50) for _ in range(1000)]  # 小范围，计数排序优势
        large_range = [random.randint(0, 10000) for _ in range(1000)]  # 大范围，可能劣势
        
        algorithms = {
            "Python内置排序": sorted,
            "计数排序(小范围)": lambda arr: CountingSort.counting_sort(arr) if arr else [],
            "快速排序": None,  # 需要导入quick_sort
            "归并排序": None,  # 需要导入merge_sort
        }
        
        print("小范围数据(0-50):")
        start = time.perf_counter()
        sorted(small_range)
        builtin_time = time.perf_counter() - start
        
        start = time.perf_counter()
        CountingSort.counting_sort(small_range)
        counting_time = time.perf_counter() - start
        
        print(f"  Python内置排序: {builtin_time:.6f}秒")
        print(f"  计数排序: {counting_time:.6f}秒")
        
        if counting_time < builtin_time:
            speedup = builtin_time / counting_time if counting_time > 0 else float('inf')
            print(f"  🚀 计数排序快 {speedup:.1f} 倍！")
        
        print("\n大范围数据(0-10000):")
        start = time.perf_counter()
        sorted(large_range)
        builtin_time = time.perf_counter() - start
        
        start = time.perf_counter()
        CountingSort.counting_sort(large_range)
        counting_time = time.perf_counter() - start
        
        print(f"  Python内置排序: {builtin_time:.6f}秒")
        print(f"  计数排序: {counting_time:.6f}秒")


def main() -> None:
    """主函数"""
    print("🔢 计数排序算法实现")
    print("=" * 60)
    print("特性:")
    print("  1. 非比较排序算法")
    print("  2. 时间复杂度: O(n + k)，k为数据范围")
    print("  3. 稳定排序（标准实现）")
    print("  4. 适合小范围整数排序")
    print("  5. 支持负数版本可用")
    print("=" * 60)
    
    # 运行测试
    CountingSortTester.run_basic_tests()
    
    # 运行性能测试
    CountingSortTester.performance_test()
    
    # 可视化演示
    CountingSortTester.visualize_sorting()
    
    # 算法比较
    CountingSortTester.compare_with_other_sorts()
    
    # 示例使用
    print("\n💡 示例使用:")
    
    # 示例1: 标准计数排序
    example1 = [4, 2, 2, 8, 3, 3, 1]
    print(f"示例1（非负整数）: {example1}")
    result1 = CountingSort.counting_sort(example1)
    print(f"计数排序结果: {result1}")
    
    # 示例2: 支持负数的计数排序
    example2 = [-5, -10, 0, -3, 8, 5, -1]
    print(f"\n示例2（包含负数）: {example2}")
    result2 = CountingSort.counting_sort_with_negative(example2)
    print(f"计数排序结果: {result2}")
    
    # 示例3: 简化版
    example3 = [1, 4, 1, 2, 7, 5, 2]
    print(f"\n示例3（简化版）: {example3}")
    result3 = CountingSort.counting_sort_simple(example3)
    print(f"简化版计数排序: {result3}")
    
    print("\n✨ 计数排序程序完成！")


if __name__ == "__main__":
    main()