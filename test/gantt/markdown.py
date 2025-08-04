#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
##############################################
# Home	: https://www.netkiller.cn
# Author: Neo <netkiller@msn.com>
##############################################
import os
import sys

module = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ".")
sys.path.insert(1, module)

try:
    from src.netkiller.gantt import Gantt, Data, Workload
    from src.netkiller.markdown import Markdown

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    text = """
    # Table
    | id | name | start | finish | resource | predecessor | milestone | parent |
    |------|------|--------|
    | 1 | 测试麦克风 | 2025-07-01 | 2025-07-02 | 工程师 |
    | 2 | 设备送检 | 2025-07-03 | 2025-07-04   | 设计师 |
    | 3 | 完成包装 | 2025-07-05 | 2025-07-10   | 设计师 |
    | 4 | 竞品评估 | 2025-07-02 | 2025-07-04   | 设计师 |
    | 5 | 分析报告 | 2025-07-08 | 2025-07-15   | 设计师 |
    | 6 | 集成测试 | 2025-07-01 | 2025-07-06   | 设计师 |
    
    https://www.netkiller.cn/python/
        """

    markdown = Markdown(text)
    items = markdown.table2dict()
    print(items)
    tmp = Data()
    no = 1
    for item in items:
        print(item)
        # tmp.add(item["id"], item["name"], item["start"], item["finish"], item["resource"],
        #         item["predecessor"], item["milestone"], item["parent"])
        tmp.add(no, item["name"], item["start"], item["finish"], item["resource"],
                None, None, None)
        no += 1
    data = tmp.data
    print(data)

    try:

        gantt = Gantt()
        # gantt.hideTable()
        gantt.load(data)
        gantt.author("Neo Chen")
        # gantt.setWorkweeks(workweeks, options.oddeven)
        gantt.title("Test")
        gantt.legend(False)
        gantt.save("markdown.svg")

        # gantt.export(file)

        # gantt.main()
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
