#!/usr/bin/env python3
"""
重复文件检测和清理脚本 - 修复版
优先保留无后缀的原始文件，删除带各种后缀的重复文件
"""

import os
import sys
from pathlib import Path
from collections import defaultdict
import re


def get_file_size(filepath):
    """获取文件大小"""
    try:
        return os.path.getsize(filepath)
    except (OSError,):
        return None


def extract_base_name_and_suffix(filename_stem):
    """提取基础名称和后缀信息"""
    # 定义各种后缀模式的正则表达式
    suffix_patterns = [
        (r'(.*)的副本$', '副本'),
        (r'(.*)复件$', '复件'),
        (r'(.*)备份$', '备份'),
        (r'(.*) copy$', 'copy'),
        (r'(.*) backup$', 'backup'),
        (r'(.*)\([0-9]+\)$', '括号数字'),
        (r'(.*)\[[0-9]+\]$', '方括号数字'),
        (r'(.*)_[0-9]+$', '下划线数字'),
        (r'(.*)-[0-9]+$', '连字符数字'),
        (r'(.*) [0-9]+$', '空格数字'),
        (r'(.*)\.[0-9]+$', '点数字'),
    ]
    
    for pattern, suffix_type in suffix_patterns:
        match = re.match(pattern, filename_stem, re.IGNORECASE)
        if match:
            return match.group(1), True, suffix_type
    
    # 检查是否以数字结尾
    if re.match(r'.*[0-9]+$', filename_stem):
        base_name = re.sub(r'[0-9\s]+$', '', filename_stem)
        return base_name, True, '数字'
    
    # 没有后缀，是原始文件
    return filename_stem, False, None


def find_duplicates(root_path):
    """查找重复文件，优先保留无后缀的原始文件"""
    files_by_base_name = defaultdict(list)
    
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for filename in files:
            if filename.startswith('.'):
                continue
                
            filepath = os.path.join(root, filename)
            file_size = get_file_size(filepath)
            if file_size is None:
                continue
            
            name_without_ext = Path(filename).stem
            base_name, has_suffix, suffix_type = extract_base_name_and_suffix(name_without_ext)
            
            files_by_base_name[base_name].append({
                'filepath': filepath,
                'file_size': file_size,
                'original_name': filename,
                'has_suffix': has_suffix,
                'suffix_type': suffix_type,
                'name_without_ext': name_without_ext
            })
    
    duplicates = {}
    for base_name, file_list in files_by_base_name.items():
        if len(file_list) > 1:
            # 排序：无后缀文件优先，然后按路径长度和文件名长度
            file_list.sort(key=lambda x: (
                x['has_suffix'],  # False优先（无后缀的原始文件）
                len(x['filepath'].split(os.sep)),
                len(x['name_without_ext'])
            ))
            
            keep_file = file_list[0]['filepath']
            remove_files = [item['filepath'] for item in file_list[1:]]
            
            duplicates[base_name] = {
                'keep': keep_file,
                'remove': remove_files,
                'files_info': file_list
            }
    
    return duplicates


def format_file_info(filepath):
    size = get_file_size(filepath)
    size_str = f"{size:,} bytes" if size else "Unknown"
    return f"{filepath} ({size_str})"


def delete_files(duplicates):
    """删除重复文件"""
    deleted_count = 0
    errors = []
    
    for key, files in duplicates.items():
        for filepath in files['remove']:
            try:
                os.remove(filepath)
                print(f"已删除: {filepath}")
                deleted_count += 1
            except (OSError, IOError) as e:
                errors.append(f"删除失败 {filepath}: {e}")
    
    return deleted_count, errors


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='检测并清理重复文件 - 优先保留无后缀原始文件',
        epilog='支持识别各种后缀格式：数字、括号、下划线、副本、copy等'
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
        help='只检测不删除，显示将要删除的文件'
    )
    
    args = parser.parse_args()
    
    # 检查路径是否存在
    if not os.path.exists(args.path):
        print(f"错误: 路径 '{args.path}' 不存在")
        return 1
    
    if not os.path.isdir(args.path):
        print(f"错误: '{args.path}' 不是文件夹")
        return 1
    
    print(f"正在检查文件夹: {os.path.abspath(args.path)}")
    
    # 查找重复文件
    duplicates = find_duplicates(args.path)
    
    if not duplicates:
        print("未找到重复文件。")
        return 0
    
    # 显示结果
    print(f"\n发现 {len(duplicates)} 组重复文件：\n")
    
    total_remove = 0
    for i, (base_name, files) in enumerate(duplicates.items(), 1):
        print(f"组 {i}: 基础名称 '{base_name}'")
        print(f"  保留: {format_file_info(files['keep'])}")
        print("  删除:")
        for f in files['remove']:
            print(f"    - {format_file_info(f)}")
            total_remove += 1
        print()
    
    print(f"总计将删除 {total_remove} 个文件。")
    
    if args.dry_run:
        print("\n=== 试运行模式 - 未实际删除文件 ===")
        return 0
    
    # 请求用户确认
    while True:
        choice = input("是否确认删除这些文件? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            print("\n开始删除重复文件...")
            deleted_count, errors = delete_files(duplicates)
            
            print(f"\n删除完成！共删除 {deleted_count} 个文件。")
            
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
