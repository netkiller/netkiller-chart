from src.netkiller.markdown import Markdown

text = """
# Table
| 姓名 | 年龄 | 职业   |
|------|------|--------|
| 张三 | 25   | 工程师 |
| 李四 | 30   | 设计师 |
hello word
    """

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

markdown = Markdown(text1)
# print(markdown.title())
# print(markdown.table2dict())
print(markdown.gantt())
