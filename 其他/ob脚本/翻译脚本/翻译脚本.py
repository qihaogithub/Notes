#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Obsidian 插件翻译脚本
支持自动发现插件、批量处理、词典优先级翻译、同目录备份
"""

import re
import requests
import json
import time
import os
import csv
import argparse
import datetime
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class TranslationStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    REVIEWED = "reviewed"
    EXCLUDED = "excluded"

@dataclass
class PluginInfo:
    name: str
    path: str
    main_file: str
    manifest_file: str
    version: str = ""
    last_modified: datetime.datetime = None

@dataclass
class DictionaryEntry:
    source_text: str
    translated_text: str

class PluginScanner:
    """插件自动发现器"""
    
    def __init__(self, plugins_path: str):
        self.plugins_path = Path(plugins_path)
    
    def scan_all_plugins(self) -> List[PluginInfo]:
        """扫描所有插件"""
        plugins = []
        if not self.plugins_path.exists():
            print(f"插件目录不存在: {self.plugins_path}")
            return plugins
        
        for item in self.plugins_path.iterdir():
            if item.is_dir():
                plugin_info = self._validate_plugin(item)
                if plugin_info:
                    plugins.append(plugin_info)
        
        print(f"发现 {len(plugins)} 个有效插件")
        return plugins
    
    def _validate_plugin(self, plugin_dir: Path) -> Optional[PluginInfo]:
        """验证插件目录是否有效"""
        main_file = plugin_dir / "main.js"
        manifest_file = plugin_dir / "manifest.json"
        
        if not (main_file.exists() and manifest_file.exists()):
            return None
        
        # 提取版本信息
        version = ""
        try:
            with open(manifest_file, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
                version = manifest.get('version', '')
        except Exception as e:
            print(f"读取插件清单失败 {plugin_dir.name}: {e}")
        
        # 获取最后修改时间
        last_modified = datetime.datetime.fromtimestamp(main_file.stat().st_mtime)
        
        return PluginInfo(
            name=plugin_dir.name,
            path=str(plugin_dir),
            main_file=str(main_file),
            manifest_file=str(manifest_file),
            version=version,
            last_modified=last_modified
        )

class DictionaryManager:
    """词典管理器"""
    
    def __init__(self, dictionary_dir: str):
        self.dictionary_dir = Path(dictionary_dir)
        self.dictionary_dir.mkdir(exist_ok=True)
    
    def get_dictionary_path(self, plugin_name: str) -> Path:
        """获取插件词典文件路径（与插件文件夹名称相同）"""
        return self.dictionary_dir / f"{plugin_name}.txt"
    
    def load_dictionary(self, plugin_name: str) -> Dict[str, DictionaryEntry]:
        """加载词典（TXT格式：原文\n翻译\n\n）"""
        dictionary_path = self.get_dictionary_path(plugin_name)
        dictionary = {}
        
        if not dictionary_path.exists():
            return dictionary
        
        try:
            with open(dictionary_path, 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()
                
            i = 0
            while i < len(lines):
                source_text = lines[i].strip()
                if source_text and i + 1 < len(lines):  # 有原文且还有下一行
                    translated_text = lines[i + 1].strip()
                    if translated_text:  # 翻译文本不为空
                        entry = DictionaryEntry(
                            source_text=source_text,
                            translated_text=translated_text
                        )
                        dictionary[entry.source_text] = entry
                    i += 2  # 跳过翻译行
                    # 跳过空行
                    while i < len(lines) and not lines[i].strip():
                        i += 1
                else:
                    i += 1
                    
        except Exception as e:
            print(f"加载词典失败 {plugin_name}: {e}")
        
        return dictionary
    
    def save_dictionary(self, plugin_name: str, dictionary: Dict[str, DictionaryEntry]):
        """保存词典（TXT格式：原文\n翻译\n\n）"""
        dictionary_path = self.get_dictionary_path(plugin_name)
        
        try:
            with open(dictionary_path, 'w', encoding='utf-8-sig') as f:
                for entry in dictionary.values():
                    f.write(f"{entry.source_text}\n")
                    f.write(f"{entry.translated_text}\n\n")
        except Exception as e:
            print(f"保存词典失败 {plugin_name}: {e}")
    
    def add_new_entries(self, plugin_name: str, new_texts: List[Tuple[str, str]]):
        """已移除：人工维护词典，不需要自动添加条目"""
        print("注意：自动更新词典功能已移除，请手动维护词典文件")
        return 0
    
    def _auto_translate_text(self, text: str) -> str:
        """自动翻译文本"""
        try:
            url = "https://translate.googleapis.com/translate_a/single"
            params = {
                "client": "gtx",
                "sl": "auto",
                "tl": "zh-CN",
                "dt": "t",
                "q": text,
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                result = json.loads(response.text)
                if result and result[0] and result[0][0]:
                    return result[0][0][0]
        except Exception as e:
            print(f"自动翻译失败: {e}")
        
        return text  # 翻译失败返回原文



class TextExtractor:
    """文本提取器（已简化，仅用于参考）"""
    
    # 插件设置菜单相关的函数列表
    TARGET_FUNCTIONS = [
        'setName', 'setDesc', 'setText', 'setTitle', 
        'addText', 'addTitle', 'addToggle', 'addTextArea', 
        'addMomentFormat', 'addColorPicker', 'addFileSuggest', 
        'addFolderSuggest', 'addDropDown', 'addSlider', 'addSearch',
        'setPlaceholder', 'setTooltip', 'setClass'
    ]
    
    @classmethod
    def extract_translatable_texts(cls, plugin_path: str) -> List[Tuple[str, str]]:
        """已简化：仅用于参考，不再主动提取文本"""
        print("注意：文本提取功能已简化，请直接编辑词典文件")
        return []
    
    @classmethod
    def _should_translate(cls, text: str) -> bool:
        """判断是否应该翻译"""
        if not text or len(text.strip()) < 2:
            return False
        
        # 检查排除规则
        for pattern in cls.EXCLUSION_PATTERNS:
            if re.match(pattern, text):
                return False
        
        # 检查是否已包含中文
        if any('\u4e00' <= char <= '\u9fff' for char in text):
            return False
        
        return True
    
    @classmethod
    def _get_context(cls, match, content: str) -> str:
        """获取上下文信息"""
        # 简化的上下文获取
        start = max(0, match.start() - 50)
        end = min(len(content), match.end() + 50)
        context = content[start:end]
        
        # 提取函数名
        func_match = re.search(r'(\w+)\s*\(\s*["\']', context)
        if func_match:
            return func_match.group(1)
        
        return "unknown"

class TranslationProcessor:
    """翻译处理器"""
    
    def __init__(self, dictionary_manager: DictionaryManager):
        self.dictionary_manager = dictionary_manager
    
    def translate_plugin(self, plugin_info: PluginInfo, use_dict_first: bool = True) -> Dict:
        """翻译插件"""
        
        # 加载词典
        dictionary = self.dictionary_manager.load_dictionary(plugin_info.name)
        
        # 如果词典为空，跳过该插件（静默跳过，不打印）
        if not dictionary:
            return None
        
        try:
            # 创建备份文件路径
            backup_file = plugin_info.main_file + '.backup'
            
            # 如果存在备份文件，先还原为原始文件
            if os.path.exists(backup_file):
                print(f"发现备份文件，正在还原 {plugin_info.name} 到原始状态...")
                with open(backup_file, 'r', encoding='utf-8') as f:
                    original_content = f.read()
                with open(plugin_info.main_file, 'w', encoding='utf-8') as f:
                    f.write(original_content)
                content = original_content
            else:
                # 首次翻译，创建备份
                print(f"首次翻译 {plugin_info.name}，正在创建备份...")
                with open(plugin_info.main_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                with open(backup_file, 'w', encoding='utf-8') as f:
                    f.write(content)
            
            # 直接使用原始内容进行翻译（移除预检查逻辑）
            print(f"开始翻译插件: {plugin_info.name}")
            translated_content = self._process_content(content, dictionary, use_dict_first)
            translation_stats = self._get_translation_stats()
            
            # 如果没有翻译任何内容，提示用户
            if translation_stats['total_translated'] == 0:
                print(f"插件 {plugin_info.name} 没有需要翻译的内容")
                return None
            
            # 写回翻译后的内容
            with open(plugin_info.main_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            
            print(f"插件 {plugin_info.name} 翻译完成")
            print(f"  翻译文本数: {translation_stats['total_translated']}")
            print(f"  词典命中: {translation_stats['dictionary_hits']}")
            print(f"  自动翻译: {translation_stats['auto_translations']}")
            
            return {
                'plugin_name': plugin_info.name,
                'stats': translation_stats
            }
            
        except Exception as e:
            print(f"翻译插件失败 {plugin_info.name}: {e}")
            return None
    
    def _process_content(self, content: str, dictionary: Dict, use_dict_first: bool) -> str:
        """处理内容（仅翻译词典中存在的文本）"""
        self.translation_stats = {'total_translated': 0, 'dictionary_hits': 0, 'auto_translations': 0}
        
        def replace_text_match(match):
            original_text = match.group(2)  # 第2个捕获组是文本内容
            
            # 仅当词典中存在该文本时才进行翻译
            if original_text in dictionary:
                entry = dictionary[original_text]
                # 仅翻译有译文的条目
                if entry.translated_text and entry.translated_text.strip():
                    self.translation_stats['dictionary_hits'] += 1
                    self.translation_stats['total_translated'] += 1
                    return match.group(0).replace(original_text, entry.translated_text)
            
            # 词典中不存在的文本，保持原样
            return match.group(0)
        
        # 使用正则表达式匹配文本（包含设置菜单相关函数）
        pattern = r'(?:(setName|setDesc|setText|setTitle|create_collapsible|addText|addTitle|addToggle|addTextArea|addMomentFormat|addColorPicker|addFileSuggest|addFolderSuggest|addDropDown|addSearch|setPlaceholder|setTooltip|setClass)\(\s*"((?:[^"\\]|\\.|\s)*?)"\s*\)|text:\s*[\'"]((?:[^\'"\\]|\\.|\s)*?)[\'"](\s*,)?|description:\s*[\'"]((?:[^\'"\\]|\\.|\s)*?)[\'"](\s*,)?|name:\s*[\'"]((?:[^\'"\\]|\\.|\s)*?)[\'"](\s*,)?)'
        # 使用正则表达式匹配文本（包含设置菜单相关函数）
        pattern = r'\.(setName|setDesc|setText|setTitle|addText|addTitle|addToggle|addTextArea|addMomentFormat|addColorPicker|addFileSuggest|addFolderSuggest|addDropDown|addSlider|addSearch|setPlaceholder|setTooltip|setClass)\(\s*"((?:[^"\\]|\\.|\s)*?)"\s*\)'
        return re.sub(pattern, replace_text_match, content, flags=re.DOTALL)
    
    def _get_translation_stats(self) -> Dict:
        """获取翻译统计"""
        return self.translation_stats.copy()

class TranslationScript:
    """主翻译脚本类"""
    
    def __init__(self, config: Dict):
        self.plugins_path = config.get('obsidian_plugins_path', '')
        self.dictionary_dir = config.get('dictionary_directory', './词典文件')
        
        # 初始化管理器
        self.plugin_scanner = PluginScanner(self.plugins_path)
        self.dictionary_manager = DictionaryManager(self.dictionary_dir)
        self.translation_processor = TranslationProcessor(self.dictionary_manager)
    
    def update_dictionary(self, plugin_names: List[str] = None) -> Dict:
        """已移除：人工维护词典，不需要自动更新功能"""
        print("注意：自动更新词典功能已移除")
        print("请直接编辑词典文件：")
        print(f"  词典目录: {self.dictionary_dir}")
        print("  词典格式: source_text,translated_text")
        return {}
    
    def translate_scripts(self, plugin_names: List[str] = None, use_dict_first: bool = True) -> Dict:
        """翻译脚本动作"""
        print("=== 开始翻译脚本 ===")
        
        # 获取目标插件
        if plugin_names:
            all_plugins = self.plugin_scanner.scan_all_plugins()
            target_plugins = [p for p in all_plugins if p.name in plugin_names]
        else:
            target_plugins = self.plugin_scanner.scan_all_plugins()
        
        if not target_plugins:
            print("没有找到需要处理的插件")
            return {}
        
        results = {}
        for plugin_info in target_plugins:
            try:
                result = self.translation_processor.translate_plugin(plugin_info, use_dict_first)
                if result:
                    results[plugin_info.name] = result
            except Exception as e:
                print(f"处理插件失败 {plugin_info.name}: {e}")
                continue
        
        print(f"\n=== 翻译完成 ===")
        print(f"成功处理 {len(results)} 个插件")
        
        return results

def load_config(config_file: str = "config.json") -> Dict:
    """加载配置文件"""
    config_path = Path(config_file)
    default_config = {
        'obsidian_plugins_path': 'E:\\我的笔记\\.obsidian\\plugins',
        'dictionary_directory': './词典文件',
        'batch_processing': True
    }
    
    if config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                # 合并默认配置
                default_config.update(config)
                return default_config
        except Exception as e:
            print(f"加载配置文件失败，使用默认配置: {e}")
    
    return default_config

def main():
    """主函数（简化为仅支持翻译功能）"""
    parser = argparse.ArgumentParser(description='Obsidian 插件翻译脚本 - 基于人工维护词典')
    parser.add_argument('--plugins', type=str, help='指定插件名称（逗号分隔）')
    parser.add_argument('--all-plugins', action='store_true', help='处理所有插件')
    parser.add_argument('--config', type=str, default='config.json',
                       help='配置文件路径')
    
    args = parser.parse_args()
    
    # 加载配置
    config = load_config(args.config)
    
    # 创建翻译脚本实例
    script = TranslationScript(config)
    
    # 解析插件列表
    plugin_names = None
    if args.plugins:
        plugin_names = [name.strip() for name in args.plugins.split(',')]
    elif args.all_plugins:
        plugin_names = None  # 处理所有插件
    else:
        print("错误：必须指定 --plugins 或 --all-plugins")
        return
    
    # 执行翻译（唯一的功能）
    print("=== Obsidian 插件翻译脚本 ===")
    print("注意：仅翻译词典中已存在的人工维护翻译")
    script.translate_scripts(plugin_names, use_dict_first=True)

if __name__ == "__main__":
    main()
