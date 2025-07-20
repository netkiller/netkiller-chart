#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
##############################################
# Home	: http://netkiller.github.io
# Author: Neo <netkiller@msn.com>
# Data: 2025-07-19
##############################################
try:
    import svgwrite
    import markdown2
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

    def __init__(self, width=800, height=600):
        self.coordinate = {}
        self.horizontalPosition = 0
        self.verticalPosition = 0
        self.width = width
        self.height = height
        # 创建一个 Drawing 对象
        self.dwg = svgwrite.Drawing('example.svg', size=(width, height), profile='tiny'
                                    # , viewBox="0 0 200 200",
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
        y = self.verticalPosition // 2 + self.frontSize *2
        width = self.frontSize * len(text)
        height = self.frontSize * 2

        self.dwg.add(self.dwg.rect(insert=(0, y), size=(width, height), rx=30, ry=10, fill='lightgreen',
                                   stroke='green',
                                   stroke_width=2))
        self.dwg.add(
            self.dwg.text(text, insert=(width // 2, y + self.frontSize + self.frontSize // 4), text_anchor='middle'))

        # self.horizontalPosition + width
        # self.verticalPosition + height // 2

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
        # self.verticalPosition += self.frontSize
        # self.verticalPosition + height // 2

        path = self.dwg.path(
            d=f'M {parentNode["x"]},{parentNode["y"]} H {parentNode["x"] + self.distance / 2} V {node["y"]} H {node["x"]}',
            fill='none', stroke='#FF5722', stroke_width=2)

        self.dwg.add(path)

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
        self.arrange(self.jsonObject['children'])
        self.center(self.jsonObject['text'])

        self.dwg.save(pretty=True)


def main():
    mindmapData = {
        "type": "root",
        "level": 0,
        "title": "会议思维导图",
        "text": "咖啡营销会议",
        "children": [
            {
                "type": "heading",
                "direction": "right",
                "level": 1,
                "text": "一级标题",
                "children": [
                    {
                        "type": "list_item",
                        "text": "更多内容 1",
                        "children": [
                        ]
                    },
                    {
                        "type": "list_item",
                        "text": "更多内容 1",
                        "children": []
                    },
                    {
                        "type": "list_item",
                        "text": "子列表B1",
                        "children": [
                        ]
                    }
                ]
            },
            {
                "type": "list_item",
                "text": "AAA",
                "children": []
            },
            {
                "type": "list_item",
                "text": "AAA",
                "children": []
            },
            {
                "type": "list_item",
                "text": "子列表B2",
                "children": [
                    {
                        "type": "list_item",
                        "text": "列表A",
                        "children": []
                    },
                    {
                        "type": "list_item",
                        "text": "子列表A1",
                        "children": []
                    },
                    {
                        "type": "list_item",
                        "text": "列表B",
                        "children": []
                    }
                ]
            },
            {
                "type": "list_item",
                "text": "孙列表B1-1",
                "children": []
            }
        ]
    }
    mindmap = Mindmap()
    mindmap.data(mindmapData)
    # mindmap.rectangle("咖啡营销会议")
    # mindmap.ellipse("咖啡营销会议")
    # node = Node()
    # node.add("AAA")
    # node.add("BBB")
    print(mindmapData)

    mindmap.save()

    # mindmap.debug()


if __name__ == "__main__":
    main()
