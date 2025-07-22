#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
##############################################
# Home	: http://netkiller.github.io
# Author: Neo <netkiller@msn.com>
# Data: 2025-07-19
##############################################

try:
    import svgwrite
    # import drawsvg as draw
    # from datetime import datetime, date
    # from PIL import ImageFont
    # import requests
    # import os
    # import platform
except ImportError as err:
    print("Import Error: %s" % (err))


# class Node:
#     nodes = []
#
#     def __init__(self):
#         pass
#
#     def add(self, text: str):
#         self.nodes.append(text)

class Point:
    def __init__(self, x=0, y=0):
        """初始化点的坐标"""
        self.x = x
        self.y = y


class Mindmap:
    spacing = 200
    distance = 50
    frontSize = 20
    charWidth = 0.5
    level = 0

    def __init__(self, width=1024, height=768):
        self.coordinate = {}
        self.horizontalPosition = 0
        self.verticalPosition = 0
        self.horizontalOffset = 0
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
        self.verticalPosition = self.frontSize * 2

    def center(self, text: str):
        x = self.horizontalPosition
        y = self.verticalPosition // 2 + self.frontSize * 2
        width = self.frontSize * len(text)
        height = self.frontSize * 2

        self.dwg.add(self.dwg.rect(insert=(0, y), size=(width, height), rx=30, ry=10, fill='lightgreen',
                                   stroke='green',
                                   stroke_width=2))
        self.dwg.add(
            self.dwg.text(text, insert=(width // 2, y + self.frontSize + self.frontSize // 4), text_anchor='middle'))

    def root(self, text: str):
        x = self.horizontalPosition
        y = self.verticalPosition
        # y = self.verticalPosition // 2 + self.frontSize
        width = self.frontSize * len(text)
        height = self.frontSize * 2

        self.dwg.add(self.dwg.line(start=(0, y), end=(width, y), fill='lightgreen',
                                   stroke='green',
                                   stroke_width=2))

        circle = self.dwg.circle(center=(width, y), r=5, fill="white", stroke="green", stroke_width="2")
        self.dwg.add(circle)
        self.dwg.add(self.dwg.text(text, insert=(width // 2, y), text_anchor='middle'))

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

    def textNode(self, parentNode: dict, node: dict):
        self.dwg.add(self.dwg.text(node['text'], insert=(node["x"], node["y"]), text_anchor='start'))
        path = self.dwg.path(
            d=f'M {parentNode["x"]},{parentNode["y"]} H {parentNode["x"] + self.distance / 2} V {node["y"]} H {node["x"]}',
            fill='none', stroke='#FF5722', stroke_width=2)
        # self.dwg.add(path)

    def bezierCurveNode(self, parentNode: dict, node: dict, width: int):
        self.dwg.add(self.dwg.text(node['text'], insert=(node["x"], node["y"]), text_anchor='start'))

        path = self.dwg.path(
            d=f'M{parentNode["x"]},{parentNode["y"]} C{parentNode["x"] + self.distance / 2},{parentNode["y"]} {node["x"] - self.distance / 2},{node["y"]} {node["x"]},{node["y"]} L{node["x"] + width},{node["y"]}',
            fill='none', stroke='#FF5722', stroke_width=2)

        self.dwg.add(path)

    def parent(self, text: str):
        x = self.horizontalPosition
        y = self.verticalPosition
        # y = self.verticalPosition // 2 + self.frontSize
        width = self.frontSize * len(text)
        height = self.frontSize * 2

        self.dwg.add(self.dwg.line(start=(0, y), end=(width, y), fill='lightgreen',
                                   stroke='green',
                                   stroke_width=2))

        circle = self.dwg.circle(center=(width, y), r=5, fill="white", stroke="green", stroke_width="2")
        self.dwg.add(circle)
        self.dwg.add(self.dwg.text(text, insert=(width // 2, y), text_anchor='middle'))

    def rander(self, childNode: dict):
        # self.level += 1
        # print(self.level)
        # for child in childNode['children']:
        #     self.rander(child)
        #     print(child['text'])
        #     # if 'children' in child and len(child['children']) > 0:
        #     #     #             self.horizontalPosition += columnWidth
        #     #     self.scan(child['children'])
        # # coordinates
        #
        # y = len(childNode['children']) * self.frontSize // 2
        # childNode['xy'] = (0, y)
        # # self.verticalPosition = len(childNode)
        # self.level -= 1

        self.distance = 100

        # if not tree:
        #     return
        # print(len(childNode))
        self.verticalPosition += (len(childNode['children'])) * self.frontSize // 2
        parentY = self.verticalPosition + (len(childNode['children'])) * self.frontSize // 2

        # self.horizontalPosition += len(childNode['text']) * self.frontSize
        parentX = self.horizontalPosition
        columnWidth = 0
        for child in childNode['children']:
            if len(child['text']) > columnWidth:
                columnWidth = len(child['text']) * self.frontSize

        self.horizontalPosition += self.distance  # + columnWidth * self.frontSize

        x = self.horizontalPosition

        for child in childNode['children']:

            if 'children' in child:
                if len(child['children']) > 0:
                    self.horizontalPosition += columnWidth
                    self.rander(child)
                else:
                    self.verticalPosition += self.frontSize

            print(child['text'])
            y = self.verticalPosition
            self.bezierCurveNode({"x": parentX, "y": parentY}, {"x": x, "y": y, "text": child["text"]}, 100)

        # self.verticalPosition += (len(childNode['children'])) * self.frontSize // 2;
        if childNode['type'] == 'root':
            self.parent(childNode['text'])
        self.horizontalPosition -= self.distance

    def scan(self, childNode: list):

        self.distance = 100

        # # if not tree:
        # #     return
        # # print(len(childNode))
        # # self.verticalPosition = (len(childNode) + 1) * self.frontSize // 2
        # parentY = self.verticalPosition
        #
        # # self.horizontalPosition += len(childNode['text']) * self.frontSize
        # parentX = self.horizontalPosition
        #
        columnWidth = 0
        for child in childNode:
            if len(child['text']) > columnWidth:
                columnWidth = len(child['text']) * self.frontSize

        # self.distance += columnWidth
        # self.horizontalPosition += self.distance  # + columnWidth * self.frontSize

        x = self.horizontalPosition

        currentVerticalPosition = self.verticalPosition

        for child in childNode:

            if 'children' in child:
                if len(child['children']) > 0:
                    self.horizontalPosition += self.distance
                    self.scan(child['children'])
                else:
                    print()

            print(child['text'])

            if self.horizontalOffset:
                # self.verticalPosition += self.horizontalOffset
                y = self.verticalPosition - self.horizontalOffset + self.frontSize // 2
                self.horizontalOffset = 0

            else:
                self.verticalPosition += self.frontSize;
                y = self.verticalPosition

            self.textNode({"x": 0, "y": 0}, {"x": x, "y": y, "text": child["text"]})

        # self.horizontalOffset = len(childNode) // 2 * self.frontSize

        self.horizontalOffset = (self.verticalPosition - currentVerticalPosition) // 2

        self.horizontalPosition -= self.distance

    def arrange(self, childNode: list):
        if not childNode:
            return 0;

        self.verticalPosition = len(childNode) * self.frontSize // 2
        parentY = self.verticalPosition + self.frontSize

        # self.horizontalPosition += len(childNode['text']) * self.frontSize
        parentX = self.horizontalPosition
        columnWidth = 0
        for child in childNode:
            if len(child['text']) > columnWidth:
                columnWidth = len(child['text']) * self.frontSize

        self.horizontalPosition += self.distance  # + columnWidth * self.frontSize

        x = self.horizontalPosition
        y = 0

        for child in childNode:
            print(child['text'])

            if 'children' in child and len(child['children']) > 0:
                self.horizontalPosition += columnWidth
                self.arrange(child['children'])

            y += self.frontSize
            # self.verticalPosition += y;

            self.textNode({"x": parentX, "y": parentY}, {"x": x, "y": y, "text": child["text"]})

        self.horizontalPosition -= self.distance
        # return len(childNode) * self.frontSize

        # self.horizontalPosition = len(node['text']) * self.frontSize
        # # children = node['children']
        # self.node(node)        #
        # # print(self.dwg.)
        # pass

    def data(self, jsonObject: dict):
        self.jsonObject = jsonObject

    def save(self):
        self.horizontalPosition = len(self.jsonObject['text']) * self.frontSize
        # self.verticalPosition = len(self.jsonObject['children']) * self.frontSize // 2
        # self.title(node["title"])

        # self.arrange(self.jsonObject['children'])
        # self.center(self.jsonObject['text'])
        self.dwg.save(pretty=True)

    def debug(self):
        self.horizontalPosition = len(self.jsonObject['text']) * self.frontSize
        self.scan(self.jsonObject['children'])
        self.root(self.jsonObject['text'])

        # self.rander(self.jsonObject)
        self.dwg.save(pretty=True)


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
                "text": "Linux",
                "children": [
                    {
                        "type": "list_item",
                        "text": "Redhat 1",
                        "children": [
                        ]
                    },
                    {
                        "type": "list_item",
                        "text": "CentOS 2",
                        "children": [
                            {
                                "type": "list_item",
                                "text": "子列表项1",
                                "children": [
                                ]
                            }, {
                                "type": "list_item",
                                "text": "列表项2",
                                "children": [
                                ]
                            }
                        ]
                    },
                    {
                        "type": "list_item",
                        "text": "Mandrank",
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
