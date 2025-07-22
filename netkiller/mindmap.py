#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
##############################################
# Home	: http://netkiller.github.io
# Author: Neo <netkiller@msn.com>
# Data: 2025-07-19
##############################################
import random

import cairo

try:
    import svgwrite
    from PIL import ImageFont, ImageDraw, Image
except ImportError as err:
    print("Import Error: %s" % (err))


# class Point:
#     def __init__(self, x=0, y=0):
#         """初始化点的坐标"""
#         self.x = x
#         self.y = y


class Mindmap:
    fontSize = 16
    # fontFamily = "SimHei"
    # fontFamily = "Helvetica"
    # fontFamily = "Times"
    # fontFamily = "PingFang"
    # fontFamily = "SimSun"
    fontFamily = "Songti"
    # fontColor = "black"
    fontColor = "#515151"

    distance = 100
    charHeight = 30
    level = 0

    def __init__(self, width=1024, height=768):
        self.coordinate = {}
        self.horizontalPosition = 0
        self.verticalPosition = 0
        self.verticalOffset = 0
        self.width = width
        self.height = height
        # 创建一个 Drawing 对象
        self.dwg = svgwrite.Drawing('example.svg', size=(width, height), profile='tiny'
                                    # , viewBox=f"0 -{height // 2} {width} {height // 2}",
                                    # preserveAspectRatio="xMidYMid slice"
                                    )
        pass

    def title(self, text):
        title = self.dwg.text(text, insert=(self.width / 2, 30), text_anchor='middle',
                              font_size='20', font_family='Arial')
        self.dwg.add(title)

        self.horizontalPosition = len(text) // 2
        self.verticalPosition = self.fontSize * 2

    def center(self, text: str):
        x = self.horizontalPosition
        y = self.verticalPosition // 2 + self.fontSize * 2
        width = self.fontSize * len(text)
        height = self.fontSize * 2

        self.dwg.add(self.dwg.rect(insert=(0, y), size=(width, height), rx=30, ry=10, fill='lightgreen',
                                   stroke='green',
                                   stroke_width=2))
        self.dwg.add(
            self.dwg.text(text, insert=(width // 2, y + self.fontSize + self.fontSize // 4), text_anchor='middle'))

    def root(self, text: str):
        x = self.horizontalPosition
        # y = self.verticalPosition
        y = self.verticalPosition // 2 + self.charHeight // 2
        width = self.horizontalPosition
        height = self.fontSize * 2
        color = self.randomColor()

        self.dwg.add(self.dwg.line(start=(2, y), end=(width, y), fill='lightgreen',
                                   stroke=f'{color}',
                                   stroke_width=4))

        circle = self.dwg.circle(center=(width, y), r=4, fill="white", stroke=f"{color}", stroke_width="2")
        self.dwg.add(circle)
        self.dwg.add(self.dwg.text(text, insert=(width // 2, y - 5), text_anchor='middle',
                                   font_family=f"{self.fontFamily}",
                                   font_size=f"{self.fontSize}",
                                   fill=f"{self.fontColor}"
                                   ))

    def rectangle(self, text: str):
        rect1 = self.dwg.rect(insert=(50, 70), size=(100, 80), rx=15, ry=15,
                              fill='lightblue', stroke='blue', stroke_width=2)
        self.dwg.add(rect1)
        self.dwg.add(self.dwg.text(text, insert=(100, 120), text_anchor='middle'))
        # self.dwg.add(self.dwg.rect(insert=(0, 0), size=("100%", "100%"), fill='green'))

    def ellipse(self, text: str):
        # 1. 基本椭圆：中心点(150, 100)，水平半径100，垂直半径50
        # 参数说明：
        # center: (cx, cy) 椭圆中心点坐标
        # r: (rx, ry) 水平半径和垂直半径
        basic_ellipse = self.dwg.ellipse(center=(150, 100), r=(100, 50),
                                         fill="lightblue",  # 填充色
                                         stroke="blue",  # 边框色
                                         stroke_width=2)  # 边框宽度
        self.dwg.add(basic_ellipse)
        # self.dwg.add(self.dwg.text("基本椭圆", insert=(150, 100), text_anchor="middle", dominant_baseline="middle"))

    def textNode(self, parentNode: dict, node: dict, color: str, width):

        width = node['x'] + width

        self.dwg.add(self.dwg.text(node['text'], insert=(node["x"], node["y"] - 4), text_anchor='start',
                                   font_family=f"{self.fontFamily}",
                                   font_size=f"{self.fontSize}",
                                   fill=f"{self.fontColor}"))
        path = self.dwg.path(
            d=f'M {parentNode["x"]},{parentNode["y"]} H {parentNode["x"] + self.distance / 2} V {node["y"]} H {node["x"]}',
            fill='none', stroke='#FF5722', stroke_width=2)
        # self.dwg.add(path)
        line = self.dwg.line(start=(node["x"], node["y"]), end=(width, node["y"]), stroke=f'{color}', stroke_width=2)

        circle = self.dwg.circle(center=(width, node["y"]), r=5, fill="white", stroke=f"{color}", stroke_width="2")

        self.dwg.add(line)
        self.dwg.add(circle)

    def bezierCurveNode(self, parentNode: dict, node: dict, width: int):
        self.dwg.add(self.dwg.text(node['text'], insert=(node["x"], node["y"]), text_anchor='start'))

        path = self.dwg.path(
            d=f'M{parentNode["x"]},{parentNode["y"]} C{parentNode["x"] + self.distance / 2},{parentNode["y"]} {node["x"] - self.distance / 2},{node["y"]} {node["x"]},{node["y"]} L{node["x"] + width},{node["y"]}',
            fill='none', stroke='#FF5722', stroke_width=2)

        self.dwg.add(path)

    def curve(self, parentNode, node, color: str):
        # self.dwg.add(self.dwg.text(node['text'], insert=(node["x"], node["y"]), text_anchor='start'))

        path = self.dwg.path(
            d=f'M{parentNode["x"]},{parentNode["y"]} C{parentNode["x"] + self.distance / 2},{parentNode["y"]} {node["x"] - self.distance / 2},{node["y"]} {node["x"]},{node["y"]}',
            fill='none', stroke=f'{color}', stroke_width=2)

        self.dwg.add(path)

    def parent(self, text: str):
        x = self.horizontalPosition
        y = self.verticalPosition
        # y = self.verticalPosition // 2 + self.fontSize
        width = self.fontSize * len(text)
        height = self.fontSize * 2

        self.dwg.add(self.dwg.line(start=(0, y), end=(width, y), fill='lightgreen',
                                   stroke='green',
                                   stroke_width=2))

        circle = self.dwg.circle(center=(width, y), r=5, fill="white", stroke="green", stroke_width="2")
        self.dwg.add(circle)
        self.dwg.add(self.dwg.text(text, insert=(width // 2, y), text_anchor='middle'))

    def rander(self):

        width, height = self.getTextSize(self.jsonObject['text'])

        # self.background(self.jsonObject['children'], True)

        self.horizontalPosition = 0
        self.verticalPosition = 0

        self.horizontalPosition = width + self.fontSize  # + self.distance

        self.scan(self.jsonObject['children'])
        self.root(self.jsonObject['text'])

        # self.getTextSize("中国")
        self.dwg.save(pretty=True)

        pass

    def scan(self, childNode: list, horizontalOffset: int = 0):
        textWidth = 0
        for child in childNode:
            width, height = self.getTextSize(child['text'])
            if width > textWidth:
                textWidth = width

        if textWidth > 0:
            textWidth += 5

        currentVerticalPosition = self.verticalPosition
        currentHorizontalPosition = self.distance + horizontalOffset
        self.horizontalPosition += currentHorizontalPosition

        curve = []

        x = self.horizontalPosition

        for child in childNode:

            if 'children' in child:
                if len(child['children']) > 0:
                    self.scan(child['children'], textWidth)
                else:
                    pass

            if self.verticalOffset:
                y = self.verticalPosition - self.verticalOffset + self.charHeight // 2
                self.verticalOffset = 0

            else:
                self.verticalPosition += self.charHeight;
                y = self.verticalPosition

            color = self.randomColor()
            text = child["text"]

            # self.textNode({"x": 0, "y": 0}, {"x": x, "y": y, "text": child["text"]}, color, textWidth)
            curve.append((x, y, color, text))

        self.verticalOffset = (self.verticalPosition - currentVerticalPosition) // 2
        self.horizontalPosition -= currentHorizontalPosition

        px = self.horizontalPosition + horizontalOffset
        py = self.verticalPosition - self.verticalOffset + self.charHeight // 2
        for x, y, c, t in curve:
            self.curve({"x": px, "y": py}, {"x": x, "y": y}, c)
            self.textNode({"x": 0, "y": 0}, {"x": x, "y": y, "text": t}, c, textWidth + 5)

    def randomColor(self):
        """生成随机 RGB 颜色（返回 (r, g, b) 元组）"""
        # r = random.randint(0, 255)
        # g = random.randint(0, 255)
        # b = random.randint(0, 255)
        # return f'#{r:02X}{g:02X}{b:02X}'

        # a = round(random.uniform(0, 1), 2)  # 透明度保留2位小数
        # return (r, g, b, a)

        # 红色：red（  # FF0000）
        # 绿色：green（  # 008000）
        # 蓝色：blue（  # 0000FF）
        # 黄色：yellow（  # FFFF00）
        # 黑色：black（  # 000000）
        # 白色：white（  # FFFFFF）
        # 灰色：gray（  # 808080）
        # 粉色：pink（  # FFC0CB）
        # 紫色：purple（  # 800080）
        # 橙色：orange（  # FFA500）
        # 棕色：brown（  # A52A2A）
        # 青色：cyan（  # 00FFFF）
        # 品红：magenta（  # FF00FF）
        # 银色：silver（  # C0C0C0）
        # 金色：gold（  # FFD700）
        color = [
            "red", "green", "blue", "black", "gray", "pink", "purple", "orange", "brown", "cyan", "magenta", "gold",
            "#005588",
        ]
        return random.choice(color)

    def arrange(self, childNode: list):
        if not childNode:
            return 0;

        self.verticalPosition = len(childNode) * self.fontSize // 2
        parentY = self.verticalPosition + self.fontSize

        # self.horizontalPosition += len(childNode['text']) * self.fontSize
        parentX = self.horizontalPosition
        columnWidth = 0
        for child in childNode:
            if len(child['text']) > columnWidth:
                columnWidth = len(child['text']) * self.fontSize

        self.horizontalPosition += self.distance  # + columnWidth * self.fontSize

        x = self.horizontalPosition
        y = 0

        for child in childNode:
            print(child['text'])

            if 'children' in child and len(child['children']) > 0:
                self.horizontalPosition += columnWidth
                self.arrange(child['children'])

            y += self.fontSize
            # self.verticalPosition += y;

            self.textNode({"x": parentX, "y": parentY}, {"x": x, "y": y, "text": child["text"]})

        self.horizontalPosition -= self.distance
        # return len(childNode) * self.fontSize

        # self.horizontalPosition = len(node['text']) * self.fontSize
        # # children = node['children']
        # self.node(node)        #
        # # print(self.dwg.)
        # pass

    def getTextSize(self, text, size: float = 16):

        # 创建一个临时图像用于测量
        img = Image.new('RGB', (1, 1))
        draw = ImageDraw.Draw(img)

        # import matplotlib.font_manager as fm
        # font_path = fm.findfont(fm.FontProperties())  # 获取默认字体路径
        # print(f"查看字体文件：{font_path}")

        try:
            font = ImageFont.truetype(self.fontFamily, size=self.fontSize, encoding="utf-8")
        except IOError:
            # raise FileNotFoundError(f"字体文件不存在：{font_path}，请替换为系统中实际存在的字体路径")
            if self.fontSize > 0:
                font = ImageFont.load_default(size)
            else:
                font = ImageFont.load_default()
                # print()

        # 计算文本尺寸
        # 使用 textbbox 获取边界框（参数为文本左上角坐标）
        left, top, right, bottom = draw.textbbox((0, 0), text, font=font,
                                                 # spacing=0,
                                                 align="left")

        # 计算宽度和高度
        width = right - left
        height = bottom - top
        # print(f"文本：{text} 宽度：{width}px，高度：{height}px 字体：{font.getname()} ")
        return width, height

    def calculate_text_width(self, text, font_family="Arial", font_size=16):
        """用cairo计算文本宽度（像素）"""
        # 创建虚拟SVG表面用于测量
        surface = cairo.SVGSurface(None, 0, 0)
        ctx = cairo.Context(surface)
        # 设置字体样式
        ctx.select_font_face(self.fontFamily)
        ctx.set_font_size(self.fontSize)
        # 获取文本边界信息
        # _, _, width, _, _, _ = ctx.text_extents(text)
        x_bearing, y_bearing, width, height, x_advance, y_advance = ctx.text_extents(text)

        print(f"文本：{text} 宽度：{width}px，高度：px")
        return width

    def data(self, jsonObject: dict):
        self.jsonObject = jsonObject

    def save(self):
        self.horizontalPosition = len(self.jsonObject['text']) * self.fontSize
        # self.verticalPosition = len(self.jsonObject['children']) * self.fontSize // 2
        # self.title(node["title"])

        # self.arrange(self.jsonObject['children'])
        # self.center(self.jsonObject['text'])
        self.dwg.save(pretty=True)

    def font(self):
        import matplotlib.font_manager as fm

        # 获取所有系统字体
        font_list = fm.findSystemFonts()
        print("\n".join(font_list))

    def background(self, childNode: list, bg: bool = False):

        if bg:
            self.dwg.add(self.dwg.rect(insert=(0, 0), size=(self.width, self.height), fill='#EEEEEE'))
            circle = self.dwg.circle(center=(0, 0), r=5, fill="white", stroke="green", stroke_width="2")
            self.dwg.add(circle)

        self.horizontalPosition += self.distance
        x = self.horizontalPosition

        self.dwg.add(self.dwg.line(start=(x, 0), end=(x, self.height),
                                   stroke='grey', stroke_width=1, stroke_dasharray='2,8'
                                   ))

        # textWidth = 0
        # for child in childNode:
        #     width, height = self.getTextSize(child['text'])
        #     if width > textWidth:
        #         textWidth = width
        #
        # x1 = self.horizontalPosition + textWidth
        # self.dwg.add(self.dwg.line(start=(x1, 0), end=(x1, self.height),
        #                            stroke='black', stroke_width=1, stroke_dasharray='10,2'
        #                            ))

        for child in childNode:
            print(child['text'])

            if 'children' in child and len(child['children']) > 0:
                # self.horizontalPosition += columnWidth
                self.background(child['children'])

            self.verticalPosition += self.charHeight
            y = self.verticalPosition
            self.dwg.add(self.dwg.line(start=(0, y), end=(self.width, y),
                                       stroke='grey', stroke_width=1, stroke_dasharray='2,8'
                                       ))

    def debug(self):
        # self.getTextSize("中")
        # self.getTextSize("中国")
        # self.getTextSize("W")
        # self.getTextSize("ABCDEFG")
        # self.getTextSize("a")
        # self.getTextSize("abc")
        # self.getTextSize("aB")
        # self.getTextSize("中A")
        # self.calculate_text_width("中")
        # self.calculate_text_width("A")
        # self.calculate_text_width("中国")
        # self.calculate_text_width("AB")
        # self.calculate_text_width("a")

        # rect1 = self.dwg.rect(insert=(50, 70), size=(100, 80), rx=15, ry=15,
        #                       fill='lightblue', stroke='blue', stroke_width=2)
        # self.dwg.add(rect1)
        # self.dwg.add(self.dwg.text(text, insert=(100, 120), text_anchor='middle'))
        # self.debug = True

        self.rander()


def main():
    mindmapData = {
        "type": "root",
        "level": 0,
        "title": "会议思维导图",
        "text": "计算机语言语言",
        "children": [
            {
                "type": "heading",
                "direction": "right",
                "level": 1,
                "text": "中国",
                "children": [
                    {
                        "type": "list_item",
                        "text": "台湾",
                        "children": [
                        ]
                    },
                    {
                        "type": "list_item",
                        "text": "大陆",
                        "children": [
                            {
                                "type": "list_item",
                                "text": "东北",
                                "children": [
                                    {
                                        "type": "list_item",
                                        "text": "黑龙江",
                                        "children": [
                                        ]
                                    },
                                    {
                                        "type": "list_item",
                                        "text": "吉林",
                                        "children": [
                                        ]
                                    },
                                    {
                                        "type": "list_item",
                                        "text": "辽宁",
                                        "children": [
                                        ]
                                    }
                                ]
                            }, {
                                "type": "list_item",
                                "text": "华南",
                                "children": [
                                ]
                            }
                        ]
                    },
                    {
                        "type": "list_item",
                        "text": "香港",
                        "children": [
                        ]
                    }
                ]
            },
            {
                "type": "list_item",
                "text": "孙列表项1",
                "children": []
            },

            {
                "type": "list_item",
                "text": "Python",
                "children": [
                    {
                        "type": "list_item",
                        "text": "列表项1",
                        "children": [
                        ]
                    }, {
                        "type": "list_item",
                        "text": "内容段落2",
                        "children": [
                        ]
                    }, {
                        "type": "list_item",
                        "text": "内容段落1",
                        "children": [
                        ]
                    }, {
                        "type": "heading",
                        "level": 1,
                        "text": "一级标题",
                        "children": [

                        ]
                    }
                ]
            },
            {
                "type": "list_item",
                "text": "PHP",
                "children": []
            },
            {
                "type": "list_item",
                "text": "C语言",
                "children": [
                    {
                        "type": "list_item",
                        "text": "GNU C",
                        "children": []
                    },
                    {
                        "type": "list_item",
                        "text": "Clang",
                        "children": []
                    },
                    {
                        "type": "list_item",
                        "text": "C++ 语言",
                        "children": []
                    }
                ]
            },
            {
                "type": "list_item",
                "text": "Rust",
                "children": []
            }
        ]
    }
    data = """
# 操作系统
- Linux
  - Redhat
  - CentOS
  - Rocky Linux
  - AlmaLinux
    """

    # markdown = Markdown(data)
    # jsonData = markdown.jsonData()
    # markdown.debug()

    mindmap = Mindmap()
    mindmap.data(mindmapData)
    # mindmap.rectangle("咖啡营销会议")
    # mindmap.ellipse("咖啡营销会议")
    # print(mindmapData)
    # mindmap.save()
    mindmap.debug()


if __name__ == "__main__":
    main()
