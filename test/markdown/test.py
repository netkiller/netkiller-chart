from src.netkiller.markdown import Markdown

text = """
# Table
| 姓名 | 年龄 | 职业   |
|------|------|--------|
| 张三 | 25   | 工程师 |
| 李四 | 30   | 设计师 |
hello word
    """

markdown = Markdown(text)
print(markdown.table2dict())
