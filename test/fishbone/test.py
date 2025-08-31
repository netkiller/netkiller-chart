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
    # from netkiller import Data
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
  - 品牌形象
  - 产品生命周期
  - 发现了一个名
- 开发目标
  - 编码开发
  - 代码测试
- 运营目标
  - 区域投放
- 运营目标1
  - 区域投放1
  - 区域投放2
  - 区域投放3
  - 区域投放4
  - 区域投放5
- 运营目标1运营
  - 区域投放11
  - 区域投放21    
  - 区域投放31区域投放31
  - 区域投放41
  - 区域投放51
- 区域投放513
  - 竞品分析
  - 品牌形象
  - 产品生命周期
  - 发现了一个名
  - 区域投放3
  - 区域投放4
  - 区域投放5
- 运营目标1运营99
  - 区域投放11
  - 区域投放21
  - 区域投放31  
        """
    try:

        # markdown = Markdown()
        # data = markdown.fishbone()
        # print(data)
        fishbone = Fishbone()
        fishbone.markdown(text)
        fishbone.title("石川鱼骨图")
        # fishbone.border(5)
        fishbone.legend(False)
        fishbone.save("test.svg")
        # fishbone.debug()
        print(fishbone.show())




    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
