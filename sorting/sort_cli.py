#!/usr/bin/env python3
"""
命令行归并排序工具
可以从命令行参数或标准输入读取整数进行排序
"""

import sys
from merge_sort import merge_sort

def parse_input(input_str):
    """
    解析输入字符串为整数列表
    :param input_str: 输入的字符串，可以是逗号、空格分隔的数字
    :return: 整数列表
    """
    # 移除空白字符，替换各种分隔符为空格
    cleaned = input_str.strip()
    for sep in [',', ';', '|']:
        cleaned = cleaned.replace(sep, ' ')
    
    # 分割并转换为整数
    numbers = []
    for item in cleaned.split():
        try:
            numbers.append(int(item))
        except ValueError:
            print(f"警告: 跳过非数字输入 '{item}'")
    
    return numbers

def main():
    """主函数：处理命令行输入"""
    print("=== 归并排序命令行工具 ===")
    print("输入整数进行排序（用空格、逗号或分号分隔）")
    print("输入 'q' 或 'quit' 退出")
    print("=" * 40)
    
    while True:
        try:
            # 获取用户输入
            user_input = input("\n请输入要排序的数字: ").strip()
            
            # 检查退出命令
            if user_input.lower() in ['q', 'quit', 'exit']:
                print("再见！")
                break
            
            # 跳过空输入
            if not user_input:
                print("请输入一些数字")
                continue
            
            # 解析输入
            numbers = parse_input(user_input)
            
            if not numbers:
                print("没有找到有效的数字")
                continue
            
            print(f"输入的数字: {numbers}")
            print(f"数量: {len(numbers)}")
            
            # 执行排序
            sorted_numbers = merge_sort(numbers.copy())
            
            print(f"排序结果: {sorted_numbers}")
            
            # 显示排序信息
            print(f"最小值: {sorted_numbers[0] if sorted_numbers else 'N/A'}")
            print(f"最大值: {sorted_numbers[-1] if sorted_numbers else 'N/A'}")
            
        except KeyboardInterrupt:
            print("\n\n程序被中断")
            break
        except Exception as e:
            print(f"发生错误: {e}")

if __name__ == "__main__":
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        # 从命令行参数获取输入
        input_str = ' '.join(sys.argv[1:])
        numbers = parse_input(input_str)
        
        if numbers:
            print(f"输入: {numbers}")
            sorted_numbers = merge_sort(numbers)
            print(f"排序后: {sorted_numbers}")
        else:
            print("没有有效的数字输入")
            print("用法: python sort_cli.py [数字1 数字2 ...]")
            print("示例: python sort_cli.py 5 2 8 1 9")
    else:
        # 进入交互模式
        main()