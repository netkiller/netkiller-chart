import os
import sys

# module = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ".")
# sys.path.insert(1, module)
src = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))), 'src')
sys.path.insert(1, src)
# print(src)
# print(module)

try:
    from netkiller.svg.ScalableVectorGraphics import Svg
    from netkiller.svg.elements import Rectangle
    from netkiller.svg.filter import Filter, feOffset


except ImportError as err:
    print("Error: %s" % (err))
    exit()


def main():
    svg = Svg(800, 600)
    # svg.link("style.css")
    svg.title("Test")
    svg.desc("https://www.netkiller.cn")
    filter = Filter(id="offset", width="180", height="180")
    filter.append(feOffset(inn="SourceGraphic", dx="60", dy="60"))

    svg.defs(filter)
    svg.append(Rectangle(x="0", y="0", width="100", height="100", stroke="black", fill="green"))
    svg.append(Rectangle(x="0",
                         y="0",
                         width="100",
                         height="100",
                         stroke="black",
                         fill="green",
                         filter="url(#offset)"))

    svg.save('feOffset.svg')


if __name__ == "__main__":
    main()
