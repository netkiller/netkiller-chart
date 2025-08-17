import os
import sys

module = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ".")
sys.path.insert(1, module)

try:
    from src.netkiller.gantt import Gantt, Data
    from src.netkiller.markdown import Markdown

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    text = """
    # Table
    | id | name | start | finish | resource | progress | predecessor | milestone | parent |
    |------|------|--------|
    | 1 | 测试麦克风 | 2025-07-01 | 2025-07-02 | 工程师 |
    | 2 | 设备送检 | 2025-07-03 | 2025-07-04   | 设计师 |
    | 3 | 完成包装 | 2025-07-05 | 2025-07-10   | 设计师 |
    | 4 | 竞品评估 | 2025-07-02 | 2025-07-04   | 设计师 |
    | 5 | 分析报告 | 2025-07-08 | 2025-07-15   | 设计师 |
    | 6 | 集成测试 | 2025-07-01 | 2025-07-06   | 设计师 |
    
    https://www.netkiller.cn/python/
        """

    # markdown = Markdown(text1)
    # items = markdown.table2dict()
    # print(items)
    # tmp = Data()
    # no = 1
    # for item in items:
    #     print(item)
    #     # tmp.add(item["id"], item["name"], item["start"], item["finish"], item["resource"],
    #     #         item["predecessor"], item["milestone"], item["parent"])
    #     tmp.add(no, item["name"], item["start"], item["finish"], item["resource"],
    #             None, None, None)
    #     no += 1
    # data = tmp.data
    # print(data)

    text1 = """
    # Table
    | id | name | start | finish | resource | predecessor | milestone | parent |
    |------|------|--------|
    | 1 | 测试麦克风 | 2025-07-01 | 2025-07-02 | 工程师 | 1 | False | 0 |
    | 2 | 设备送检 | 2025-07-03 | 2025-07-04   | 设计师 | 1 | False | 0 |
    | 3 | 完成包装 | 2025-07-05 | 2025-07-10   | 设计师 | 1 | False | 0 |
    | 4 | 竞品评估 | 2025-07-02 | 2025-07-04   | 设计师 | 1 | False | 0 |
    | 5 | 分析报告 | 2025-07-08 | 2025-07-15   | 设计师 | 1 | False | 0 |
    | 6 | 集成测试 | 2025-07-01 | 2025-07-06   | 设计师 | 1 | False | 0 |

    https://www.netkiller.cn/python/
    """

    # markdown = Markdown(text1)
    # data = markdown.gantt()
    # print(data)

    text2 = """
    ## 工作计划
    | 序号 | 任务名称 | 执行人 | 开始日期 | 结束日期 | 工时 |
    | :-----| :---- | :----: | :----: | :----: | :----: |
    | 1 | 1居家办公试行方案细则 | 发言人4 | 2025-08-06 | 2025-08-07 | 1.5天 |
    | 2 | 虚拟白板系统操作指南 | 技术部张磊 | 2025-08-07 | 2025-08-09 | 2天 |
    | 3 | 每日站会制度设计 | 周经理 | 2025-08-06 | 2025-08-06 | 0.5天 |
    | 4 | 行政支持清单 | 行政部门 | 2025-08-06 | 2025-08-07 | 1天 |
    | 5 | 效率对比分析表 | 数据分析组 | 2025-08-08 | 2025-08-09 | 1.5天 |
    | 6 | 成本核算模型 | 财务部 | 2025-08-09 | 2025-08-10 | 1天 |
    | 7 | 满意度问卷 | HR部门 | 2025-08-11 | 2025-08-12 | 1天 |
    | 8 | 焦点小组计划 | 市场部 | 2025-08-12 | 2025-08-13 | 0.5天 |
    """

    markdown = Markdown(text2)
    items = markdown.table2dict()
    # print(items)
    tmp = Data()
    no = 1
    for item in items:
        # print(item)
        # tmp.add(item["id"], item["name"], item["start"], item["finish"], item["resource"],
        #         item["predecessor"], item["milestone"], item["parent"])
        tmp.add(item["序号"], item["任务名称"], item["开始日期"], item["结束日期"], item["执行人"],
                0, None, None, None)
        no += 1
    data = tmp.data
    # print(data)
    try:

        gantt = Gantt()
        # gantt.hideTable()
        gantt.load(data)
        gantt.author("Neo Chen")
        # gantt.setWorkweeks(workweeks, options.oddeven)
        gantt.title("Test")
        gantt.legend(False)
        gantt.save("markdown.svg")
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
