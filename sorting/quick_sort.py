#!/usr/bin/env python3
"""
快速排序算法实现
作为现有归并排序的补充
"""

import random
import time
from typing import List, Tuple


def insertion_sort(arr: List[int], left: int, right: int) -> None:
    """
    插入排序，用于小数组优化
    
    Args:
        arr: 待排序数组
        left: 左边界索引
        right: 右边界索引
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def partition(arr: List[int], left: int, right: int) -> int:
    """
    标准分区函数
    
    Args:
        arr: 待分区数组
        left: 左边界索引
        right: 右边界索引
        
    Returns:
        pivot的最终位置
    """
    # 随机选择pivot，避免最坏情况
    pivot_idx = random.randint(left, right)
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    pivot = arr[right]
    
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def three_way_partition(arr: List[int], left: int, right: int) -> Tuple[int, int]:
    """
    三路分区函数，处理大量重复元素
    
    Args:
        arr: 待分区数组
        left: 左边界索引
        right: 右边界索引
        
    Returns:
        (lt, gt) - 等于pivot的区间边界
    """
    # 随机选择pivot
    pivot_idx = random.randint(left, right)
    pivot = arr[pivot_idx]
    
    lt = left      # 小于pivot的右边界
    gt = right     # 大于pivot的左边界
    i = left       # 当前检查的元素
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1
    
    return lt, gt


def quick_sort_basic(arr: List[int], left: int = 0, right: int = None) -> None:
    """
    基本快速排序（递归实现）
    
    Args:
        arr: 待排序数组
        left: 左边界索引
        right: 右边界索引
    """
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        # 小数组使用插入排序优化
        if right - left + 1 <= 16:
            insertion_sort(arr, left, right)
            return
        
        pivot_idx = partition(arr, left, right)
        quick_sort_basic(arr, left, pivot_idx - 1)
        quick_sort_basic(arr, pivot_idx + 1, right)


def quick_sort_three_way(arr: List[int], left: int = 0, right: int = None) -> None:
    """
    三路快速排序（处理重复元素）
    
    Args:
        arr: 待排序数组
        left: 左边界索引
        right: 右边界索引
    """
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        # 小数组使用插入排序优化
        if right - left + 1 <= 16:
            insertion_sort(arr, left, right)
            return
        
        lt, gt = three_way_partition(arr, left, right)
        quick_sort_three_way(arr, left, lt - 1)
        quick_sort_three_way(arr, gt + 1, right)


def quick_sort(arr: List[int], use_three_way: bool = False) -> List[int]:
    """
    快速排序主函数
    
    Args:
        arr: 待排序数组
        use_three_way: 是否使用三路快速排序
        
    Returns:
        排序后的数组（新数组，不修改原数组）
    """
    if not arr:
        return []
    
    arr_copy = arr.copy()
    
    if use_three_way:
        quick_sort_three_way(arr_copy)
    else:
        quick_sort_basic(arr_copy)
    
    return arr_copy


class QuickSortTester:
    """快速排序测试类"""
    
    @staticmethod
    def run_tests() -> None:
        """运行所有测试用例"""
        print("🧪 快速排序测试套件")
        print("=" * 60)
        
        test_cases = [
            ("普通数组", [64, 34, 25, 12, 22, 11, 90]),
            ("已排序数组", [1, 2, 3, 4, 5, 6, 7]),
            ("逆序数组", [7, 6, 5, 4, 3, 2, 1]),
            ("重复元素数组", [5, 2, 8, 2, 5, 8, 1, 5]),
            ("单个元素", [42]),
            ("空数组", []),
            ("随机大数组", [random.randint(1, 1000) for _ in range(100)]),
        ]
        
        all_passed = True
        
        for name, test_arr in test_cases:
            print(f"\n测试: {name}")
            print(f"原始数组: {test_arr[:20]}{'...' if len(test_arr) > 20 else ''}")
            
            # 测试基本快速排序
            result_basic = quick_sort(test_arr, use_three_way=False)
            expected = sorted(test_arr)
            
            basic_passed = result_basic == expected
            status = "✅" if basic_passed else "❌"
            print(f"  基本快速排序: {status}")
            
            if not basic_passed:
                print(f"    结果: {result_basic[:10]}...")
                print(f"    期望: {expected[:10]}...")
                all_passed = False
            
            # 测试三路快速排序（如果有重复元素或需要）
            if len(test_arr) > 1:
                result_three_way = quick_sort(test_arr, use_three_way=True)
                three_way_passed = result_three_way == expected
                status = "✅" if three_way_passed else "❌"
                print(f"  三路快速排序: {status}")
                
                if not three_way_passed:
                    all_passed = False
        
        print(f"\n{'🎉 所有测试通过！' if all_passed else '⚠️  有测试失败'}")
    
    @staticmethod
    def performance_comparison() -> None:
        """性能比较测试"""
        print("\n📊 性能比较测试")
        print("=" * 60)
        
        # 生成测试数据
        sizes = [100, 1000, 5000, 10000]
        
        for size in sizes:
            print(f"\n数组大小: {size}")
            test_arr = [random.randint(1, 10000) for _ in range(size)]
            
            # Python内置排序
            start = time.time()
            sorted(test_arr)
            builtin_time = time.time() - start
            
            # 基本快速排序
            start = time.time()
            quick_sort(test_arr, use_three_way=False)
            basic_time = time.time() - start
            
            # 三路快速排序
            start = time.time()
            quick_sort(test_arr, use_three_way=True)
            three_way_time = time.time() - start
            
            print(f"  Python内置排序: {builtin_time:.6f}秒")
            print(f"  基本快速排序: {basic_time:.6f}秒")
            print(f"  三路快速排序: {three_way_time:.6f}秒")
            
            # 计算相对性能
            if builtin_time > 0:
                basic_ratio = basic_time / builtin_time
                three_way_ratio = three_way_time / builtin_time
                print(f"  相对性能: 基本{basic_ratio:.2f}x, 三路{three_way_ratio:.2f}x")


def main() -> None:
    """主函数"""
    print("⚡ 快速排序算法实现")
    print("=" * 60)
    print("功能:")
    print("  1. 基本快速排序")
    print("  2. 三路快速排序（处理重复元素）")
    print("  3. 随机化pivot选择")
    print("  4. 小数组插入排序优化")
    print("  5. 完整测试套件")
    print("  6. 性能比较")
    print("=" * 60)
    
    # 运行测试
    QuickSortTester.run_tests()
    
    # 运行性能比较
    QuickSortTester.performance_comparison()
    
    # 示例使用
    print("\n💡 示例使用:")
    example_arr = [3, 6, 8, 10, 1, 2, 1]
    print(f"示例数组: {example_arr}")
    
    sorted_basic = quick_sort(example_arr, use_three_way=False)
    print(f"基本快速排序结果: {sorted_basic}")
    
    sorted_three_way = quick_sort(example_arr, use_three_way=True)
    print(f"三路快速排序结果: {sorted_three_way}")
    
    print("\n✨ 快速排序程序完成！")


if __name__ == "__main__":
    main()