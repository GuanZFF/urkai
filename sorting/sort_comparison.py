#!/usr/bin/env python3
"""
排序算法比较工具
比较归并排序和快速排序的性能
"""

import time
import random
import sys
from typing import List, Dict, Callable
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import HeapSort
from counting_sort import CountingSort


class SortingBenchmark:
    """排序算法性能基准测试"""
    
    def __init__(self):
        self.algorithms: Dict[str, Callable] = {
            'Python内置排序': sorted,
            '归并排序': lambda arr: merge_sort(arr.copy()),
            '快速排序(基本)': lambda arr: quick_sort(arr, use_three_way=False),
            '快速排序(三路)': lambda arr: quick_sort(arr, use_three_way=True),
            '堆排序': lambda arr: HeapSort.heap_sort(arr),
            '堆排序(原地)': lambda arr: HeapSort.heap_sort_inplace(arr.copy()) if arr else [],
            '计数排序': lambda arr: CountingSort.counting_sort(arr) if arr and min(arr) >= 0 else [],
            '计数排序(含负数)': lambda arr: CountingSort.counting_sort_with_negative(arr) if arr else [],
        }
    
    def generate_test_data(self, size: int, data_type: str = 'random') -> List[int]:
        """生成测试数据"""
        if data_type == 'random':
            return [random.randint(1, 10000) for _ in range(size)]
        elif data_type == 'sorted':
            return list(range(size))
        elif data_type == 'reverse':
            return list(range(size, 0, -1))
        elif data_type == 'duplicates':
            return [random.choice([1, 2, 3, 4, 5]) for _ in range(size)]
        else:
            raise ValueError(f"未知的数据类型: {data_type}")
    
    def run_benchmark(self, arr: List[int], iterations: int = 1) -> Dict[str, float]:
        """运行性能测试"""
        results = {}
        
        for name, algorithm in self.algorithms.items():
            total_time = 0
            
            for _ in range(iterations):
                test_arr = arr.copy()
                start_time = time.perf_counter()
                algorithm(test_arr)
                end_time = time.perf_counter()
                total_time += (end_time - start_time)
            
            avg_time = total_time / iterations
            results[name] = avg_time
        
        return results
    
    def print_results(self, results: Dict[str, float], data_info: str):
        """打印测试结果"""
        print(f"\n📊 {data_info}")
        print("-" * 60)
        
        # 按时间排序
        sorted_results = sorted(results.items(), key=lambda x: x[1])
        
        fastest_time = sorted_results[0][1]
        for name, time_taken in sorted_results:
            relative = time_taken / fastest_time if fastest_time > 0 else 1
            print(f"{name:20} {time_taken:.6f}秒 ({relative:.2f}x)")
    
    def run_comprehensive_test(self):
        """运行全面的性能测试"""
        print("🎯 排序算法全面性能比较")
        print("=" * 60)
        
        test_cases = [
            ("随机数据(1000)", self.generate_test_data(1000, 'random')),
            ("已排序数据(1000)", self.generate_test_data(1000, 'sorted')),
            ("逆序数据(1000)", self.generate_test_data(1000, 'reverse')),
            ("重复数据(1000)", self.generate_test_data(1000, 'duplicates')),
            ("随机大数据(10000)", self.generate_test_data(10000, 'random')),
        ]
        
        for name, test_data in test_cases:
            results = self.run_benchmark(test_data, iterations=3)
            self.print_results(results, name)


