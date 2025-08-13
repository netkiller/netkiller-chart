#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
##############################################
# Home	: https://www.netkiller.cn
# Author: Neo <netkiller@msn.com>
# Data: 2025-08-04
##############################################
import os
import sys

module = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ".")
sys.path.insert(1, module)
src = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'src')
sys.path.insert(2, src)
print()
# print(module)

try:
    from netkiller.gantt import Gantt
    from netkiller.markdown import Markdown

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    text = """
    # Table
    | id | name | start | finish | resource | progress | predecessor | milestone | parent |
    |------|------|--------|
    | 1 | 测试麦克风 | 2025-07-01 | 2025-07-02 | 工程师 | 1 | 0 | False | 0 |
    | 2 | 设备送检 | 2025-07-03 | 2025-07-04   | 设计师 | 1 | 1 | False | 0 |
    | 3 | 完成包装 | 2025-07-05 | 2025-07-10   | 设计师 | 1 | 1 | False | 0 |
    | 4 | 竞品评估 | 2025-07-02 | 2025-07-04   | 设计师 | 1 | 0 | True | 0 |
    | 5 | 分析报告 | 2025-07-08 | 2025-07-15   | 设计师 | 1 | 0 | False | 0 |
    | 6 | 集成测试 | 2025-07-01 | 2025-07-06   | 设计师 | 1 | 0 | False | 0 |

    https://www.netkiller.cn/python/
    """

    markdown = Markdown(text)
    data = markdown.gantt()

    print(data)
    try:

        gantt = Gantt()
        # gantt.hideTable()
        gantt.load(data)
        gantt.author("Neo Chen")
        gantt.setWorkweeks(6, 1)
        gantt.title("Test")
        # gantt.legend(False)
        # gantt.blank(True)
        gantt.save("markdown1.svg")
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
