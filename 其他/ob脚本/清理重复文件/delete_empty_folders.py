#!/usr/bin/env python3
"""
空文件夹清理脚本
自动检测并删除指定目录下的空文件夹，支持试运行模式
"""

import os
import sys
from pathlib import Path


def is_empty_folder(folder_path):
    """检查文件夹是否为空（不包含任何文件或子文件夹）"""
    try:
        return len(os.listdir(folder_path)) == 0
    except (OSError, PermissionError):
        return False


def find_empty_folders(root_path):
    """查找所有空文件夹"""
    empty_folders = []
    
    for root, dirs, files in os.walk(root_path, topdown=False):
        # 跳过隐藏文件夹
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        # 检查当前文件夹是否为空
        if not dirs and not files:
            empty_folders.append(root)
    
    return empty_folders


def delete_empty_folders(empty_folders):
    """删除空文件夹"""
    deleted_count = 0
    errors = []
    
    for folder_path in empty_folders:
        try:
            os.rmdir(folder_path)
            print(f"已删除空文件夹: {folder_path}")
            deleted_count += 1
        except (OSError, IOError) as e:
            errors.append(f"删除失败 {folder_path}: {e}")
    
    return deleted_count, errors


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='检测并删除空文件夹',
        epilog='支持试运行模式，先预览再删除'
    )
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='要检查的文件夹路径 (默认: 当前目录)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='只检测不删除，显示将要删除的空文件夹'
    )
    
    args = parser.parse_args()
    
    # 检查路径是否存在
    if not os.path.exists(args.path):
        print(f"错误: 路径 '{args.path}' 不存在")
        return 1
    
    if not os.path.isdir(args.path):
        print(f"错误: '{args.path}' 不是文件夹")
        return 1
    
    print(f"正在检查空文件夹: {os.path.abspath(args.path)}")
    
    # 查找空文件夹
    empty_folders = find_empty_folders(args.path)
    
    if not empty_folders:
        print("未找到空文件夹。")
        return 0
    
    # 显示结果
    print(f"\n发现 {len(empty_folders)} 个空文件夹：")
    for i, folder in enumerate(empty_folders, 1):
        rel_path = os.path.relpath(folder, args.path)
        print(f"  {i}. {rel_path}")
    
    print(f"\n总计将删除 {len(empty_folders)} 个空文件夹。")
    
    if args.dry_run:
        print("\n=== 试运行模式 - 未实际删除文件夹 ===")
        return 0
    
    # 请求用户确认
    while True:
        choice = input("是否确认删除这些空文件夹? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            print("\n开始删除空文件夹...")
            deleted_count, errors = delete_empty_folders(empty_folders)
            
            print(f"\n删除完成！共删除 {deleted_count} 个空文件夹。")
            
            if errors:
                print("\n删除过程中出现以下错误:")
                for error in errors:
                    print(f"  {error}")
            break
        elif choice in ['no', 'n']:
            print("操作已取消。")
            break
        else:
            print("请输入 'yes' 或 'no'")
    
    return 0


if __name__ == "__main__":
    main()