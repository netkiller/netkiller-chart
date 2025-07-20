import re

import svgwrite
from svgwrite.shapes import Line
from svgwrite.text import Text


class MindMapGenerator:
    def __init__(self, width=800, height=600, node_padding=15, node_spacing=40):
        """初始化思维导图生成器"""
        self.width = width
        self.height = height
        self.node_padding = node_padding  # 节点内边距
        self.node_spacing = node_spacing  # 节点间距
        self.font_size = 14
        self.font_family = "Arial, sans-serif"
        self.node_color = "#e6f7ff"
        self.node_border_color = "#1890ff"
        self.node_border_width = 1.5
        self.link_color = "#bfbfbf"
        self.link_width = 1.5
        self.root_color = "#1890ff"
        self.root_text_color = "#ffffff"

    def parse_markdown(self, markdown_text):
        """解析 Markdown 文本，提取列表结构"""
        lines = markdown_text.strip().split('\n')
        root = {"text": "Root", "children": [], "level": 0, "x": 0, "y": 0}
        current_parents = {0: root}
        current_level = 0

        for line in lines:
            line = line.rstrip()

            # 检查是否为列表项
            list_match = re.match(r'(\s*)([-*+])\s+(.*)', line)
            if list_match:
                indent = len(list_match.group(1))
                text = list_match.group(3)

                # 计算缩进级别（假设2个空格为一个缩进级别）
                level = indent // 2 + 1  # 根节点级别为0

                # 创建新节点
                node = {"text": text, "children": [], "level": level, "x": 0, "y": 0}

                # 确定父节点
                if level > 1:
                    parent_level = level - 1
                    if parent_level in current_parents:
                        parent = current_parents[parent_level]
                    else:
                        # 如果找不到合适的父级，使用根节点
                        parent = root
                else:
                    parent = root

                parent["children"].append(node)
                current_parents[level] = node
                current_level = level

        return root

    def calculate_node_dimensions(self, node):
        """计算节点的宽度和高度"""
        # 简单估算文本宽度（每个字符约为 font_size * 0.5）
        text_width = len(node["text"]) * self.font_size * 0.5
        node_width = text_width + 2 * self.node_padding
        node_height = self.font_size + 2 * self.node_padding
        return node_width, node_height

    def layout_tree(self, root, x=0, y=0, direction=1):
        """递归布局树结构，计算每个节点的位置"""
        # 计算当前节点尺寸
        width, height = self.calculate_node_dimensions(root)
        root["width"] = width
        root["height"] = height

        # 设置当前节点位置
        root["x"] = x
        root["y"] = y

        # 如果没有子节点，直接返回
        if not root["children"]:
            return y + height + self.node_spacing

        # 计算子节点的总高度
        total_child_height = 0
        for child in root["children"]:
            child_height = self.calculate_node_dimensions(child)[1]
            total_child_height += child_height

        # 子节点之间的间隔
        if len(root["children"]) > 1:
            child_spacing = (self.height - total_child_height) / (len(root["children"]) - 1)
        else:
            child_spacing = 0

        # 递归布局子节点
        current_y = y - total_child_height / 2
        for child in root["children"]:
            child_width, child_height = self.calculate_node_dimensions(child)
            child_x = x + width + self.node_spacing if direction == 1 else x - width - self.node_spacing
            current_y += child_height / 2
            self.layout_tree(child, child_x, current_y, -direction)
            current_y += child_height / 2 + child_spacing

        return current_y

    def draw_mindmap(self, root, filename="mindmap.svg"):
        """绘制思维导图并保存为SVG文件"""
        # 创建SVG对象
        dwg = svgwrite.Drawing(filename, size=(self.width, self.height), profile='full')

        # 居中布局根节点
        root_width, root_height = self.calculate_node_dimensions(root)
        root_x = self.width / 2 - root_width / 2
        root_y = self.height / 2
        self.layout_tree(root, root_x, root_y)

        # 绘制连接线（先绘制连接线，避免被节点覆盖）
        self._draw_links(dwg, root)

        # 绘制节点
        self._draw_nodes(dwg, root)

        # 保存SVG文件
        dwg.save()
        print(f"思维导图已保存为: {filename}")

    def _draw_nodes(self, dwg, node):
        """递归绘制所有节点"""
        # 计算节点矩形位置
        x = node["x"]
        y = node["y"] - node["height"] / 2
        width = node["width"]
        height = node["height"]

        # 根节点使用特殊样式
        if node["level"] == 0:
            rect = dwg.rect(insert=(x, y), size=(width, height),
                            rx=5, ry=5,
                            fill=self.root_color,
                            stroke=self.root_color,
                            stroke_width=self.node_border_width)
            text_color = self.root_text_color
        else:
            rect = dwg.rect(insert=(x, y), size=(width, height),
                            rx=5, ry=5,
                            fill=self.node_color,
                            stroke=self.node_border_color,
                            stroke_width=self.node_border_width)
            text_color = "black"

        dwg.add(rect)

        # 添加文本
        text = Text(node["text"], insert=(x + width / 2, y + height / 2),
                    text_anchor="middle",
                    dominant_baseline="middle",
                    font_size=self.font_size,
                    font_family=self.font_family,
                    fill=text_color)
        dwg.add(text)

        # 递归绘制子节点
        for child in node["children"]:
            self._draw_nodes(dwg, child)

    def _draw_links(self, dwg, node):
        """递归绘制所有连接线"""
        for child in node["children"]:
            # 计算连接线起点和终点
            start_x = node["x"] + node["width"] if node["x"] < child["x"] else node["x"]
            start_y = node["y"]
            end_x = child["x"] if node["x"] < child["x"] else child["x"] + child["width"]
            end_y = child["y"]

            # 绘制连接线
            line = Line(start=(start_x, start_y), end=(end_x, end_y),
                        stroke=self.link_color,
                        stroke_width=self.link_width,
                        stroke_linecap="round")
            dwg.add(line)

            # 递归绘制子节点的连接线
            self._draw_links(dwg, child)


# 示例 Markdown 文本
markdown_text = """
- 项目管理
  - 计划制定
    - 目标设定
    - 资源分配
  - 执行监控
    - 进度跟踪
    - 风险管理
  - 质量管理
    - 测试策略
    - 缺陷管理
- 团队协作
  - 沟通方式
    - 每日站会
    - 周会
  - 角色分工
    - 开发人员
    - 测试人员
    - 产品经理
- 技术栈
  - 前端
    - HTML/CSS
    - JavaScript
    - React
  - 后端
    - Python
    - Flask
    - Django
  - 数据库
    - MySQL
    - PostgreSQL
"""

# 生成思维导图
generator = MindMapGenerator(width=1200, height=800)
root = generator.parse_markdown(markdown_text)
generator.draw_mindmap(root, "mindmap.svg")
