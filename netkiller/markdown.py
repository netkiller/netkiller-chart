#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
##############################################
# Home	: http://netkiller.github.io
# Author: Neo <netkiller@msn.com>
# Data: 2025-07-20
##############################################
try:
    import re
    import json
except ImportError as err:
    print("Import Error: %s" % (err))


class Markdown:
    def __init__(self, markdown: str = None):
        self.markdown = markdown
        pass

    def _parse_heading(self, line, current_level, current_node, root, parent_map):
        """解析标题行，返回更新后的节点状态"""
        title_match = re.match(r'(#+) (.*)', line)
        if not title_match:
            return current_level, current_node, parent_map

        level = len(title_match.group(1))
        text = title_match.group(2)

        # 创建新标题节点
        title_node = {
            'type': 'heading',
            'level': level,
            'text': text,
            'children': []
        }

        # 确定父节点
        if level == 1:
            # 顶级标题，父节点为根
            parent = root
        else:
            # 查找最近的上级标题作为父节点
            parent_level = level - 1
            while parent_level > 0:
                if parent_level in parent_map:
                    parent = parent_map[parent_level]
                    break
                parent_level -= 1
            else:
                # 没找到合适的父级，使用根节点
                parent = root

        # 添加到父节点
        parent['children'].append(title_node)

        # 更新当前节点和父节点映射
        current_node = title_node
        parent_map[level] = current_node

        return level, current_node, parent_map

    def _parse_list_item(self, line, current_node, parent_map, list_stack):
        """解析列表项行，返回更新后的节点状态"""
        list_match = re.match(r'(\s*)([-*+]) (.*)', line)
        if not list_match:
            return current_node, parent_map, list_stack

        indent = len(list_match.group(1))
        text = list_match.group(3)

        # 计算缩进级别（假设2个空格为一个缩进级别）
        indent_level = indent // 2

        # 创建新列表项节点
        list_node = {
            'type': 'list_item',
            'text': text,
            'children': []
        }

        # 确定父节点
        if indent_level == 0:
            # 顶级列表项，父节点为当前标题
            parent = current_node
            list_stack = [list_node]  # 重置列表栈
        else:
            # 子列表项，找到合适的父列表项
            if indent_level <= len(list_stack):
                # 收缩列表深度
                list_stack = list_stack[:indent_level]

            # 获取父列表项
            parent = list_stack[-1] if list_stack else current_node
            list_stack.append(list_node)  # 将当前列表项添加到栈中

        # 添加到父节点
        parent['children'].append(list_node)

        return current_node, parent_map, list_stack

    def parser(self, markdown_text):
        """解析 Markdown 文本，提取标题和列表结构"""
        lines = markdown_text.strip().split('\n')
        root = {'type': 'root', 'children': []}
        current_node = root
        current_heading_level = 0  # 当前标题级别
        parent_map = {}  # 跟踪各级标题节点
        list_stack = []  # 跟踪列表嵌套层级

        for line in lines:
            line = line.rstrip()  # 移除右侧空白

            # 先尝试解析为标题
            current_heading_level, current_node, parent_map = self._parse_heading(
                line, current_heading_level, current_node, root, parent_map
            )

            # 如果不是标题，尝试解析为列表项
            if line.startswith((' ', '\t', '-', '*', '+')):
                current_node, parent_map, list_stack = self._parse_list_item(
                    line, current_node, parent_map, list_stack
                )

        return root

    def dumps(self):
        result = self.parser(self.markdown)
        json_output = json.dumps(result, ensure_ascii=False, indent=2)
        return json_output

    def debug(self):
        print(self.dumps())

    def jsonData(self):
        return self.parser(self.markdown)

    def main(self):
        # 示例 Markdown 文本
        self.markdown = """
        # 一级标题
        - 内容段落1
        - 内容段落2
        
        ## 二级标题
        - 列表项1
        - 列表项2
          - 子列表项1
            - 孙列表项1
        
        ## 三级标题
        - 更多内容 1
          - AAA
          - AAA
        - 更多内容 1
        
        ## 另一个二级标题
        - 列表A
          - 子列表A1
        - 列表B
          - 子列表B1
            - 孙列表B1-1
          - 子列表B2
        """

        # 解析并转换为 JSON
        # result = self.parser(markdown_text)
        # json_output = json.dumps(result, ensure_ascii=False, indent=2)
        self.debug()
        # 打印 JSON 输出


if __name__ == "__main__":
    markdown = Markdown()
    markdown.main()
