from netkiller.markdown import Markdown
from netkiller.mindmap import Mindmap


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
    - AAA
      - aaa
      - bbb
      - ccc
    - BBB
    - CCC 
  - AlmaLinux
    """

    markdown = Markdown(data)
    jsonData = markdown.jsonData()
    markdown.debug()

    mindmap = Mindmap()
    mindmap.data(mindmapData)
    # mindmap.data(jsonData)
    # mindmap.markdown(data)
    # mindmap.rectangle("咖啡营销会议")
    # mindmap.ellipse("咖啡营销会议")
    # print(mindmapData)
    mindmap.save('../tmp/example.svg')
    # mindmap.debug()


if __name__ == "__main__":
    main()
