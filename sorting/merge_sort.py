#!/usr/bin/env python3
"""
归并排序算法实现
用于对整数列表进行排序
"""

def merge_sort(arr):
    """
    归并排序主函数
    :param arr: 待排序的整数列表
    :return: 排序后的整数列表
    """
    if len(arr) <= 1:
        return arr
    
    # 分割数组
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 递归排序
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # 合并排序后的子数组
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    合并两个已排序的数组
    :param left: 已排序的左半部分
    :param right: 已排序的右半部分
    :return: 合并后的已排序数组
    """
    merged = []
    left_idx, right_idx = 0, 0
    
    # 比较两个数组的元素，将较小的添加到结果中
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    # 添加剩余的元素
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged

def main():
    """主函数：演示归并排序的使用"""
    print("=== 归并排序演示程序 ===")
    
    # 示例数据
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 12, 1, 7],
        [1, 2, 3, 4, 5],  # 已排序
        [5, 4, 3, 2, 1],  # 逆序
        [42],  # 单个元素
        []     # 空数组
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"\n测试用例 {i}:")
        print(f"原始数组: {arr}")
        
        sorted_arr = merge_sort(arr.copy())
        print(f"排序后: {sorted_arr}")
        
        # 验证排序结果
        if sorted_arr == sorted(arr):
            print("✓ 排序正确")
        else:
            print("✗ 排序错误")

if __name__ == "__main__":
    main()