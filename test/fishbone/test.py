import os
import sys

# module = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, ".")
# sys.path.insert(1, module)
src = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'src')
sys.path.insert(2, src)
# print(src)
# print(module)


try:
    import io
    from netkiller import Data
    from netkiller.fishbone import Fishbone
    from netkiller.markdown import Markdown

except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    text = """
# 石川鱼骨图
- 产品目标
  - 竞品分析
- 开发目标
  - 编码开发
  - 代码测试
- 运营目标
  - 区域投放
        """
    try:
        with io.StringIO(text) as csv:
            markdown = Markdown(text)
            data = markdown.fishbone()
            print(data)
            fishbone = Fishbone(data)
            fishbone.main()

            # workload.title("工作负载图")
            # workload.department("技术研发部")
            # workload.setWorkweeks(6, 1)
            # # workload.workload()
            # workload.save("workload1.svg")


    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
