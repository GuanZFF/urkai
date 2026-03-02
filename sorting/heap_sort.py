#!/usr/bin/env python3
"""
堆排序算法实现
作为排序算法扩展的一部分
"""

import time
import random
from typing import List, Tuple


class HeapSort:
    """堆排序类"""
    
    @staticmethod
    def heapify(arr: List[int], n: int, i: int) -> None:
        """
        构建最大堆
        
        Args:
            arr: 待堆化的数组
            n: 堆的大小
            i: 当前根节点索引
        """
        largest = i          # 初始化最大值为根节点
        left = 2 * i + 1     # 左子节点
        right = 2 * i + 2    # 右子节点
        
        # 如果左子节点存在且大于根节点
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        # 如果右子节点存在且大于当前最大值
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        # 如果最大值不是根节点
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # 交换
            HeapSort.heapify(arr, n, largest)  # 递归堆化受影响的子树
    
    @staticmethod
    def heap_sort(arr: List[int]) -> List[int]:
        """
        堆排序主函数
        
        Args:
            arr: 待排序数组
            
        Returns:
            排序后的数组（新数组，不修改原数组）
        """
        if not arr:
            return []
        
        arr_copy = arr.copy()
        n = len(arr_copy)
        
        # 构建最大堆
        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(arr_copy, n, i)
        
        # 逐个提取元素
        for i in range(n - 1, 0, -1):
            arr_copy[0], arr_copy[i] = arr_copy[i], arr_copy[0]  # 交换
            HeapSort.heapify(arr_copy, i, 0)  # 堆化减少的堆
        
        return arr_copy
    
    @staticmethod
    def heap_sort_inplace(arr: List[int]) -> None:
        """
        原地堆排序（修改原数组）
        
        Args:
            arr: 待排序数组（会被修改）
        """
        n = len(arr)
        
        if n <= 1:
            return
        
        # 构建最大堆
        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(arr, n, i)
        
        # 逐个提取元素
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # 交换
            HeapSort.heapify(arr, i, 0)
    
    @staticmethod
    def build_heap_visual(arr: List[int]) -> List[Tuple[int, List[int]]]:
        """
        构建堆的可视化过程
        
        Args:
            arr: 原始数组
            
        Returns:
            每一步的堆状态列表
        """
        steps = []
        n = len(arr)
        arr_copy = arr.copy()
        
        # 记录初始状态
        steps.append((0, arr_copy.copy()))
        
        # 构建最大堆的过程
        for i in range(n // 2 - 1, -1, -1):
            HeapSort._heapify_with_steps(arr_copy, n, i, steps)
        
        # 提取元素的过程
        for i in range(n - 1, 0, -1):
            arr_copy[0], arr_copy[i] = arr_copy[i], arr_copy[0]
            steps.append((i, arr_copy.copy()))  # 记录交换后
            HeapSort._heapify_with_steps(arr_copy, i, 0, steps)
        
        return steps
    
    @staticmethod
    def _heapify_with_steps(arr: List[int], n: int, i: int, steps: List[Tuple[int, List[int]]]) -> None:
        """带步骤记录的堆化函数"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            steps.append((i, arr.copy()))  # 记录交换后
            HeapSort._heapify_with_steps(arr, n, largest, steps)


class HeapSortTester:
    """堆排序测试类"""
    
    @staticmethod
    def run_basic_tests() -> bool:
        """运行基本测试"""
        print("🧪 堆排序基本测试")
        print("=" * 50)
        
        test_cases = [
            ("普通数组", [64, 34, 25, 12, 22, 11, 90]),
            ("已排序数组", [1, 2, 3, 4, 5, 6, 7]),
            ("逆序数组", [7, 6, 5, 4, 3, 2, 1]),
            ("重复元素数组", [5, 2, 8, 2, 5, 8, 1, 5]),
            ("单个元素", [42]),
            ("空数组", []),
            ("随机数组", [random.randint(1, 100) for _ in range(20)]),
        ]
        
        all_passed = True
        
        for name, test_arr in test_cases:
            print(f"\n测试: {name}")
            print(f"原始数组: {test_arr}")
            
            # 测试堆排序
            result = HeapSort.heap_sort(test_arr)
            expected = sorted(test_arr)
            
            passed = result == expected
            status = "✅" if passed else "❌"
            print(f"堆排序结果: {status}")
            
            if not passed:
                print(f"  结果: {result}")
                print(f"  期望: {expected}")
                all_passed = False
            
            # 测试原地堆排序
            if test_arr:
                arr_copy = test_arr.copy()
                HeapSort.heap_sort_inplace(arr_copy)
                inplace_passed = arr_copy == expected
                status = "✅" if inplace_passed else "❌"
                print(f"原地堆排序: {status}")
                
                if not inplace_passed:
                    all_passed = False
        
        print(f"\n{'🎉 所有测试通过！' if all_passed else '⚠️  有测试失败'}")
        return all_passed
    
    @staticmethod
    def performance_test() -> None:
        """性能测试"""
        print("\n📊 堆排序性能测试")
        print("=" * 50)
        
        sizes = [100, 1000, 5000, 10000]
        
        for size in sizes:
            print(f"\n数组大小: {size}")
            test_arr = [random.randint(1, 10000) for _ in range(size)]
            
            # Python内置排序
            start = time.perf_counter()
            sorted(test_arr)
            builtin_time = time.perf_counter() - start
            
            # 堆排序
            start = time.perf_counter()
            HeapSort.heap_sort(test_arr)
            heap_time = time.perf_counter() - start
            
            # 原地堆排序
            arr_copy = test_arr.copy()
            start = time.perf_counter()
            HeapSort.heap_sort_inplace(arr_copy)
            heap_inplace_time = time.perf_counter() - start
            
            print(f"  Python内置排序: {builtin_time:.6f}秒")
            print(f"  堆排序: {heap_time:.6f}秒")
            print(f"  原地堆排序: {heap_inplace_time:.6f}秒")
            
            if builtin_time > 0:
                heap_ratio = heap_time / builtin_time
                heap_inplace_ratio = heap_inplace_time / builtin_time
                print(f"  相对性能: 堆排序{heap_ratio:.2f}x, 原地{heap_inplace_ratio:.2f}x")
    
    @staticmethod
    def visualize_heap_building() -> None:
        """可视化堆构建过程"""
        print("\n🔍 堆构建过程可视化")
        print("=" * 50)
        
        sample_arr = [3, 9, 2, 1, 4, 5]
        print(f"原始数组: {sample_arr}")
        
        steps = HeapSort.build_heap_visual(sample_arr)
        
        print("\n堆构建步骤:")
        for i, (step_num, arr_state) in enumerate(steps[:10]):  # 只显示前10步
            if i == 0:
                print(f"步骤 {step_num}: 初始状态 {arr_state}")
            else:
                print(f"步骤 {step_num}: {arr_state}")
        
        if len(steps) > 10:
            print(f"... 还有 {len(steps) - 10} 步")


def main() -> None:
    """主函数"""
    print("🌲 堆排序算法实现")
    print("=" * 60)
    print("特性:")
    print("  1. 基于完全二叉树的排序算法")
    print("  2. 时间复杂度: O(n log n)")
    print("  3. 原地排序版本可用")
    print("  4. 不稳定排序")
    print("  5. 适合优先级队列实现")
    print("=" * 60)
    
    # 运行测试
    HeapSortTester.run_basic_tests()
    
    # 运行性能测试
    HeapSortTester.performance_test()
    
    # 可视化演示
    HeapSortTester.visualize_heap_building()
    
    # 示例使用
    print("\n💡 示例使用:")
    example_arr = [12, 11, 13, 5, 6, 7]
    print(f"示例数组: {example_arr}")
    
    sorted_result = HeapSort.heap_sort(example_arr)
    print(f"堆排序结果: {sorted_result}")
    
    # 原地排序示例
    arr_copy = example_arr.copy()
    HeapSort.heap_sort_inplace(arr_copy)
    print(f"原地堆排序结果: {arr_copy}")
    
    print("\n✨ 堆排序程序完成！")


if __name__ == "__main__":
    main()