class SortingVisualizer:
    """排序过程可视化"""
    
    @staticmethod
    def visualize_partition(arr: List[int], pivot_idx: int, left: int, right: int):
        """可视化分区过程"""
        print("\n🔍 分区过程可视化:")
        print(f"数组: {arr}")
        print(f"Pivot索引: {pivot_idx}, 值: {arr[pivot_idx]}")
        print(f"分区范围: [{left}, {right}]")
        
        # 显示分区标记
        markers = [' '] * len(arr)
        markers[pivot_idx] = 'P'  # Pivot
        if left >= 0:
            markers[left] = 'L'   # 左边界
        if right < len(arr):
            markers[right] = 'R'  # 右边界
        
        print("标记: " + ' '.join(markers))
    
    @staticmethod
    def compare_algorithms_step_by_step(arr: List[int]):
        """逐步比较不同算法"""
        print("\n🔄 算法逐步比较")
        print("原始数组:", arr)
        
        # 归并排序过程
        print("\n1. 归并排序过程:")
        sorted_merge = merge_sort(arr.copy())
        print(f"   结果: {sorted_merge}")
        
        # 快速排序过程
        print("\n2. 快速排序过程:")
        sorted_quick = quick_sort(arr.copy(), use_three_way=False)
        print(f"   结果: {sorted_quick}")
        
        # 验证结果
        print("\n✅ 验证:")
        print(f"   归并排序 == 快速排序: {sorted_merge == sorted_quick}")
        print(f"   正确排序: {sorted_merge == sorted(arr)}")


def interactive_mode():
    """交互模式"""
    benchmark = SortingBenchmark()
    visualizer = SortingVisualizer()
    
    print("🧮 排序算法交互工具")
    print("=" * 60)
    print("选项:")
    print("  1. 性能比较测试")
    print("  2. 算法可视化")
    print("  3. 自定义测试")
    print("  4. 退出")
    
    while True:
        try:
            choice = input("\n请选择选项 (1-4): ").strip()
            
            if choice == '1':
                print("\n运行全面性能测试...")
                benchmark.run_comprehensive_test()
                
            elif choice == '2':
                # 生成示例数据
                sample_data = [random.randint(1, 20) for _ in range(10)]
                visualizer.compare_algorithms_step_by_step(sample_data)
                
            elif choice == '3':
                # 自定义测试
                size = int(input("输入数组大小: "))
                data_type = input("数据类型 (random/sorted/reverse/duplicates): ")
                
                test_data = benchmark.generate_test_data(size, data_type)
                print(f"测试数据: {test_data[:20]}...")
                
                algorithm = input("选择算法 (all/merge/quick_basic/quick_three): ")
                
                if algorithm == 'all':
                    results = benchmark.run_benchmark(test_data)
                    benchmark.print_results(results, f"自定义测试 - 大小:{size}, 类型:{data_type}")
                else:
                    # 测试单个算法
                    if algorithm == 'merge':
                        func = lambda arr: merge_sort(arr.copy())
                        name = "归并排序"
                    elif algorithm == 'quick_basic':
                        func = lambda arr: quick_sort(arr, use_three_way=False)
                        name = "快速排序(基本)"
                    elif algorithm == 'quick_three':
                        func = lambda arr: quick_sort(arr, use_three_way=True)
                        name = "快速排序(三路)"
                    else:
                        print("未知算法")
                        continue
                    
                    start_time = time.perf_counter()
                    result = func(test_data)
                    end_time = time.perf_counter()
                    
                    print(f"\n{name} 结果:")
                    print(f"  时间: {end_time - start_time:.6f}秒")
                    print(f"  排序正确: {result == sorted(test_data)}")
                    
            elif choice == '4':
                print("👋 再见！")
                break
                
            else:
                print("❌ 无效选项")
                
        except ValueError as e:
            print(f"❌ 输入错误: {e}")
        except KeyboardInterrupt:
            print("\n👋 已退出")
            break
        except Exception as e:
            print(f"❌ 错误: {e}")


def main():
    """主函数"""
    if len(sys.argv) > 1:
        # 命令行模式
        if sys.argv[1] == 'benchmark':
            benchmark = SortingBenchmark()
            benchmark.run_comprehensive_test()
        elif sys.argv[1] == 'visualize':
            sample_data = [random.randint(1, 20) for _ in range(10)]
            visualizer = SortingVisualizer()
            visualizer.compare_algorithms_step_by_step(sample_data)
        else:
            print("用法:")
            print("  python sort_comparison.py benchmark  # 运行性能测试")
            print("  python sort_comparison.py visualize  # 可视化演示")
            print("  python sort_comparison.py            # 交互模式")
    else:
        # 交互模式
        interactive_mode()


if __name__ == "__main__":
    main()