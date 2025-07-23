import json
import re


def parse_markdown_list(md_text):
    """
    解析Markdown列表为嵌套字典结构，确保同级节点正确识别
    修复AlmaLinux的层级问题
    """
    # 按行分割文本，保留原始缩进信息（不strip()）
    lines = [line for line in md_text.split('\n') if line.strip()]

    # 提取根标题（以#开头的行）
    root_title = ""
    if lines and lines[0].startswith('#'):
        root_title = lines[0].lstrip('#').strip()
        lines = lines[1:]  # 移除根标题行

    # 解析每一行的缩进级别和内容
    parsed_lines = []
    for line in lines:
        # 匹配列表项（-/*/+ 开头），精确捕获缩进
        match = re.match(r'^(\s*)([-*+])\s+(.*)$', line)
        if match:
            indent = len(match.group(1))  # 原始缩进空格数
            content = match.group(3).strip()

            # 计算缩进级别（2个空格为一级）
            level = max(0, indent // 2)
            parsed_lines.append((level, content))

    # 递归构建嵌套结构
    def build_hierarchy(lines, start_idx, parent_level):
        nodes = []
        i = start_idx

        while i < len(lines):
            current_level, current_content = lines[i]

            # 如果当前级别小于等于父级别，说明不属于当前父节点的子节点
            if current_level <= parent_level:
                return i, nodes  # 返回当前索引和已构建的节点列表

            # 创建当前节点
            node = {"title": current_content, "children": []}

            # 递归处理子节点（下一行开始，父级别为当前级别）
            next_i, children = build_hierarchy(lines, i + 1, current_level)
            node["children"] = children
            nodes.append(node)

            # 移动到下一个待处理节点
            i = next_i

        return i, nodes

    # 从第0行开始构建，根节点的父级别为-1
    _, children = build_hierarchy(parsed_lines, 0, -1)

    # 构建根节点
    root = {
        "title": root_title,
        "children": children
    }

    return root


def main():
    # 示例Markdown文本（保持原始缩进格式）
    md_text = """# 操作系统
- Linux
  - Redhat
  - CentOS
  - Rocky Linux
    - AAA
      - aaa
      - bbb
        - 11111
      - ccc
    - BBB
    - CCC 
  - AlmaLinux
  - Debian
    - Ubuntu
      - Stable
      - Unstable
        - beta
        - preview
    - Kyle
      - test
"""

    # 解析Markdown列表
    parsed_data = parse_markdown_list(md_text)

    # 转换为JSON格式并打印
    json_data = json.dumps(parsed_data, ensure_ascii=False, indent=2)
    print(json_data)

    # 保存为JSON文件
    with open('os_hierarchy.json', 'w', encoding='utf-8') as f:
        f.write(json_data)
    print("\n解析结果已保存到 os_hierarchy.json 文件")


if __name__ == "__main__":
    main()
